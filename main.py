"""Monday, Reviewed in One Line.

Writes one funny one-line review of the entrant's own Monday to
/output/entry.txt. Pure Python standard library, deterministic: the
same bytes on every run, no network, no input files.
"""

from __future__ import annotations

from pathlib import Path

LINE = (
    "One star for Monday: the standup ran long, my inbox hit triple "
    "digits before coffee, and the Wi-Fi died the second I said "
    "'can you see my screen?'"
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate mirror: 1-200 characters, one line, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
