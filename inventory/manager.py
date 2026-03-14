
import json
from .models import Habit

class HabitManager:
    def __init__(self, file_path="habits.json"):
        self.file_path = file_path
        self.habits = []


    def save(self):
        habits_in_dict = [habit.to_dict() for habit in self.habits]
        
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(habits_in_dict, file, indent=4)
            
    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return

        for habit_data in data:
            habit = Habit(
                habit_data["name"],
                habit_data["frequency"],
                habit_data["is_done_today"]
            )
            self.habits.append(habit)


    def add_habit(self, name, frequency):
        new_habit = Habit(name, frequency)
        self.habits.append(new_habit)
        self.save()
    
    def delete_habit(self, index):
        index -= 1
        if 0 <= index < len(self.habits):
            del self.habits[index]
            self.save()

    def get_habits(self):
        return self.habits.copy()

    def mark_as_done(self, index):
        index -= 1
        if 0 <= index < len(self.habits):
            self.habits[index].complete()
            self.save()

    def change_frequency(self, index, frequency):
        index -= 1
        if 0 <= index < len(self.habits):
            self.habits[index].change_frequency(frequency)
            self.save()
