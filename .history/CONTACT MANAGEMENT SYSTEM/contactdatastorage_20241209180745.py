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

if contacts_

