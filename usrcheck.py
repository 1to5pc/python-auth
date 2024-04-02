def load_users():
    try:
        with open("usrlist.txt", "r") as f:
            return [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_users(usrlist):
    with open("usrlist.txt", "w") as f:
        for usr in usrlist:
            f.write(",".join(usr) + "\n")

def login_init(usrname, pswd):
    usrlist = load_users()
    return any(usrname == u[0] and pswd == u[1] for u in usrlist)

def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Test Authentication")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            usr = input("Input username: ")
            pswd = input("Input password: ")
            if login_init(usr, pswd):
                print("Access authorized")
            else:
                print("Access denied")
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
