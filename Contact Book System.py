# Contact Book System
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

import json 
import os 
import sys

print ("============ Welcome to Contact Book System =============")

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            data = json.load(file)   # yaha 'load' hai, 'dump' nahi
        return data
    else:
        return []

contacts = load_contacts()

# ----------------Functions for Contact Book System----------------
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def display_contact(contact):
    print("-" * 50)
    print("Name:", contact["Name"])
    print("Contact ID:", contact["Contact ID"])
    print("Phone:", contact["Phone"])
    print("Email:", contact["Email"])
    print("City:", contact["City"])
    print("-" * 50)

def add_contact():
    try:
        contact_id = int(input("Enter the Contact ID: "))
    except ValueError:
        print("Invalid Contact ID! Please enter a number.")
        return
    if contact_id <= 0:
        print("Enter a valid Contact ID!")
        return

    for contact in contacts:
        if contact["Contact ID"] == contact_id:
            print("Contact ID already exists!")
            return

    Name = input("Enter the name: ")

    if Name == "":
        print("Name cannot be empty!")
        return

    Email = input("Enter the Email: ")
    if Email == "":
        print("Email cannot be empty!")
        return

    City = input("Enter the City: ")
    if City == "":
        print("City cannot be empty!")
        return
    
    Phone = (input("Enter the Phone Number: "))
    if not Phone.isdigit():
        print("Invalid Phone Number! Please enter digits only.")
        return

    Name = Name.strip()
    City = City.strip()

    new_contact = {
        "Name": Name,
        "Email": Email,
        "Phone": Phone,
        "Contact ID": contact_id,
        "City": City,
    }

    contacts.append(new_contact)
    save_contacts()
    print("New Contact Added Successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No Contacts in record!")
        return
    for contact in contacts:
        display_contact(contact)

def search_contact():

    search_choice = input("Do you want to search by Contact ID or Name? (Enter 'ID' or 'Name'): ").strip().lower()

    if search_choice == 'id':
        try:
            search_contactid = int(input("Enter the Contact ID: "))
        except ValueError:
            print("Invalid Contact ID! Please enter a number.")
            return

        found = False
        for contact in contacts:
            if contact["Contact ID"] == search_contactid:
                display_contact(contact)
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif search_choice == 'name':
        search_name = input("Enter the Name: ").strip()

        if search_name == "":
            print("Name cannot be empty!")
            return

        found = False
        for contact in contacts:
            if contact["Name"].lower() == search_name.lower():
                display_contact(contact)
                found = True
                break

        if not found:
            print("Contact Not Found!")

    else:
        print("Invalid choice! Please enter 'ID' or 'Name'.")

def update_contact():
    try:
        search = int(input("Enter the Contact ID: "))
    except ValueError:
        print("Invalid Contact ID! Please enter a number.")
        return

    found = False
    for contact in contacts:
        if contact["Contact ID"] == search:
            print("-" * 50)
            print("Current Contact Details:")
            display_contact(contact)

            Name = input("Enter the new name (leave blank to keep current): ")
            Phone= input("Enter the new Phone Number (leave blank to keep current): ")
            Email = input("Enter the new Email  (leave blank to keep current): ")
            City = input("Enter the new City (leave blank to keep current): ")

            if Name.strip():
                contact["Name"] = Name.strip()
            if Email.strip():
                contact["Email"] = Email.strip()
            if City.strip():
                contact["City"] = City.strip()
            if Phone.strip():
                try:
                    Phone = int(Phone)
                    if Phone <= 0:
                        print("Phone Number must be a positive number! Keeping current amount.")
                    else:
                        contact["Phone"] = Phone
                except ValueError:
                    print("Invalid Phone Number! Keeping current phone number.")
            print("Contact Updated Successfully!")
            save_contacts()
            found = True
            break
    if not found:
        print("Contact Not Found!")

def delete_contact():
    try:
        search = int(input("Enter the Contact ID: "))
    except ValueError:
        print("Invalid Contact ID! Please enter a number.")
        return

    found = False
    for contact in contacts:
        if contact["Contact ID"] == search:
            confirm = input(f"Are you sure you want to delete contact {contact['Name']}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            contacts.remove(contact)
            print("Contact Deleted Successfully!")
            save_contacts()
            found = True
            break
    if not found:
        print("Contact Not Found!")

def exit_system():
    print("---------------------------------------------------")
    print("Exiting the Contact Book System.")
    print("Thank you for using the system. Goodbye!")
    print("---------------------------------------------------")
    sys.exit()

while True:
    print()
    print("=============== Select the Option (0-5) ===============")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 0:
        exit_system()
        break
    else:
        print("Invalid Choice! Choose between 0 to 5")