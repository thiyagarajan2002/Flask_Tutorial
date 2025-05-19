import datetime
import os
import json

def Create_Data(data):
    date = datetime.date.today().isoformat()
    base_dir = os.getcwd() + '/data/'
    os.makedirs(base_dir, exist_ok=True)
    file_path = base_dir + date + ".txt"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    print("Data saved successfully.")

def View_Data(date):
    base_dir = os.getcwd() + '/data/'
    file_path = base_dir + date + ".txt"
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return '\n'.join(data)
    except FileNotFoundError:
        return "No data found for the given date."
    except json.JSONDecodeError:
        return "Corrupted data file."

def Delete_Data(date):
    base_dir = os.getcwd() + '/data/'
    file_path = base_dir + date + '.txt'
    try:
        os.remove(file_path)
        print("Data deleted successfully.")
    except FileNotFoundError:
        print("No data found to delete.")

while True:
    print("\nMain Menu")
    print("1. Create Data")
    print("2. View Data")
    print("3. Delete Data")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input")
        continue

    if choice == 1:
        ls = []
        print("Enter data (type 'exit' to finish):")
        while True:
            data = input("> ")
            if data.lower() != 'exit':
                ls.append(data)
            else:
                break
        Create_Data(ls)
    elif choice == 2:
        date = input("Enter date (YYYY-MM-DD): ")
        print(View_Data(date))
    elif choice == 3:
        date = input("Enter date (YYYY-MM-DD) to delete: ")
        Delete_Data(date)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Input")
