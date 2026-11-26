"""The Funniest Out-of-Office (u-kreutzx-the-funniest-out-of-office-054815cf).

Writes one line of an out-of-office auto-reply, the funniest we can make it,
to /output/entry.txt.

The line: the sender is out until Monday, and the server they are asked about
is out of office too — it left before they did. One concrete object, one
scene, twist in the last four words.
"""

from pathlib import Path

ENTRY = (
    "I am out until Monday. If this is about the server, "
    "it is also out of office. It left before I did."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: entry must be 1-140 characters, UTF-8, one line, not only whitespace.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    # Read back what was written and confirm it matches, byte for byte.
    if OUTPUT_PATH.read_text(encoding="utf-8") != ENTRY:
        raise ValueError("entry.txt does not match ENTRY after write")


if __name__ == "__main__":
    main()
