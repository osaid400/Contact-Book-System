# Contact Book System
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

print ("============ Welcome to Contact Book System =============")

# ---------------- Contact Book System List ----------------
contacts = [
    {"Contact ID": 101, "Name": "Ali", "Phone": "03001234567", "Email": "ali@example.com", "City": "Karachi"},
    {"Contact ID": 102, "Name": "Ahmed", "Phone": "03011234567", "Email": "ahmed@example.com", "City": "Lahore"},
    {"Contact ID": 103, "Name": "Usman", "Phone": "03021234567", "Email": "usman@example.com", "City": "Islamabad"},
    {"Contact ID": 104, "Name": "Hassan", "Phone": "03031234567", "Email": "hassan@example.com", "City": "Peshawar"},
    {"Contact ID": 105, "Name": "Bilal", "Phone": "03041234567", "Email": "bilal@example.com", "City": "Quetta"},
    {"Contact ID": 106, "Name": "Hamza", "Phone": "03051234567", "Email": "hamza@example.com", "City": "Multan"},
    {"Contact ID": 107, "Name": "Ayesha", "Phone": "03061234567", "Email": "ayesha@example.com", "City": "Faisalabad"},
    {"Contact ID": 108, "Name": "Fatima", "Phone": "03071234567", "Email": "fatima@example.com", "City": "Hyderabad"},
    {"Contact ID": 109, "Name": "Zain", "Phone": "03081234567", "Email": "zain@example.com", "City": "Sialkot"},
    {"Contact ID": 110, "Name": "Maryam", "Phone": "03091234567", "Email": "maryam@example.com", "City": "Gujranwala"},
    {"Contact ID": 111, "Name": "Saad", "Phone": "03101234567", "Email": "saad@example.com", "City": "Rawalpindi"},
    {"Contact ID": 112, "Name": "Noor", "Phone": "03111234567", "Email": "noor@example.com", "City": "Bahawalpur"},
    {"Contact ID": 113, "Name": "Abdullah", "Phone": "03121234567", "Email": "abdullah@example.com", "City": "Sukkur"},
    {"Contact ID": 114, "Name": "Umer", "Phone": "03131234567", "Email": "umer@example.com", "City": "Larkana"},
    {"Contact ID": 115, "Name": "Sana", "Phone": "03141234567", "Email": "sana@example.com", "City": "Mardan"},
    {"Contact ID": 116, "Name": "Hina", "Phone": "03151234567", "Email": "hina@example.com", "City": "Abbottabad"},
    {"Contact ID": 117, "Name": "Shahzaib", "Phone": "03161234567", "Email": "shahzaib@example.com", "City": "Mirpur"},
    {"Contact ID": 118, "Name": "Laiba", "Phone": "03171234567", "Email": "laiba@example.com", "City": "Gwadar"},
    {"Contact ID": 119, "Name": "Areeb", "Phone": "03181234567", "Email": "areeb@example.com", "City": "Kasur"},
    {"Contact ID": 120, "Name": "Iqra", "Phone": "03191234567", "Email": "iqra@example.com", "City": "Sahiwal"}
]

# ----------------Functions for Contact Book System----------------

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
    
    try:
        Phone = int(input("Enter the Phone Number: "))
        if Phone <= 0:
            print("Phone number cannot be a negative number or zero!")
            return
    except ValueError:
        print("Invalid Phone Number! Please enter a valid Phone Number.")
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
            found = True
            break
    if not found:
        print("Contact Not Found!")

def exit_system():
    print("---------------------------------------------------")
    print("Exiting the Contact Book System.")
    print("Thank you for using the system. Goodbye!")
    print("---------------------------------------------------")
    import sys
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