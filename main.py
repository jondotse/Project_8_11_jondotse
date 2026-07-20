"""
File: main.py
Author: Jonathan Dotse
Purpose: A program that lets multiple users manager a contact through a menu
Date: 07/17/26
"""
from contact_manager import ContactManager

username = (input("What's your username?")).title()

manager = ContactManager(username)

print(f"Welcome {username}!")

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
            print("Contact is successfully deleted.")

        else:
            print("This contact does not exist.\n")

    elif user_input == 5:
        print(f"Goodbye, {username}!")
        break

    else:
        print("Input not valid\n")



