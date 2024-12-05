def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print(contact)
            print("-" * 20)
