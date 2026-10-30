"""Normalize a text context without network calls or model dependencies."""

import argparse
import json
import unicodedata
from pathlib import Path


def prepare_context(text: str, max_chars: int = 4000) -> dict:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(max_chars, int) or isinstance(max_chars, bool) or max_chars < 1:
        raise ValueError("max_chars must be a positive integer")
    lines = []
    for line in unicodedata.normalize("NFC", text).splitlines():
        normalized = " ".join(line.split())
        if normalized:
            lines.append(normalized)
    clean = "\n".join(lines)
    result = clean[:max_chars]
    return {
        "text": result,
        "input_chars": len(text),
        "normalized_chars": len(clean),
        "output_chars": len(result),
        "truncated": len(clean) > max_chars,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--max-chars", type=int, default=4000)
    args = parser.parse_args()
    try:
        result = prepare_context(args.input.read_text(encoding="utf-8"), args.max_chars)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
