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

    def test_4_noninvariant_feature_deterministic_falsifier(self):
        """противник №1, п. 14: при n = 6 класс «шесть точек на главной диагонали» непуст (a = id, b — дерандж), любые три из них
        коллинеарны ⇒ E[T | d = 6] ≥ C(6,3) = 20 > 154/25 — неинвариантный признак меняет условное среднее; без skipTest."""
        n = 6; acc = collections.defaultdict(lambda: [0, 0])
        for S in L.configs(n):
            d = sum(1 for r, c in S if r == c); acc[d][0] += 1; acc[d][1] += L.collinear_triples(S)
        self.assertIn(6, acc, "класс d = 6 должен быть непуст")
        self.assertGreaterEqual(Fraction(acc[6][1], acc[6][0]), 20)
        self.assertNotEqual(Fraction(acc[6][1], acc[6][0]), Fraction(154, 25))

    def test_5_predicted_value_before_enumeration(self):
        """противник №1, п. 15: предсказанное число |B|·N_O/|O| (lem-004: c(n)·τ(n)/(6·C(n,3)²)) против перебора — n = 4, 5, 6."""
        from math import comb, gcd
        A000938 = lambda n: 2 * sum((n-k+1)*(n-m+1)*gcd(k-1, m-1) for k in range(2, n+1) for m in range(2, n+1)) - n*n*(n*n-1)//6
        for n, expect in ((4, Fraction(2)), (5, Fraction(13, 3)), (6, Fraction(154, 25))):
            c = A000938(n) - 2*n*comb(n, 3); tau = comb(2*n, 3) - 4*n*n + 6*n
            self.assertEqual(Fraction(c * tau, 6 * comb(n, 3)**2), expect)
            ok, means = L.statement(n)
            self.assertEqual(next(iter(means.values())), expect)

    def test_6_noninvariant_measure_breaks_it(self):
        """противник №1, п. 7: X = {1,2,3}, G = Z/3, k = 1, O = X, F ≡ const; μ({1}) = μ({2}) = 1/2 — НЕинвариантна ⇒
        E[1{1 ∈ S}] = 1/2 ≠ |B|·N_O/|O| = 1/3. Предпосылка инвариантности меры неустранима."""
        mu = {frozenset({1}): Fraction(1, 2), frozenset({2}): Fraction(1, 2)}
        e = sum(w for S, w in mu.items() if 1 in S)
        self.assertNotEqual(e, Fraction(1, 3)); self.assertEqual(e, Fraction(1, 2))
        # инвариантная версия той же меры — формула верна
        mu_inv = {frozenset({i}): Fraction(1, 3) for i in (1, 2, 3)}
        self.assertEqual(sum(w for S, w in mu_inv.items() if 1 in S), Fraction(1, 3))

    def test_7_second_moment_is_not_blind(self):
        """противник №1 п. 13 и №2 п. 4: Var[T | тип циклов] при n = 6 различна — и равна заявленным в lem-002 v2 дробям
        (285968/16875 (2,2,2), 1313533/101250 (4,2), 247199/22500 (6), 245599/22500 (3,3)); P(T = 0 | тип) = 0, 1/4050, 7/7200, 1/1800."""
        n = 6; acc = collections.defaultdict(lambda: [0, 0, 0, 0])
        for S in L.configs(n):
            t = L.cycle_type(S, n); T = L.collinear_triples(S); a = acc[t]; a[0] += 1; a[1] += T; a[2] += T * T; a[3] += (T == 0)
        var = {t: Fraction(v[2], v[0]) - Fraction(v[1], v[0]) ** 2 for t, v in acc.items()}
        p0 = {t: Fraction(v[3], v[0]) for t, v in acc.items()}
        self.assertEqual(var[(2, 2, 2)], Fraction(285968, 16875)); self.assertEqual(var[(4, 2)], Fraction(1313533, 101250))
        self.assertEqual(var[(6,)], Fraction(247199, 22500)); self.assertEqual(var[(3, 3)], Fraction(245599, 22500))
        self.assertEqual(p0, {(2, 2, 2): 0, (4, 2): Fraction(1, 4050), (6,): Fraction(7, 7200), (3, 3): Fraction(1, 1800)})
        self.assertEqual({t: v[0] for t, v in acc.items()}, {(6,): 43200, (4, 2): 16200, (3, 3): 7200, (2, 2, 2): 1350})
        self.assertGreater(len(set(var.values())), 1)

    def test_8_general_form_ratio_checked_by_assert(self):
        """противник №2 п. 7(в): усиленная общая форма E[N_B | 𝒜]·|O| = |B|·E[N_O | 𝒜] должна проверяться ассертом, не печатью."""
        L.boundary_case(4)
        ratio_ok = getattr(L.boundary_case, "ratio_ok", None)
        self.assertIsNotNone(ratio_ok, "boundary_case не выставляет ratio_ok")
        self.assertTrue(ratio_ok)

if __name__ == "__main__":
    unittest.main()
