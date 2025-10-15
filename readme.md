# 🪄 md2ipynb – Markdown → Jupyter Notebook Converter

**md2ipynb** is a lightweight Python script that converts Markdown (`.md`) files into Jupyter Notebook (`.ipynb`) files.  
It preserves Markdown formatting, LaTeX math expressions (`$...$`, `$$...$$`), and code blocks (```python ... ```),  
making it easy to turn notes or reports into interactive notebooks.

---

## 📂 Project Structure

```
md2ipynb/
┣ 📄 converter.py # Main converter script
┣ 📁 markdowns/ # Put your .md files here
┣ 📁 outputs/ # Converted .ipynb files will be saved here
┗ 📄 README.md
```

---

## ⚙️ How to Use

### 1️⃣ Add your Markdown files
Put all `.md` files you want to convert inside the `markdowns/` folder.

### 2️⃣ Run the converter
```bash
python converter.py
```
### 3️⃣ Check the output
Converted .ipynb files will appear in the outputs/ folder.

---
## Features
1. LaTex support : Math expressions like `$...$ and `$$...$$` are preserved and rendered by Jupyter
2. Code block detection : code blocks (python ...) are automatically converted into code cells
3. Batch conversion : All `.md` files in the `markdowns/` folder are converted at once
4. No dependencies : Works only Python's standard library. no need to install :3
---
## Example 
### Input (`markdowns/example.md`)
```# Sample Note

This is a test.  
Here’s a formula: $$E = mc^2$$
# commented it out for markdown view
# ```python
for i in range(3):
    print(i)
```
**Output (`outputs/example.ipynb`)**
- A markdown cell with the title and formula  
- A code cell running the loop

---
## 💡 Tip

You can preview the generated `.ipynb` files directly on **GitHub** or through **nbviewer.org**  
without needing to open Jupyter locally.

---

## 📄 License

This project is released under the **MIT License**. See `LICENSE` file for details.
