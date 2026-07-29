# Stock Portfolio Tracker 📊

A simple interactive Python application designed to calculate and manage total investment value based on defined stock prices. Built as part of the **CodeAlpha Python Programming Internship (Task 2)**.

## 🚀 Features
- Pre-defined dictionary containing stock symbols and their respective hardcoded prices.
- Interactive Command Line Interface (CLI) for users to add stock holdings and quantities.
- Error handling for invalid stock names, zero/negative quantities, and non-integer inputs.
- Detailed portfolio summary showing quantity, price per unit, individual total value, and grand total investment.
- Option to export and save the final portfolio summary report into a `.txt` file (`portfolio_summary.txt`).

## 🛠️ Concepts & Key Technologies Used
- **Language:** Python 3
- **Data Structures:** Dictionaries, Lists
- **Control Flow:** Loops (`while`), Conditionals (`if-elif-else`)
- **File Handling:** Reading and writing text files (`open()`)
- **Input Validation:** Exception handling (`try-except`)

## 💻 How to Run
1. Make sure Python 3.x is installed on your system.
2. Run the script using terminal:
   ```bash
   python stock_tracker.py