import csv
from contact import Contact

def save_contacts(contacts, filename='contacts.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact.name, contact.email, contact.phone, contact.address])
