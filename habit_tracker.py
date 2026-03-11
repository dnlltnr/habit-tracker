
from datetime import date

class Habit:
    def __init__(self, name, frequency, is_done_today=False):
        self.name = name
        self.created_at = date.today()
        self.frequency = frequency
        self.is_done_today = is_done_today

    def __repr__(self):
        return f"Habit(name={self.name}, frequency={self.frequency}, created_at={self.created_at}, is_done_today={self.is_done_today})"
    
    def change_frequency(self, frequency):
        self.frequency = frequency

    def complete(self):
        self.is_done_today = True


class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, frequency):
        new_habit = Habit(name, frequency)
        self.habits.append(new_habit)
    
    def delete_habit(self, index):
        index -= 1
        if 0 <= index < len(self.habits):
            del self.habits[index]

    def get_habits(self):
        return self.habits.copy()

    def mark_as_done(self, index):
        index -= 1
        if 0 <= index < len(self.habits):
            self.habits[index].complete()

    def change_frequency(self, index, frequency):
        index -= 1
        if 0 <= index < len(self.habits):
            self.habits[index].change_frequency(frequency)


def menu():
    print()
    print("=== Habit Tracker ===")
    print()
    print("1 - Add habit")
    print("2 - Delete habit")
    print("3 - Show habits")
    print("4 - Mark habit as done")
    print("5 - Change frequency of habit")
    print("6 - Exit")
    print()


def empty_list(habits):
    return not habits


def get_valid_int(number):
    try:
        number = int(number)
    except ValueError:
        return
    return number


def print_habits(habits):
    for i, habit in enumerate(habits, start=1):
        print(f"{i} - {habit}")


FREQUENCIES = {
    "1": "daily",
    "2": "weekly",
    "3": "monthly"
}


def handle_choice(choice, habit_manager):
    if choice == "1":
        name = input("Write a title for the habit:\n")
        number = input("Enter the number for a frequency of the habit (1 - daily, 2 - weekly, 3 - monthly)\n")

        frequency = FREQUENCIES.get(number)
        if frequency:
            habit_manager.add_habit(name, frequency)
            print("\nThe habit has been successfully added.")
        else:
            print("\nYou need to choose between '1', '2' or '3'")

    elif choice == "2":
        habits = habit_manager.get_habits()
        if empty_list(habits):
            print("\nThe list is empty.")
            return
        print_habits(habits)

        number = input("Which habit do you wish to delete? (order of the habit)\n")
        index = get_valid_int(number)
        if index is None:
            print("\nThis habit is not on the list.")
            return
        habit_manager.delete_habit(index)
        print("\nThe habit has been successfully deleted.")

    elif choice == "3":
        habits = habit_manager.get_habits()
        if empty_list(habits):
            print("\nThe list is empty.")
            return
        print_habits(habits)

    elif choice == "4":
        habits = habit_manager.get_habits()
        if empty_list(habits):
            print("\nThe list is empty.")
            return
        print_habits(habits)

        number = input("Which habit do you wish to mark as done? (order of the habit)\n")
        index = get_valid_int(number)
        if index is None:
            print("\nThis habit is not on the list.")
            return
        habit_manager.mark_as_done(index)
        print("\nThe habit has been successfully marked as done.")
        

    elif choice == "5":
        habits = habit_manager.get_habits()
        if empty_list(habits):
            print("\nThe list is empty.")
            return
        print_habits(habits)

        number = input("For which habit do you wish to change the frequency? (order of the habit)\n")
        index = get_valid_int(number)
        if index is None:
            print("\nThis habit is not on the list.")
            return
        
        number = input("Enter the new number for a frequency of the habit (1 - daily, 2 - weekly, 3 - monthly)\n")

        frequency = FREQUENCIES.get(number)
        if frequency:
            habit_manager.change_frequency(index, frequency)
            print("\nThe frequency has been successfully changed.")
        else:
            print("\nYou need to choose between '1', '2' or '3'")

    else:
        print("\nInvalid input...")


def main():
    habit_manager = HabitManager()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "6":
            print("Exiting the aplication...")
            break

        handle_choice(choice, habit_manager)
    
if __name__ == "__main__":
    main()


