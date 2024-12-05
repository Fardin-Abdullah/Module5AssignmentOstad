from save_contacts import save_contacts

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ")
    original_length = len(contacts)
    contacts = [contact for contact in contacts if contact.phone != phone]

    if len(contacts) < original_length:
        save_contacts(contacts)
        print("Contact removed successfully.")
    else:
        print("Error: Contact not found.")

    return contacts
