
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from habit_tracker import Habit

def test_create_habit():
    habit = Habit("Walk", "daily")

    assert habit.name == "Walk"
    assert habit.frequency == "daily"
    assert habit.is_done_today is False


def test_complete_habit():
    habit = Habit("walk", "daily")

    habit.complete()

    assert habit.is_done_today is True


def test_change_frequency():
    habit = Habit("walk", "daily")

    habit.change_frequency("weekly")

    assert habit.frequency == "weekly"


def test_to_dict():
    habit = Habit("walk", "daily")

    data = habit.to_dict()

    assert data["name"] == "walk"
    assert data["frequency"] == "daily"
    assert data["is_done_today"] is False

