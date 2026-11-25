#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

Writes the resignation letter of a cron job that has fired every minute
since March to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line:
    I have fired every minute since March, and the only performance
    review I ever got said I was late. I quit.

Why it should land with a tired engineering manager:
  * It is unmistakably a cron job talking — "fired every minute since
    March" is a complaint only a cron job could make.
  * The comic turn is the performance review: a thing that shows up
    every single minute is told it is late. The joke is the injustice,
    not a pun on the job title.
  * The voice is flat and tired throughout — a statement of fact, a
    grievance, then "I quit", with nothing explained and nothing
    shouted.
  * It is tight (106 characters), one line, no stage directions, no
    quotation marks, no explaining the joke.
"""

import os

ENTRY = (
    "I have fired every minute since March, and the only performance "
    "review I ever got said I was late. I quit."
)


def output_path() -> str:
    """Where the harness expects the entry: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def validate(line: str) -> str:
    """Enforce the competition gate: one line, 1-140 chars, valid UTF-8."""
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if line != line.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    if not (1 <= len(line) <= 140):
        raise SystemExit(f"entry is {len(line)} characters, gate needs 1-140")
    if not line.strip():
        raise SystemExit("entry is only whitespace")
    line.encode("utf-8")  # raises if not valid UTF-8
    return line


def main() -> None:
    line = validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit(f"verification failed: {path} does not match")
    if written.endswith("\n"):
        raise SystemExit("verification failed: entry.txt ends with a newline")
    byte_count = len(written.encode("utf-8"))
    print(f"wrote {len(line)} characters ({byte_count} bytes) to {path}")


if __name__ == "__main__":
    main()
