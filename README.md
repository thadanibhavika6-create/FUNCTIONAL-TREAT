# DATA-ANALYZER-TRANSFORMER
---
##📊 Data Analyzer and Transformer — Python Project

 A simple, menu-driven console application built in Python to input, analyze, filter, sort, and summarize numeric data, all through an easy-to-use terminal interface.

---
## 🚀 Project Overview

This project is a **Data Analyzer and Transformer** built using core Python (no external libraries required). It allows anyone to load a dataset and instantly explore it — summarize it, filter it, sort it, and calculate statistics — directly from the terminal with a clean menu system.

The tool lets you:
- ➕ **Input Data** — enter a 1D array of numbers
- 📋 **Display Data Summary** — view total elements, min, max, sum & average using built-in functions
- 🔁 **Calculate Factorial** — compute the factorial of a number using recursion
- 🧹 **Filter Data by Threshold** — filter out values above a limit using a lambda function
- 🔽 **Sort Data** — arrange data in ascending or descending order
- 📈 **Display Dataset Statistics** — get min, max, sum & average returned together from one function
- 🚪 **Exit** — close the program safely

It's a great beginner-to-intermediate project demonstrating loops, built-in functions, recursion, lambda functions, and functions that return multiple values in Python.

---
<img width="1200" height="538" alt="data_analyzer_overview" src="https://github.com/user-attachments/assets/f43ff2b2-b5db-406e-b70d-56e5305d5cb9" />

---

## 🗂️ Project Files

| File Name | Description |
|---|---|
| 🐍 `data_analyzer.py` | Main Python script with all functionality |
| 📘 `README.md` | Project documentation |

---

## 🧩 Program Structure

The program runs on a `while True` main loop displaying a menu, and routes user choices to the following features:

| Menu Option | Functionality |
|---|---|
| 1 | Input data for the array |
| 2 | Display data summary (built-in functions) |
| 3 | Calculate factorial of a number (recursion) |
| 4 | Filter data by threshold (lambda function) |
| 5 | Sort data (ascending / descending) |
| 6 | Display dataset statistics (multiple return values) |
| 7 | Exit the program |

---

## 🔹 Key Features

### 1️⃣ Input Data
Accepts a 1D array of integers from the user as space-separated values and stores it for use across the program.

### 2️⃣ Display Data Summary
Uses Python's built-in functions to instantly show:
- Total number of elements
- Minimum value
- Maximum value
- Sum of all values
- Average value

### 3️⃣ Calculate Factorial (Recursion)
Takes a number from the user and calculates its factorial using a recursive function, then prints the function's docstring.

### 4️⃣ Filter Data by Threshold (Lambda Function)
Takes a threshold value and uses `filter()` with a `lambda` function to return only the values greater than that threshold.

### 5️⃣ Sort Data
Lets the user choose ascending or descending order and displays the sorted dataset accordingly.

### 6️⃣ Display Dataset Statistics (Multiple Return Values)
Calls a function that calculates and returns the minimum, maximum, total, and average all at once, then prints them along with the function's docstring.

### 7️⃣ Exit
Gracefully ends the program with a thank-you message.

---

## 📦 Data Fields Used

| Field | Description |
|---|---|
| `arr` | The stored 1D array of numbers entered by the user |
| `threshold` | Value used to filter the array |
| `sort_choice` | User's choice of ascending or descending order |

---

## 🛠️ Tools & Concepts Used

Python (Core / Standard Library only):
- ✅ Lists for data storage
- ✅ `while` loop for menu-driven interface
- ✅ Built-in functions — `min()`, `max()`, `sum()`, `len()`
- ✅ Recursion for factorial calculation
- ✅ Lambda functions with `filter()`
- ✅ Functions returning multiple values
- ✅ Conditional statements (`if` / `elif`)
- ✅ `input()` for user interaction
- ✅ Type casting (`int()`)

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open a terminal in the project folder
4. Run the script:
```bash
python data_analyzer.py
```
5. Follow the on-screen menu to input, summarize, filter, sort, or analyze your data

---

## 📌 Sample Workflow

- Choose **1** → Input your dataset
- Choose **2** → View the data summary
- Choose **3** → Calculate a factorial
- Choose **4** → Filter data above a threshold
- Choose **5** → Sort the data
- Choose **6** → View full dataset statistics
- Choose **7** → Exit the program

---

## 🌟 Future Enhancements

- 💾 Save/load data to a file (CSV / JSON) for persistence
- 🔢 Support for 2D arrays / matrices
- ✅ Input validation (e.g., non-numeric entries, empty array checks)
- 🖥️ GUI version using Tkinter
- 📊 Export results to Excel/CSV report
- 📉 Add data visualization (charts/graphs) using matplotlib
  
---
## sample output
<img width="900" height="1350" alt="sample output1" src="https://github.com/user-attachments/assets/92a1ce52-404a-4be9-b63e-a7ce30184f7e" />
---

---
## video link
[watch_video_here](https://drive.google.com/file/d/1O_Wd6bEZuwT2334J76wLjm2ccrJAd1Sf/view?usp=drive_link)
---
---
## 👩‍💻 Author

Bhavika Thadani
📍 India
---
---

## 🙌 Feedback & Contributions

Suggestions, improvements, and pull requests are always welcome! Feel free to fork this repository or open an issue if you'd like to contribute.

---
📊 *Turning Raw Numbers Into Insights, One Dataset at a Time*

---
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![GitHub stars](https://img.shields.io/github/stars/thadanibhavika6-create/FUNCTIONAL-TREAT?style=social)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
