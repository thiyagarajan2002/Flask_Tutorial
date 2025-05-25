import datetime
import os

def Create_Data(data):
    date = datetime.date.today().isoformat()
    base_dir = os.getcwd() + '/data/'
    os.makedirs(base_dir, exist_ok=True)
    file_path = base_dir + date + ".txt"
    with open(file_path, 'w') as file:
        file.write("\n".join(data))
    print("Data saved successfully.")

def View_Data(date):
    base_dir = os.getcwd() + '/data/'
    file_path = base_dir + date + ".txt"
    try:
        with open(file_path, 'r') as file:
            data=file.read()
            return ''.join(data)
    except Exception:
        return "No data found for the given date."


def Delete_Data(date):
    base_dir = os.getcwd() + '/data/'
    file_path = base_dir + date + '.txt'
    try:
        os.remove(file_path)
        print("Data deleted successfully.")
    except Exception:
        print("No data found to delete.")

while True:
    print("\nMain Menu")
    print("1. Create Data")
    print("2. View Data")
    print("3. Delete Data")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except:
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
        print("Exit")
        break
    else:
        print("Invalid Input")
