"""test_lem_005.py — тест-фальсификатор к lem-005 («модель прямых»: производящая функция для m-подмножеств с ≤ 2 клетками на каждой прямой
направления v и ожидаемое число дважды занятых прямых). Автор теста — втора (не автор леммы). Всё независимо от statement, кроме самих
проверяемых функций: своё разбиение клеток на прямые (инвариант b·x − a·y), свой перебор подмножеств, своя производящая функция.
1. Тождество Z_m и E_m против своего перебора на семи новых случаях (в т. ч. несимметричное направление (2,1), осевое, m нечётное).
2. Своя производящая функция (дроби) = функциям statement на случайных (n, v, m) до n = 9.
3. Зубы: модель независимых клеток и модель «L вместо C(L,2)» не совпадают с точным E_m.
4. Перенормировка spectrum_model: Z_n = (2n² − 3n)/Σ_v E_v по ВСЕМ неосевым примитивным направлениям (обе ориентации по знаку) — своим счётом при n = 8, 10;
   после перенормировки Σ_v c_v·n по всем таким направлениям = 2n² − 3n.
5. Граница: без перенормировки модель занижает (Z_n > 1 при n = 20); дрейф по n есть (c_(1,1) при n = 12 и 24 различаются > 1 %).
6. Применение (слепое измерение втора, база n = 19…57): модель при n = 30 в пределах 15 % от измеренных пятнадцати констант, порядок первых восьми совпадает."""
import itertools, random, unittest
from fractions import Fraction
from math import comb, gcd
import lemmas.lem_005_statement as L

def my_lines(n, a, b):
    """прямые направления (a, b): клетки с одинаковым b·x − a·y."""
    groups = {}
    for x in range(n):
        for y in range(n): groups.setdefault(b * x - a * y, []).append((x, y))
    return list(groups.values())

def my_enum(n, a, b, m):
    lines = my_lines(n, a, b); idx = {c: i for i, ln in enumerate(lines) for c in ln}; cells = [c for ln in lines for c in ln]
    Z = 0; tot = 0
    for S in itertools.combinations(cells, m):
        occ = [0] * len(lines)
        ok = True
        for c in S:
            occ[idx[c]] += 1
            if occ[idx[c]] > 2: ok = False; break
        if not ok: continue
        Z += 1; tot += sum(1 for o in occ if o == 2)
    return Z, (Fraction(tot, Z) if Z else None)

def my_gf(lens, m):
    """[t^k] ∏(1 + L t + C(L,2) t²), k ≤ m, дробями — своя реализация."""
    poly = [Fraction(1)] + [Fraction(0)] * m
    for Lh in lens:
        new = [Fraction(0)] * (m + 1)
        for k in range(m + 1):
            if poly[k]:
                new[k] += poly[k]
                if k + 1 <= m: new[k + 1] += poly[k] * Lh
                if k + 2 <= m: new[k + 2] += poly[k] * comb(Lh, 2)
        poly = new
    return poly

def my_E(lens, m):
    Z = my_gf(lens, m)[m]; s = Fraction(0)
    for i, Lh in enumerate(lens):
        if Lh >= 2: s += comb(Lh, 2) * my_gf(lens[:i] + lens[i+1:], m - 2)[m - 2]
    return s / Z

def my_model(n):
    """E_v для всех неосевых примитивных направлений (a > 0, b ≠ 0, gcd = 1, обе ориентации по знаку b), перенормировка на 2n² − 3n."""
    E = {}
    for a in range(1, n):
        for b in range(-(n - 1), n):
            if b == 0 or gcd(a, abs(b)) != 1: continue
            lens = [len(ln) for ln in my_lines(n, a, b)]; E[(a, b)] = float(my_E(lens, 2 * n))
    Zr = (2 * n * n - 3 * n) / sum(E.values())
    return E, Zr

MEAS = {(1,1): 0.7322, (1,2): 0.5629, (1,3): 0.4567, (2,3): 0.4108, (1,4): 0.3778, (1,5): 0.3073, (2,5): 0.2846, (3,4): 0.3043,
        (1,6): 0.2618, (1,7): 0.2233, (2,7): 0.2081, (3,5): 0.2701, (4,5): 0.2390, (1,8): 0.1859, (3,7): 0.1961}

class TestLem005(unittest.TestCase):
    def test_1_identity_vs_own_enumeration(self):
        for n, a, b, m in ((3, 1, 1, 3), (4, 1, 1, 5), (4, 2, 1, 6), (4, 1, 3, 7), (4, 1, 0, 8), (5, 1, 2, 6), (5, 2, 3, 7)):
            Z, E = my_enum(n, a, b, m); lens = [len(ln) for ln in my_lines(n, a, b)]
            self.assertEqual(Z, L.gf_counts(lens, m)[m], f"Z_m при {(n, a, b, m)}")
            self.assertEqual(E, L.expected_double_lines(lens, m), f"E_m при {(n, a, b, m)}")
            self.assertEqual(sorted(lens), sorted(len(ln) for ln in L.lines_of_direction(n, a, b)), "разбиения на прямые различны")
    def test_2_generating_function_random(self):
        rnd = random.Random(5)
        for _ in range(25):
            n = rnd.randrange(3, 10); a = rnd.randrange(1, n); b = rnd.randrange(-(n - 1), n)
            if gcd(a, abs(b)) != 1 or b == 0: continue
            lens = [len(ln) for ln in my_lines(n, a, b)]; m = rnd.randrange(2, min(2 * n, len(lens) * 2) + 1)
            self.assertEqual(my_gf(lens, m)[m], L.gf_counts(lens, m)[m]); self.assertEqual(my_E(lens, m), L.expected_double_lines(lens, m))
    def test_3_teeth(self):
        lens = [len(ln) for ln in my_lines(5, 1, 2)]; m = 8; N = sum(lens); exact = L.expected_double_lines(lens, m)
        indep = sum(Fraction(comb(Lh, 2) * comb(N - Lh, m - 2), comb(N, m)) for Lh in lens)     # независимые клетки без cap
        self.assertNotEqual(exact, indep, "модель независимых клеток не должна совпадать с точным E_m")
        wrong = Fraction(0); Z = my_gf(lens, m)[m]
        for i, Lh in enumerate(lens): wrong += Lh * my_gf(lens[:i] + lens[i+1:], m - 2)[m - 2]
        self.assertNotEqual(exact, wrong / Z, "L вместо C(L,2) не должно совпадать")
    def test_4_renormalisation_sum(self):
        for n in (8, 10):
            E, Zr = my_model(n); mod, Zr_st = L.spectrum_model(n, keys=((1, 1), (1, 2), (2, 3)))
            self.assertAlmostEqual(Zr, Zr_st, places=9, msg="перенормировка Z_n различна — сумма по направлениям взята иначе")
            self.assertAlmostEqual(sum(E.values()) * Zr, 2 * n * n - 3 * n, places=9)
            for (a, b), v in mod.items():
                mine = (E[(a, b)] + E[(b, a)] + E[(a, -b)] + E[(b, -a)]) / 4 if a != b else (E[(a, b)] + E[(a, -b)]) / 2
                self.assertAlmostEqual(v, mine / n * Zr, places=9, msg=f"c_{(a,b)} при n={n}")
    def test_5_boundary_renorm_and_drift(self):
        _, Zr20 = L.spectrum_model(20, keys=((1, 1),)); self.assertGreater(Zr20, 1.05, "без перенормировки модель должна занижать")
        c12 = L.spectrum_model(12, keys=((1, 1),))[0][(1, 1)]; c24 = L.spectrum_model(24, keys=((1, 1),))[0][(1, 1)]
        self.assertGreater(abs(c12 / c24 - 1), 0.01, "дрейф по n заявлен как граница — он должен быть виден")
    def test_6_blind_measurement_within_15_percent(self):
        mod, _ = L.spectrum_model(30, keys=tuple(MEAS))
        ratios = {k: mod[k] / MEAS[k] for k in MEAS}
        self.assertTrue(all(0.85 <= r <= 1.15 for r in ratios.values()), f"вне 15 %: {ratios}")
        first8 = [(1,1), (1,2), (1,3), (1,4), (2,3), (1,5), (3,4), (2,5)]
        self.assertEqual(sorted(first8, key=lambda k: -MEAS[k]), sorted(first8, key=lambda k: -mod[k]), "порядок первых восьми должен совпасть")

if __name__ == "__main__":
    unittest.main()
