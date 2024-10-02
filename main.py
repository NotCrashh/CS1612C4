import turtle

def instructions():
    print("Test")
    menu()

def playgame():
    print("hello")

def bunker1():
    print("test")

def menu():
    input("1. Play\n2. Instructions\n3. Quit\nChoose: ")
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