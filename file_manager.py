
import os

# Create folder for storing files
FOLDER = "managed_files"

if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)


# 1. Create File
def create_file():

    filename = input("Enter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(FOLDER, filename)

    if os.path.exists(filepath):
        print("File already exists!")
        return

    content = input("Enter file content: ")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    print("File created successfully!")


# 2. View All Files
def view_files():

    files = os.listdir(FOLDER)

    if len(files) == 0:
        print("No files found!")
        return

    print("\nAvailable Files:")

    for filename in files:
        if os.path.isfile(os.path.join(FOLDER, filename)):
            print(filename)


# 3. Read File
def read_file():

    filename = input("Enter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(FOLDER, filename)

    if not os.path.isfile(filepath):
        print("File not found!")
        return

    with open(filepath, "r", encoding="utf-8") as file:
        print("\nFile Content:")
        print(file.read())


# 4. Update File
def update_file():

    filename = input("Enter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(FOLDER, filename)

    if not os.path.isfile(filepath):
        print("File not found!")
        return

    content = input("Enter new content: ")

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    print("File updated successfully!")


# 5. Rename File
def rename_file():

    old_name = input("Enter old file name: ")
    new_name = input("Enter new file name: ")

    if not old_name.endswith(".txt"):
        old_name += ".txt"

    if not new_name.endswith(".txt"):
        new_name += ".txt"

    old_path = os.path.join(FOLDER, old_name)
    new_path = os.path.join(FOLDER, new_name)

    if not os.path.isfile(old_path):
        print("File not found!")
        return

    if os.path.exists(new_path):
        print("New file name already exists!")
        return

    os.rename(old_path, new_path)

    print("File renamed successfully!")


# 6. Delete File
def delete_file():

    filename = input("Enter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(FOLDER, filename)

    if not os.path.isfile(filepath):
        print("File not found!")
        return

    os.remove(filepath)

    print("File deleted successfully!")


# 7. Search File
def search_file():

    filename = input("Enter file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(FOLDER, filename)

    if os.path.isfile(filepath):
        print("File found!")
    else:
        print("File not found!")


# Main Menu
def main():

    while True:

        print("\n===== FILE MANAGEMENT SYSTEM =====")
        print("1. Create File")
        print("2. View Files")
        print("3. Read File")
        print("4. Update File")
        print("5. Rename File")
        print("6. Delete File")
        print("7. Search File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            view_files()

        elif choice == "3":
            read_file()

        elif choice == "4":
            update_file()

        elif choice == "5":
            rename_file()

        elif choice == "6":
            delete_file()

        elif choice == "7":
            search_file()

        elif choice == "8":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
