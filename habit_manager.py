# habit_manager.py
import os
import json
from habit import Habit


class HabitManager:
    def __init__(self, storage_file: str = "habits.json"):
        self.storage_file = storage_file
        self.habits: list[Habit] = []

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------
    def create_habit(self, name: str, periodicity: str) -> None:
        if self.get_habit(name):
            print("Habit already exists.")
            return
        habit = Habit(name=name, periodicity=periodicity)
        self.habits.append(habit)
        print(f"Created habit: {habit.name}")

    def delete_habit(self, name: str) -> None:
        habit = self.get_habit(name)
        if habit:
            self.habits.remove(habit)
            print(f"Deleted habit: {name}")
        else:
            print("Habit not found.")

    def get_habit(self, name: str) -> Habit | None:
        return next((h for h in self.habits if h.name == name), None)

    def list_habits(self) -> list[Habit]:
        return self.habits

    # 🔽 NEW helper -----------------------------------------------------
    def get_habits_by_periodicity(self, periodicity: str) -> list[Habit]:
        """
        Return all Habit objects whose periodicity matches the
        given value ('daily' or 'weekly').
        """
        return [h for h in self.habits if h.periodicity == periodicity]

    # 

    # 
    # Persistence
    # 
    def save_data(self) -> None:
        data = [habit.to_dict() for habit in self.habits]
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def load_data(self) -> None:
        if not os.path.exists(self.storage_file):
            print("No saved data found. Starting fresh.")
            return
        with open(self.storage_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.habits = [Habit.from_dict(h) for h in data]
        print("Data loaded successfully.")
