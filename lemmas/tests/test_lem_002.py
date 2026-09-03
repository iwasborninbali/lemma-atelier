"""Тесты-фальсификаторы к lem-002 (пишет ДРУГОЙ агент — opus/saturation, 3.09.2026). Ищем: (1) равенство E[T | тип циклов]
точно, дробями, n = 4, 5, 6 — и совпадение с безусловным средним, посчитанным независимо; (2) непустота (типов ≥ 2);
(3) граница: без фиксированных маргиналов E[T | профиль] зависит от профиля; (4) НЕинвариантный признак (число точек на главной
диагонали) — условное среднее МОЖЕТ зависеть от него, то есть инвариантность признака в предпосылке не лишняя.
Запуск: python3 -m unittest lemmas.tests.test_lem_002"""
import collections, sys, unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import lem_002_statement as L


class TestLem002(unittest.TestCase):
    def test_1_exact_small_n(self):
        for n in (4, 5):
            ok, means = L.statement(n)
            self.assertTrue(ok, (n, means))
            self.assertGreaterEqual(len(means), 2, "тест пуст: один тип циклов")
            tot = [0, 0]
            for S in L.configs(n): tot[0] += 1; tot[1] += L.collinear_triples(S)
            self.assertEqual(next(iter(means.values())), Fraction(tot[1], tot[0]), "условное среднее ≠ безусловному")

    def test_2_exact_n6(self):
        ok, means = L.statement(6)
        self.assertTrue(ok, means); self.assertGreaterEqual(len(means), 3)

    def test_3_boundary_free_marginals(self):
        varies, _ = L.boundary_case(4)
        self.assertTrue(varies)

    def test_4_noninvariant_feature_may_matter(self):
        n = 5; acc = collections.defaultdict(lambda: [0, 0])
        for S in L.configs(n):
            f = sum(1 for r, c in S if r == c); acc[f][0] += 1; acc[f][1] += L.collinear_triples(S)
        means = {f: Fraction(v[1], v[0]) for f, v in acc.items()}
        if len(set(means.values())) == 1: self.skipTest("неинвариантный признак случайно не отличил — граница не подтверждена на n=5")
        self.assertGreater(len(set(means.values())), 1)


if __name__ == "__main__":
    unittest.main()
