"""
File: contact.py
Author: Jonathan Dotse
Purpose: Defines the contact class with an object that takes name and 
phone as parameters and then return it as a string
Date: 07/14/26
"""
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"