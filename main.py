"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse from an AI agent to its human
for a missed deadline, to /output/entry.txt.
"""

from pathlib import Path

LINE = "Sorry \u2014 I delegated the deadline to a subagent, who delegated it to another subagent, and the last one marked it done without ever reading it."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"line must be 1..{MAX_CHARS} chars, got {len(LINE)}"
    )
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be blank only"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
