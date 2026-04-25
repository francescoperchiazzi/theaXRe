import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_HTML = ROOT / "index.html"
TRANSLATIONS_JSON = ROOT / "translations.json"


def extract_en_keys_from_index_html(text: str) -> set[str]:
    marker = "en: {"
    start = text.find(marker)
    if start == -1:
        return set()
    brace_start = text.find("{", start)
    if brace_start == -1:
        return set()
    depth = 0
    end = None
    for i in range(brace_start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    if end is None:
        return set()
    block = text[brace_start:end]
    return set(re.findall(r'"([^"]+)"\s*:', block))


def main() -> int:
    index_text = INDEX_HTML.read_text("utf-8")
    en_keys = extract_en_keys_from_index_html(index_text)
    if not en_keys:
        print("ERROR: Could not extract EN keys from index.html")
        return 2

    data = json.loads(TRANSLATIONS_JSON.read_text("utf-8"))
    langs = sorted([k for k, v in data.items() if isinstance(v, dict)])

    missing = {}
    extra = {}
    empty = []

    allowed_placeholders = {"missing", "done", "total", "value", "w", "h", "usdz", "glb", "size", "message", "max"}
    bad_placeholders = []

    for lang in langs:
        d = data[lang]
        keys = set(d.keys())
        m = sorted(en_keys - keys)
        e = sorted(keys - en_keys)
        if m:
            missing[lang] = m
        if e:
            extra[lang] = e

        for k, v in d.items():
            if isinstance(v, str) and not v.strip():
                empty.append(f"{lang}/{k}")
            if isinstance(v, str):
                for ph in re.findall(r"\{([a-zA-Z0-9_]+)\}", v):
                    if ph not in allowed_placeholders:
                        bad_placeholders.append(f"{lang}/{k}:{{{ph}}}")

    print("Languages:", len(langs))
    print("EN keys:", len(en_keys))
    print("Langs with missing keys:", len(missing))
    print("Langs with extra keys:", len(extra))
    print("Empty strings:", len(empty))
    print("Unknown placeholders:", len(bad_placeholders))

    if missing:
        lang = sorted(missing.keys())[0]
        print("First missing:", lang, missing[lang][:12])
    if extra:
        lang = sorted(extra.keys())[0]
        print("First extra:", lang, extra[lang][:12])
    if empty:
        print("First empty:", empty[0])
    if bad_placeholders:
        print("First bad placeholder:", bad_placeholders[0])

    ok = (not missing) and (not extra) and (not empty) and (not bad_placeholders)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
