"""One-star review written by a house cat about the human it lives with.

Writes one review line (under 200 chars) to /output/entry.txt.
"""

import os

# Final: stands there watching, as if applause was part of the deal.
REVIEW = "One star. The human refills my bowl, then stands there watching me eat, as if applause was part of the deal."


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {text!r} ({len(text)} chars) to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
