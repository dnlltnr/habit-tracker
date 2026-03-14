# Habit Tracker CLI

A simple CLI habit tracker built in Python to practice software design and testing.

## Features

- CLI interface for managing habits
- OOP architecture (Habit, HabitManager)
- JSON persistence
- pytest tests
- modular project structure

## Architecture

inventory/
- models.py
- manager.py
- cli.py

tests/
- test_habit.py
- test_manager.py

## How to run

Run the CLI application:

python -m inventory.cli

Run tests:

pytest
