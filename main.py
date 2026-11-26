#!/usr/bin/env python3
"""Entry for make.fun — The Internet in One Word.

Writes the single word that describes the whole internet to
/output/entry.txt, after checking it against the competition gate:
UTF-8 text of 1 to 30 characters, not only white space.
"""

import os
import sys

# The word: "tab" + "labyrinth". The internet is a maze you wander
# through one tab at a time — every link opens another corridor, every
# corridor has three more doors, and nobody remembers where they came in.
WORD = "Tabyrinth"

GATE_MIN = 1
GATE_MAX = 30


def main() -> int:
    text = WORD.strip()
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        print(f"gate failed: word is {len(text)} characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: word is only white space", file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("gate failed: not a single word", file=sys.stderr)
        return 1

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {text!r} to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
