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
    try:
        contact_id = input("Enter the contact's unique identifier (phone number or email): ")

        if contact_id in contacts:
            print("A contact with this identifier already exists.")
            return

        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        email = input("Enter the contact email address: ")
        address = input("Enter the contact address: ")
        notes = input("Enter any additional notes: ")

        contacts[contact_id] = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'notes': notes
        }
        print(f"{name} added successfully.")

    except Exception as e:
        print(f"Error! Unable to add contact: {e}")

def edit_contact():
    try:
        contact_id = input("Enter the contact's unique identifier (phone number or email) to edit: ")

        if contact_id not in contacts:
            print("Contact not found.")
            return

        print("Editing contact details. Leave field blank to keep current value.")
        name = input(f"Name ({contacts[contact_id]['name']}): ") or contacts[contact_id]['name']
        phone = input(f"Phone ({contacts[contact_id]['phone']}): ") or contacts[contact_id]['phone']
        email = input(f"Email ({contacts[contact_id]['email']}): ") or contacts[contact_id]['email']
        address = input(f"Address ({contacts[contact_id]['address']}): ") or contacts[contact_id]['address']
        notes = input(f"Notes ({contacts[contact_id]['notes']}): ") or contacts[contact_id]['notes']

        contacts[contact_id] = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'notes': notes
        }
        print(f"{name} updated successfully.")
    except Exception as e:
        print(f"Error! Unable to update contact: {e}")

def delete_contact():
    try:
        contact_id = input("Enter the contact's unique identifier (phone number or email) to delete: ")

        if contact_id not in contacts:
            print("Contact not found.")
            return

        del contacts[contact_id]
        print("Contact deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the contact: {e}")

def search_contact():
    try:
        search_term = input("Enter the contact's name, phone, or email to search for: ")
        found = False
        for contact_id, details in contacts.items():
            if any(search_term.lower() in value.lower() for value in details.values()):
                print(f"Found contact: {details['name']} (Phone: {details['phone']}, Email: {details['email']})")
                found = True
        if not found:
            print("No contact found.")
    except Exception as e:
        print(f"An error occurred while searching for the contact: {e}")

def display_contacts():
    try:
        if not contacts:
            print("No contacts available.")
        for contact_id, details in contacts.items():
            print(f"ID: {contact_id}")
            print(f"Name: {details['name']}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print(f"Notes: {details['notes']}")
            print("-" * 20)
    except Exception as e:
        print(f"An error occurred while displaying contacts: {e}")

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for contact_id, details in contacts.items():
                file.write(f"ID: {contact_id}\n")
                for key, value in details.items():
                    file.write(f"{key.capitalize()}: {value}\n")
                file.write("-" * 20 + "\n")
        print("Contacts exported to 'contacts.txt'.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")


def import_contacts():
    try:
        if not os.path.exists("contacts.txt"):
            with open("contacts.txt", "r") as file:
                print("No file found!")
                return
            with open("contacts.txt", "r") as file:
                lines = file.readlines()

        contacts_id = None
    contacts_data = {}

    for line in lines:
        if line.startswith("ID: "):
            if contacts_id and contact_data:
                contacts[contacts_id] = contact_data
            contacts_id = line.split(":")[1].strip()
            contacts_data ={}

        elif line.startswith("Name:"):
            contacts_data['name'] = line.split(":")[1].strip()
        elif line.startswith("Email:"):
            contacts_data['email'] = line.split(":")[1].strip()
        elif line.startswith("Phone: "):
            contacts_data['phone'] = line.split(":")[1].split(":")[1].strip

    if contacts_id and contacts_data:
        contacts[contacts_id] = contacts_data

    print("Contacts imported!")

except File

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