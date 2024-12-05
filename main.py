from add_contact import add_contact
from view_contacts import view_contacts
from remove_contact import remove_contact
from load_contacts import load_contacts
from save_contacts import save_contacts
from search_contact import search_contact

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Save Contacts")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            contacts = remove_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved.")
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print(f"Invalid input: {choice}. Please select a valid option.")

if __name__ == "__main__":
    main()
