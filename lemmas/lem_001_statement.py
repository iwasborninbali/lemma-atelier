"""lem_001_statement.py — исполнимое утверждение lem-001 (единственность убийцы через точку для запрета «k+1 на прямой»).
Предикат, генератор случаев и граничные случаи; тест-фальсификатор пишет ДРУГОЙ агент (правило владельца 3.09).
Утверждение: S ⊂ Z^d без k+1 точек на одной прямой, q — пустая клетка, κ_k(q) = число k-подмножеств S, коллинеарных с q;
для любой p ∈ S число убийц q, содержащих p, не больше 1 (⇒ Δ_p κ_k(q) ≤ 1)."""
import itertools, math, random

def collinear(pts):
    a = pts[0]; d = None
    for b in pts[1:]:
        v = tuple(b[i] - a[i] for i in range(len(a)))
        if all(x == 0 for x in v): return True
        if d is None: d = v; continue
        # параллельность: все 2×2 миноры (d, v) нулевые
        for i, j in itertools.combinations(range(len(a)), 2):
            if d[i] * v[j] - d[j] * v[i] != 0: return False
    return True

def no_kplus1_on_a_line(S, k):
    return not any(collinear(list(sub)) for sub in itertools.combinations(S, k + 1))

def killers(S, q, k):
    return [sub for sub in itertools.combinations(S, k) if collinear([q, *sub])]

def statement(S, q, k):
    """True ⟺ утверждение леммы для данных S, q: через каждую p ∈ S проходит ≤ 1 убийца q (при выполненной предпосылке).
    Определение требует q ∉ S (замечание тестов коллеги 3.09): для q ∈ S предикат вне области — возвращаем False (тест 6).
    k ≥ 2 — предпосылка леммы; при k = 1 утверждение тоже верно (тест 7), ограничение безвредно."""
    if q in S: return False
    K = killers(S, q, k)
    return all(sum(1 for sub in K if p in sub) <= 1 for p in S)

def generate(rnd, d=2, n=6, k=2):
    """случайное максимальное S без k+1 на прямой в [n]^d (жадный рост) и случайная пустая клетка q."""
    cells = list(itertools.product(range(n), repeat=d)); S = []
    while True:
        alive = [c for c in cells if c not in S and no_kplus1_on_a_line(S + [c], k)]
        if not alive: break
        S.append(rnd.choice(alive))
    empty = [c for c in cells if c not in S]
    return S, rnd.choice(empty), k

def boundary_cases():
    """где предпосылка нарушена или запрет другой природы — предикат МОЖЕТ быть ложен, лемма молчит."""
    # (а) предпосылка нарушена: три точки на прямой при k = 2 — через p проходят два «убийцы» клетки q на той же прямой
    S_bad = [(0, 0), (1, 0), (2, 0)]; q_bad = (3, 0)
    # (б) запрет на плоскости (A280537): убийцы q — тройки, компланарные с q; через p их много (см. lem-001 §граница)
    return {"premise_violated": (S_bad, q_bad, 2), "planes_not_lines": "см. kappa_general.py cube4 — Δκ до |S|−2"}

if __name__ == "__main__":
    rnd = random.Random(1); bad = 0
    for _ in range(50):
        S, q, k = generate(rnd, d=2, n=7, k=rnd.choice([2, 3]))
        if not statement(S, q, k): bad += 1
    Sb, qb, kb = boundary_cases()["premise_violated"]
    print("случаи с нарушенной предпосылкой: предикат", statement(Sb, qb, kb), "(ожидаемо может быть False);", "нарушений на 50 законных случаях:", bad)
