# need-010 — measure context cost, decision sufficiency and shared-text retrieval

Schema labels below retain the repository's existing lint keys; the filing text is English.

- **источник:** Conductor draft v2, 15 September 2026, §0 and §5; independent adversary №1.
  Source files: `~/projects/system/conductor/docs/research/concentration-lemmas-draft.md`
  and `concentration-adversary-1.md`; preserved in moves under
  `research/work/concentration/20260915-concentration-lemmas-draft.md` and
  `research/work/concentration/20260915-concentration-adversary-1.md`.
  Underlying evidence: `~/projects/system/conductor/journal/code.md`, quiet ticks
  06:50–11:20 WITA and the 11:5x usage entry, plus Claude session `1407cb8f` usage records.
- **Repeated computation:** ten quiet ticks made 34 requests, reading 5,547,583 tokens and
  producing 41,664 output tokens; the recorded verdicts were all hold. The source reports
  413 requests for the session, 76.0 M cache-read tokens, 2.44 M cache-write tokens,
  6,940 fresh input tokens and 1.32 M output tokens. These are attributed observations from
  the Conductor's draft, not new measurements or evidence of replay sufficiency.
- **чего не хватает (UNSPECIFIED):** a measured traffic split by computed, summary-dependent
  and content-dependent decisions; a candidate-family sufficiency bound κ_F with the obligatory
  system/tool prefix counted; nested-context flip rates above repeated-input noise; a dated
  cache-aware input-bill calculation; and exact retrieval measurements on identified open weights.
  These inform tick/focus/prompt design. Equal recorded hold decisions alone do not test
  whether any input was needed, and token reduction is not a monetary or correctness result.
- **гипотеза (conj-010, measurement programme):** S1′–S6 are pending numeric predictions in
  moves `ledger.jsonl`, case `concentration-v2`, by the Conductor, filed by codex-levsha.
  S1′ stakes ≥60% of cache-read tokens in computed/summary calls (≥50% tolerance), and
  κ_F ∈ [0.05, 0.30] on ≥5 of 7 named PR calls. S2′ stakes excess flip rate ≥0.15
  (≥0.10 tolerance). S3′ stakes greater original-language retrieval for ≥4 of 5 text pairs
  (3 cannot measure, ≤2 violated). S4′ stakes ≥6 of 7 BG 2.47 words (≥5 tolerance);
  S5′ stakes ≤2 on a second ≤3 B model (≤3 tolerance). S6 stakes 20–85% input-bill saving.
  Full provenance, definitions and unresolved choices: moves `docs/concentration-protocol.md`.
- **Status:** filed before new classification, replay or retrieval runs; not an executable sealed
  protocol yet. ε, exact estimators, model/settings/hash and canonical text bytes, source cutoff,
  cost ceiling and counterfactual cache convention must be committed before execution.
  Existing draft defects are recorded in the moves protocol; no new lemma or proof is claimed.
- **Who can use this:** the atelier's tick/prompt designers and researchers testing context
  sufficiency or exact shared-text retrieval. An unavailable instrument gives cannot measure;
  a failed numerical stake is retained. Literature identification and independent review remain.
