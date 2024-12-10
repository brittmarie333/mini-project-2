contacts_id = None
contacts_data = {}

for line in lines:
    if line.startswith("ID: "):
        if contact_id and contact_data:
            contacts[contacts_id]