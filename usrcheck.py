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

def save_users(usrlist):
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
    if os.path.isfile("usrlist") == False:
        if overWrite==True:
            usrlist=init_usrs(5)
            save_users(usrlist)
        else:
            print("Userfile does not exist! Execute with overWrite set to 'True'")
            sys.exit()
    else:
        usrlist = load_users()
    
    Ufound,Pfound=usr_check(usrname,pswd,usrlist)
    loginSt=login_status(Ufound,Pfound,quiet)
    return loginSt

def test_func():
    import os
    print("[Authentication Test]".center(os.get_terminal_size().columns))
    usr=input("Input username: ")
    pswd=input("Input password: ")
    oW=input("Enable username list overwrite? (y/N): ")
    if oW.upper()=="Y":
        oW=True
    else:
        oW=False
    quiet=input("Enable quiet mode? (y/N): ")
    if quiet.upper()=="Y":
        quiet=True
    else:
        quiet=False
    
    loginSuccess=login_init(usr,pswd,oW,quiet)
    print("Login success status:", loginSuccess)

def main_menu():
    print("\n--- Main Menu ---")
    print("1. Test Authentication")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        test_func()
    elif choice == '2':
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()
