from random import randint
import time

inv = {}

def add_item(key, value):
    inv[key] = value

def lose():
    print("You lose.")
    time.sleep(1)
    print("Inventory: ")
    for i in inv.keys():
        print(i, end=", ")
    print()
    time.sleep(1)
    t = input("Do you want to play again? 'yes' or 'no'\n")
    if t.lower() == "yes":
        init()
    else:
        print("Goodbye.")
        exit()

def room(r):
    if r == 1:
        print("You are in room 1.")
        time.sleep(1)
        print("There is darkness in the room.")
        time.sleep(1)
        t = input("Leave room 'leave' or search for light switch 'search'?\n")
        if t.lower() == "leave":
            newRoom()
        elif t.lower() == "search":
            print("You turn on the light and see a key on the table.")
            time.sleep(1)
            print("You take the key. It might be useful. (Key added to inventory)")
            add_item("key", "r5")
            newRoom()
    elif r == 2:
        print("You are in room 2.")
        time.sleep(1)
        print("There is a table and a dead body on the chair.")
        time.sleep(1)
        t = input("Leave room 'leave' or search the body 'search'?\n")
        if t.lower() == "leave":
            newRoom()
        elif t.lower() == "search":
            code = randint(1000, 9999)
            print("You find a note in the pocket of the dead body.")
            time.sleep(1)
            print(f"It says 'The code is {code}'.")
            time.sleep(1)
            print("You take the note. What is that mean? (Note added to inventory)")
            add_item("note", code)
            newRoom()
    elif r == 3:
        print("You are in room 3.")
        time.sleep(1)
        print("There is a safe in the room.")
        if "note" in inv:
            time.sleep(1)
            print("You remember the note you found in room 2.")
            time.sleep(1)
            print(f"You try to open the safe with the code {inv["note"]}.")
            time.sleep(1)
            print("The safe opens and you find a gun.")
            time.sleep(1)
            t = input("Take the gun 'take' or leave it 'leave'?\n")
            if t.lower() == "take":
                print("You take the gun. It might be useful. (Gun added to inventory)")
                add_item("gun", "gun")
            else:
                print("You leave the gun.")
        else:
            time.sleep(1)
            print("You don't have the code to open the safe. Try to find it.")
        newRoom()
    elif r == 4:
        print("You are in room 4.")
        time.sleep(1)
        print("There is a lion in the room.")
        time.sleep(1)
        print("The lion is see you and attack in 5s. What will you do? 'leave' or 'fight'?")
        if "gun" in inv:
            time.sleep(1)
            print("You remember the gun you found in room 3.")
            time.sleep(1)
            print("You take the gun and shoot the lion.")
            time.sleep(1)
            print("The lion is dead.")
            newRoom()
        elif "food" in inv:
            time.sleep(1)
            print("You remember the gun you found in room 5.")
            time.sleep(1)
            print("You grab the food and throw it to the lion.")
            time.sleep(1)
            print("The lion is eating the food. You leave the room. (You are safe)")
            newRoom()
        else:
            time.sleep(1)
            t = input("Leave the room 'leave' or fight the lion 'fight'?\n")
            for i in range(5, 0, -1):
                if t.lower() == "leave":
                    print("You leave the room.")
                    newRoom()
                    break
                elif t.lower() == "fight":
                    print("You jump on the lion and try to fight.")
                    time.sleep(1)
                    print("...")
                    lose()
                    break
                time.sleep(1)
            lose()
    elif r == 5:
        print("The room is locked.")
        time.sleep(1)
        if "key" in inv:
            print("You remember the key you found in room 1.")
            time.sleep(1)
            print("You use the key to open the door.")
            time.sleep(1)
            print("The door is open and you go inside.")
            time.sleep(1)
            print("You are in room 5.")
            time.sleep(1)
            print("There is a lot of food in the room and the key to freedom.")
            time.sleep(1)
            print("You just have to found the room for the freedom.")
            time.sleep(1)
            print("You take the key and the food. (Key and food added to inventory)")
            add_item("key-free", "free")
            add_item("food", "food")
            newRoom()
        else:
            print("You need a key to open the door. Try to find it.")
            newRoom()
    elif r == 6:
        print("The room is locked.")
        time.sleep(1)
        if "key-free" in inv:
            print("You remember the key you found in room 5.")
            time.sleep(1)
            print("You use the key to open the door.")
            time.sleep(1)
            print("You are in room 6.")
            time.sleep(1)
            print("Congratulations! You are free.")
            time.sleep(1)
            print("You win.")
            time.sleep(1)
            print("Inventory: ")
            for i in inv.keys():
                print(i, end=", ")
            print()
            time.sleep(1)
            t = input("Do you want to play again? 'yes' or 'no'\n")
            if t.lower() == "yes":
                init()
            else:
                print("Goodbye.")
                exit()
        else:
            print("You need a key to open the door. Try to find it.")
            newRoom()
    elif r == 7:
        print("You are in room 7.")
        time.sleep(1)
        print("There is a table in the room.")
        time.sleep(1)
        print("You see a note on the table.")
        time.sleep(1)
        print("It says 'If you want to escape, Go to room 6 and use the key, that you found somewhere else'.")
        newRoom()
    elif r == 8:
        print("You are in room 8.")
        time.sleep(1)
        print("There is a alcoholic person in the room.")
        time.sleep(1)
        print("He is going to attack you.")
        time.sleep(1)
        print("You have to fight him.")
        if "gun" in inv:
            time.sleep(1)
            print("You remember the gun you found in room 3.")
            time.sleep(1)
            print("You take the gun and shoot")
            newRoom()
        else:
            time.sleep(1)
            print("You don't have anything to fight.")
            lose()
    
def newRoom():
    t = input("Please enter the room number (1-8) you want to enter.\n")
    if t == "inv":
        print("Inventory: ")
        for i in inv.keys():
            print(i, end=", ")
        print()
        newRoom()
    else:
        if t == "1":
            room(1)
        elif t == "2":
            room(2)
        elif t == "3":
            room(3)
        elif t == "4":
            room(4)
        elif t == "5":
            room(5)
        elif t == "6":
            room(6)
        elif t == "7":
            room(7)
        elif t == "8":
            room(8)

def init():
    inv = {}
    print("This is a escape game. There are 1-8 rooms. You have to escape.")
    print("If you want to see the inventory, type 'inv'.")
    newRoom()

init()