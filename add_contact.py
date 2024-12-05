from contact import Contact
from save_contacts import save_contacts
from error_handling import validate_name, validate_phone
from prevent_duplicate import is_duplicate

def add_contact(contacts):
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    if not validate_name(name) or not validate_phone(phone):
        return contacts

    if is_duplicate(phone, contacts):
        print("Error: Phone number already exists.")
    else:
        new_contact = Contact(name, email, phone, address)
        contacts.append(new_contact)
        save_contacts(contacts)
        print("Contact added successfully!")

    return contacts
