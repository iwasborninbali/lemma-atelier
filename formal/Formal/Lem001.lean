import Mathlib

/-!
# lem-001 — убийцы пустой клетки попарно не пересекаются (дизъюнктная форма)

Абстрактная геометрия инцидентности: точки `P`, прямые — некоторые множества точек, аксиома одна:
две различные точки лежат ровно на одной общей прямой. Это единственное, что использует доказательство
(вердикт противника №1, «против формы» 6). Носители: `ℤ^d`, аффинные пространства над полями, торы простого
модуля; вне области — тор `(ℤ/4)²` (контрпример в `lemmas/tests/test_lem_001.py`).

Формализовано: (1) дизъюнктность убийц; (2) через точку проходит ≤ 1 убийца; (3) `κ_k(q)·k ≤ |S|`;
(4) шаг для радиуса обмена: если удалено меньше `κ_k(q)` точек, какой-то убийца `q` уцелел целиком
(значит `q` остаётся недопустимой; наследственность семейства — отдельная лемма ниже).
-/

open Classical

/-- Геометрия инцидентности: две различные точки лежат ровно на одной прямой. -/
structure LineSpace (P : Type*) where
  lines : Set (Set P)
  unique_line : ∀ {p q : P}, p ≠ q → ∃! ℓ, ℓ ∈ lines ∧ p ∈ ℓ ∧ q ∈ ℓ

namespace LineSpace

variable {P : Type*} (G : LineSpace P)

/-- множество точек коллинеарно, если целиком лежит на одной прямой -/
def Collinear (A : Finset P) : Prop := ∃ ℓ ∈ G.lines, ∀ x ∈ A, x ∈ ℓ

/-- «нет `k+1` на прямой»: на каждой прямой не больше `k` точек `S` -/
def NoKPlusOne (S : Finset P) (k : ℕ) : Prop := ∀ ℓ ∈ G.lines, (S.filter (· ∈ ℓ)).card ≤ k

/-- убийцы клетки `q`: `k`-подмножества `S`, коллинеарные вместе с `q` -/
noncomputable def killers (S : Finset P) (k : ℕ) (q : P) : Finset (Finset P) :=
  (S.powersetCard k).filter (fun K => G.Collinear (insert q K))

/-- `κ_k(q)` — число убийц -/
noncomputable def kappa (S : Finset P) (k : ℕ) (q : P) : ℕ := (G.killers S k q).card

lemma mem_killers {S : Finset P} {k : ℕ} {q : P} {K : Finset P} :
    K ∈ G.killers S k q ↔ K ⊆ S ∧ K.card = k ∧ G.Collinear (insert q K) := by
  simp [killers, Finset.mem_filter, Finset.mem_powersetCard, and_assoc]

/-- **lem-001 (дизъюнктная форма).** `q ∉ S`, в `S` нет `k+1` точек на прямой ⇒ два различных убийцы `q`
не пересекаются. Доказательство: общая точка `p` и `q` задают единственную прямую, оба убийцы лежат на ней,
а на ней не больше `k` точек `S` — значит оба равны `S ∩ ℓ`. -/
theorem killers_disjoint {S : Finset P} {k : ℕ} {q : P} (hq : q ∉ S) (hS : G.NoKPlusOne S k)
    {K₁ K₂ : Finset P} (h₁ : K₁ ∈ G.killers S k q) (h₂ : K₂ ∈ G.killers S k q) (hne : K₁ ≠ K₂) :
    Disjoint K₁ K₂ := by
  rw [Finset.disjoint_left]
  intro p hp₁ hp₂
  obtain ⟨hK₁S, hcard₁, ℓ₁, hℓ₁, hsub₁⟩ := (G.mem_killers).1 h₁
  obtain ⟨hK₂S, hcard₂, ℓ₂, hℓ₂, hsub₂⟩ := (G.mem_killers).1 h₂
  have hpq : p ≠ q := fun h => hq (h ▸ hK₁S hp₁)
  obtain ⟨ℓ, ⟨hℓ, -, -⟩, huniq⟩ := G.unique_line hpq
  have e₁ : ℓ₁ = ℓ := huniq ℓ₁
    ⟨hℓ₁, hsub₁ p (Finset.mem_insert_of_mem hp₁), hsub₁ q (Finset.mem_insert_self q K₁)⟩
  have e₂ : ℓ₂ = ℓ := huniq ℓ₂
    ⟨hℓ₂, hsub₂ p (Finset.mem_insert_of_mem hp₂), hsub₂ q (Finset.mem_insert_self q K₂)⟩
  have hK₁ : K₁ ⊆ S.filter (· ∈ ℓ) := fun x hx =>
    Finset.mem_filter.2 ⟨hK₁S hx, e₁ ▸ hsub₁ x (Finset.mem_insert_of_mem hx)⟩
  have hK₂ : K₂ ⊆ S.filter (· ∈ ℓ) := fun x hx =>
    Finset.mem_filter.2 ⟨hK₂S hx, e₂ ▸ hsub₂ x (Finset.mem_insert_of_mem hx)⟩
  have hc := hS ℓ hℓ
  have eq₁ : K₁ = S.filter (· ∈ ℓ) := Finset.eq_of_subset_of_card_le hK₁ (by rw [hcard₁]; exact hc)
  have eq₂ : K₂ = S.filter (· ∈ ℓ) := Finset.eq_of_subset_of_card_le hK₂ (by rw [hcard₂]; exact hc)
  exact hne (eq₁.trans eq₂.symm)

/-- Следствие 1: через каждую точку проходит не больше одного убийцы `q` (исходная форма lem-001). -/
theorem card_killers_through_le_one {S : Finset P} {k : ℕ} {q : P} (hq : q ∉ S)
    (hS : G.NoKPlusOne S k) (p : P) :
    ((G.killers S k q).filter (fun K => p ∈ K)).card ≤ 1 := by
  rw [Finset.card_le_one]
  intro K₁ hK₁ K₂ hK₂
  by_contra hne
  have d := G.killers_disjoint hq hS (Finset.mem_filter.1 hK₁).1 (Finset.mem_filter.1 hK₂).1 hne
  exact Finset.disjoint_left.1 d (Finset.mem_filter.1 hK₁).2 (Finset.mem_filter.1 hK₂).2

/-- Следствие 2: `κ_k(q) · k ≤ |S|` — убийцы образуют дизъюнктное семейство `k`-подмножеств `S`. -/
theorem kappa_mul_le {S : Finset P} {k : ℕ} {q : P} (hq : q ∉ S) (hS : G.NoKPlusOne S k) :
    G.kappa S k q * k ≤ S.card := by
  have hdisj : ∀ K₁ ∈ G.killers S k q, ∀ K₂ ∈ G.killers S k q,
      K₁ ≠ K₂ → Disjoint (id K₁) (id K₂) :=
    fun K₁ h₁ K₂ h₂ hne => G.killers_disjoint hq hS h₁ h₂ hne
  have hunion : (G.killers S k q).biUnion id ⊆ S := by
    intro x hx
    obtain ⟨K, hK, hxK⟩ := Finset.mem_biUnion.1 hx
    exact ((G.mem_killers).1 hK).1 hxK
  have hcard : ((G.killers S k q).biUnion id).card = G.kappa S k q * k := by
    rw [Finset.card_biUnion hdisj]
    simp only [id]
    rw [Finset.sum_const_nat (fun K hK => ((G.mem_killers).1 hK).2.1)]
    rfl
  calc G.kappa S k q * k = ((G.killers S k q).biUnion id).card := hcard.symm
    _ ≤ S.card := Finset.card_le_card hunion

/-- Следствие 3 (шаг радиуса обмена): если удалено меньше `κ_k(q)` точек, какой-то убийца `q`
не задет — `q` остаётся недопустимой в `S \ R`. -/
theorem exists_killer_disjoint_of_card_lt {S : Finset P} {k : ℕ} {q : P} (hq : q ∉ S)
    (hS : G.NoKPlusOne S k) (R : Finset P) (hR : R.card < G.kappa S k q) :
    ∃ K ∈ G.killers S k q, Disjoint K R := by
  by_contra hcon
  have hcon' : ∀ K ∈ G.killers S k q, ¬ Disjoint K R := fun K hK hd => hcon ⟨K, hK, hd⟩
  let f : Finset P → P := fun K => if h : ∃ x, x ∈ K ∧ x ∈ R then Classical.choose h else q
  have hf : ∀ K ∈ G.killers S k q, f K ∈ K ∧ f K ∈ R := by
    intro K hK
    have h : ∃ x, x ∈ K ∧ x ∈ R := by
      obtain ⟨x, hx₁, hx₂⟩ := Finset.not_disjoint_iff.1 (hcon' K hK)
      exact ⟨x, hx₁, hx₂⟩
    simp only [f, dif_pos h]
    exact Classical.choose_spec h
  obtain ⟨K₁, hK₁, K₂, hK₂, hne, heq⟩ :=
    Finset.exists_ne_map_eq_of_card_lt_of_maps_to hR (fun K hK => (hf K hK).2)
  have d := G.killers_disjoint hq hS hK₁ hK₂ hne
  exact Finset.disjoint_left.1 d (hf K₁ hK₁).1 (by rw [heq]; exact (hf K₂ hK₂).1)

/-- Наследственность: подмножество множества без `k+1` на прямой — тоже без `k+1` на прямой. -/
theorem noKPlusOne_mono {S T : Finset P} {k : ℕ} (hTS : T ⊆ S) (hS : G.NoKPlusOne S k) :
    G.NoKPlusOne T k := fun ℓ hℓ =>
  le_trans (Finset.card_le_card (Finset.filter_subset_filter _ hTS)) (hS ℓ hℓ)

end LineSpace
