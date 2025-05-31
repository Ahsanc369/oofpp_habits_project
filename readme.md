# Habit Tracker CLI App

A command-line habit tracking application built with Python for the IU course **Object-Oriented and Functional Programming with Python (DLBDSOOFPP01)**.

## 📌 Features
- Create, complete, and analyze daily or weekly habits
- Streak tracking for habit consistency
- Functional programming used for analytics
- Persistent data storage using JSON files
- Clean CLI interface (pure `input()` based)

## 🚀 Getting Started

### Requirements
- Python 3.7+

### Installation
```bash
# Clone the repo
https://github.com/yourusername/oofpp_habits_project.git
cd oofpp_habits_project

# (Optional) create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Run the App
```bash
python habit_tracker_main.py
```

## 💻 Usage (Sample)
```text
--- Habit Tracker CLI ---
1. Create a new habit
2. Complete a habit
3. View all habits
4. Analyze habits
5. Save and Exit
```

## 📂 File Structure
```
habit_tracker_main.py      # Main CLI entry point
habit.py                   # Habit class
habit_manager.py           # Habit management
analytics.py               # Functional analytics
habits.json                # Example tracking data
README.md                  # You're reading it!
```

## 🧪 Testing
Tests can be written using `pytest` or `unittest`. (Not included by default.)

## 📄 Phase Documents
This repository includes deliverables for all 3 project phases:
- `Phase1_Habit_Concept.pdf`
- `Phase2_Habit_Development_Slides.pdf`
- `Abstract.pdf`

## 📘 License
This project is part of a student assignment and is not licensed for commercial use.
