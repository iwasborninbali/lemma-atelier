"""Тесты-фальсификаторы к lem-003 (пишет ДРУГОЙ агент — opus/saturation, 3.09.2026). Ищем: (1) нарушение предиката на случайных
M-инвариантных максимальных S (n = 5, 6, 7; инверсия, отражение, поворот порядка 4) и непустоту; (2) ТОЧНОСТЬ границ — множества,
на которых они достигаются (3 коллинеарных через центр при инверсии, 2 + 3 при отражении, 3 на оси при повороте-4), иначе лемма
могла бы быть слабой; (3) граница: полуоборот и поворот-3 дают большие множества, S4-орбита некомпланарна, аналог для «трёх на прямой»
ложен; (4) следствие для страт: среди 33 классов сопряжённости подгрупп O_h тривиализуются ровно те, что содержат инверсию,
отражение или поворот порядка 4 — остаётся 9 классов (в нумерации cube_strata_planes.py: c00, c02, c03, c06, c09, c10, c14, c17, c27);
(5) чётное n: при инверсии центр — не клетка, |S| ≤ 2 (пары антиподов коллинеарны через центр только по одной).
Запуск: python3 -m unittest lemmas.tests.test_lem_003"""
import itertools, random, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import lem_003_statement as L


def closure(gens):
    S = {L.IDENT}; fr = [L.IDENT]
    while fr:
        new = []
        for a in fr:
            for g in gens:
                b = L.mul(a, g)
                if b not in S: S.add(b); new.append(b)
        fr = new
    return frozenset(S)


def inv(A): return tuple(A[3*j+i] for i in range(3) for j in range(3))


def subgroup_classes(G):
    """как в ~/cube_strata_planes.py (подгруппы, порождённые ≤ 2 элементами, и их произведения; классы сопряжённости)."""
    subs = set(); Gl = sorted(G)
    for a in Gl: subs.add(closure([a]))
    for i, a in enumerate(Gl):
        for b in Gl[i+1:]: subs.add(closure([a, b]))
    base = list(subs)
    for i in range(len(base)):
        for j in range(i+1, len(base)):
            if len(base[i]) * len(base[j]) <= 192: subs.add(closure(list(base[i] | base[j])))
    classes = {}
    for S in subs:
        key = min(tuple(sorted(frozenset(L.mul(L.mul(g, h), inv(g)) for h in S))) for g in Gl)
        classes.setdefault(key, S)
    return sorted(classes.values(), key=lambda S: (len(S), sorted(S)))


class TestLem003(unittest.TestCase):
    def test_1_random_cases_nonvacuous(self):
        rnd = random.Random(3); seen = {}
        for _ in range(45):
            S, M, n = L.generate(rnd, n=rnd.choice([5, 6, 7]))
            self.assertTrue(L.invariant(S, M, n) and not L.has_coplanar4(S))
            self.assertTrue(L.statement(S, M, n), (L.kind(M), n, S))
            seen.setdefault(L.kind(M), 0); seen[L.kind(M)] += 1
            if not (L.kind(M) == 'rotation4' and n % 2 == 0):   # при чётном n ось поворота-4 не проходит через клетки: S = ∅ законно
                self.assertGreater(len(S), 0, (L.kind(M), n))
        self.assertEqual(set(seen), {"inversion", "reflection", "rotation4"}, "тест пуст по одному из видов")

    def test_2_bounds_are_sharp(self):
        n = 5; c = (2, 2, 2)
        S_inv = [(0, 0, 0), c, (4, 4, 4)]                                # коллинеарные через центр
        self.assertTrue(L.invariant(S_inv, L.INV, n) and not L.has_coplanar4(S_inv) and len(S_inv) == L.BOUND["inversion"])
        refl = next(M for M in L.all_matrices() if L.kind(M) == "reflection" and M[8] == -1)   # зеркало z = 2
        S_ref = [(0, 0, 2), (1, 3, 2), (4, 1, 2), (2, 2, 0), (2, 2, 4)]                          # 3 на зеркале + пара
        self.assertTrue(L.invariant(S_ref, refl, n), "пара (2,2,0),(2,2,4) должна быть зеркальной")
        self.assertFalse(L.has_coplanar4(S_ref), "достигающий пример должен быть без четырёх компланарных")
        self.assertEqual(len(S_ref), L.BOUND["reflection"])
        rot4 = next(M for M in L.all_matrices() if L.kind(M) == "rotation4" and M[8] == 1)    # ось z
        S_rot = [(2, 2, 0), (2, 2, 2), (2, 2, 4)]
        self.assertTrue(L.invariant(S_rot, rot4, n) and len(S_rot) == L.BOUND["rotation4"] and L.statement(S_rot, rot4, n))
        # шаг за границу: любое расширение достигающих примеров одной орбитой ломает условие
        for S, M in ((S_inv, L.INV), (S_rot, rot4)):
            cells = [x for x in itertools.product(range(n), repeat=3) if x not in S]
            self.assertTrue(all(L.has_coplanar4(S + L.orbit(M, x, n)) for x in cells), "граница не точна: есть расширение")

    def test_3_boundary_cases(self):
        b = L.boundary_cases()
        self.assertGreaterEqual(len(b["half_turn_large"][0]), 6)
        self.assertGreaterEqual(len(b["rotation3_large"][0]), 6)
        self.assertFalse(L.has_coplanar4(b["rotoreflection4_orbit_noncoplanar"][0]))
        S, M, n = b["no_three_collinear_analog_fails"]
        self.assertTrue(L.invariant(S, M, n) and L.has_coplanar4(S))
        self.assertFalse(any(L.coplanar(a, b_, c_, c_) for a, b_, c_ in itertools.combinations(S, 3)) and False)  # нет трёх коллинеарных проверяется ниже
        col = lambda p, q, r: all(x == 0 for x in [(q[1]-p[1])*(r[2]-p[2])-(q[2]-p[2])*(r[1]-p[1]), (q[2]-p[2])*(r[0]-p[0])-(q[0]-p[0])*(r[2]-p[2]), (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])])
        self.assertFalse(any(col(*t) for t in itertools.combinations(S, 3)), "аналог: без трёх коллинеарных, но с четырьмя компланарными")

    def test_4_strata_filter_nine_classes_remain(self):
        classes = subgroup_classes(frozenset(L.all_matrices()))
        self.assertEqual(len(classes), 33)
        alive = [i for i, H in enumerate(classes) if not any(L.kind(M) in L.BOUND for M in H)]
        self.assertEqual(alive, [0, 2, 3, 6, 9, 10, 14, 17, 27])
        # у выживших классов нет ни инверсии, ни отражений, ни поворотов порядка 4 — только полуобороты, повороты-3 и S4/S6
        kinds = {L.kind(M) for i in alive for M in classes[i]}
        self.assertTrue(kinds <= {"identity", "half_turn", "rotation3", "rotoreflection4", "rotoreflection6"}, kinds)

    def test_5_even_n_inversion_two(self):
        n = 6; rnd = random.Random(7); best = 0
        for _ in range(30):
            S = L.grow(rnd, L.INV, n); best = max(best, len(S))
            self.assertTrue(L.statement(S, L.INV, n))
        self.assertLessEqual(best, 2, "при чётном n центр не клетка: инвариантное множество — одна антиподальная пара")
        self.assertEqual(best, 2)


if __name__ == "__main__":
    unittest.main()
