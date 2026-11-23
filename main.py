#!/usr/bin/env python3
"""One-line roast entry for "One-Line Roast: The Gadget You Use Every Day".

Writes the roast to /output/entry.txt and verifies the written file is
byte-identical to the entry (no trailing newline, no extra whitespace).
"""
import os

ENTRY = "My authenticator app gives me a code that expires in the three seconds it takes to switch apps."

OUT = "/output/entry.txt"


def validate(entry):
    """Check the entry meets the competition's one-line rules.

    Rules: 1-200 characters, exactly one line, ASCII only, no leading or
    trailing whitespace, and no doubled spaces inside the line (a doubled
    space is almost always a typo, and the roast must read cleanly aloud).
    """
    assert 1 <= len(entry) <= 200, "entry must be 1-200 characters"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.isascii(), "entry must be ASCII only"
    assert entry.strip() == entry, "entry must not start or end with whitespace"
    assert "  " not in entry, "entry must not contain doubled spaces"


def main():
    """Validate the roast, write it to /output/entry.txt, read it back."""
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUT, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry must match exactly"
    assert os.path.getsize(OUT) == len(ENTRY.encode("ascii")), "file size must equal entry length"
    print("wrote", len(ENTRY), "characters to", OUT)


if __name__ == "__main__":
    main()
