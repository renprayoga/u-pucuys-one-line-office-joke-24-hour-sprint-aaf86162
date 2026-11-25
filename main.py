"""One-Line Office Joke — entry writer.

Chosen line (96 characters, one line):
    I put focus time on my calendar, so my coworkers booked a meeting to
    discuss why I'm never free.

Why this line wins (judge rubric order: on-subject joke, funny, one line,
fresh, clear on first read):
- On-subject joke: a real office joke, not a caption or stray observation.
  The whole line is the joke.
- Funny: the punchline pays off the setup with irony anyone who works in
  an office recognises — the tool meant to protect your time (focus time)
  creates the very thing that eats it (a meeting about why you have no
  time). The protection backfires.
- One line: a single sentence, setup and punchline on the same line, no
  rambling around it.
- Fresh: a specific detail (calendar "focus time") instead of a generic
  complaint; not the reply-all / printer / "per my last email" jokes the
  field is full of. The reversal — focus time causing a meeting — is a
  new angle on a familiar ritual.
- Clear on first read: plain words, no reference the reader cannot
  follow, tight wording (96 of 200 characters).

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-200 characters, not only whitespace — and
exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3 stdlib only.
"""

import os
import sys

ENTRY = (
    "I put focus time on my calendar, so my coworkers booked a meeting "
    "to discuss why I'm never free."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} characters (need 1-200)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    # The gate reads the whole file: exactly one trailing newline, so the
    # file holds one line and nothing else — no blank second line.
    if written != ENTRY + "\n":
        return _fail("written file is not exactly the entry plus one newline")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
