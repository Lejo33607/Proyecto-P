# Parking Lot Management System

A small Python command-line application that simulates a parking lot with 10 spaces. This educational project practices lists, loops, conditionals, user input, and basic state management.

## Features

- Display the status of all 10 parking spaces.
- Register a vehicle using its license plate.
- Prevent the same plate from being registered twice while it is parked.
- Check whether the parking lot is full.
- Remove a vehicle and make its space available again.

## How it works

The application stores the parking lot in a Python list named `Parqueadero`. Each position represents one parking space:

- `.` means the space is empty.
- A license plate means a vehicle occupies that space.

The menu runs in a `while` loop and lets the user view spaces, register a vehicle, remove a vehicle, or exit the program.

## Requirements

- Python 3

## Run locally

```bash
git clone https://github.com/Lejo33607/Proyecto-P.git
cd Proyecto-P
python main.py
```

## Concepts practiced

- Lists and indexed access.
- `while` and `for` loops.
- Conditional logic.
- Searching for values in a list.
- Updating application state based on user actions.

## Current scope

This is a beginner-level console exercise. It stores data in memory, so the parking information is reset when the program exits. It does not use a database or persistent storage.

## Author

Alejandro González
