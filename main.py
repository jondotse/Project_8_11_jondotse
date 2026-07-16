from contact_manager import ContactManager

user_input = (input("What's your username?")).title()

manager = ContactManager(user_input)

print(f"Welcome {user_input}!")

# Initializing while loop

while True:
    print("Contact Manager")
    print("----------------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        user_input = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a number.")

        continue

    # Initializing if statements

    if user_input == 1:
        name = (input("Enter name: ")).title()
        phone = input("Enter phone number: ")

        manager.add_contact(name, phone)

        print("Contact added successfully.")

    elif user_input == 2:
        name = input("Enter name to search the contact.")
        result = manager.search_contact(name)
        if result:
            print(result)

        else:
            print("Contact not found.")

    
    
    elif user_input == 3:
        result = manager.view_all_contacts()
        if result:
            print("---- All Contacts ----")
            for name in result:
                print(name + ": " + result[name].phone)
        else:
            print("No contact found.\n")

    elif user_input == 4:
        name = input("Enter name to delete contact.")
        result = manager.delete_contact(name)
        if result:
            True

        else:
             False

    elif user_input == 5:
        print("Goodbye.")
        break

    else:
        print("Input not valid\n")



"""
Part 4: Main Menu (main.py)
Description: Entry point. Handles username prompt, instantiates ContactManager, and runs the menu loop.
Requirements:
Import:

from contact_manager import ContactManager
Ask for username at startup, store as variable
Instantiate ContactManager(username)
Print welcome message using username
Run while True menu loop with try/except for invalid input
Call ContactManager methods for each menu option — no logic in main
Print "Goodbye." and break on exit



```python
# Creating a program that lets a user manage a list of contacts through a menu
# Add, searc, view, and delete contacts by name
# Jonathan Dotse, 06/22/26

# Initializing dictionary to hold contacts
contact_list = {}

# Initializing while loop

while True:
    print("Contact Manager")
    print("----------------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        user_input = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a number.")

        continue

    # Initializing if statements

    if user_input == 1:
        name.title() = input("Enter name: ")
        phone_number = input("Enter phone number: ")

        contact_list[name] = phone_number

        print("Contact added successfully.")

    elif user_input == 2:
        name = input("Enter name to search the contact.")
        if name in contact_list:
            print(name + ": " + contact_list[name])

        else:
            print("Contact not found.")
    
    
    elif user_input == 3:
        if contact_list:
            print("---- All Contacts ----")
            for name in contact_list:
                print(name + ": " + contact_list[name])

        else:
            print("No contact found.\n")

    elif user_input == 4:
        name = input("Enter name to delete contact.")
        if name in contact_list:
            del contact_list[name]

            print("Contact is successfully deleted.")

        else:
            print("This contact does not exist.\n")

    elif user_input == 5:
        print("Goodbye.")
        break

    else:
        print("Input not valid\n")
```
"""