# Contact Book Application

# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact(name, phone, email):
    if name in contacts:
        print(f"Contact {name} already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def display_contacts():
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

# Menu-driven program
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        add_contact(name, phone, email)
    
    elif choice == '2':
        name = input("Enter name to search: ")
        search_contact(name)
    
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
    
    elif choice == '4':
        display_contacts()
    
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
