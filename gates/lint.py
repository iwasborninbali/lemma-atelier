#!/usr/bin/env python3
"""Гейт связности ателье лемм: нужда без свидетельства, лемма без нужды, лемма без обязательных разделов — красный.
Запуск: python3 gates/lint.py  (код возврата 1 при нарушении)."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEED_FIELDS = ("**источник:**", "**чего не хватает", "**гипотеза")
LEM_SECTIONS = ("## Формулировка", "## Доказательство", "## Машинная проверка", "## Опознание", "## Граница", "## Носители", "## Противник")
LEM_FIELDS = ("**нужда:**", "**статус доказательства:**", "**дальность", "**кто возьмёт:**")

def main() -> int:
    bad = 0
    needs = sorted(ROOT.glob("needs/need-*.md"))
    ids = {p.stem for p in needs}
    for p in needs:
        t = p.read_text(encoding="utf-8")
        for f in NEED_FIELDS:
            if f not in t: print(f"{p.name}: нет поля {f}"); bad += 1
    for p in sorted(ROOT.glob("lemmas/lem-*.md")):
        if ".adversary-" in p.name or ".holes" in p.name: continue   # отчёты противника и списки дыр — не леммы
        t = p.read_text(encoding="utf-8")
        m = re.search(r"\*\*нужда:\*\*\s*(need-\d+)", t)
        if not m or m.group(1) not in ids: print(f"{p.name}: нужда не названа или не существует"); bad += 1
        for f in LEM_FIELDS:
            if f not in t: print(f"{p.name}: нет поля {f}"); bad += 1
        for s in LEM_SECTIONS:
            if s not in t: print(f"{p.name}: нет раздела {s}"); bad += 1
        # правило владельца 3.09: лемма без исполнимого утверждения и без чужого теста-фальсификатора — красная
        stem = p.stem.replace("-", "_")
        if not (ROOT / f"lemmas/{stem}_statement.py").exists(): print(f"{p.name}: нет lemmas/{stem}_statement.py (исполнимый предикат + генератор + границы)"); bad += 1
        if not (ROOT / f"lemmas/tests/test_{stem}.py").exists(): print(f"{p.name}: нет lemmas/tests/test_{stem}.py (тест-фальсификатор ДРУГОГО агента)"); bad += 1
    # обратная связность: у каждой нужды с леммой — ссылка на неё
    lems = {p.stem for p in ROOT.glob("lemmas/lem-*.md") if ".adversary-" not in p.name and ".holes" not in p.name}
    print(f"нужд: {len(ids)}, лемм: {len(lems)}, нарушений: {bad}")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
