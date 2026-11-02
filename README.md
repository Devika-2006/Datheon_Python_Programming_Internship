# 🐍 Datheon Python Programming Internship Projects

## 📝 Project Overview

This repository contains four Python projects created as part of the Datheon Python Programming Internship. The projects apply Python to practical tasks, including an interactive word game, a customer support chatbot, a file organizer, and an investment portfolio tracker.

## 🎯 Objectives

The objectives of these projects are to:

- Build interactive programs that accept and validate user input.
- Use Python collections, functions, loops, and conditional logic.
- Apply regular expressions to recognize common questions.
- Organize files safely using Python’s file-handling tools.
- Calculate portfolio values and export results to a CSV file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| `random` | Random word selection in Hangman |
| `re` | Pattern matching in the chatbot |
| `pathlib` | File and folder paths |
| `shutil` | Moving files |
| `csv` | Saving portfolio summaries |
| GitHub | Version control and project hosting |

## 📂 Projects

### 1. 🎮 Hangman

A terminal-based word-guessing game. The player guesses a hidden word one letter at a time and has up to six incorrect guesses.

**Features**

- Randomly selects a word from a built-in list.
- Displays ASCII gallows as incorrect guesses accumulate.
- Shows the correctly guessed letters and letters already tried.
- Prevents repeated guesses from counting as extra mistakes.
- Displays a win or loss message.

**Run the game**

```bash
python hangman.py
```

### 2. 🤖 Customer Support Chatbot

A rule-based terminal chatbot that responds to greetings and common questions using keywords and regular expressions.

**Topics it recognizes**

- Business hours
- Shipping and delivery
- Returns and refunds
- Payment methods
- Support contact information

The chatbot can answer multiple recognized topics in one message and provides a fallback when it does not recognize a question. Type `bye`, `exit`, or `quit` to end the conversation.

**Run the chatbot**

```bash
python chatbot.py
```

> The business hours and support contact details are sample values. Update them in the script to match the business you want to represent.

### 3. 🗂️ File Organizer

A command-line utility that sorts files in a selected folder into category subfolders based on file extensions.

**Categories**

- Documents
- Images
- Videos
- Audio
- Archives
- Code

**Features**

- Organizes files directly inside the selected folder.
- Leaves existing subfolders and symbolic links untouched.
- Avoids overwriting files when a destination name already exists.
- Reports files moved, skipped, or affected by errors.
- Includes a dry-run option to preview planned moves.

**Preview planned changes**

```bash
python organizer.py "PATH_TO_FOLDER" --dry-run
```

**Organize the folder**

```bash
python organizer.py "PATH_TO_FOLDER"
```

> Replace `PATH_TO_FOLDER` with the directory you want to organize.

### 4. 📈 Portfolio Tracker

A terminal program for recording stock holdings and calculating their value and gain or loss.

For each holding, enter a ticker symbol, purchase price per share, number of shares, and current price per share. Type `DONE` when you have finished entering holdings.

**Features**

- Calculates the amount invested in each holding.
- Calculates each holding’s current value and gain or loss.
- Displays portfolio-wide totals and percentage gain or loss.
- Writes the transaction summary to `portfolio_summary.csv`.

**Run the tracker**

```bash
python portfolio.py
```

> Current prices are entered manually. The program does not fetch live market data.

## 🔄 Project Workflow

```text
Plan each project
        ↓
Write the Python program
        ↓
Handle user input and common errors
        ↓
Display results in the terminal
        ↓
Save portfolio data to CSV where applicable
        ↓
Upload the projects to GitHub
```

## 📁 Project Structure

```text
Datheon_Python_Programming_Internship/
├── hangman.py
├── chatbot.py
├── organizer.py
├── portfolio.py
├── portfolio_summary.csv   # Generated when portfolio.py is run
└── README.md
```

## 🎓 Learning Outcomes

Through these projects, I practiced:

- Python functions, loops, conditionals, and collections.
- Input validation and exception handling.
- Text normalization and regular-expression matching.
- File and directory operations.
- Collision-safe file naming.
- CSV file creation and formatted console output.
- Organizing and documenting projects in GitHub.

## 📋 Requirements

- Python 3.10 or later
- No third-party packages required

## 👤 Author

**Devika S**  
Computer Science Student

## ⭐ Conclusion

These four projects demonstrate practical uses of Python, from interactive terminal programs to file organization and CSV reporting. Building them provided hands-on experience with input handling, pattern matching, file operations, calculations, and clear project documentation.
