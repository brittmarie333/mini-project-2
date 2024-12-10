#User Interface (UI):
#Create a user-friendly command-line interface (CLI) for the Contact Management System.
#Display a welcoming message and provide a menu with the following options:
#Welcome to the Contact Management System! 
#Menu:
#1. Add a new contact
#2. Edit an existing contact
#3. Delete a contact
#4. Search for a contact
#5. Display all contacts
#6. Export contacts to a text file
#7. Import contacts from a text file *BONUS*
#8. Quit

import os

contacts ={}

def display_menu():
    print("Menu:")
    print("1. Add Contact")
    print("2. Edit")
    print("3. Delte")
    print("4. Search Contacts")
    print("5. Display All Contacts:")
    print("6. Export Contacts to text file:")
    print("7. Import Contacts from text file:")
    print("8. Quit")


def add_contact():
    pass
def edit():
    name = input("Please provide the contact you would like to edit: ")
    if name in contacts:
        phone = input(f"Please provide phone number for {name} or press Enter to keep {contacts[name]['phone']}") 
        email = input(f"Please provide email address for {name} or press Enter to keep {contacts[name]['email']}")
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
    else:
        print(f"{name} not found!")

def delete_contact():
    name = input("Please provide the contact you would like to delete: ")
    if name in contacts:
        del contacts[name]
        print(f'{name} has been deleted!')
    else:
        print("{name} not found!")

def search_contacts():
    name = input("Please provide contact: ")
    if name in contacts:
        print(f"{name}")
        print(f"{contacts[name]['phone']}")
        print(f"{contacts[name]['email']}")
    else:
        print("Contact not found!")


def display_all_contacts():
    print("\nFull Contact List: " )
    if name in contacts:
        for name, info in contacts.items():
            print(f"{name}")
            print(f"{info['phone']}")
            print(f"{info['email']}")
    else;
        print("No contacts found!")

def export_contacts():
    with open("contacts.txt", "w") as file:
        for name, info in contacts.items():
            file.write(f"Name: {name}\nEmaill: {info['email']}\nPhone: {info['phone']}\n")
        print("Contacts have been exported to contacts.tXt")


def import_contacts():
    if os.path.exists(contacts.txt):
        with open ("contacts.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                name = lines[i].strip().split(":")[1]
                email = lines[i+1].strip().split(":")[1]
                phone = lines[i+2].strip().split(":")[1]
                contacts[name]= {'email': email, 'phone': phone}
    else:
        print("No file found!")



def quit():
    print