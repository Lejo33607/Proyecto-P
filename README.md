# Hi my name is Alejandro Gonzalez, and this is project-parking
------------------------------------------------------------------
This presentation about a code that simulates a small parking lot system.
The objective of this program is to manage vehicles inside a parking lot with 10 spaces.
The program allows the user to check available spaces, insert a vehicle using a license plate, remove a vehicle, and exit the program.
I am going to explain the code step by step.
________________________________________________________________________________________________
#
At the beginning there is a variable called Parqueadero.
This variable is a list that represents the parking lot.
The list contains ten elements, and each element represents one parking space.

Each space is initialized with a dot ".".
This symbol is used to represent an empty space in the parking lot.

And that's i'm using for make it more easy for me (the coder) at the time of making the list.

So, at the start of the program, every parking space is empty.

The list is acting as a structure that stores the vehicles currently parked in the system.

After the parking lot is created, the program starts a loop using while True.

The while True statement creates an infinite loop.

This means the program keeps running continuously until it receives a command to stop.

Inside this loop, the program is showing a menu to the user.

The menu shows four options:

View available spaces

Insert a vehicle

Remove a vehicle

And exit the program

At this moment, the program is waiting for the user to choose an option.

The program uses the input() function to read the user's selection and store it in the variable called opcion.

If the user chooses option "1", the program shows the current state of the parking lot.

First, the program prints a title that indicates the parking lot status.

And show the empty space in it.

Next, the program uses a for loop.

This loop iterates through the ten positions of the parking list.

The variable i represents the index of each parking space.

In Python, list indexes start at zero, so the values of i range from 0 to 9.

While this loop is executing, the program is checking each position in the parking lot.

For every iteration, the program evaluates a condition.

The condition checks whether the element at position i is equal to ".".

If the element is a dot, the program prints a message indicating that the space is empty.

If the element is not a dot, this means that a vehicle is occupying that parking space.

In that case, the program prints the space number and the license plate stored in that position.

While this process is happening, the program is scanning the parking lot one space at a time.

At the end of the loop, the user can see the complete status of the parking lot.

If the user chooses option "1", the program shows the current state of the parking lot.

First, the program prints a title that indicates the parking lot status.

Next, the program uses a for loop.

This loop iterates through the ten positions of the parking list.

The variable i represents the index of each parking space.

In Python, list indexes start at zero, so the values of i range from 0 to 9.

While this loop is executing, the program is checking each position in the parking lot.

For every iteration, the program evaluates a condition.

The condition checks whether the element at position i is equal to ".".

If the element is a dot, the program prints a message indicating that the space is empty.

If the element is not a dot, this means that a vehicle is occupying that parking space.

In that case, the program prints the space number and the license plate stored in that position.

While this process is happening, the program is scanning the parking lot one space at a time.

At the end of the loop, the user can see the complete status of the parking lot.

If the user chooses option "1", the program shows the current state of the parking lot.

First, the program prints a title that indicates the parking lot status.

Next, the program uses a for loop.

This loop iterates through the ten positions of the parking list.

The variable i represents the index of each parking space.

In Python, list indexes start at zero, so the values of i range from 0 to 9.

While this loop is executing, the program is checking each position in the parking lot.

For every iteration, the program evaluates a condition.

The condition checks whether the element at position i is equal to ".".

If the element is a dot, the program prints a message indicating that the space is empty.

If the element is not a dot, this means that a vehicle is occupying that parking space.

In that case, the program prints the space number and the license plate stored in that position.

While this process is happening, the program is scanning the parking lot one space at a time.

At the end of the loop, the user can see the complete status of the parking lot.

If the user chooses option "2", the program starts the vehicle insertion process.

First, the system asks the user to enter the license plate of the vehicle.

The license plate is stored in a variable called placa.

Before inserting the vehicle, the program performs several checks.

The first check determines whether the vehicle is already inside the parking lot.

The program uses the expression placa in Parqueadero.

This expression searches the list to see if the plate already exists.

If the license plate is already present, the program prints a message informing the user that the vehicle is already parked.

This prevents duplicate vehicles in the parking lot.

If the vehicle is not present, the program checks whether the parking lot is full.

To do this, the program verifies if the symbol "." does not exist in the list.

If the dot is not found, it means there are no empty spaces available.

In that case, the system prints a message indicating that the parking lot is full.

If the parking lot still has empty spaces, the program starts searching for the first available spot.

At this moment, the program is looping through the list again using another for loop.

While the loop is running, the program is examining each parking space.

When the program finds a space containing ".", it replaces that dot with the license plate.

This action stores the vehicle in the parking lot.

After storing the plate, the program prints a message showing the space number where the vehicle is parked.

Immediately after inserting the vehicle, the program uses the break statement.

The break statement stops the loop.

This ensures that the vehicle is inserted only once.

If the user selects option "4", the program prints a message saying "Saliendo".

After printing the message, the program uses the break statement.

The break statement terminates the while True loop.

Once the loop stops, the program ends its execution.
