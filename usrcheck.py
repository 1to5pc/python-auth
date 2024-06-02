import configparser
import string
import secrets
import os
import sys
from typing import List, Tuple
import hash

# Global variable for the hasher
hasher = None

def config_read() -> Tuple[bool, str, int]:
    """Reads the configuration from the config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        quiet = config['Config']['quiet'].lower() in ("true")
    except KeyError:
        quiet = False
    
    try:
        alg = config['Config']['alg'].lower()
        if alg not in hash.SUPPORTED_HASHES:
            raise KeyError
    except KeyError:
        print("ERROR: Algorithm not defined or unsupported. Reverting to SHA256")
        alg = 'sha256'
    
    global hasher
    hasher = hash.Hasher(alg)
    
    try:
        salt_size = int(config['Salt']['saltSize'])
    except (KeyError, ValueError):
        salt_size = 8
        print("ERROR: saltSize not defined or not an integer. Reverting to 8")
    
    return quiet, alg, salt_size

def salter(pswd: str, salt_size: int) -> Tuple[str, str]:
    """Generates a salt and returns the salted password and salt."""
    alphabet = string.ascii_letters + string.digits
    salt = ''.join(secrets.choice(alphabet) for _ in range(salt_size))
    return pswd + salt, salt

def init_users(n_usr: int, salt_size: int) -> List[List[str]]:
    """Initializes user accounts with salted and hashed passwords."""
    user_list = []
    for index in range(n_usr):
        username = input("Enter username: ").strip()
        while not username:
            username = input("Enter username: ").strip()
        
        password = input("Enter password: ").strip()
        while not password:
            password = input("Enter password: ").strip()
        
        salted_password, salt = salter(password, salt_size)
        hasher.update(salted_password.encode())
        hashed_password = hasher.hexdigest()
        hasher.clear_hasher()
        
        user_list.append([username, hashed_password, salt])
    
    return user_list

def load_users() -> List[List[str]]:
    """Loads user data from the usrlist file."""
    user_list = []
    with open("usrlist", "r") as file:
        data = file.read().split(",")
        for i in range(0, len(data), 3):
            user_list.append(data[i:i+3])
    return user_list

def save_users(user_list: List[List[str]], overwrite: bool) -> None:
    """Saves user data to the usrlist file."""
    mode = 'w' if overwrite else 'a'
    with open("usrlist", mode) as file:
        if not overwrite and os.path.getsize("usrlist") > 0:
            file.write(',')
        for i, user in enumerate(user_list):
            file.write(",".join(user))
            if i < len(user_list) - 1:
                file.write(',')

def user_check(username: str, password: str, user_list: List[List[str]], test_hasher: hash.Hasher = None) -> Tuple[bool, bool]:
    """Checks if the username and password match any entry in the user list."""
    if test_hasher:
        hasher = test_hasher
    else:
        config_read()
    
    for user in user_list:
        if user[0] == username:
            hasher.update((password + user[2]).encode())
            hashed_password = hasher.hexdigest()
            hasher.clear_hasher()
            return True, hashed_password == user[1]
    return False, False

def login_status(user_found: bool, password_correct: bool, quiet: bool) -> bool:
    """Prints the login status based on the quiet mode and the authentication results."""
    if not quiet:
        if user_found and password_correct:
            print("Access authorized")
        elif user_found:
            print("Incorrect password. Access denied")
        else:
            print("User does not exist. Access denied")
    return user_found and password_correct

def login_init(username: str, password: str, overwrite: bool, quiet: bool, salt_size: int) -> bool:
    """Initializes the login process based on the given parameters."""
    if not os.path.isfile("usrlist") and not overwrite:
        print("User file does not exist! Execute with overwrite set to 'True'")
        sys.exit()
    
    if overwrite:
        new_file = not os.path.isfile("usrlist")
        if os.path.isfile("usrlist") and input("Do you want to overwrite the existing user list [y/N]? ").upper() == 'Y':
            new_file = True
        
        while True:
            n_usr = input("Enter the number of users to initialize ('0' Clears the database): ")
            try:
                n_usr = int(n_usr)
                if n_usr < 0:
                    print('The value must not be negative.')
                else:
                    break
            except ValueError:
                pass
        
        if n_usr > 0:
            user_list = init_users(n_usr, salt_size)
            save_users(user_list, new_file)
        elif n_usr == 0:
            save_users([], True)
        return False
    else:
        user_list = load_users()
        user_found, password_correct = user_check(username, password, user_list)
        return login_status(user_found, password_correct, quiet)

def auth_test(quiet: bool) -> None:
    """Conducts an authentication test."""
    config_read()
    print("[Authentication Test]".center(os.get_terminal_size().columns))
    username = input("Input username: ").strip()
    password = input("Input password: ").strip()
    login_success = login_init(username, password, False, quiet, 0)
    print(f"Login success status: {login_success}")

def main_menu() -> None:
    """Displays the main menu and handles user choices."""
    quiet, alg, salt_size = config_read()
    print("\n--- Main Menu ---")
    print("0. Initialize user accounts")
    print("1. Test Authentication")
    print("2. Exit")
    choice = input("Enter your choice: ").strip()
    
    if choice == '0':
        login_init('', '', True, quiet, salt_size)
    elif choice == '1':
        auth_test(quiet)
    elif choice == '2':
        print("Exiting program.")
        sys.exit()
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()
