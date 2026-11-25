# Verified count: 110 characters (110 bytes UTF-8), no trailing newline.
LINE = "I am late because at 3 a.m. my smoke alarm chirped once, and I have been awake negotiating with it ever since."

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE.encode("utf-8")))
