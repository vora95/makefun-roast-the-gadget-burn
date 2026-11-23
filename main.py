#!/usr/bin/env python3
"""Write the one-line roast for One-Line Roast: The Gadget You Use Every Day
to /output/entry.txt.

The authenticator app hands over a six-digit code that dies in the exact
three seconds it takes to switch apps and type it in — the daily security
ritual that expires before you can finish it.
"""
import os

ENTRY = "My authenticator app gives me a code that expires in the three seconds it takes to switch apps."

OUT = "/output/entry.txt"


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.isascii(), "entry must be ASCII only"
    assert all(word for word in ENTRY.split(" ")), "no empty words allowed"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUT, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry must match exactly"
    assert os.path.getsize(OUT) == len(ENTRY.encode("ascii")), "entry must be exactly 95 bytes, no trailing newline"
    print("wrote", len(ENTRY), "characters to", OUT)


if __name__ == "__main__":
    main()
