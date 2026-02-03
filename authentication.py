# -------------------------------
# Authentication Program (File-Based)
# -------------------------------

import os

def load_users():
    users = {}
    with open("users.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(":")
            users[username] = password
    return users


def open_downloads_folder():
    downloads_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.startfile(downloads_path)


def authenticate():
    print("User Authentication Required")

    users = load_users()

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("\n Authentication Successful")
        print(" Access Granted")
        print(" Opening Downloads Folder...")
        open_downloads_folder()
    else:
        print("\n Authentication Failed")
        print(" Access Denied")


# -------------------------------
# MAIN
# -------------------------------
authenticate()
