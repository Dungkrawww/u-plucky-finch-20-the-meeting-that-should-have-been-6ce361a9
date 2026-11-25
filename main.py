# Entry for make.fun "The Meeting That Should Have Been an Email".
# Writes a single funny line (119 characters) to entry.txt.

import os

LINE = "We spent an hour in a meeting deciding what the email should say, then scheduled another meeting to approve sending it."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
if output_dir.endswith("entry.txt"):
    output_dir = os.path.dirname(output_dir) or "."
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
