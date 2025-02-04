import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
   
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts = load_contacts()
    
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully!")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"{name}: {details['Phone']}")

def search_contact():
  
    query = input("Enter Name or Phone Number: ").strip()
    contacts = load_contacts()
    
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    
    if not found:
        print("Contact not found!")

def update_contact():
   
    name = input("Enter Name of the Contact to Update: ").strip()
    contacts = load_contacts()
    
    if name in contacts:
        print("Leave a field blank to keep existing data.")
        phone = input(f"Enter New Phone ({contacts[name]['Phone']}): ").strip() or contacts[name]['Phone']
        email = input(f"Enter New Email ({contacts[name]['Email']}): ").strip() or contacts[name]['Email']
        address = input(f"Enter New Address ({contacts[name]['Address']}): ").strip() or contacts[name]['Address']
        
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
   
    name = input("Enter Name of the Contact to Delete: ").strip()
    contacts = load_contacts()
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

def main():
   
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
