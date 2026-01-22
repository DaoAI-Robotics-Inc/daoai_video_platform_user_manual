from pathlib import Path
import polib
from googletrans import Translator

root = Path('docs/locale/en/LC_MESSAGES')
translator = Translator()
changed_files = 0
translated = 0


def tr(text: str) -> str:
    if not text:
        return ''
    try:
        return translator.translate(text, dest='en').text
    except Exception as e:
        print(f'translate failed: {e}; text: {text[:60]!r}')
        return text

for path in root.rglob('*.po'):
    po = polib.pofile(path)
    changed = False
    for entry in po:
        if entry.obsolete:
            continue
        if entry.msgid_plural:
            for k in list(entry.msgstr_plural.keys()):
                src = entry.msgid if k == '0' else entry.msgid_plural
                new = tr(src)
                if entry.msgstr_plural.get(k) != new:
                    entry.msgstr_plural[k] = new
                    changed = True
                    translated += 1
        else:
            new = tr(entry.msgid)
            if entry.msgstr != new:
                entry.msgstr = new
                changed = True
                translated += 1
    if changed:
        po.save(path)
        changed_files += 1

print(f'files changed: {changed_files}, entries updated: {translated}')
