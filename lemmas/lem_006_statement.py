"""lem_006_statement.py — исполнимое утверждение lem-006 (теорема окна HJSW: точный максимум no-three-in-line подмножества модулярной
гиперболы в окне 2p×2p). Код независим от slack/hjsw_window_check.py статьи (не читался): точки, богатые прямые (перебор пар), компоненты,
точный максимум и число максимумов — всё заново. Тест-фальсификатор пишет ДРУГОЙ агент.

Утверждение (Theorem main, hjsw_window v1.17). p — нечётное простое, h = (p−1)/2, c ∈ F_p^*, окно HJSW G_p = {−h..3h+1} × {0..2p−1},
P = {(x, y) ∈ G_p : xy ≡ c (mod p)}, |P| = 4(p−1). Множество законно, если нет трёх коллинеарных. Тогда:
 (i)  всякая прямая с ≥ 3 точками P имеет наклон ±1; таких прямых 3(p−1)/2 − s (p−1 с тремя точками, (p−1)/2 − s с четырьмя);
      ровно 2s точек P не лежат ни на одной богатой прямой; s = [c — КВ] + [−c — КВ] ∈ {0, 1, 2};
 (ii) максимум законного подмножества P равен 3(p−1) (и ЛП-релаксация «≤ 2 на богатую прямую» тоже даёт 3(p−1));
 (iii) число законных подмножеств размера 3(p−1) равно 9^s.
Theorem window: для любого окна W = [x0, x0+2p) × [y0, y0+2p) максимум законного подмножества H_c ∩ W не больше 3(p−1)."""
import itertools, math, random, collections

def is_qr(a, p): return pow(a % p, (p - 1) // 2, p) == 1

def s_of(c, p): return int(is_qr(c, p)) + int(is_qr(-c, p))

def points(p, c, x0=None, y0=None):
    """точки H_c в окне [x0, x0+2p) × [y0, y0+2p); по умолчанию — окно HJSW (x0 = −h, y0 = 0)."""
    h = (p - 1) // 2
    if x0 is None: x0 = -h
    if y0 is None: y0 = 0
    return [(x, y) for x in range(x0, x0 + 2 * p) for y in range(y0, y0 + 2 * p) if (x * y - c) % p == 0]

def rich_lines(P):
    """прямые с ≥ 3 точками P: перебор пар, ключ прямой — нормированное (a, b, c) для ax + by = c."""
    lines = collections.defaultdict(set)
    for (x1, y1), (x2, y2) in itertools.combinations(P, 2):
        a, b = y2 - y1, x1 - x2; g = math.gcd(a, b); a //= g; b //= g
        if a < 0 or (a == 0 and b < 0): a, b = -a, -b
        cc = a * x1 + b * y1
        lines[(a, b, cc)].update([(x1, y1), (x2, y2)])
    return {k: frozenset(v) for k, v in lines.items() if len(v) >= 3}

def slope(key):
    a, b, _ = key
    return 'inf' if b == 0 else (0 if a == 0 else -a / b)

def components(P, L):
    """компоненты связности гиперграфа «точки — богатые прямые»."""
    parent = {q: q for q in P}
    def find(q):
        while parent[q] != q: parent[q] = parent[parent[q]]; q = parent[q]
        return q
    for pts in L.values():
        it = iter(pts); r = find(next(it))
        for q in it: parent[find(q)] = r
    comp = collections.defaultdict(list)
    for q in P: comp[find(q)].append(q)
    return list(comp.values())

def max_lawful(P, L):
    """точный максимум |S| при |S ∩ ℓ| ≤ 2 для всех богатых ℓ (⟺ законность) и число максимумов: по компонентам, в компоненте — DFS с отсечением."""
    total = 0; count = 1
    for C in components(P, L):
        lines_of = {q: [l for l, pts in L.items() if q in pts] for q in C}
        Cs = sorted(C, key=lambda q: -len(lines_of[q])); n = len(Cs)
        best = [0, 0]; load = collections.Counter(); nodes = [0]
        def dfs(i, size):
            nodes[0] += 1
            if nodes[0] > 5_000_000: raise RuntimeError("перебор слишком велик для этой компоненты (граничный случай) — нужна другая техника")
            # верхняя оценка: оставшиеся точки, но не больше суммарной свободной ёмкости их богатых прямых (точка на прямой без ёмкости не войдёт)
            rest = [q for q in Cs[i:] if all(load[l] < 2 for l in lines_of[q])]
            if size + len(rest) < best[0] or (size + len(rest) == best[0] and False): return
            if i == n:
                if size > best[0]: best[0], best[1] = size, 1
                elif size == best[0]: best[1] += 1
                return
            q = Cs[i]
            if all(load[l] < 2 for l in lines_of[q]):
                for l in lines_of[q]: load[l] += 1
                dfs(i + 1, size + 1)
                for l in lines_of[q]: load[l] -= 1
            dfs(i + 1, size)
        dfs(0, 0); total += best[0]; count *= best[1]
    return total, count

def statement(p, c):
    """True ⟺ (i)–(iii) для (p, c): наклоны ±1, число богатых прямых и их размеры, Z = 2s, максимум 3(p−1), число максимумов 9^s."""
    P = points(p, c); L = rich_lines(P); s = s_of(c, p)
    if len(P) != 4 * (p - 1): return False
    if any(slope(k) not in (1.0, -1.0) for k in L): return False
    sizes = collections.Counter(len(v) for v in L.values())
    if sizes.get(3, 0) != p - 1 or sizes.get(4, 0) != (p - 1) // 2 - s or set(sizes) - {3, 4}: return False
    on_rich = set().union(*L.values()) if L else set()
    if len(P) - len(on_rich) != 2 * s: return False
    m, cnt = max_lawful(P, L)
    return m == 3 * (p - 1) and cnt == 9 ** s

def statement_window(p, c, x0, y0):
    """True ⟺ максимум законного подмножества H_c ∩ W не больше 3(p−1) для окна W = [x0, x0+2p) × [y0, y0+2p)."""
    P = points(p, c, x0, y0); L = rich_lines(P)
    return max_lawful(P, L)[0] <= 3 * (p - 1)

def generate(rnd, pmax=13):
    """случайные (p, c) и случайное окно."""
    primes = [q for q in range(3, pmax + 1) if all(q % d for d in range(2, int(q ** 0.5) + 1))]
    p = rnd.choice(primes); c = rnd.randrange(1, p); x0 = rnd.randrange(-p, p); y0 = rnd.randrange(-p, p)
    return p, c, x0, y0

def boundary_cases(p=7):
    """за границей условий: (а) составной модуль m = 9 — лемма Лагранжа (≤ 2 класса на прямой) не работает, богатые прямые других наклонов;
    (б) окно шире 2p (2p+1 столбцов) — точек больше, максимум может превысить 3(p−1); (в) две гиперболы H(1) ∪ H(−1) в окне HJSW —
    максимум больше 3(p−1) (статья: ≤ 4(p−1) − 4m₈)."""
    out = {}
    m = 9; h = 4; Pm = [(x, y) for x in range(-h, 3 * h + 2) for y in range(0, 2 * m) if (x * y - 1) % m == 0]
    Lm = rich_lines(Pm); out["composite_modulus_9_slopes"] = sorted({slope(k) for k in Lm}, key=str)
    p = min(p, 5)   # компоненты у объединений велики — граничные случаи считаем при p = 5
    h = (p - 1) // 2; Pw = [(x, y) for x in range(-h, 3 * h + 3) for y in range(0, 2 * p) if (x * y - 1) % p == 0]
    out["wider_window_max"] = (max_lawful(Pw, rich_lines(Pw))[0], 3 * (p - 1))
    P2 = sorted(set(points(p, 1)) | set(points(p, p - 1))); out["two_hyperbolae_max"] = (max_lawful(P2, rich_lines(P2))[0], 3 * (p - 1))
    return out

if __name__ == "__main__":
    for p in (3, 5, 7, 11, 13):
        res = [statement(p, c) for c in range(1, p)]
        P = points(p, 1); L = rich_lines(P); m, cnt = max_lawful(P, L)
        print(f"p={p}: statement верно для всех c: {all(res)}; c=1: |P|={len(P)}, богатых прямых {len(L)}, max={m} (3(p−1)={3*(p-1)}), максимумов {cnt} (9^s={9**s_of(1, p)})")
    rnd = random.Random(1); ok = all(statement_window(*generate(rnd, 11)) for _ in range(30)); print("30 случайных окон (p ≤ 11): max ≤ 3(p−1):", ok)
    print("граница:", boundary_cases(7))
