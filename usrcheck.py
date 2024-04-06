def init_usrs(nUsr):
    import hashlib
    usrlist=[]
    for index in range(nUsr):
        usrname=input("Enter username: ")
        pswd=input("Enter password: ")
        pswd=hashlib.sha256(pswd.encode()).hexdigest()
        usrlist.append([])
        usrlist[index].append(usrname)
        usrlist[index].append(pswd)
    return usrlist

def load_users():
    usrlist=[]
    saveFile = open("usrlist", "r")
    temp = saveFile.read().split(",")
    for x in range(len(temp)//2):
        usrlist.append([])
        usrlist[x].append(temp[(2*x)])
        usrlist[x].append(temp[(2*x)+1])
    saveFile.close()
    return usrlist

def save_users(usrlist,overWrite):
    if overWrite==True:
        saveFile = open("usrlist", "w")
    else:
        saveFile = open("usrlist", "a")
    for x in range(len(usrlist)):
        if (x-2)<len(usrlist):
            saveFile.write(str(usrlist[x][0])+","+str(usrlist[x][1])+",")
        else:
            saveFile.write(str(usrlist[x][0])+","+str(usrlist[x][1]))
    saveFile.close()
   
def usr_check(usrn,pswd,usrlist):
    import hashlib
    index=0
    Ufound=False
    Pfound=False
    pswd=hashlib.sha256(pswd.encode()).hexdigest()
    while Ufound==False and index<len(usrlist):
        if usrlist[index][0]==usrn:
            Ufound=True
            if usrlist[index][1]==pswd:
                Pfound=True
            break
        index=index+1
    return Ufound,Pfound

def login_status(Ufound,Pfound,quiet):
    if quiet==False:
        if Ufound==True and Pfound==True:
            print("Access authorized")
            return True
        elif Ufound==True:
            print("Incorrect password. Access denied")
            return False
        else:
            print("User does not exist. Access denied")
            return False
    else:
        if Ufound==True and Pfound==True:
            return True
        else:
            return False
            
def login_init(usrname,pswd,overWrite,quiet):
    import os
    import sys
    loginSt=False
    if os.path.isfile("usrlist") == False and overWrite==False:
        print("Userfile does not exist! Execute with overWrite set to 'True'")
        sys.exit()
    elif overWrite==True:
        if input("Do you want to overwrite the existing user list[y/N]? ").upper()=='Y':
            newFile=True
        else:
            newFile=False
        while True:
            nUsr=input("Enter the number of users to initialize: ")
            try:
                nUsr=int(nUsr)
                break
            except ValueError:
                pass
        if nUsr>0:
            usrlist=init_usrs(nUsr)
            save_users(usrlist,newFile)
    else:
        usrlist = load_users()
        Ufound,Pfound=usr_check(usrname,pswd,usrlist)
        loginSt=login_status(Ufound,Pfound,quiet)
    return loginSt


def Auth_test():
    import os
    try:
        print("[Authentication Test]".center(os.get_terminal_size().columns))
    except OSError:
        print("[Authentication Test]")
    usr=input("Input username: ")
    pswd=input("Input password: ")
    if input("Enable quiet mode? [y/N]").upper() == "Y":
        quiet=True
    else:
        quiet=False
    loginSuccess=login_init(usr,pswd,False,quiet)
    print("Login success status:", loginSuccess)

def main_menu():
    print("\n--- Main Menu ---")
    print("0. Initialize user accounts")
    print("1. Test Authentication")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '0':
        login_init('','',True,False)
    elif choice == '1':
        Auth_test()
    elif choice == '2':
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()
