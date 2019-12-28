
import time
import platform
import os
from getpass import getpass
import json

## Data dictionary to store data of costumers

def getpassword():
    pass1 = getpass("\n\t\t Password: ").strip()
    pass2 = getpass("\n\t\t Verify Password: ").strip()
    if pass1 == pass2:
        return pass1
    else:
        print("\n\t\t Incorrect password...")
        return getpassword()


## clear screen function 
def clr_scr():
    if platform.system() == "Windows":
        print("\n\n.......Clearing Screen..........\n\n")
        time.sleep(2)
        os.system('cls')
    else : 
        print("\n\n.......Clearing Screen..........\n\n")
        time.sleep(2)
        os.system('clear')
    

def main_page():
    clr_scr()
    print("--"*40)
    print("\n\n\t\t Welcome User to the Banking Application!")
    print("--"*40)
    print("\n\n Please Select One of the Following Options.")
    print("\n\t\t 1. Log In")
    print("\n\t\t 2. Sign Up")
    print("\n\t\t 3. Exit")
    n = int(input("\n Enter any One option from above list."))
    if n==1:
        print("\n\t Taking you to the login screen.\n\t Please wait....")
        login_page()
    if n==2:
        print("\n\t Taking You to the Sign Up page.")
        signup_page()
    if n==3:
        exit()
        
        
## Log in function for existing user
def login_page():
    clr_scr()
    with open("data.json") as fp:
        login = json.load(fp) # de-serialization
        fp.close()    
    print("--"*40)
    print("\n\n\t\t Welcome User to the Banking Application!")
    print("--"*40)
    account_number = int(input("\n\t\t  Enter your account number - "))
    number = str(account_number)
    if number in login:
        password =  getpass("\n\t\t  Enter your password - ")
        if password in login[number]['password']:
            clr_scr()
            print("\n\t LOG IN successful.")
            print("--"*40)
            print("\n\n\t\t Welcome User to the Banking Application!")
            print("--"*40)
            print("\n\n Please Select One of the Following Options.")
            print("\n\t\t 1. Debit")
            print("\n\t\t 2. Credit")
            print("\n\t\t 3. Check Balance")
            print("\n\t\t 4. Logout")
            n = int(input("Enter any One option from above list."))
            if n==1:
                print("\n\t Taking you to the debit screen.\n\t Please wait....")
                clr_scr()
                print("--"*40)
                print("\n\n\t\t Welcome User to the Banking Application!")
                print("--"*40)
                current_bal = login[number]['balance']
                print(f"\n\t Your current balance is- {current_bal}.")
                debit_bal = int(input("\n\t Enter the amount you want to debit - "))
                ##debit_bal = int(input("\n\t Enter the amount you want to debit - "))
                while debit_bal > current_bal:
                    print("\n\t Insufficient Balance... Plese Enter a valid amount.")
                    debit_bal = int(input("\n\t Enter the amount you want to debit - "))
                else:
                    print("\n\t Debiting money from your account...")
                    new_bal = current_bal - debit_bal
                    login[number]['balance'] = new_bal
                    fp = open('data.json','w')
                    json.dump(login,fp)
                    fp.close()
                    print(f"\n\t Debit successfull.\n\t Your current balance is {new_bal}.")
                    a = int(input("\n\t Press 1 to go back to main menu - "))
                    main_page()
            if n==2:
                print("\n\t Taking You to the Credit screen.\n\t Please wait...")
                clr_scr()
                print("--"*40)
                print("\n\n\t\t Welcome User to the Banking Application!")
                print("--"*40)
                current_bal = login[number]['balance']
                print(f"\n\t Your current balance is- {current_bal}.")
                credit_bal = int(input("\n\t Enter the amount you want to credit - "))   
                print("\n\t creaditing money to your account...")
                new_bal = current_bal + credit_bal
                login[number]['balance'] = new_bal
                fp = open('data.json','w')
                json.dump(login,fp)
                fp.close()
                print(f"\n\t credit successfull.\n\t Your current balance is {new_bal}.")
                a = int(input("\n\t Press 1 to go back to main menu - "))
                main_page()

            if n==3:
                print("\n\t Taking You to the Balance screen.\n\t Please wait...")
                clr_scr()
                print("--"*40)
                print("\n\n\t\t Welcome User to the Banking Application!")
                print("--"*40)
                current_bal = login[number]['balance']
                print(f"\n\t Your current balance is- {current_bal}.")
                a = int(input("\n\t Press 1 to go back to main menu - "))
                main_page()

            if n==4:
                clr_scr()
                print("\n\t Logging out.\n\t Please wait....")
        else:
            print("\n\t\t Incorrect Password please try again.")
            login_page()
    else:
        print("\n\t\t Account does not exist. ")
        int(input("\n\t\t To create new accouunt please enter 1 for sign up"))
        signup_page()
    
    
## Sign up Function for new user    
def signup_page():
    clr_scr()
    print("--"*40)
    print("\n\n\t\t Welcome User to the Banking Application!")
    print("--"*40)
    db = json.load(open("data.json"))
    name = input("\n\t\t Enter your name - ")
    password = getpassword()
    ##password = getpass("\n\t\t Enter Pasword - ")
    balance = eval(input("\n\t\t Enter initial balance that you want to deposite."))
    detail = list(map(int,db))
    detail.sort(reverse=True)
    account_number = str(detail[0]+1)
    db[account_number] = { 'name':name, 'balance':balance, 'password': password}
    with open("data.json","w") as fp: 
        json.dump(db,fp)
        fp.close()
    print("\n\t\t Congratulation ! your account was created successfully.")
    print(f"\n\t\t For LOG IN please save your account number - {account_number}.")
    print(f"\n\t\t Password - {password}")
    a = int(input("\n\t Press 1 to go back to main menu - "))
    main_page()

    

    
    
    
main_page()
    
        
