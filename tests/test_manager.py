
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from inventory.manager import HabitManager


def test_add_habit():
    manager = HabitManager()

    manager.add_habit("walk", "daily")

    assert len(manager.habits) == 1
    assert manager.habits[0].name == "walk"


def test_delete_habit():
    manager = HabitManager()

    manager.add_habit("walk", "daily")
    manager.delete_habit(1)

    assert len(manager.habits) == 0


def test_mark_as_done():
    manager = HabitManager()

    manager.add_habit("walk", "daily")
    manager.mark_as_done(1)

    assert manager.habits[0].is_done_today is True


def test_save_and_load(tmp_path):
    file_path = tmp_path / "habits.json"

    manager = HabitManager(file_path)
    manager.add_habit("walk", "daily")
    manager.save()

    new_manager = HabitManager(file_path)
    new_manager.load()

    assert len(new_manager.habits) == 1
    assert new_manager.habits[0].name == "walk"

    

def test_delete_invalid_index():
    manager = HabitManager()

    manager.add_habit("walk", "daily")
    manager.delete_habit(5)

    assert len(manager.habits) == 1



