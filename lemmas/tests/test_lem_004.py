"""test_lem_004.py — тест-фальсификатор к lem-004 (точное среднее число коллинеарных троек в нуль-модели «две точки в строке и столбце»).
Автор теста — втора (не автор леммы, правило владельца 3.09). Всё независимо от lem_004_statement и lem_002_statement: свой перебор
конфигураций, свой счёт коллинеарности, свои сэмплеры. Из statement берём только формулу formula(n), tau(n), A000938 — то, что проверяем.
1. Точный перебор n = 3, 4, 5 своим кодом: число конфигураций = A001499 (6, 90, 2040), E[T] = formula(n) дробью.
2. τ(n) детерминировано: у каждой перебранной конфигурации (n ≤ 5) и у 300 случайных при n = 8…12 трансверсальных троек ровно tau(n).
3. Общая форма: мера «пара перестановок без совпадений» НЕ равномерна (вес 2^{число циклов}), но S_n×S_n-инвариантна — среднее T
   обязано равняться formula(n): Монте-Карло n = 8, 10, 12 в пределах 4 стандартных ошибок.
4. Зубы: без поправки τ (наивное C(2n,3)) и с GK формула НЕ совпадает с точным средним при n = 4, 5.
5. Граница: мера, инвариантная только под циклическим сдвигом (циркулянтные конфигурации {i+a, i+b} mod n), даёт другое среднее при n = 7.
6. A000938 по формуле Ларросы Каньестро = прямой счёт коллинеарных троек клеток, n = 3…7."""
import itertools, random, unittest
from fractions import Fraction
from math import comb
import lemmas.lem_004_statement as L

def collinear(a, b, c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0
def T(S): return sum(1 for t in itertools.combinations(S, 3) if collinear(*t))
def transversal(S): return sum(1 for a, b, c in itertools.combinations(S, 3) if len({a[0], b[0], c[0]}) == 3 and len({a[1], b[1], c[1]}) == 3)

def all_configs(n):
    """все 0/1-матрицы n×n с суммами 2 по строкам и столбцам — рекурсия по строкам с учётом остатка по столбцам (свой код)."""
    out = []
    def rec(i, colrem, rows):
        if i == n:
            if all(x == 0 for x in colrem): out.append([(r, c) for r, cs in enumerate(rows) for c in cs])
            return
        avail = [c for c in range(n) if colrem[c] > 0]
        for cs in itertools.combinations(avail, 2):
            for c in cs: colrem[c] -= 1
            rec(i + 1, colrem, rows + [cs])
            for c in cs: colrem[c] += 1
    rec(0, [2] * n, []); return out

def sample_perm_pair(n, rnd):
    """конфигурация из двух перестановок без совпадений: строка i → столбцы {σ(i), π(i)}; мера инвариантна под S_n×S_n, но не равномерна."""
    while True:
        s = list(range(n)); rnd.shuffle(s); p = list(range(n)); rnd.shuffle(p)
        if all(s[i] != p[i] for i in range(n)): return [(i, s[i]) for i in range(n)] + [(i, p[i]) for i in range(n)]

class TestLem004(unittest.TestCase):
    def test_1_exact_enumeration_matches_formula(self):
        for n, count in ((3, 6), (4, 90), (5, 2040)):
            cf = all_configs(n); self.assertEqual(len(cf), count, f"A001499({n})")
            mean = Fraction(sum(T(S) for S in cf), len(cf))
            self.assertEqual(mean, L.formula(n), f"n={n}: точное {mean} ≠ формула {L.formula(n)}")
    def test_2_tau_is_deterministic(self):
        for n in (3, 4, 5):
            self.assertEqual({transversal(S) for S in all_configs(n)}, {L.tau(n)})
        rnd = random.Random(4)
        for n in (8, 10, 12):
            self.assertTrue(all(transversal(sample_perm_pair(n, rnd)) == L.tau(n) for _ in range(100)), f"τ({n}) не детерминировано")
    def test_3_invariant_nonuniform_measure_has_same_mean(self):
        rnd = random.Random(7)
        for n, N in ((8, 6000), (10, 4000), (12, 3000)):
            xs = [T(sample_perm_pair(n, rnd)) for _ in range(N)]
            mean = sum(xs) / N; var = sum((x - mean) ** 2 for x in xs) / (N - 1); se = (var / N) ** 0.5
            self.assertLess(abs(mean - float(L.formula(n))), 4 * se + 1e-9, f"n={n}: MC {mean:.3f} ± {se:.3f} против формулы {float(L.formula(n)):.3f}")
    def test_4_teeth_wrong_variants_fail(self):
        for n in (4, 5):
            cf = all_configs(n); mean = Fraction(sum(T(S) for S in cf), len(cf))
            naive = Fraction(L.c_transversal(n) * comb(2 * n, 3), 6 * comb(n, 3) ** 2)
            self.assertNotEqual(mean, naive, "без поправки τ формула не должна совпадать")
            self.assertNotEqual(mean, L.guy_kelly(n), "эвристика GK не должна совпадать")
    def test_5_boundary_cyclic_only_invariance_breaks_formula(self):
        n = 7; means = []
        for a, b in itertools.combinations(range(n), 2):
            S = [(i, (i + a) % n) for i in range(n)] + [(i, (i + b) % n) for i in range(n)]
            self.assertEqual(len(set(S)), 2 * n); means.append(T(S))
        cyc = Fraction(sum(means), len(means))
        self.assertNotEqual(cyc, L.formula(n), "циркулянтная мера (инвариантность только под сдвигом) должна давать другое среднее")
    def test_6_A000938_formula_vs_direct(self):
        for n in range(3, 8):
            cells = [(r, c) for r in range(n) for c in range(n)]
            direct = sum(1 for t in itertools.combinations(cells, 3) if collinear(*t))
            self.assertEqual(direct, L.A000938(n))

if __name__ == "__main__":
    unittest.main()
