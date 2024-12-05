import csv
from contact import Contact

class FileManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename

    def save_to_file(self, contacts):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for contact in contacts:
                writer.writerow([contact.name, contact.email, contact.phone, contact.address])

    def load_from_file(self):
        contacts = []
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        contacts.append(Contact(*row))
        except FileNotFoundError:
            print("No previous contacts found.")
        return contacts
