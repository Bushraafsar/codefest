#Task 6:
#Create a function that validates a password to conform to the following rules:
#At least one uppercase letter
#At least one lower case letter
#At least one digit
#Maximum of repeated character
special_characters = ["!","@","#","$","%","^","&","*","_","(",")","=","+","{","}",":",";","'","?","<",".",",",">"]
def password_checker():
    while True:
        user_password =input("Enter your password here: ")
        if len(user_password) < 6:
           print("Not valid--Your password  must have atleast 6 characters! ")
           continue
        elif len(user_password) > 24:
           print("Not valid--Your password can have atmost 24 characters! ")
           continue
        elif not any(character.isdigit() for character in user_password):
           print("Not valid---Your password must have atleast one digit!")
           continue
        elif not any(character.isupper() for character in user_password):
           print("Not valid---Your password must have atleast one uppercase letter!") 
           continue
        elif not any(character.islower() for character in user_password) :
           print("Not valid---Your password must have atleast one lowercase letter!")
           continue 
        elif not any(character in special_characters for character in user_password) :
           print("Not valid---Your password have supported characters!") 
           continue
        for i in user_password:
            if i*3 in user_password:
               print ("Not valid----Your password can have maximum of two rep characters!") 
               break
            continue   
        else:
           print("--------Valid password----------")
           break      
        
         
password_checker() 




          