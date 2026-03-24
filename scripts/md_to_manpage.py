#!/usr/bin/env python3

import re
import argparse
from pathlib import Path

# =========================
# CONSTANTS
# =========================
SECTION_HEADERS = {
    "NAME",
    "SYNOPSIS",
    "DESCRIPTION",
    "ENVIRONMENT VARIABLES",
    "EXAMPLES",
    "EXIT VALUES",
    "SEE ALSO",
}

# =========================
# HEADER FORMATTER
# =========================
def manpage_header(cmd):
    left = f"{cmd.upper()}(1)"
    middle = "ZOAU Command Syntax"
    right = f"{cmd.upper()}(1)"

    spaces_before_middle = max(1, 30 - len(left))
    return f"{left}{' ' * spaces_before_middle}{middle}{' ' * 23}{right}"

# =========================
# MARKDOWN → MAN
# =========================
def md_to_man(lines):
    out = []
    in_code = False
    current_section = None
    skipped_title = False

    def emit(line=""):
        out.append(line)

    for raw in lines:
        line = raw.rstrip()

        if line.startswith("<!--") or "<br" in line:
            continue

        if line.strip().startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            if current_section == "EXAMPLES":
                emit("\t\t" + line)
            else:
                emit("\t" + line)
            continue

        m = re.match(r"^#{1,6}\s+(.*)", line)
        if m:
            title = m.group(1).strip()

            if not skipped_title and line.startswith("# "):
                skipped_title = True
                continue

            current_section = title.upper()
            emit(current_section)
            continue

        line = re.sub(r"`([^`]*)`", r"\1", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"^\s*-\s+", "- ", line)

        if line.strip():
            emit("\t" + line)
        else:
            emit("")

    return out

# =========================
# SECTION NORMALIZER
# =========================
def normalize_sections(lines, cmd):
    result = []
    seen_see_also = False
    prev_blank = False
    i = 0

    while i < len(lines):
        line = lines[i]
        is_blank = (line.strip() == "")

        if line in SECTION_HEADERS:
            if line == "SEE ALSO":
                seen_see_also = True

            while result and result[-1].strip() == "":
                result.pop()

            if result:
                result.append("")

            result.append(line)
            result.append("")
            prev_blank = True

            i += 1
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            continue

        if is_blank:
            if not prev_blank:
                result.append("")
                prev_blank = True
        else:
            result.append(line)
            prev_blank = False

        i += 1

    if not seen_see_also:
        while result and result[-1].strip() == "":
            result.pop()
        result.append("")
        result.append("SEE ALSO")
        result.append("")
        result.append(f"\t{cmd.lower()}(1)")

    while result and result[-1].strip() == "":
        result.pop()

    return result

# =========================
# ARGUMENT PARSING
# =========================
def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate .1 manpages from Markdown files"
    )

    parser.add_argument(
        "-i", "--input",
        type=Path,
        default=Path("zoau-core-manpage"),
        help="Input directory containing .md files"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("catgen1"),
        help="Output directory for .1 manpages"
    )

    return parser.parse_args()

# =========================
# DRIVER
# =========================
def main():
    args = parse_args()

    md_input_dir = args.input.resolve()
    man_output_dir = args.output.resolve()

    if not md_input_dir.is_dir():
        raise RuntimeError(f"Input directory not found: {md_input_dir}")

    man_output_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(
        f for f in md_input_dir.glob("*.md")
        if not f.name.startswith("_")
    )

    if not md_files:
        print("No markdown files found.")
        return

    for md_file in md_files:
        cmd = md_file.stem
        out_file = man_output_dir / f"{cmd}.1"

        with md_file.open() as f:
            md_lines = f.readlines()

        man = md_to_man(md_lines)
        man = normalize_sections(man, cmd)

        with out_file.open("w") as f:
            f.write(manpage_header(cmd) + "\n\n")
            f.write("\n".join(man) + "\n")

        print(f"Generated: {out_file}")

if __name__ == "__main__":
    main()
