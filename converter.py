import json
from pathlib import Path

def md_to_ipynb(md_path, output_path):
    """Convert one .md file to .ipynb"""
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cells = []
    buffer = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            # 코드 블록 여닫기
            if not in_code:
                in_code = True
                if buffer:
                    cells.append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": buffer
                    })
                    buffer = []
            else:
                in_code = False
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

    # 남은 텍스트 처리
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
    print(f"✅ {md_path.name} → {output_path.name} 변환 완료")


def main():
    base_dir = Path(__file__).parent
    input_dir = base_dir / "markdowns"
    output_dir = base_dir / "outputs"

    # 폴더 없으면 자동 생성
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    md_files = list(input_dir.glob("*.md"))

    if not md_files:
        print("⚠️ 변환할 .md 파일이 없습니다. markdowns/ 폴더에 파일을 넣어주세요.")
        return

    for md_file in md_files:
        output_file = output_dir / md_file.with_suffix(".ipynb").name
        md_to_ipynb(md_file, output_file)

    print("\n🎉 모든 변환이 완료되었습니다!")
    print(f"📁 결과 폴더: {output_dir.resolve()}")


if __name__ == "__main__":
    main()

