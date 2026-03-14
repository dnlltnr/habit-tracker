
from datetime import date

class Habit:
    def __init__(self, name, frequency, is_done_today=False):
        self.name = name
        self.created_at = date.today()
        self.frequency = frequency
        self.is_done_today = is_done_today
    

    def to_dict(self):
        return {
            "name": self.name,
            "created_at": str(self.created_at),
            "frequency": self.frequency,
            "is_done_today": self.is_done_today
        }


    def __repr__(self):
        return f"Habit(name={self.name}, frequency={self.frequency}, created_at={self.created_at}, is_done_today={self.is_done_today})"
    
    def change_frequency(self, frequency):
        self.frequency = frequency

    def complete(self):
        self.is_done_today = True
