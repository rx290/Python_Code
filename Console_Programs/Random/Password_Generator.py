import random as r
import string

choice= str.lower(input("Do you want a new password? \nAnswer yes or no only!\nYour Choice: "))
length= input("Default length is 8 characters you can increase it upto 25 \n Please Enter Your Deseired Password Length: ")
special_characters=("!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~")
password = []
size_of_sc= len(special_characters)
print()
if(choice=='yes' ):
    for x in range(0,int(length)):
        if(x == 0):
            password.append(special_characters[r.randrange(0,size_of_sc)])
        elif(x%2==0):
            password.append(r.choice(string.ascii_letters))
        else:
            password.append(str(r.randrange(0,9)))

    print("Password Generated!")

elif(choice=='no'):
    print("Sayonara!")
    exit()
else:
    print("invalid Option!")
    exit()

    
seprator=""
string_generated= seprator.join(password) 

print(string_generated)
    
