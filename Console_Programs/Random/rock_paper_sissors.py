import random as r


choices = ["rock", "paper", "sissor"]

comp_choice = choices[r.randrange(0,2)]
user_choice = str.lower(input("Please Enter your choice: "))
while(True):
    if ((comp_choice== choices[1]) and (user_choice == choices[0])):
        
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nComputer won!")
        break
    elif ((comp_choice== choices[2]) and (user_choice == choices[1])):
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nComputer won!")
        break
    elif ((comp_choice== choices[0]) and (user_choice == choices[2])):
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nComputer won!")
        break
    elif ((comp_choice== choices[0]) and (user_choice == choices[1])):
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nUser won!")
        break
    elif ((comp_choice== choices[1]) and (user_choice == choices[2])):
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nUser won!")
        break
    elif ((comp_choice== choices[2]) and (user_choice == choices[0])):
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\nUser won!")
        break
    else:
        print("Computer Choice: " + comp_choice+"\nUser Choice: "+user_choice+"\ntie")
        break
        


