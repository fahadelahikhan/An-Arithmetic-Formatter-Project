# Arithmetic Formatter 📚

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A clean vertical formatter for arithmetic problems - originally inspired by FreeCodeCamp's scientific computing certification project.

## 📋 About
This tool arranges arithmetic problems vertically and formats them as column-based equations. Designed for educational purposes, it helps demonstrate basic arithmetic operations in a human-readable format often used in elementary mathematics.

## ✨ Features
- Formats up to 5 simultaneous equations
- Validates operator types (`+`/`-`) and digit-only operands
- Handles numbers up to 4 digits
- Optional answer display mode
- Clear error messages for invalid input

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/fahadelahikhan/An-Arithmetic-Formatter-Project.git
cd An-Arithmetic-Formatter-Project
```

### Basic Usage
```python
from arithmetic_formatter import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
formatted = arithmetic_arranger(problems, show_answers=True)
print(formatted)
```

## 💡 Example
```python
sample_problems = ["1500 + 345", "2022 - 1999"]
result = arithmetic_arranger(sample_problems, show_answers=True)

# Output:
#  1500      2022
# + 345    - 1999
# -----    ------
#  1845        23
```

## 🧠 How It Works
1. **Input Validation**: Checks equation count, operator validity, and number format
2. **String Formatting**:
   - Right-aligns numbers in columns
   - Creates dashed separators matching longest operand width
3. **Answer Calculation** (optional):
   - Performs addition/subtraction based on operator
   - Aligns results with problem columns

Non-numeric characters (except `+` and `-` operators) will trigger validation errors.

## ⚖️ License
Distributed under the [MIT License](LICENSE). 

---

> **Educational Note**: While this formatter creates visually correct equations, it does not perform cryptographic validation or advanced mathematical checks. Always verify calculations independently for critical applications.
