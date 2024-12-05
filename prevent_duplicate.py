def is_duplicate(phone, contacts):
    return any(contact.phone == phone for contact in contacts)
