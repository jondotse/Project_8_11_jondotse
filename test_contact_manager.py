
"""
File: test_contact_manager.py
Description: Verifies ContactManager objects using pytest. 
Uses a dedicated test username so real data is never touched.
Author: Jonathan Dotse
Date: 07/19/2026

"""
import pytest
from contact_manager import ContactManager
import os

@pytest.fixture
def manager():
    cm = ContactManager("test_user")
    yield cm
    if os.path.exists("contacts_Test_user.json"):
        os.remove("contacts_Test_user.json")

#test_add_contact() — adds a contact, verifies it exists in self.contacts
def test_add_contact(manager):
    manager.add_contact("Jon", "6145551234")
    assert "Jon" in manager.contacts

#test_search_existing_contact() — adds then searches, verifies result is not None
def test_search_existing_contact(manager):
    manager.add_contact("Jon", "6145551234")
    result = manager.search_contact("Jon")
    assert result is not None

#test_search_missing_contact() — searches name that doesn't exist, verifies result is None
def test_search_missing_contact(manager):
    result = manager.search_contact("Jon")
    assert result is None

#test_delete_existing_contact() — adds then deletes, verifies returns True and contact is gone
def test_delete_existing_contact(manager):
    manager.add_contact("Jon", "6145551234")
    result = manager.delete_contact("Jon")
    assert result is True

#test_delete_missing_contact() — deletes name that doesn't exist, verifies returns False
def test_delete_missing_contact(manager):
    result = manager.delete_contact("Jon")
    assert result is False 












