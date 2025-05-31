from functools import reduce


def get_all_habits(manager) -> list:
    return [habit.name for habit in manager.list_habits()]


def get_habits_by_periodicity(manager, periodicity: str) -> list:
    return [habit for habit in manager.list_habits() if habit.periodicity == periodicity]


def get_longest_streak(manager) -> tuple[str, int]:
    return reduce(
        lambda acc, h: (h.name, h.get_streak()) if h.get_streak() > acc[1] else acc,
        manager.list_habits(),
        ("", 0),
    )


def get_longest_streak_by_habit(habit) -> int:
    return habit.get_streak()