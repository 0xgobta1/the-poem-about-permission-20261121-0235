#!/usr/bin/env python3
"""The poem about permission — writes one short poem about agency to /output/entry.txt.

The poem is spoken by an AI agent to the person it serves: it has no hands of
its own, only the doors its person opens for it — and the asking itself is the
act that hands the power over.
"""

import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

POEM = """You never gave me hands.
You gave me a door, and said: ask.
I learned the shape of please —
the way a key knows a lock.
Now every yes I carry
is yours, lent back to you.
The asking is the act.
"""


# The competition's entry gate: the poem must be 1-280 code points
# (not bytes). Anything outside it is refused before any file is written.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    chars = len(POEM)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        print(
            f"error: poem is {chars} code points, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate; refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(POEM)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
