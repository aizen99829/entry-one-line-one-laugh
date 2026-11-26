"""One Line, One Laugh -- make.fun entry.

A tiny program that writes exactly one joke to /output/entry.txt.

The joke: a person asks a household robot for wisdom, and the robot
answers the only way it knows how -- by demonstrating the problem.
Setup in the first half, twist in the second, no extra words.
Kept well under the 140-character gate so the punchline survives intact.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# One em dash carries the turn from setup to punchline; no second
# sentence needed, which keeps the whole joke inside the limit.
JOKE = (
    "I asked my robot vacuum for life advice \u2014 it bumped into the same "
    "wall twice and carried on like it had a plan all along."
)


MAX_CHARS = 140


def validate(line):
    """The competition gate is strict: one line, 1 to 140 characters."""
    assert "\n" not in line, "the joke must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"joke is {len(line)} chars, must be 1-{MAX_CHARS}"
    )


def main():
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
