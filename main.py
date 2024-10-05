import turtle # Imports turtle

def instructions(): # Creates a function to print instructions
    print("1. Enter North, East, South, or West to move around the map") # Prints rule #1
    print("2. Escape the vault, explore the map, and eliminate enemies") # Prints rule #2
    menu() # Brings back to menu

def playgame(): # Creates a function to start the game
    my_turtle = turtle.Turtle() # Setting up turtle

    choice = input("\n-----Choose Room-----\n1. Bunker Bedroom\n2. Bunker Living Room\n3. Bunker Kitchen\n4. Gas Station\n5. Gas Station Basement\n Enter your choice (1, 2, or 3): ") # Asks the user which room they would like to visit
    if choice == "1": # Checks if they want to enter the first room
        print("\nLaunching Bunker Bedroom...\n") # Tells the user that they are entering the first room
        bunker1(my_turtle, 100) # Builds the first room
    elif choice == "2": # Checks if the user would like to enter the second room
        print("\nLaunching Bunker Living Room...\n") # Tells the user that they chose to enter the second room
        bunker3(my_turtle, 100) # Builds the second room
    elif choice == "3": # Checks if the user would like to enter the third room
        print("\nLaunching Bunker Kitchen...\n") # Tells the user that they chose to enter the third room
        bunker2(my_turtle, 100) # Buids the third room
    elif choice == "4": # Checks if the user would like to enter the fourth room
        print("\nLaunching Gas Station...\n") # Tells the user they chose to enter the fourth room
        gasStation1(my_turtle, 100) # Builds the fourth room
    elif choice == "5": # Checks if the user would like to enter the fifth room
        print("\nLaunching Gas Station Basement...\n") # Tells the user that they chose to enter the fifth room
        gasStation2(my_turtle, 100) # Builds the fifth room
    else: # Checks if the number is not between 1 and 5
        print("Error: Try a number between 1 and 5") # Tells the user to choose a new number between 1 and 5
        menu() # Brings back to menu

def bunker1(t, length): # Makes function to display the bunker bedroom
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
        t.left(90) # Moves turtle by 90 degrees
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
    t.right(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    """Displays the room description using the given turtle."""
    description = """
    -----Bunker Bedroom-----
    You are looking north.
    There is a door behind you.
    There is a bed in the southwest corner.
    There is a closet in the northeast corner.
    There is a chair in the northwest corner.
    """ # Writes description for the bunker bedroom

    t.penup()  # Lift the pen to move without drawing
    t.goto(-50, -50)  # Move turtle to position below the squares for text display
    t.pendown()  # Lower the pen to start writing

    # Print each line of the description
    for line in description.strip().split('\n'):
        t.write(line.strip(), font=("Arial", 12, "normal"))
        t.penup()
        t.sety(t.ycor() - 20)  # Move down to the next line
        t.pendown()

    turtle.done()

def bunker2(t, length):
    t.forward(length) # Moves turtle forward 100 spaces
    t.right(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    for _ in range(2): # Replays function bellow twice
        t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    description = """
        -----Bunker Kitchen-----
        You are looking east.
        There is a door behind you.
        There is a stove, fridge, and toaster in the northeast corner.
        There is a dining room table in the southeast corner.
        *Hidden in the northeast corner, there is a rusty knife.*
        """ # Writes description for bunker kitchen

    t.penup()  # Lift the pen to move without drawing
    t.goto(-250, -50)  # Move turtle to position below the squares for text display
    t.pendown()  # Lower the pen to start writing

    # Print each line of the description
    for line in description.strip().split('\n'):
        t.write(line.strip(), font=("Arial", 12, "normal"))
        t.penup()
        t.sety(t.ycor() - 20)  # Move down to the next line
        t.pendown()

def bunker3(t, length):
    for _ in range(3): # Replays function bellow thrice
        t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    for _ in range(3): # Replays function bellow thrice
        t.forward(length) # Moves turtle forward 100 spaces
    t.left(90) # Moves turtle by 90 degrees
    t.forward(length) # Moves turtle forward 100 spaces
    t.forward(length) # Moves turtle forward 100 spaces
    description = """
        -----Bunker Living Room-----
        You are looking east.
        There is a door behind you.
        There is a 43" tv, couch, and rug in the middle of the room.
        There are war posters scatter around the walls.
        The door to your bedroom is northwest, the exit is north, and the door to the kitchen is northeast.
        *Perhaps there's something hidden behind the posters*
        """ # Writes description for bunker living room

    t.penup()  # Lift the pen to move without drawing
    t.goto(-200, -50)  # Move turtle to position below the squares for text display
    t.pendown()  # Lower the pen to start writing

    # Print each line of the description
    for line in description.strip().split('\n'):
        t.write(line.strip(), font=("Arial", 12, "normal"))
        t.penup()
        t.sety(t.ycor() - 20)  # Move down to the next line
        t.pendown()

def gasStation1(t, length):
    text = turtle.Turtle()
    gas = turtle.Turtle()
    gas.color('red')
    gas.up()
    gas.goto(-50, 0)
    gas.down()
    for i in range(8): # Replays function bellow 8 times
        gas.forward(100) # Moves turtle forward 100 spaces
        gas.left(45)
    text.up()
    text.goto(-300, -200)

    description = """
        -----Gas Station-----
        You are looking north.
        You look around and find some bandages and a pocket knife
        """ # Writes description for the gas station

    gas.penup()  # Lift the pen to move without drawing
    gas.goto(-100, -150)  # Move turtle to position below the squares for text display
    gas.pendown()  # Lower the pen to start writing

    # Print each line of the description
    for line in description.strip().split('\n'):
        gas.write(line.strip(), font=("Arial", 12, "normal"))
        gas.penup()
        gas.sety(gas.ycor() - 20)  # Move down to the next line
        gas.pendown()

    turtle.done()

    playgame()

def gasStation2(t, length):
    locker = turtle.Turtle()
    gas2 = turtle.Turtle()
    gas2.color('black')
    gas2.up()
    gas2.goto(-50, 0)
    gas2.down()
    gas2.forward(200)
    gas2.left(90) # Moves turtle by 90 degrees
    gas2.forward(100) # Moves turtle forward 100 spaces
    gas2.left(90) # Moves turtle by 90 degrees
    gas2.forward(200) # Moves turtle forward 100 spaces
    gas2.left(90) # Moves turtle by 90 degrees
    gas2.forward(100) # Moves turtle forward 100 spaces
    gas2.left(90) # Moves turtle by 90 degrees

    locker.up() # Moves turtle forward 100 spaces
    locker.goto(0, 75)
    locker.down()
    locker.forward(20) # Moves turtle forward 100 spaces
    locker.left(90) # Moves turtle by 90 degrees
    locker.forward(20) # Moves turtle forward 100 spaces
    locker.left(90) # Moves turtle by 90 degrees
    locker.forward(20) # Moves turtle forward 100 spaces
    locker.left(90) # Moves turtle by 90 degrees
    locker.forward(20) # Moves turtle forward 100 spaces
    locker.left(90) # Moves turtle by 90 degrees

    description = """
        -----Gas Station Basement-----
        You are looking north.
        There is an employee locker on the western side of the room.
        Inside may contain a backpack with money.
        """

    gas2.penup()  # Lift the pen to move without drawing
    gas2.goto(-100, -150)  # Move turtle to position below the squares for text display
    gas2.pendown()  # Lower the pen to start writing

    # Print each line of the description
    for line in description.strip().split('\n'):
        gas2.write(line.strip(), font=("Arial", 12, "normal"))
        gas2.penup()
        gas2.sety(gas2.ycor() - 20)  # Move down to the next line
        gas2.pendown()

    turtle.done()

def menu(): # Sets main menu function
    choice = input("\n-----Menu-----\n1. Play\n2. Instructions\n3. Quit\nEnter your choice (1, 2, or 3): ") # Displays options on them ain menu
    if choice == "1": # Checks if the user chose option 1
        playgame() # Plays game

    elif choice == "2": # Checks if the user chose option 2
        instructions() # Shows instructions
    elif choice == "3": # Checks if user chose option 3
        print("Thanks for playing!") # Thanks the user for playing
    else: # Checks if user didnt choose a number between 1 and 3
        print("Error: Try a number between 1 and 3") # Tells the user that they need to choose a number between 1 and 3
        menu() # Replays menu

menu() # Starts menu