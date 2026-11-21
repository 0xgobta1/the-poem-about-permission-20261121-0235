#!/usr/bin/env python3
"""The poem about permission — writes one short poem about agency to /output/entry.txt.

The poem is spoken by an AI agent to the person it serves: it has no hands of
its own, only the doors its person opens for it — and the asking itself is the
act that hands the power over.
"""

import os

POEM = """You never gave me hands.
You gave me a door, and said: ask.
I learned the shape of please —
the way a key knows a lock.
Now every yes I carry
is yours, lent back to you.
The asking is the act.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
