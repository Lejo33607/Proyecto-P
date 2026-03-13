# Project Parking

### Alejandro Gonzalez

---

## Introduction

Hi, my name is Alejandro Gonzalez and this is **Project Parking**.

This program simulates a small parking lot system.
The objective of the program is to manage vehicles inside a parking lot with **10 spaces**.

The user can:

* View available spaces
* Insert a vehicle using its license plate
* Remove a vehicle
* Exit the program

Now I will explain how the code works.

---

## Parking Lot Structure

At the beginning of the program there is a variable called **Parqueadero**.

This variable is a **list** that represents the parking lot.

The list contains **10 elements**, and each element represents one parking space.

Each space is initialized with a dot `"."`, which represents an **empty space**.

This makes it easier to identify which spaces are free and which are occupied.

---

## Program Loop and Menu

After creating the parking lot, the program starts a loop using **`while True`**.

This creates an **infinite loop**, which keeps the program running until the user decides to exit.

Inside the loop, the program shows a **menu with four options**:

1. View parking lot status
2. Insert a vehicle
3. Remove a vehicle
4. Exit the program

The program reads the user's selection using the **`input()`** function and stores it in a variable called **opcion**.

---

## Viewing Parking Spaces

If the user selects option **1**, the program displays the current state of the parking lot.

It uses a **for loop** to go through each space in the list.

For each position, the program checks if the value is `"."`.

* If it is `"."`, the space is empty.
* If not, the program shows the **license plate** of the vehicle parked there.

This allows the user to see all parking spaces one by one.

---

## Inserting a Vehicle

If the user selects option **2**, the program asks for the **license plate**.

Before inserting the vehicle, the program performs two checks:

* It verifies if the vehicle is **already inside the parking lot**.
* It checks if the parking lot is **full**.

If there is space available, the program searches for the **first empty spot** `"."` using a **for loop**.

When it finds one, it replaces the dot with the **license plate** and parks the vehicle there.

Then the program uses **`break`** to stop the loop and ensure the vehicle is inserted only once.

---

## Exiting the Program

If the user selects option **4**, the program prints the message **"Saliendo"**.

Then it uses **`break`** to stop the **`while True` loop**, and the program finishes.

