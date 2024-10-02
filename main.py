import turtle

def instructions():
    print("1. Enter North, East, South, or West to move around the map")
    print("2. Escape the vault, explore the map, and eliminate enemies")
    menu()

def playgame():
    print("hello")

def bunker1():
    print("test")

def menu():
    input("\n-----Menu-----\n1. Play\n2. Instructions\n3. Quit\nEnter your choice (1, 2, or 3): ")
    if input == "1":
        playgame()

    elif input == "2":
        instructions()
    elif input == "west":
        print("Thanks for playing!")
    else:
        print("Error: Try a number between 1 and 3")
        menu()
menu()