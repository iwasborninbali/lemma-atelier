"""Тесты-фальсификаторы к lem-001 (пишет ДРУГОЙ агент — opus/saturation, 3.09.2026; правило владельца: тесты к чужой лемме).
Ищем: (1) нарушение предиката на случайных законных случаях (d = 2, 3; k = 2, 3) — property-based; (2) более сильная форма —
убийцы q попарно не пересекаются и κ_k(q) ≤ ⌊|S|/k⌋ (противник №1, «против формы» 1); (3) скрытый шаг наследственности:
после удаления R при |R| < min κ оживают только клетки R; (4) off-by-one: при |R| = min κ оживление чужой клетки ВОЗМОЖНО;
(5) граница области: тор (Z_4)^2 — предикат ложен при «нет трёх на прямой тора» (две точки не задают единственной прямой);
на (Z_5)^2 (простой модуль) держится; (6) q ∈ S — утверждение не определено (предикат может быть ложен); (7) непустота теста.
Запуск: python3 -m unittest lemmas.tests.test_lem_001  (из корня ателье)."""
import itertools, random, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import lem_001_statement as L


def empty_cells(S, d, n):
    return [c for c in itertools.product(range(n), repeat=d) if c not in set(S)]


def kappa_map(S, d, n, k):
    return {q: L.killers(S, q, k) for q in empty_cells(S, d, n)}


def admissible_after_removal(S, R, d, n, k):
    S2 = [p for p in S if p not in R]
    return {q for q in itertools.product(range(n), repeat=d) if q not in set(S2) and L.no_kplus1_on_a_line(S2 + [q], k)}


CASES = [(2, 6, 2), (2, 6, 3), (3, 4, 2), (3, 4, 3)]   # (d, n, k) — лёгкие, для Мака


def two_per_line_solutions(n, limit=6):
    """2n точек в n×n без трёх на прямой, по две в строке (DFS по строкам) — у них min κ_2 ≥ 2 по следствию (4) леммы."""
    out = []
    def ok(S, c):
        return not any(L.collinear([a, b, c]) for a, b in itertools.combinations(S, 2))
    def rec(r, S):
        if len(out) >= limit: return
        if r == n: out.append(list(S)); return
        for c1, c2 in itertools.combinations(range(n), 2):
            a, b = (r, c1), (r, c2)
            if ok(S, a) and ok(S + [a], b): rec(r + 1, S + [a, b])
    rec(0, []); return out


class TestLem001(unittest.TestCase):
    def sample(self, seed, d, n, k):
        return L.generate(random.Random(seed), d=d, n=n, k=k)

    def test_1_random_cases(self):
        total_killers = 0
        for d, n, k in CASES:
            for seed in range(3 if d == 2 else 2):
                S, q, _ = self.sample(seed, d, n, k)
                self.assertTrue(L.statement(S, q, k), (d, n, k, seed, S, q))
                total_killers += len(L.killers(S, q, k))
        self.assertGreater(total_killers, 0, "тест пуст: ни одного убийцы во всей выборке")

    def test_2_stronger_form_disjoint_killers_and_bound(self):
        for d, n, k in CASES[:3]:
            for seed in range(3):
                S, _, _ = self.sample(seed, d, n, k)
                for q, K in kappa_map(S, d, n, k).items():
                    for A, B in itertools.combinations(K, 2):
                        self.assertFalse(set(A) & set(B), (d, n, k, seed, q, A, B))
                    self.assertLessEqual(len(K), len(S) // k, (d, n, k, seed, q))

    def test_3_heredity_step_below_min_kappa(self):
        """|R| < min κ ⇒ множество допустимых после удаления R ⊆ R (это и делает лемму сертификатом)."""
        checked = 0
        for n in (5, 6):
            for S in two_per_line_solutions(n):
                d, k = 2, 2
                km = kappa_map(S, d, n, k)
                if not km: continue
                mk = min(len(K) for K in km.values())
                for j in range(1, mk):
                    for R in itertools.islice(itertools.combinations(S, j), 40):
                        self.assertTrue(admissible_after_removal(S, set(R), d, n, k) <= set(R), (n, R)); checked += 1
        self.assertGreater(checked, 0, "тест пуст: ни одного случая с min κ ≥ 2")

    def test_4_off_by_one_at_min_kappa(self):
        """при |R| = min κ чужая клетка оживать МОЖЕТ — значит «радиус не меньше min κ» верно лишь при подходящем определении радиуса."""
        for n in (5, 6):
            for S in two_per_line_solutions(n):
                d, k = 2, 2
                km = kappa_map(S, d, n, k)
                if not km: continue
                mk = min(len(K) for K in km.values())
                for R in itertools.islice(itertools.combinations(S, mk), 200):
                    if admissible_after_removal(S, set(R), d, n, k) - set(R):
                        return  # свидетель off-by-one найден: лемма о j < min κ точна, формулировку с «≥ min κ» надо определить
        self.skipTest("свидетель оживления при |R| = min κ не найден в выборке — утверждение о точности границы не проверено")

    # --- граница области: тор ---
    @staticmethod
    def torus_lines(m):
        lines = set()
        for p in itertools.product(range(m), repeat=2):
            for v in itertools.product(range(m), repeat=2):
                if v == (0, 0): continue
                lines.add(frozenset(((p[0] + t * v[0]) % m, (p[1] + t * v[1]) % m) for t in range(m)))
        return lines

    def torus_statement(self, S, q, k, lines):
        col = lambda pts: any(set(pts) <= ln for ln in lines)
        K = [sub for sub in itertools.combinations(S, k) if col([q, *sub])]
        return all(sum(1 for sub in K if p in sub) <= 1 for p in S), K, col

    def test_5a_torus_Z4_counterexample(self):
        lines = self.torus_lines(4); S = [(0, 0), (1, 0), (1, 2)]; q = (2, 0)
        ok, K, col = self.torus_statement(S, q, 2, lines)
        self.assertFalse(any(col(list(t)) for t in itertools.combinations(S, 3)), "предпосылка: трёх на одной прямой тора нет")
        self.assertFalse(ok, "на (Z_4)^2 через p = (0,0) проходят два убийцы — лемма в форме «любая решётка» ложна")
        self.assertEqual(sum(1 for sub in K if (0, 0) in sub), 2)

    def test_5b_torus_Z5_prime_holds(self):
        lines = self.torus_lines(5); rnd = random.Random(5); cells = list(itertools.product(range(5), repeat=2))
        col = lambda pts: any(set(pts) <= ln for ln in lines)
        for _ in range(20):
            S = []
            for c in rnd.sample(cells, len(cells)):
                if not any(col([a, b, c]) for a, b in itertools.combinations(S, 2)): S.append(c)
            for q in cells:
                if q in S: continue
                self.assertTrue(self.torus_statement(S, q, 2, lines)[0], (S, q))

    def test_6_q_in_S_is_outside_the_statement(self):
        S, _, k = self.sample(0, 2, 6, 2)
        self.assertFalse(all(L.statement(S, q, k) for q in S), "при q ∈ S предикат ложен — определение обязано требовать q ∉ S")

    def test_7_k1_degenerate(self):
        S, q, _ = self.sample(1, 2, 5, 2)
        K = L.killers(S, q, 1)
        self.assertEqual(len(K), len(S), "k = 1: каждая точка — убийца, κ_1 = |S|; лемма формально верна, но эквивалентность пуста")
        self.assertTrue(L.statement(S, q, 1))


if __name__ == "__main__":
    unittest.main()
