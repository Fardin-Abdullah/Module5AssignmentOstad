def search_contact(contacts):
    term = input("Enter name, email, phone, or address to search: ")
    results = [contact for contact in contacts if term in contact.name or term in contact.email or term in contact.phone or term in contact.address]

    if results:
        for contact in results:
            print(contact)
            print("-" * 20)
    else:
        print("No contacts found matching the search criteria.")
