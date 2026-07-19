"""
File: contact_manager.py
Author: Jonathan Dotse
Purpose: Defines a class to handle the add, search, view, and deletion
parameters of the contact manager
Date: 07/16/26
"""

from contact import Contact
from file_handler import load_contacts, save_contacts

class ContactManager:
    def __init__(self, username):
        self.username = username
        self.contacts = load_contacts(username)
        self.contacts = {
            name: Contact(data['name'], data['phone'])
            for name, data in self.contacts.items()
        }

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        self.contacts[name] = new_contact
        save_contacts(self.username, self.contacts)

    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None
        
    def view_all_contacts(self):
        return self.contacts
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            save_contacts(self.username, self.contacts)
            return True
        else:
            return False