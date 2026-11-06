"""Convert indented code blocks into fenced blocks with a language tag.

Language: "cpp" under a heading containing "C++", "sh" in install.md, else "c".
Common leading whitespace of each block is removed.
"""
import sys
from pathlib import Path


def lang_for(path, heading):
    if path.name == "install.md":
        return "sh"
    return "cpp" if "C++" in heading else "c"


def convert(path):
    lines = path.read_text().split("\n")
    out, heading, i, n = [], "", 0, 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line
        prev_blank = not out or out[-1].strip() == ""
        if line.startswith("    ") and line.strip() and prev_blank:
            block = []
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                block.append(lines[i])
                i += 1
            while block and block[-1].strip() == "":
                block.pop()
                i -= 1
            indent = min(len(l) - len(l.lstrip(" ")) for l in block if l.strip())
            out.append("```" + lang_for(path, heading))
            out.extend(l[indent:] if l.strip() else "" for l in block)
            out.append("```")
            n += 1
            continue
        out.append(line)
        i += 1
    path.write_text("\n".join(out))
    return n


for arg in sys.argv[1:]:
    p = Path(arg)
    print(f"{convert(p):3d} {p}")
