"""lem_005_statement.py — исполнимое утверждение кандидата lem-005 («модель прямых» для спектра направлений; need-008).
Предикат, генератор и граничные случаи; тест-фальсификатор пишет ДРУГОЙ агент.

Утверждение (точное, доказуемое). Пусть прямые направления v в решётке n×n имеют длины L_1, …, L_r (каждая клетка ровно на одной
прямой). Рассмотрим равномерное распределение на m-подмножествах клеток, у которых на каждой прямой направления v не больше двух
клеток. Тогда число таких подмножеств Z_m = [t^m] ∏_i (1 + L_i t + C(L_i,2) t²), а ожидаемое число прямых с ровно двумя выбранными
клетками равно E_m = (1/Z_m) Σ_i C(L_i,2) · [t^{m−2}] ∏_{j≠i} (1 + L_j t + C(L_j,2) t²).
Использование (не часть утверждения): при m = 2n и одной перенормировке на 2n² − 3n значения E_{2n}/n воспроизводят абсолютный спектр
направлений базы Фламменкампа в 5–10 % (need-008, шаг 2)."""
import itertools
from math import comb, gcd
from fractions import Fraction

def lines_of_direction(n, a, b):
    """прямые направления (a,b) как списки клеток; каждая клетка ровно на одной прямой."""
    seen = set(); lines = []
    for x in range(n):
        for y in range(n):
            if (x, y) in seen: continue
            cx, cy = x, y
            while 0 <= cx - a < n and 0 <= cy - b < n: cx -= a; cy -= b
            ln = []; px, py = cx, cy
            while 0 <= px < n and 0 <= py < n: seen.add((px, py)); ln.append((px, py)); px += a; py += b
            lines.append(ln)
    return lines

def poly_mul(p, q, m):
    out = [Fraction(0)] * (m + 1)
    for i, a in enumerate(p):
        if a == 0: continue
        for j, b in enumerate(q):
            if i + j > m: break
            out[i + j] += a * b
    return out

def gf_counts(lens, m):
    """Z_k для k ≤ m и, для каждой прямой i, коэффициенты произведения без i."""
    poly = [Fraction(1)]
    for L in lens: poly = poly_mul(poly, [Fraction(1), Fraction(L), Fraction(comb(L, 2))], m)
    return poly

def expected_double_lines(lens, m):
    """E_m по формуле утверждения (дроби)."""
    poly = gf_counts(lens, m); Z = poly[m] if m < len(poly) else Fraction(0)
    if Z == 0: return None
    E = Fraction(0)
    for i, L in enumerate(lens):
        if L < 2: continue
        others = lens[:i] + lens[i+1:]; q = gf_counts(others, m - 2)
        E += comb(L, 2) * (q[m - 2] if m - 2 < len(q) else 0)
    return E / Z

def exact_by_enumeration(lines, m):
    """прямой перебор всех m-подмножеств клеток с ≤ 2 на прямой: среднее число прямых с двумя клетками (маленькие n)."""
    cells = [c for ln in lines for c in ln]; line_of = {c: i for i, ln in enumerate(lines) for c in ln}
    tot = 0; cnt = 0
    for S in itertools.combinations(cells, m):
        occ = [0] * len(lines)
        for c in S: occ[line_of[c]] += 1
        if max(occ) > 2: continue
        cnt += 1; tot += sum(1 for o in occ if o == 2)
    return (Fraction(tot, cnt) if cnt else None), cnt

def statement(n, a, b, m):
    """True ⟺ формула совпадает с прямым перебором для решётки n×n, направления (a,b), m точек."""
    lines = lines_of_direction(n, a, b); lens = [len(l) for l in lines]
    e_formula = expected_double_lines(lens, m); e_exact, cnt = exact_by_enumeration(lines, m)
    poly = gf_counts(lens, m)
    return e_formula == e_exact and poly[m] == cnt

def generate():
    return [(3, 1, 1, 4), (3, 1, 2, 5), (4, 1, 1, 6), (4, 1, 2, 7), (4, 1, 3, 8), (4, 2, 3, 8), (5, 1, 1, 8)]

def spectrum_model(n, keys=((1,1), (1,2), (1,3), (2,3), (1,4), (1,5), (2,5), (3,4))):
    """использование: c_v модели прямых при m = 2n с перенормировкой на 2n² − 3n (float)."""
    from collections import Counter
    def E2(a, b):
        mm = 2 * n; cnt = Counter(len(l) for l in lines_of_direction(n, a, b)); poly = [0.0] * (mm + 1); poly[0] = 1.0
        for L, c in cnt.items():
            for _ in range(c):
                new = [0.0] * (mm + 1)
                for k in range(mm + 1):
                    if poly[k] == 0.0: continue
                    new[k] += poly[k]
                    if k + 1 <= mm: new[k + 1] += poly[k] * L
                    if k + 2 <= mm and L >= 2: new[k + 2] += poly[k] * comb(L, 2)
                poly = new
        Z = poly[mm]; E = 0.0
        for L, c in cnt.items():
            if L < 2: continue
            q = [0.0] * (mm + 1); r = poly[:]
            for k in range(mm + 1):
                q[k] = r[k]
                if k + 1 <= mm: r[k + 1] -= q[k] * L
                if k + 2 <= mm: r[k + 2] -= q[k] * comb(L, 2)
            E += c * comb(L, 2) * q[mm - 2] / Z
        return E
    total = 0.0; per = {}
    for a in range(0, n):
        for b in range(-(n - 1), n):
            if (a, b) == (0, 0) or (a == 0 and b < 0) or gcd(a, abs(b)) != 1 or a == 0 or b == 0: continue
            e = E2(a, b); total += e; per.setdefault((min(a, abs(b)), max(a, abs(b))), []).append(e)
    Zr = (2 * n * n - 3 * n) / total
    return {k: sum(per[k]) / len(per[k]) / n * Zr for k in keys}, Zr

def boundary_cases():
    """(а) без перенормировки модель систематически ниже базы на 13–26 % (n=20); (б) модель не воспроизводит константность по n
    (дрейф 3–8 % между n=20 и 40); (в) осевые направления: cap 2 выполняется тождественно (ровно две в строке), формула даёт E = n."""
    return {"axis_n4_two_per_row": expected_double_lines([4, 4, 4, 4], 8)}

if __name__ == "__main__":
    for n, a, b, m in generate(): print(f"n={n} v=({a},{b}) m={m}: утверждение {statement(n, a, b, m)}")
    print("осевое направление n=4, m=8 (две в каждой строке): E =", boundary_cases()["axis_n4_two_per_row"])
    mod, Z = spectrum_model(20); MEAS = {(1,1): 0.7306, (1,2): 0.5633, (1,3): 0.4545, (2,3): 0.4095, (1,4): 0.3744, (1,5): 0.3073, (2,5): 0.2846, (3,4): 0.3043}
    print("n=20, Z=%.3f:" % Z, {k: (round(v, 4), round(v / MEAS[k], 3)) for k, v in mod.items()})
