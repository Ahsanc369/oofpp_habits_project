from datetime import datetime, timedelta


class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.created_at = datetime.now()
        self.completions = []

    def complete_task(self, date=None):
        if date is None:
            date = datetime.now().date()
        self.completions.append(date)

    def is_broken(self) -> bool:
        """
        A habit is broken if any gap between consecutive completions
        (or between the most-recent completion and today) exceeds
        the allowed period (1 day for daily, 7 days for weekly).
        """
        if not self.completions:
            return True

        dates = sorted(self.completions)

        # Add today as final comparison point
        today = datetime.now().date()
        dates.append(today)

        # Daily: max 1 day gap, Weekly: max 7 day gap
        max_gap = timedelta(days=1 if self.periodicity == "daily" else 7)

        for i in range(1, len(dates)):
            if (dates[i] - dates[i - 1]) > max_gap:
                return True

        return False

    def get_streak(self) -> int:
        if not self.completions:
            return 0

        sorted_dates = sorted(self.completions, reverse=True)
        streak = 1
        max_gap = timedelta(days=1 if self.periodicity == "daily" else 7)

        for i in range(1, len(sorted_dates)):
            if (sorted_dates[i - 1] - sorted_dates[i]) <= max_gap:
                streak += 1
            else:
                break

        return streak

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [d.isoformat() for d in self.completions],
        }

    @staticmethod
    def from_dict(data):
        h = Habit(name=data["name"], periodicity=data["periodicity"])
        h.created_at = datetime.fromisoformat(data["created_at"])
        h.completions = [datetime.fromisoformat(d).date() for d in data["completions"]]
        return h

    def __str__(self):
        return f"Habit(name={self.name}, periodicity={self.periodicity}, streak={self.get_streak()})"