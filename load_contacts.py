import csv
from contact import Contact

def load_contacts(filename='contacts.csv'):
    contacts = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    contacts.append(Contact(*row))
    except FileNotFoundError:
        print("No previous contacts found.")
    return contacts
