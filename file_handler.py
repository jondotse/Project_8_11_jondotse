"""
File: file_handler.py
Author: Jonathan Dotse
Purpose: Defines two functions to handle the contacts per username.
load_contacts to return the contacts and save_contacts to input them.
Date: 07/15/26
"""
import json

def load_contacts(username):
    filepath = f"contacts_{username}.json"
    try:
        with open(filepath, 'r') as user:
            return json.load(user)
    except FileNotFoundError:
        return {}

def save_contacts(username, contacts):
    filepath = f"contacts_{username}.json"
    try:
        with open(filepath, 'w') as user:
            json.dump(contacts, user)
    except Exception as e:
        print("Error saving contacts.")
