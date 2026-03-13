# Project Parking

### Alejandro Gonzalez and this is my code

I'll explain how the code work.

---

## Parking Lot Structure

At the beginning of the program there is a variable called **Parqueadero**.

This variable is a **list** that represents the parking lot.

The list contains **10 elements**, and each element represents one parking space.

Each space is initialized with a dot `"."`, which represents an **empty space**.

This makes it easy to identify which spaces are free and which are occupied.

---

## Program Loop

After creating the parking lot, the program starts a loop using **`while True`**.

This creates an **infinite loop**, which keeps the program running until the user decides to exit.

Inside this loop, the program shows a menu where the user can choose different actions.

The user's selection is read using the **`input()`** function and stored in a variable called **opcion**.

---

## Viewing Parking Spaces

If the user selects option **1**, the program displays the current state of the parking lot.

To do this, the program uses a **for loop** that goes through each position in the list.

For each space, the program checks if the value is `"."`.

If it is `"."`, the space is empty.

If it is not `"."`, the program prints the **license plate** of the vehicle parked in that space.

This allows the user to see the status of all parking spaces.

---

## Inserting a Vehicle

If the user selects option **2**, the program asks for the **license plate**.

Before inserting the vehicle, the program performs two checks.

First, it verifies if the vehicle is **already in the parking lot**.

Second, it checks if the parking lot is **full**.

If there is an empty space available, the program searches for the **first spot containing `"."`** using another **for loop**.

When it finds one, it replaces the dot with the **license plate**.

After inserting the vehicle, the program uses **`break`** to stop the loop so the vehicle is inserted only once.

---

## Exiting the Program

If the user selects option **4**, the program prints **"Saliendo"**.

Then the program uses **`break`** to stop the **`while True` loop**, and the program ends.
