# 🤖 AI Code Refactor & Auto-Optimizer

An intelligent Python script that automatically refactors and optimizes Python code using AI-inspired heuristics and Abstract Syntax Tree (AST) analysis. It transforms clunky, inefficient code into clean, Pythonic, and performance-optimized masterpieces.

---

## 🚀 Features

- 🧠 AI-Based Refactor Engine  
  Uses lightweight machine learning-inspired decision trees to analyze and improve code readability, structure, and logic.

- ⚙️ Performance Optimizer  
  Detects redundant operations and unnecessary variables, replacing them with optimized alternatives.

- 🧱 AST-Powered Parsing  
  Parses and reconstructs Python code using Python’s native `ast` module for deep code introspection.

- 📊 Code Quality Scoring  
  Evaluates code complexity and assigns a quality score to help you understand how clean and maintainable your code is.

- 🔁 Automatic Refactoring  
  Applies transformations like:
    - Loop simplification
    - Nested `if` flattening
    - Recursion detection
    - Unused variable cleanup

---

## 📦 Installation

Clone the repository and run the script:

``` git clone https://github.com/brettadams0/ai-code-refactor.git cd ai-code-refactor python3 refactor.py ```


---

## 🧠 How It Works

1. Parses your Python source code into an Abstract Syntax Tree (AST).
2. Evaluates the AST using a set of intelligent rules and heuristics.
3. Suggests or automatically applies:
   - Pythonic simplifications
   - Structural optimizations
   - Variable renaming and loop transformation
4. Outputs the refactored code along with a code quality score (0–100).

---

## 📂 Project Structure

```
ai-code-refactor/ 
├── refactor.py # Main script to run refactoring 
├── sample_code.py # Example Python file for testing 
└── README.md # This file
```
---

## ✨ Example

Input:
```
def example(a, b): x = a + b for i in range(len(x)): print(i) return x
```
Refactored Output:
```
def example(a, b): x = a + b for x_item in x: print(x_item) return x
```

Code Quality Score: 92/100

---

## ⚠️ Disclaimer

This tool uses simple heuristics and does not guarantee perfect code transformation. Always review refactored output before using it in production.

---

## 🧩 Future Ideas

- GPT-based code suggestion integration
- CLI with LSP-style code hints
- Integration with GitHub Actions for auto-refactor pull requests
- Web-based interface with live code evaluation

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Created by [Brett Adams] — because your code deserves to be elegant and fast.
