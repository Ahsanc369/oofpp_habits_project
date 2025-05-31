# habit_tracker_main.py
# Entry point for Habit Tracking App CLI

from datetime import datetime
from habit import Habit
from habit_manager import HabitManager
from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_by_habit,
)
import json


def main():
    manager = HabitManager()
    manager.load_data()

    while True:
        print("\n--- Habit Tracker CLI ---")
        print("1. Create a new habit")
        print("2. Complete a habit")
        print("3. View all habits")
        print("4. Analyze habits")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ")
            manager.create_habit(name, periodicity)

        elif choice == "2":
            name = input("Habit to complete: ")
            habit = manager.get_habit(name)
            if habit:
                habit.complete_task(datetime.now())
                print(f"Completed task for {habit.name}.")

        elif choice == "3":
            for habit in manager.list_habits():
                print(habit)

        elif choice == "4":
            print("Analytics:")
            print("1. All habits")
            print("2. Habits by periodicity")
            print("3. Longest streak overall")
            print("4. Longest streak for a habit")
            sub_choice = input("Choose an analytics option: ")

            if sub_choice == "1":
                print(get_all_habits(manager))
            elif sub_choice == "2":
                per = input("Enter periodicity: ")
                print(get_habits_by_periodicity(manager, per))
            elif sub_choice == "3":
                print(get_longest_streak(manager))
            elif sub_choice == "4":
                name = input("Habit name: ")
                habit = manager.get_habit(name)
                if habit:
                    print(get_longest_streak_by_habit(habit))

        elif choice == "5":
            manager.save_data()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
