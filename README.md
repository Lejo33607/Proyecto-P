# Project Parking

### Alejandro Gonzalez
# And this is my code
---

## Parking Lot Structure

At the beginning of the program there is a variable called **Parqueadero**.

This variable is a **list** that represents the parking lot.

The list has **10 elements**, and each element represents one parking space.

Each space is initialized with a dot `"."`, which represents an **empty space**.

---

## Program Loop

The program runs inside a **`while True` loop**, which keeps it running continuously.

Inside this loop, the program shows a menu and waits for the user to choose an option using the **`input()`** function.

The selected option is stored in a variable called **opcion**.

---

## Viewing Parking Spaces

If the user selects option **1**, the program shows the parking lot status.

It uses a **for loop** to go through each position in the list.

If the value is `"."`, the space is empty.
If it is not `"."`, the program shows the **license plate** of the vehicle parked there.

---

## Inserting a Vehicle

If the user selects option **2**, the program asks for the **license plate**.

The program checks if the vehicle is already in the parking lot and if there are available spaces.

If a space is available, it finds the **first empty spot `"."`** and replaces it with the license plate.

After inserting the vehicle, the program uses **`break`** to stop the loop.

---

## Exiting the Program

If the user selects option **4**, the program prints **"Saliendo"** and uses **`break`** to stop the **`while True` loop**, ending the program.
