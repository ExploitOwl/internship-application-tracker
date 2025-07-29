import json
import os

FILE_PATH = 'applications.json'

def load_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def add_application(data):
    company = input("Company name: ").strip()
    role = input("Role applied for: ").strip()
    date_applied = input("Date applied (YYYY-MM-DD): ").strip()
    status = input("Status (Applied, Interviewing, Denied, etc.): ").strip()
    notes = input("Additional notes (optional): ").strip()

    app = {
        'company': company,
        'role': role,
        'date_applied': date_applied,
        'status': status,
        'notes': notes
    }
    data.append(app)
    save_data(data)
    print("Application added.\n")

def list_applications(data):
    if not data:
        print("No applications found.\n")
        return

    for i, app in enumerate(data, 1):
        company_role = f"{app['company']} - {app['role']}"
        date_status = f"Applied: {app['date_applied']} | Status: {app['status']}"
        notes = f"Notes: {app['notes']}" if app['notes'] else ""

        if app['status'].lower() in ['rejected', 'denied']:
            RED = '\033[31m'
            STRIKE = '\033[9m'
            RESET = '\033[0m'
            line = f"{RED}{STRIKE}{company_role} | {date_status} {notes}{RESET}"
        else:
            line = f"{company_role} | {date_status} {notes}"

        print(f"{i}. {line}")
    print()

def main():
    data = load_data()

    while True:
        print("Internship Application Tracker")
        print("1. Add Application")
        print("2. List Applications")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            add_application(data)
        elif choice == '2':
            list_applications(data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == '__main__':
    main()
