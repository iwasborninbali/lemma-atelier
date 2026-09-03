"""lem_004_statement.py — исполнимое утверждение lem-004 (точное среднее число коллинеарных троек в нуль-модели фиксированных
маргиналов «две точки в каждой строке и столбце»). Предикат, генератор и граничные случаи; тест-фальсификатор пишет ДРУГОЙ агент.
Утверждение: E[T] = c(n)·τ(n)/(6·C(n,3)²), τ(n) = C(2n,3) − 4n² + 6n, c(n) = A000938(n) − 2n·C(n,3)."""
import itertools, sys
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lem_002_statement as L2

def A000938(n):
    """коллинеарные тройки клеток решётки n×n (формула Ларросы Каньестро, OEIS A000938)."""
    return 2 * sum((n-k+1)*(n-m+1)*gcd(k-1, m-1) for k in range(2, n+1) for m in range(2, n+1)) - n*n*(n*n-1)//6

def A000938_direct(n):
    cells = [(r, c) for r in range(n) for c in range(n)]
    return sum(1 for a, b, c in itertools.combinations(cells, 3) if (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]) == 0)

def tau_m(n, m):
    """число трансверсальных троек у каждой m-регулярной конфигурации (v2, обобщение противника №1)."""
    return comb(m*n, 3) - n*(comb(m, 3) + comb(m, 2)*(m*n - m)) - n*(comb(m, 2)*(m*n - 3*m + 2) + comb(m, 3))

def tau(n): return comb(2*n, 3) - 4*n*n + 6*n
def c_transversal(n): return A000938(n) - 2*n*comb(n, 3)
def formula(n): return Fraction(c_transversal(n) * tau(n), 6 * comb(n, 3)**2)

def exact(n):
    """точное E[T] перебором всех конфигураций (A001499(n) штук) — не использует формулу."""
    tot = [0, 0]
    for S in L2.configs(n): tot[0] += 1; tot[1] += L2.collinear_triples(S)
    return Fraction(tot[1], tot[0])

def transversal_count(S):
    return sum(1 for a, b, c in itertools.combinations(sorted(S), 3) if len({a[0], b[0], c[0]}) == 3 and len({a[1], b[1], c[1]}) == 3)

def statement(n):
    """True ⟺ формула совпадает с точным средним при данном n (и τ(n) — число трансверсальных троек у КАЖДОЙ конфигурации)."""
    return exact(n) == formula(n) and {transversal_count(S) for S in L2.configs(n)} == {tau(n)}

def generate(): return [3, 4, 5, 6]

def formula_m(n, m): return Fraction(c_transversal(n) * tau_m(n, m), 6 * comb(n, 3)**2) + 2*n*comb(m, 3)

def configs_m(n, m):
    """все m-регулярные конфигурации n×n (перебор по строкам с контролем столбцов) — для маленьких n."""
    rows = list(itertools.combinations(range(n), m))
    def rec(r, colcount, acc):
        if r == n:
            if all(c == m for c in colcount): yield frozenset(acc)
            return
        for cols in rows:
            if all(colcount[c] < m for c in cols):
                for c in cols: colcount[c] += 1
                yield from rec(r + 1, colcount, acc + [(r, c) for c in cols])
                for c in cols: colcount[c] -= 1
    yield from rec(0, [0]*n, [])

def exact_m(n, m):
    tot = [0, 0]
    for S in configs_m(n, m): tot[0] += 1; tot[1] += L2.collinear_triples(S)
    return Fraction(tot[1], tot[0])

def statement_m(n, m):
    """True ⟺ формула для m-регулярных конфигураций совпадает с перебором и τ_m детерминировано."""
    return exact_m(n, m) == formula_m(n, m) and {transversal_count(S) for S in configs_m(n, m)} == {tau_m(n, m)}

def naive_skew_ratio(n):
    """наивная модель «2n клеток равномерно», но только косые тройки, делённая на E[T]: 0.600 (n=4) … → 1 (граница (а) v2)."""
    return Fraction(c_transversal(n) * comb(2*n, 3), comb(n*n, 3)) / formula(n)

def naive_uniform(n):
    """НАША наивная модель «2n клеток равномерно» (атрибуция Гаю–Келли — UNSPECIFIED до чтения первоисточника)."""
    return Fraction(A000938(n) * comb(2*n, 3), comb(n*n, 3))

guy_kelly = naive_uniform   # старое имя — для тестов коллеги; модель НАША, не Гая–Келли

def boundary_cases(n=4):
    """(а) без фиксированных маргиналов (равномерные 2n-подмножества) среднее другое — и равно GK; (б) неинвариантный признак
    (число точек в классе чётности (odd, odd)) меняет условное среднее — это need-003, шаг 2."""
    cells = [(r, c) for r in range(n) for c in range(n)]; tot = [0, 0]
    for S in itertools.combinations(cells, 2*n): tot[0] += 1; tot[1] += L2.collinear_triples(S)
    uniform = Fraction(tot[1], tot[0])
    acc = {}
    for S in L2.configs(n):
        k = sum(1 for r, c in S if r % 2 == 1 and c % 2 == 1); acc.setdefault(k, [0, 0]); acc[k][0] += 1; acc[k][1] += L2.collinear_triples(S)
    by_parity = {k: Fraction(v[1], v[0]) for k, v in sorted(acc.items())}
    return {"uniform_subsets_mean": uniform, "guy_kelly": naive_uniform(n), "formula": formula(n), "by_parity_class": by_parity}

if __name__ == "__main__":
    for n in (3, 4, 5): print(f"n={n}: точно {exact(n)}, формула {formula(n)}, наивная равномерная {naive_uniform(n)} (×{float(naive_uniform(n)/formula(n)):.2f}), утверждение: {statement(n)}")
    for n, m in ((4, 1), (5, 1), (4, 3), (5, 3)): print(f"m-регулярно (n={n}, m={m}): точно {exact_m(n, m)}, формула {formula_m(n, m)}, утверждение: {statement_m(n, m)}")
    print("τ_m у всех конфигураций:", {(n, m): (sorted({transversal_count(S) for S in configs_m(n, m)}), tau_m(n, m)) for n, m in ((4, 1), (5, 1), (4, 3), (5, 2), (5, 3))})
    print("наивная без осевых / E[T] (граница (а)):", {n: round(float(naive_skew_ratio(n)), 3) for n in (4, 6, 10, 20, 46, 100, 300)})
    print("(1 − r)·n → 3:", {n: round(float((1 - naive_skew_ratio(n)) * n), 3) for n in (20, 100, 300, 1000)})
    b = boundary_cases(4); print("граница n=4: равномерные 8-подмножества:", b["uniform_subsets_mean"], "= наивная равномерная:", b["uniform_subsets_mean"] == b["guy_kelly"], "; по классу чётности:", {k: str(v) for k, v in b["by_parity_class"].items()})
