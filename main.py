"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

import os

LINE = "Tomorrow's paper printed my obituary, and the cause of death was blank."

# Gate guard: the entry must be exactly one sentence of 1-200 characters.
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
