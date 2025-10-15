import json
from pathlib import Path

def md_to_ipynb(md_path, output_path):
    """Convert a single .md file to .ipynb"""
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cells = []
    buffer = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            # Toggle code block
            if not in_code:
                in_code = True
                if buffer:
                    # Add markdown cell
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": buffer
                    })
                    buffer = []
            else:
                in_code = False
                # Add code cell
                cells.append({
                    "cell_type": "code",
                    "metadata": {},
                    "execution_count": None,
                    "outputs": [],
                    "source": buffer
                })
                buffer = []
        else:
            buffer.append(line)

    # Handle remaining text
    if buffer:
        cell_type = "code" if in_code else "markdown"
        cells.append({
            "cell_type": cell_type,
            "metadata": {},
            "execution_count": None if cell_type == "code" else None,
            "outputs": [] if cell_type == "code" else [],
            "source": buffer
        })

    notebook = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    print(f"✅ {md_path.name} → {output_path.name} conversion completed")


def main():
    base_dir = Path(__file__).parent
    input_dir = base_dir / "markdowns"
    output_dir = base_dir / "outputs"

    # Create folders if they don't exist
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    md_files = list(input_dir.glob("*.md"))

    if not md_files:
        print("⚠️ No .md files found to convert. Please put your files in the 'markdowns/' folder.")
        return

    for md_file in md_files:
        output_file = output_dir / md_file.with_suffix(".ipynb").name
        md_to_ipynb(md_file, output_file)

    print("\n🎉 All files have been converted!")
    print(f"📁 Output folder: {output_dir.resolve()}")


if __name__ == "__main__":
    main()

