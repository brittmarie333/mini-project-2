contacts_id = None
contacts_data = {}

for line in lines:
    if line.startswith("ID: "):
        if contacts_id and contact_data:
            contacts[contacts_id] = contact_data
        contacts_id = line.split(":")[1].strip()
        contacts_data ={}

    elif line.