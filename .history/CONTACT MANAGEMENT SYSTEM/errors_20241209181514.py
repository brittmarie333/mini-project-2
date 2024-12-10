def add_contact():
    try:
        contact_id = input("Enter the contact's unique identifier (phone number or email): ")

        if contact_id in contacts:
            print("A contact with this identifier already exists.")
            return

        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        address = input("Enter the contact's address: ")
        notes = input("Enter any additional notes: ")

        contacts[contact_id] = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'notes': notes
        }
        print(f"Contact for {name} added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the contact: {e}")