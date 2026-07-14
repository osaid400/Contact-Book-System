# Contact Book System

A console-based Contact Book System built with Python. This project demonstrates the use of functions, lists, dictionaries, loops, conditional statements, exception handling, and JSON-based file persistence to manage contact records.

## Features

* Add a new contact
* View all contacts
* Search contacts by ID or Name
* Update contact details
* Delete a contact
* Prevent duplicate Contact IDs
* Validate user input
* Persistent storage — contacts are saved to a JSON file and reload automatically on the next run

## Technologies Used

* Python 3

## Concepts Covered

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* User Input
* Data Validation
* CRUD Operations
* String Methods (`strip()`, `lower()`, `isdigit()`)
* File Handling with JSON (`json.load()`, `json.dump()`)
* `os.path.exists()` for safe file loading

## Project Structure

```text
Contact-Book-System/
│
├── Contact Book System.py
├── contacts.json
└── README.md
```

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/osaid400/Contact-Book-System.git
```
2. Navigate to the project folder:
```bash
cd Contact-Book-System
```
3. Run the program:
```bash
python "Contact Book System.py"
```

## Example Output

```text
============ Welcome to Contact Book System =============
=============== Select the Option (0-5) ===============
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
0. Exit
Enter the number: 3
Do you want to search by Contact ID or Name? (ID/Name): Name
Enter the Name: Ali
---------------------------------------------------
Name: Ali
Contact ID: 101
Phone: 03001234567
Email: ali@example.com
City: Karachi
---------------------------------------------------
```

## How Data Persistence Works

* On startup, the program checks if `contacts.json` exists using `os.path.exists()`.
* If it exists, all contacts are loaded into memory using `json.load()`.
* If it doesn't exist, the program starts with an empty contact list.
* Every time a contact is added, updated, or deleted, the full contact list is saved back to `contacts.json` using `json.dump()`, so no data is lost between runs.

## Future Improvements

* Search by phone number or email
* Sort contacts alphabetically
* Export and import contacts
* Add favorite contacts
* Migrate from JSON file storage to SQLite
* Implement Object-Oriented Programming (OOP)

## Learning Outcomes

This project helped me practice:

* Writing modular code using functions
* Managing data with lists and dictionaries
* Performing CRUD operations
* Searching records using different criteria
* Handling exceptions and validating user input
* Building a menu-driven console application
* Persisting data between program runs using JSON file handling
* Improving debugging and problem-solving skills

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400
