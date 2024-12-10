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

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    name = input("Please provide contact name: ")
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        email = input("Please provide email address: ")
        phone = input("Please provide phone number: ")
        contacts[name] = {'email': email, 'phone': phone}
        print(f"{name} has been added!")

def edit():
    name = input("Please provide the contact you would like to edit: ")
    if name in contacts:
        phone = input(f"Please provide phone number for {name} or press Enter to keep {contacts[name]['phone']}: ") 
        email = input(f"Please provide email address for {name} or press Enter to keep {contacts[name]['email']}: ")
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
        print(f"{name} has been deleted!")
    else:
        print(f"{name} not found!")

def search_contacts():
    name = input("Please provide contact name to search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")

def display_all_contacts():
    print("\nFull Contact List:")
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}\n")
    else:
        print("No contacts found!")

def export_contacts():
    with open("contacts.txt", "w") as file:
        for name, info in contacts.items():
            file.write(f"Name: {name}\nEmail: {info['email']}\nPhone: {info['phone']}\n\n")
        print("Contacts have been exported to contacts.txt")

def import_contacts():
    if not os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            print("No file found!")
            return
        with open("contacts.txt", "r") as


            lines = file.readlines()
            for i in range(0, len(lines), 4):  
                name = lines[i].strip().split(": ")[1]
                email = lines[i+1].strip().split(": ")[1]
                phone = lines[i+2].strip().split(": ")[1]
                contacts[name] = {'email': email, 'phone': phone}
        print("Contacts have been imported successfully!")
    else:
        print("No file found!")

def run_cli():
    while True:
        display_menu()
        try:
            choice = int(input("Please choose 1-8: "))  
        except ValueError:
            print("Invalid option, please try again.")
            continue

        if choice == 1:
            add_contact()
        elif choice == 2:
            edit()
        elif choice == 3:
            delete_contact()
        elif choice == 4:
            search_contacts()
        elif choice == 5:
            display_all_contacts()
        elif choice == 6:
            export_contacts()
        elif choice == 7:
            import_contacts()
        elif choice == 8:
            print("Thank you, have a great day!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    run_cli()