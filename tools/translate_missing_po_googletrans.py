from __future__ import annotations

import re
from pathlib import Path
import json
import time
import urllib.parse
import urllib.request
from typing import Dict, Iterable, List

import polib


PO_ROOT = Path("docs/locale/en/LC_MESSAGES")
ZH_RE = re.compile(r"[\u4e00-\u9fff]")

# Prefer deterministic translations for common UI terms / headings.
GLOSSARY: Dict[str, str] = {
    "简介": "Overview",
    "输入 / 输出": "Inputs / Outputs",
    "输入：": "Input: ",
    "输出：": "Output: ",
    "参数": "Parameters",
    "说明": "Description",
    "默认值": "Default",
    "无": "None",
    "使用步骤": "Steps",
    "注意事项": "Notes",
    "前提条件": "Prerequisites",
    "使用": "Usage",
    "支持": "Support",
    "介绍": "Introduction",
    "模块": "Blocks",
    "案例分析": "Case Studies",
}


def _split_text(text: str, max_len: int = 1400) -> List[str]:
    # Split long paragraphs to avoid URL/response issues.
    if len(text) <= max_len:
        return [text]
    parts: List[str] = []
    buf = ""
    for seg in re.split(r"([。！？；\n])", text):
        if not seg:
            continue
        cand = buf + seg
        if len(cand) > max_len and buf:
            parts.append(buf)
            buf = seg
        else:
            buf = cand
    if buf:
        parts.append(buf)
    return parts


def _google_translate(text: str, src: str = "zh-CN", dest: str = "en") -> str:
    """
    Use the unofficial translate.googleapis.com endpoint (no auth).
    Returns translated text.
    """
    base = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": src,
        "tl": dest,
        "dt": "t",
        "q": text,
    }
    url = f"{base}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    # data[0] is a list of translated segments: [[translated, original, ...], ...]
    return "".join(seg[0] for seg in data[0] if seg and seg[0])


def translate_text(text: str, cache: Dict[str, str]) -> str:
    if text in GLOSSARY:
        return GLOSSARY[text]
    if text in cache:
        return cache[text]

    parts = _split_text(text)
    translated_parts: List[str] = []
    for part in parts:
        translated_parts.append(_google_translate(part, src="zh-CN", dest="en"))
        time.sleep(0.05)  # be gentle to avoid rate limiting

    out = "".join(translated_parts).strip()
    cache[text] = out
    return out


def main() -> int:
    cache: Dict[str, str] = {}

    files_touched = 0
    entries_changed = 0
    entries_failed = 0

    for po_path in PO_ROOT.rglob("*.po"):
        po = polib.pofile(po_path)
        dirty = False

        for entry in po:
            if entry.obsolete or not entry.msgid:
                continue

            def needs_translation(s: str) -> bool:
                return (not s) or bool(ZH_RE.search(s))

            # Singular
            if not entry.msgid_plural:
                if needs_translation(entry.msgstr):
                    try:
                        entry.msgstr = translate_text(entry.msgid, cache)
                        dirty = True
                        entries_changed += 1
                    except Exception as exc:  # best-effort
                        entries_failed += 1
                        print(f"[warn] {po_path}: translate failed for msgid={entry.msgid!r}: {exc}")
                continue

            # Plurals
            # If plural strings contain Chinese/empty, translate from msgid/msgid_plural.
            for k, src in (("0", entry.msgid), ("1", entry.msgid_plural)):
                current = entry.msgstr_plural.get(k, "")
                if needs_translation(current):
                    try:
                        entry.msgstr_plural[k] = translate_text(src, cache)
                        dirty = True
                        entries_changed += 1
                    except Exception as exc:  # best-effort
                        entries_failed += 1
                        print(f"[warn] {po_path}: translate failed for plural msgid={src!r}: {exc}")

        if dirty:
            po.save(po_path)
            files_touched += 1

    print(
        f"done. files_touched={files_touched} entries_changed={entries_changed} entries_failed={entries_failed}"
    )
    return 0 if entries_failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

