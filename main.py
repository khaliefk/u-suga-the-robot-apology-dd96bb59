#!/usr/bin/env python3
"""Write the robot apology entry to /output/entry.txt.

Two lines: one sentence owning a specific mistake, one sentence
naming the lesson and the changed behaviour that follows from it.
"""

import os
from pathlib import Path

ENTRY = (
    "I am sorry I washed your passport with your navy jeans "
    "because I emptied your pockets without looking.\n"
    "From now on I will shake every pocket out over the table "
    "and check for cards and paper before I start the wash.\n"
)


def main() -> None:
    # Gate from the kit: UTF-8 text, 1 to 400 characters, two lines.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry is {len(text)} characters"
    assert len(text.splitlines()) == 2, "entry must be exactly two lines"
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
