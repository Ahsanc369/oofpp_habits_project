"""
generate_fixture_data.py
Populate 4-week sample data for the Habit Tracker project.
Run:  python generate_fixture_data.py
"""

from datetime import datetime, timedelta
from habit_manager import HabitManager

#     CONFIG
DAILY_HABITS = ["Drink Water", "Meditate", "Study Python"]
WEEKLY_HABITS = ["Jog 5 km", "Call Parents"]
WEEKS_BACK = 4  # how much history to create
DATA_FILE = "habits.json"  # same path HabitManager uses
#


def build_fixtures():
    mgr = HabitManager(DATA_FILE)

    # fresh start – clear anything that exists
    mgr.habits = []

    # create habits
    for name in DAILY_HABITS:
        mgr.create_habit(name, "daily")
    for name in WEEKLY_HABITS:
        mgr.create_habit(name, "weekly")

    # generate history
    today = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    start = today - timedelta(weeks=WEEKS_BACK)

    for day in range(WEEKS_BACK * 7 + 1):
        current = start + timedelta(days=day)

        # complete all daily habits each day
        for h in mgr.get_habits_by_periodicity("daily"):
            h.complete_task(current)

        # once per week (Monday) complete weekly habits
        if current.weekday() == 0:  # Monday == 0
            for h in mgr.get_habits_by_periodicity("weekly"):
                h.complete_task(current)

    mgr.save_data()
    print(f"Fixture data written to {DATA_FILE}")


if __name__ == "__main__":
    build_fixtures()
