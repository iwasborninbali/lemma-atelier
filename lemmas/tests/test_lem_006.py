"""Тесты-фальсификаторы к lem-006 (пишет ДРУГОЙ агент — opus/saturation, 3.09.2026). Свой код: коллинеарность через векторные произведения,
свой перебор максимума DFS (без богатых прямых), свой перебор прямых. Ищем: (1) расхождение своего максимума и числа максимумов с
max_lawful коллеги и с формулой 3(p−1), 9^s при p = 3, 5, 7 (все c); (2) наклоны богатых прямых ±1 — своим перебором при p = 5, 7, 11;
(3) зубы за границей: окно 2p+1 при p=5 ломает 3(p−1); две гиперболы при p=5 ломают; составной модуль 9 даёт прямые других наклонов;
(4) окно Theorem window — случайные окна при p ≤ 11 (её statement_window) плюс мои собственные окна с отрицательными сдвигами;
(5) непустота: |P| = 4(p−1), богатых прямых 3(p−1)/2 − s. Запуск: python3 -m unittest lemmas.tests.test_lem_006"""
import itertools, math, random, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import lem_006_statement as L


def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0


def my_max_and_count(P):
    """максимум no-three-in-line подмножества P и число максимумов — DFS по точкам с проверкой коллинеарности (без богатых прямых)."""
    P = sorted(P); N = len(P); best = [0, 0]
    bad = [[] for _ in range(N)]   # для точки k: пары (i, j) < k, коллинеарные с k
    for i, j, k in itertools.combinations(range(N), 3):
        if collinear(P[i], P[j], P[k]): bad[k].append((i, j))
    chosen = []
    def rec(k):
        if k == N:
            if len(chosen) > best[0]: best[0], best[1] = len(chosen), 1
            elif len(chosen) == best[0]: best[1] += 1
            return
        if len(chosen) + (N - k) < best[0]: return   # отсечение: не догнать текущий максимум
        rec(k + 1)
        s = set(chosen)
        if not any(i in s and j in s for i, j in bad[k]):
            chosen.append(k); rec(k + 1); chosen.pop()
    rec(0); return best[0], best[1]


def my_rich_slopes(P):
    lines = {}
    for a, b in itertools.combinations(P, 2):
        dx, dy = b[0]-a[0], b[1]-a[1]; g = math.gcd(dx, dy); dx //= g; dy //= g
        if dx < 0 or (dx == 0 and dy < 0): dx, dy = -dx, -dy
        key = (dx, dy, dy*a[0] - dx*a[1]); lines.setdefault(key, set()).update([a, b])
    return {(k[0], k[1]) for k, v in lines.items() if len(v) >= 3}


class TestLem006(unittest.TestCase):
    def test_1_max_and_count_small_p(self):
        for p in (3, 5, 7):
            for c in range(1, p):
                P = L.points(p, c); s = L.s_of(c, p)
                self.assertEqual(len(P), 4*(p-1))
                m, cnt = my_max_and_count(P)
                self.assertEqual(m, 3*(p-1), (p, c, m)); self.assertEqual(cnt, 9**s, (p, c, cnt, s))
                m2, cnt2 = L.max_lawful(P, L.rich_lines(P))
                self.assertEqual((m, cnt), (m2, cnt2), "свой перебор и max_lawful коллеги расходятся")

    def test_2_rich_slopes_pm1_and_counts(self):
        for p in (5, 7, 11):
            for c in (1, 2, p-1):
                P = L.points(p, c); s = L.s_of(c, p)
                self.assertTrue(my_rich_slopes(P) <= {(1, 1), (1, -1)}, (p, c, my_rich_slopes(P)))
                Lr = L.rich_lines(P); self.assertEqual(len(Lr), 3*(p-1)//2 - s, (p, c, len(Lr)))
                self.assertGreater(len(Lr), 0)

    def test_3_teeth_beyond_the_boundary(self):
        b = L.boundary_cases(5)
        self.assertGreater(b["wider_window_max"][0], b["wider_window_max"][1], "окно 2p+1 при p=5 должно превышать 3(p−1)")
        self.assertGreater(b["two_hyperbolae_max"][0], b["two_hyperbolae_max"][1], "две гиперболы при p=5 должны превышать 3(p−1)")
        self.assertFalse(set(map(str, b["composite_modulus_9_slopes"])) <= {"1.0", "-1.0"}, "модуль 9: должны быть другие наклоны")
        # свой зуб: при p=5 окно 2p+1 — свой перебор
        p, h = 5, 2; Pw = [(x, y) for x in range(-h, 3*h+3) for y in range(0, 2*p) if (x*y - 1) % p == 0]
        self.assertGreater(my_max_and_count(Pw)[0], 3*(p-1))

    def test_4_window_theorem_random_and_shifted(self):
        rnd = random.Random(6)
        for _ in range(12):
            p, c, x0, y0 = L.generate(rnd, 11); self.assertTrue(L.statement_window(p, c, x0, y0), (p, c, x0, y0))
        for p in (5, 7):
            for (x0, y0) in ((-p, -p), (0, 0), (1, -3), (-2, 5)):
                P = L.points(p, 1, x0, y0); self.assertLessEqual(my_max_and_count(P)[0], 3*(p-1), (p, x0, y0))

    def test_5_statement_p_up_to_13(self):
        for p in (11, 13):
            self.assertTrue(L.statement(p, 1)); self.assertTrue(L.statement(p, p-1))


if __name__ == "__main__":
    unittest.main()
