"""lem_003_statement.py — исполнимое утверждение lem-003 (симметрии, несовместимые с запретом «четыре в плоскости»).
Предикат, генератор случаев и граничные случаи; тест-фальсификатор пишет ДРУГОЙ агент (правило владельца 3.09).

Утверждение. Пусть S ⊂ [n]³ (клетки куба) без четырёх компланарных точек, и пусть S инвариантно относительно движения M куба
(M — одна из 48 знаковых перестановочных матриц, действующая относительно центра куба). Тогда:
  (i)   если M = −I (инверсия),                      то |S| ≤ 3 (и S ⊂ прямая через центр);
  (ii)  если M — отражение (det −1, след 1),          то |S| ≤ 5 (вне зеркала ≤ 2 точки, на зеркале ≤ 3);
  (iii) если M — поворот порядка 4 (det 1, порядок 4), то S лежит на оси поворота, |S| ≤ 3;
  (iv)  если M — поворотное отражение порядка 6 (det −1, порядок 6), то M³ = −I и по (i) |S| ≤ 3, S на прямой через центр.
В случаях (i), (iii), (iv) S коллинеарно (v2, противник №1). Для полуоборотов, поворотов порядка 3 и поворотных отражений порядка 4
ограничения такого рода нет (см. boundary_cases). При |S| ≥ 4 запрет «четыре в плоскости» влечёт «нет трёх на прямой» (тройка на прямой
плюс любая четвёртая точка компланарны), поэтому модели «≤ 3 на плоскости» и «≤ 3 на плоскости и ≤ 2 на прямой» различаются только при |S| ≤ 3."""
import itertools, random

# ---------- группа куба: знаковые перестановочные матрицы 3×3 как кортежи из 9 чисел ----------
IDENT = (1, 0, 0, 0, 1, 0, 0, 0, 1); INV = (-1, 0, 0, 0, -1, 0, 0, 0, -1)

def all_matrices():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3): M[i][perm[i]] = signs[i]
            out.append(tuple(M[0] + M[1] + M[2]))
    return out

def mul(A, B): return tuple(sum(A[3*i+k] * B[3*k+j] for k in range(3)) for i in range(3) for j in range(3))
def det(M): return M[0]*(M[4]*M[8]-M[5]*M[7]) - M[1]*(M[3]*M[8]-M[5]*M[6]) + M[2]*(M[3]*M[7]-M[4]*M[6])
def trace(M): return M[0] + M[4] + M[8]
def order(M):
    k, A = 1, M
    while A != IDENT: A = mul(A, M); k += 1
    return k

def act(M, cell, n):
    """действие относительно центра куба ((n−1)/2, …): координаты удваиваются, чтобы остаться в целых."""
    m = n - 1; c = tuple(2 * cell[i] - m for i in range(3))
    d = tuple(sum(M[3*i+k] * c[k] for k in range(3)) for i in range(3))
    return tuple((d[i] + m) // 2 for i in range(3))

def kind(M):
    """'inversion' | 'reflection' | 'rotation4' | 'half_turn' | 'rotation3' | 'rotoreflection4' | 'rotoreflection6' | 'identity'"""
    if M == IDENT: return 'identity'
    if M == INV: return 'inversion'
    d, o = det(M), order(M)
    if d == -1 and trace(M) == 1: return 'reflection'
    if d == 1: return {2: 'half_turn', 3: 'rotation3', 4: 'rotation4'}[o]
    return {4: 'rotoreflection4', 6: 'rotoreflection6'}[o]

BOUND = {'inversion': 3, 'reflection': 5, 'rotation4': 3, 'rotoreflection6': 3}   # виды движений, к которым лемма применима, и границы
COLLINEAR_KINDS = {'inversion', 'rotation4', 'rotoreflection6'}                    # где S к тому же лежит на одной прямой

# ---------- геометрия ----------
def coplanar(p, a, b, c):
    u = [a[i]-p[i] for i in range(3)]; v = [b[i]-p[i] for i in range(3)]; w = [c[i]-p[i] for i in range(3)]
    return u[0]*(v[1]*w[2]-v[2]*w[1]) - u[1]*(v[0]*w[2]-v[2]*w[0]) + u[2]*(v[0]*w[1]-v[1]*w[0]) == 0

def has_coplanar4(S):
    return any(coplanar(*q) for q in itertools.combinations(S, 4))

def invariant(S, M, n):
    return {act(M, c, n) for c in S} == set(S)

def statement(S, M, n):
    """True ⟺ заключение леммы для данных S, M: |S| ≤ BOUND[kind(M)] (при выполненной предпосылке: S ⊂ [n]³, S M-инвариантно,
    без четырёх компланарных, kind(M) ∈ BOUND). Если предпосылка нарушена или движение не того вида — лемма молчит, возвращаем True."""
    k = kind(M)
    if k not in BOUND or not invariant(S, M, n) or has_coplanar4(S): return True
    if len(S) > BOUND[k]: return False
    if k == 'rotation4' and not all(act(M, c, n) == c for c in S): return False      # усиление: все точки на оси — неподвижны под M
    if k in COLLINEAR_KINDS and not collinear_set(S): return False                   # усиление v2: S на одной прямой
    return True

def collinear_set(S):
    S = list(S)
    if len(S) <= 2: return True
    a, b = S[0], S[1]; u = [b[i] - a[i] for i in range(3)]
    for c in S[2:]:
        v = [c[i] - a[i] for i in range(3)]
        if (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]) != (0, 0, 0): return False
    return True

# ---------- генератор: случайное M-инвариантное максимальное множество (орбитный рост) ----------
def orbit(M, c, n):
    o = {c}; x = act(M, c, n)
    while x not in o: o.add(x); x = act(M, x, n)
    return sorted(o)

def clean_add(S, new):
    allp = S + new
    for i in range(len(S), len(allp)):
        for a, b, c in itertools.combinations(allp[:i] + allp[i+1:], 3):
            if coplanar(allp[i], a, b, c): return False
    return True

def grow(rnd, M, n):
    cells = list(itertools.product(range(n), repeat=3)); rnd.shuffle(cells); S = []
    for c in cells:
        if c in S: continue
        o = orbit(M, c, n)
        if clean_add(S, o): S = S + o
    return S

def generate(rnd, n=5, kinds=('inversion', 'reflection', 'rotation4', 'rotoreflection6')):
    """случайное движение нужного вида и случайное максимальное M-инвариантное S ⊂ [n]³ без четырёх компланарных."""
    Ms = [M for M in all_matrices() if kind(M) in kinds]
    M = rnd.choice(Ms)
    return grow(rnd, M, n), M, n

def boundary_cases():
    """сразу за границей условий: (а) полуоборот — инвариантные множества бывают большими (страта c02 при n=5 даёт 10, при n=7 — 14;
    здесь: жадный рост при seed 1 даёт ≥ 6); (б) поворот порядка 3 — страта c06 достигает a(n) (13, 18, 20 при n = 5, 7, 8);
    (в) поворотное отражение порядка 4 — орбита {x, ρσx, ρ²x, ρ³σx} некомпланарна при x вне средней плоскости (определитель −8c(a²+b²));
    (г) аналог для запрета «три на прямой» ЛОЖЕН: центрально-симметричное множество без трёх коллинеарных размера 4;
    (д) |S| = 3 коллинеарных через центр при инверсии — допустимо (запрет «четыре в плоскости» пуст на трёх точках)."""
    rnd = random.Random(1)
    half = next(M for M in all_matrices() if kind(M) == 'half_turn' and M[8] == 1)         # полуоборот вокруг оси z
    rot3 = next(M for M in all_matrices() if kind(M) == 'rotation3')
    s4 = next(M for M in all_matrices() if kind(M) == 'rotoreflection4')
    return {"half_turn_large": (grow(rnd, half, 5), half, 5),
            "rotation3_large": (grow(rnd, rot3, 5), rot3, 5),
            "rotoreflection4_orbit_noncoplanar": (orbit(s4, (0, 1, 0), 5), s4, 5),
            "no_three_collinear_analog_fails": ([(0, 0, 1), (2, 2, 1), (0, 2, 0), (2, 0, 2)], INV, 3),
            "three_collinear_through_center_allowed": ([(0, 0, 0), (2, 2, 2), (4, 4, 4)], INV, 5)}

if __name__ == "__main__":
    rnd = random.Random(1); bad = 0; sizes = {}
    for _ in range(60):
        S, M, n = generate(rnd, n=rnd.choice([5, 6, 7]))
        sizes.setdefault(kind(M), []).append(len(S))
        if not statement(S, M, n): bad += 1
    print("нарушений на 60 законных случаях:", bad, "; размеры по видам:", {k: (min(v), max(v)) for k, v in sizes.items()})
    b = boundary_cases()
    print("полуоборот: |S| =", len(b["half_turn_large"][0]), "; поворот-3: |S| =", len(b["rotation3_large"][0]),
          "; S4-орбита компланарна:", has_coplanar4(b["rotoreflection4_orbit_noncoplanar"][0]),
          "; центрально-симметричные 4 без трёх коллинеарных, но с четырьмя компланарными:", has_coplanar4(b["no_three_collinear_analog_fails"][0]))
