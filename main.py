"""The Battery's Last Text to Its Charger — make.fun entry.

Writes one line of plain text (the phone battery's last text message
to the charger it waited for all day) to /output/entry.txt.
Stdlib only. No network, no files read, no side effects.
"""

import os

LINE = "I waited all day by the outlet and you plugged in the vacuum first. Enjoy the clean floors. I'm at 1%."

MAX_CHARS = 200


def main() -> None:
    # Gate (kit RULES.txt): entry.txt must be UTF-8 text of 1-200 chars.
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back check: the file must hold exactly the line, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
