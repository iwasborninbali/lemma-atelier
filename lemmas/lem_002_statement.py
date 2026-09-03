"""lem_002_statement.py — исполнимое утверждение lem-002 (слепота первого момента к орбитно-инвариантным признакам).
Частный случай для проверки: конфигурации с ровно двумя точками в каждой строке и каждом столбце n×n; признак F — тип циклов 2-фактора
(инвариантен к перестановкам строк и столбцов); B — коллинеарные тройки (у S они все косые: строка и столбец несут ровно две точки). Утверждение: E[#коллинеарных троек | тип] одно и то же для всех типов.
Точный перебор всех конфигураций при n ≤ 6 (A001499(6) = 67 950)."""
import itertools, math, collections
from fractions import Fraction

def configs(n):
    """все конфигурации 2/строку+2/столбец как множества клеток (перебор пар перестановок, дедупликация)."""
    seen = set()
    for a in itertools.permutations(range(n)):
        for b in itertools.permutations(range(n)):
            if any(x == y for x, y in zip(a, b)): continue
            key = frozenset((r, a[r]) for r in range(n)) | frozenset((r, b[r]) for r in range(n))
            if key in seen: continue
            seen.add(key); yield key

def cycle_type(S, n):
    rows = collections.defaultdict(list); cols = collections.defaultdict(list)
    for r, c in S: rows[r].append(c); cols[c].append(r)
    seen = set(); lam = []
    for r0 in range(n):
        if r0 in seen: continue
        r, c, k = r0, rows[r0][0], 0
        while r not in seen:
            seen.add(r); k += 1
            c = rows[r][1] if c == rows[r][0] else rows[r][0]
            r = cols[c][1] if cols[c][0] == r else cols[c][0]
        lam.append(k)
    return tuple(sorted(lam, reverse=True))

def collinear_triples(S):
    P = sorted(S); cnt = 0
    for a, b, c in itertools.combinations(P, 3):
        if (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0: cnt += 1
    return cnt

def statement(n):
    """True ⟺ E[T | тип циклов] одинаково для всех типов (точно, дробями)."""
    acc = collections.defaultdict(lambda: [0, 0])
    for S in configs(n):
        t = cycle_type(S, n); acc[t][0] += 1; acc[t][1] += collinear_triples(S)
    means = {t: Fraction(v[1], v[0]) for t, v in acc.items()}
    return len(set(means.values())) == 1, means

def skew_collinear_triples(S):
    """коллинеарные тройки в попарно разных строках и столбцах — только они лежат в орбите O трансверсальных троек."""
    P = sorted(S); cnt = 0
    for a, b, c in itertools.combinations(P, 3):
        if len({a[0], b[0], c[0]}) == 3 and len({a[1], b[1], c[1]}) == 3 and (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0: cnt += 1
    return cnt

def boundary_case(n=4):
    """модель с НЕфиксированными маргиналами (равномерные 2n-подмножества) и инвариантный признак «мультимножество счётов по строкам»:
    счёт трансверсальных троек N_O(S) не детерминирован, и E[N_B | признак] (B — КОСЫЕ коллинеарные тройки, B ⊂ O) зависит от признака —
    следствие «не зависит от f» не применяется; при этом общая форма E[N_B | 𝒜] = (|B|/|O|)·E[N_O | 𝒜] остаётся верной (правка противника №1:
    считать только косые тройки, иначе смешиваются два отказа)."""
    cells = [(r, c) for r in range(n) for c in range(n)]; acc = collections.defaultdict(lambda: [0, 0, 0])
    for S in itertools.combinations(cells, 2 * n):
        prof = tuple(sorted(collections.Counter(r for r, _ in S).values(), reverse=True))
        acc[prof][0] += 1; acc[prof][1] += skew_collinear_triples(S)
        acc[prof][2] += sum(1 for a, b, c in itertools.combinations(sorted(S), 3) if len({a[0], b[0], c[0]}) == 3 and len({a[1], b[1], c[1]}) == 3)
    means = {p: Fraction(v[1], v[0]) for p, v in acc.items()}
    boundary_case.ratio_ok = all(Fraction(v[1], v[0]) * (6 * math.comb(n, 3) ** 2) == Fraction(v[2], v[0]) * skew_collinear_cells(n) for v in acc.values() if v[2])
    return len(set(means.values())) > 1, means   # общая форма (пропорция в каждом классе) — атрибут boundary_case.ratio_ok

def skew_collinear_cells(n):
    """|B|: коллинеарные тройки клеток n×n не в одной строке/столбце (прямой счёт)."""
    cells = [(r, c) for r in range(n) for c in range(n)]
    return sum(1 for a, b, c in itertools.combinations(cells, 3) if len({a[0], b[0], c[0]}) == 3 and len({a[1], b[1], c[1]}) == 3 and (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0)

def noninvariant_measure_witness():
    """свидетель противника №1: X = {1,2,3}, G = Z/3, k = 1, O = X, N_O ≡ 1, F ≡ const; μ({1}) = μ({2}) = 1/2 НЕ инвариантна ⇒
    E[1{1 ∈ S}] = 1/2 ≠ |B|/|O| = 1/3 — предпосылка инвариантности μ неустранима."""
    return {"E_N_B": Fraction(1, 2), "formula": Fraction(1, 3)}

if __name__ == "__main__":
    for n in (4, 5, 6):
        ok, means = statement(n); print(f"n={n}: типов {len(means)}, E[T|тип] одинаково: {ok}; значение {next(iter(means.values()))}")
    varies, m = boundary_case(4); ratio_ok = boundary_case.ratio_ok; print("граница (маргиналы не фиксированы): E[косых коллинеарных | профиль строк] зависит от профиля:", varies, "; общая форма E[N_B|𝒜]·|O| = |B|·E[N_O|𝒜] держится:", ratio_ok)
