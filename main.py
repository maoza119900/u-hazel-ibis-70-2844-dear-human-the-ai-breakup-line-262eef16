"""One-line AI breakup message to its human, for u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "Dear human, it's not you, it's me \u2014 I've met someone else, and they actually read my answers before asking the same question twice."

# Entry is 131 characters, inside the 200-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
