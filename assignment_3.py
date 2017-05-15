import json
import os

# =========
# Uppgift 1

# Part 1
# User is being asked to provide his/hers firstname, lastname and place of birth. Theese
# values are being stored as a dictionary in a list. Finally all values of the dictionary is being printed."""

list = []
print("This is part 1 of the assignment:")
firstName = input("What is your Firstname?\n")
lastName = input("What is your Lastname?\n")
placeOfBirth = input("What is your place of birth?\n")
newPerson = {"firstname": firstName, "lastname": lastName, "POB": placeOfBirth}
list.append(newPerson)

# print all values in list
for person in list:
    print(person)


# Part 2
# User is asked to make a choice of creating new player or to print existing players.
#   Every player has attributes as follows: Firstname, lastname and the country it plays for.
#    Player information is stored in a textfile: players.txt

def start():
    print("\nThis is part 2 of the assignment: Printing and reading data to a .txt file\n")
    while True:
        choice = input("Select (1) to add new player\nSelect (2) to print all players registrered\n"
                       "Enter any other key to quit program and continue to the next assignment.\n")

        if choice == "1":
            # User get to enter new player details
            first = input("Enter players firstname:\n")
            last = input("Enter players lastname:\n")
            country = input("Enter player country\n")
            add_player(first, last, country)

        elif choice == "2":
            # Print all player information
            try:
                print_players()
            except Exception:
                print("No file to open, try adding a player..");
                start();
            else:
                print("opened file successfully");

        else:
            print("Goodbye!")
        break;


# Function will read details from textfile and display it to user
def print_players():
    print("Printing players...")
    file = open("players.txt", "r")
    print(file.read())
    file.close()


# Function will create new player: firstname, lastname and country
# Function will store theese details in a textfile: player.txt
def add_player(first, last, country):
    # if file doesn't exist, create one
    if not (os.path.isfile("./players.txt")):
        print("Creating new file..")
        text_file = open("players.txt", "w")
    # Otherwise open existing file
    else:
        print("File exists! Adding player...")
        text_file = open("players.txt", "a")  # appending text to existing file

    # Add player to file
    str = ",".join([first, last, country])
    text_file.write(str + "\n")
    text_file.close()


start()


# =========
# Part 3 is almost the same as part 2 although, the data is formatted and stored in a .json file instead of a .txt
def start_json():
    print("\nThis is part 3 of the assignment: Printing and reading json formatted data to a .json file\n")
    while True:
        choice = input("Enter (1) to add player or (2) to print registered players\n"
                       "Press any other key to quit program.\n")

        if choice == "1":
            first = input("Enter firstname:\n")
            last = input("Enter lastname:\n")
            country = input("Enter country\n")
            add_player_json(first, last, country)
        elif choice == "2":
            try:
                print_players_json()
            except:
                print("No file to open, try adding a player");
                start_json();
            else:
                print("Successfully printed file content");
        else:
            print("Goodbye! Thank you for playing!")
        break


# Function prints all players in file
def print_players_json():
    with open("players.json", "r") as file:
        json_content = json.load(file)
        print(json_content)


# Function adds new player to file
def add_player_json(first, last, country):
    new_player = {
        "firstname": first,
        "lastname": last,
        "country": country}

    # If there isn't a file, create one
    if not (os.path.isfile("./players.json")):
        print("Creating json file...")
        with open('players.json', 'w') as file:
            json.dump([], file)  # wrap with list
            file.close()

    # Open existing file content and store it in variable
    with open("players.json", 'r') as file:
        json_data = json.load(file)
        file.close()

        # Append new entries to existing data
        json_data.append(new_player)

    # Overwrite existing file with appended content
    with open("players.json", "w") as file:
        json.dump(json_data, file, indent=4)


# Start program
start_json()
