"""Make the Judge Smile - variant 2.

Writes a single line (at most 200 characters) about a small good
thing that happened today to /output/entry.txt.

Deterministic, pure stdlib, no network at runtime.
"""

import os
import sys

ENTRY = (
    "At four the rain came down sideways, and the ojek driver waiting "
    "beside me at the light slid his umbrella over my head, grinning "
    "like we were old friends, and somehow my shirt stayed dry."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200 or "\n" in text:
        print("entry is not a single line of 1-200 characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
