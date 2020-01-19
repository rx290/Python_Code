
#contact book
#features Save, Edit, Delete and Find

import sqlite3 as db
import os
import time
from sqlite3 import Error

conn= None;

try:
    conn= db.connect(':memory:')
    print(db.version)
    conn.execute('''CREATE TABLE Contacts(ID INTEGER PRIMARY KEY AUTOINCREMENT, Full_Name Text NOT NULL, Email_ID Text NOT NULL,Cell TEXT NOT NULL);''')


except Error as e:
    print(e)
    

    

def menu():
    print("Main Menu: \n \t 1. Save New Contact \n \t 2. Find Contact \n \t 3. Delete Contact \n \t 4. Edit Contact \n \t 5. Exit")


def main():
    menu()
    var=input("Please Enter Your Desired Option: ")
    if(var=="1"):
        f_name= input("Please Enter The Full Name: ")
        email= input("Please Enter The Email: ")
        cell= input("Please Enter The Phone Number: ")
        conn.execute("INSERT INTO Contacts(Full_Name, Email_ID, Cell) VALUES(?,?,?)", (f_name,email,cell))
        conn.commit()
        print("Contact Created!")
        time.sleep(3)
        os.system('cls')
        main()
    
    elif(var=="2"):
        search_entity= input("Please Enter Full name of the contact: ")
        query=conn.execute('SELECT * From Contacts Where Full_Name = ?',[search_entity])
        for num in query:
            print("ID: "+ str(num[0]) +", Full Name: "+ str(num[1]) +" , Email: "+ str(num[2])+" , Contact Number: "+str(num[3]))
        input("Press Enter To Continue")
        os.system('cls')
        main()
        
    elif(var=="3"):
        del_entity= input("Please Enter Full name of the contact: ")
        query=conn.execute('Delete From Contacts Where Full_Name = ?',[del_entity])
        print("Contact Have been Removed!")
        time.sleep(3)
        os.system('cls')
        main()

    elif(var=="4"):
        update_entity= input("Please Enter Full name of the contact: ")
        query=conn.execute('SELECT * From Contacts Where Full_Name = ?',[update_entity])
        for num in query:
            print("ID: "+ str(num[0]) +", Full Name: "+ str(num[1]) +" , Email: "+ str(num[2])+" , Contact Number: "+str(num[3]))
        
        choice=input("\n What do you want to update? \n 1. Name \n 2. Email \n 3. Contact Number \n 4. Nothing \n Choice: ")
        
        if(choice=="1"):
            os.system('cls')
            update_name= input("Please Enter The new name of the contact: ")
            query=conn.execute('Update Contacts set Full_Name = ?  Where Full_Name = ?',[update_name,update_entity])
            print("Contact Name Updated!")
            os.system('cls')
            main()
        
        elif(choice=="2"):
            os.system('cls')
            update_email= input("Please Enter The new email of the contact: ")
            query=conn.execute('Update Contacts set Email_ID = ?  Where Full_Name = ?',[update_email,update_entity])
            print("Contact Email Updated!")
            os.system('cls')
            main()
        
        elif(choice=="3"):
            os.system('cls')
            update_contact= input("Please Enter The new phone number of the contact: ")
            query=conn.execute('Update Contacts set Cell = ?  Where Full_Name = ?',[update_contact,update_entity])
            print("Contact Name Updated!")
            os.system('cls')
            main()
        
        elif(choice=="4"):
            os.system('cls')
            print("Invalid Entry!")
            os.system('cls')
            main()
        
        else:
            os.system('cls')
            main()
            
        time.sleep(3)
        os.system('cls')
        main()
        
    elif(var=="5"):
        conn.close()
        exit()
    
    else:
        print("Invalid Input!")
        os.system('cls')
        main()
        
if __name__== "__main__":
    main()