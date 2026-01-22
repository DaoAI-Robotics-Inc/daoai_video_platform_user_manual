from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import polib
from deep_translator import GoogleTranslator


CHUNK_SIZE = 10  # batch size for translate_batch
PO_ROOT = Path("docs/locale/en/LC_MESSAGES")


def translate_all():
    translator = GoogleTranslator(source="zh-CN", target="en")
    files = list(PO_ROOT.rglob("*.po"))
    changed_files = 0
    total_entries = 0

    for path in files:
        po = polib.pofile(path)
        work: List[Tuple[polib.POEntry, str | None, str]] = []

        for entry in po:
            if entry.obsolete or not entry.msgid:
                continue
            if entry.msgid_plural:
                work.append((entry, "0", entry.msgid))
                work.append((entry, "1", entry.msgid_plural))
            else:
                work.append((entry, None, entry.msgid))

        total_entries += len(work)
        if not work:
            continue

        # Batch translate to reduce API calls
        dirty = False
        for i in range(0, len(work), CHUNK_SIZE):
            chunk = work[i : i + CHUNK_SIZE]
            texts = [t[2] for t in chunk]
            try:
                translated = translator.translate_batch(texts)
            except Exception as exc:  # pragma: no cover - best-effort logging
                print(f"[warn] translate failed for {path} chunk starting {i}: {exc}")
                translated = texts  # fallback to source to avoid empty strings

            for (entry, plural_key, _), translated_text in zip(chunk, translated):
                if plural_key is None:
                    if entry.msgstr != translated_text:
                        entry.msgstr = translated_text
                        dirty = True
                else:
                    current = entry.msgstr_plural.get(plural_key, "")
                    if current != translated_text:
                        entry.msgstr_plural[plural_key] = translated_text
                        dirty = True

        if dirty:
            po.save(path)
            changed_files += 1

    print(f"Translated entries: {total_entries}, files changed: {changed_files}")


if __name__ == "__main__":
    translate_all()
