import Mathlib

/-!
# lem-003 — симметрии, несовместимые с запретом «четыре в плоскости»: ядро (инверсия)

Точки — векторы `Fin 3 → ℤ`; четыре точки компланарны, если определитель трёх разностей равен нулю.
Ядро: две антиподальные пары `{p, m − p}` и `{q, m − q}` (центр `m/2`) всегда компланарны — это тождество
`det(m − 2p, q − p, m − q − p) = 0`. Множественная форма: конечное `S ⊂ ℤ³`, инвариантное под `x ↦ m − x`,
с `|S| ≥ 4` содержит четыре различные компланарные точки (значит страты с инверсией дают `|S| ≤ 3`).
Не формализовано: отражения (`|S| ≤ 5`) и повороты порядка 4 (`|S| ≤ 3`).
-/

namespace Lem003

/-- определитель трёх векторов-строк -/
def det3 (u v w : Fin 3 → ℤ) : ℤ := Matrix.det (Matrix.of ![u, v, w])

/-- четыре точки компланарны -/
def Coplanar4 (p a b c : Fin 3 → ℤ) : Prop := det3 (a - p) (b - p) (c - p) = 0

/-- инволюция `x ↦ m − x` (инверсия относительно центра `m/2`) -/
def sym (m x : Fin 3 → ℤ) : Fin 3 → ℤ := m - x

theorem sym_sym (m x : Fin 3 → ℤ) : sym m (sym m x) = x := by
  simp [sym]

/-- **Ядро lem-003.** Две антиподальные пары компланарны. -/
theorem antipodal_pairs_coplanar (m p q : Fin 3 → ℤ) : Coplanar4 p (sym m p) q (sym m q) := by
  unfold Coplanar4 det3 sym
  simp [Matrix.det_fin_three]
  ring

/-- неподвижная точка инволюции единственна (`2x = m`) -/
theorem fixed_unique {m x y : Fin 3 → ℤ} (hx : sym m x = x) (hy : sym m y = y) : x = y := by
  funext i
  have hx' := congrFun hx i
  have hy' := congrFun hy i
  simp [sym] at hx' hy'
  omega

/-- **lem-003 (инверсия), множественная форма.** -/
theorem four_coplanar_of_symmetric (m : Fin 3 → ℤ) (S : Finset (Fin 3 → ℤ))
    (hS : ∀ x ∈ S, sym m x ∈ S) (h4 : 4 ≤ S.card) :
    ∃ p ∈ S, ∃ a ∈ S, ∃ b ∈ S, ∃ c ∈ S,
      p ≠ a ∧ p ≠ b ∧ p ≠ c ∧ a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ Coplanar4 p a b c := by
  classical
  -- неподвижных точек в S не больше одной, значит неподвижных нет хотя бы у трёх
  have hfix : (S.filter (fun x => sym m x = x)).card ≤ 1 := by
    rw [Finset.card_le_one]
    intro x hx y hy
    exact fixed_unique (Finset.mem_filter.1 hx).2 (Finset.mem_filter.1 hy).2
  set F := S.filter (fun x => sym m x = x) with hF
  set N := S \ F with hN
  have hNcard : 3 ≤ N.card := by
    have h : S.card ≤ N.card + F.card := Finset.card_le_card_sdiff_add_card
    omega
  obtain ⟨p, hp⟩ : N.Nonempty := Finset.card_pos.1 (by omega)
  have hpS : p ∈ S := (Finset.mem_sdiff.1 hp).1
  have hpfix : ¬ sym m p = p := fun h => (Finset.mem_sdiff.1 hp).2 (Finset.mem_filter.2 ⟨hpS, h⟩)
  have hp'S : sym m p ∈ S := hS p hpS
  -- вторая пара: убираем p и m − p
  have hN' : 1 ≤ ((N.erase p).erase (sym m p)).card := by
    have h1 := Finset.pred_card_le_card_erase (s := N) (a := p)
    have h2 := Finset.pred_card_le_card_erase (s := N.erase p) (a := sym m p)
    omega
  obtain ⟨q, hq⟩ : ((N.erase p).erase (sym m p)).Nonempty := Finset.card_pos.1 (by omega)
  have hq1 : q ≠ sym m p := (Finset.mem_erase.1 hq).1
  have hq2 : q ≠ p := (Finset.mem_erase.1 (Finset.mem_erase.1 hq).2).1
  have hqN : q ∈ N := (Finset.mem_erase.1 (Finset.mem_erase.1 hq).2).2
  have hqS : q ∈ S := (Finset.mem_sdiff.1 hqN).1
  have hqfix : ¬ sym m q = q := fun h => (Finset.mem_sdiff.1 hqN).2 (Finset.mem_filter.2 ⟨hqS, h⟩)
  have hq'S : sym m q ∈ S := hS q hqS
  have hq'p : sym m q ≠ p := by
    intro h; apply hq1; rw [← h, sym_sym]
  have hq'p' : sym m q ≠ sym m p := by
    intro h; apply hq2
    have := congrArg (sym m) h; rwa [sym_sym, sym_sym] at this
  refine ⟨p, hpS, sym m p, hp'S, q, hqS, sym m q, hq'S, ?_, ?_, ?_, ?_, ?_, ?_,
    antipodal_pairs_coplanar m p q⟩
  · exact fun h => hpfix h.symm
  · exact fun h => hq2 h.symm
  · exact fun h => hq'p h.symm
  · exact fun h => hq1 h.symm
  · exact fun h => hq'p' h.symm
  · exact fun h => hqfix h.symm

end Lem003
