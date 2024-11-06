# Define a dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    # Save contact details in the dictionary
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"\nContact {name} added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print()

# Function to search for a contact
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details["phone"]:
            print(f"\nFound Contact - Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
            break
    
    if not found:
        print("Contact not found.\n")

# Function to update an existing contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("\nEnter new details (leave blank to keep existing information):")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]["phone"]
        email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]["email"]
        address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]["address"]
        
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"\nContact {name} updated successfully!\n")
    else:
        print("Contact not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name} deleted successfully!\n")
    else:
        print("Contact not found.\n")

# Main function to display menu and handle user actions
def contact_book():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

# Run the Contact Book program
contact_book()
