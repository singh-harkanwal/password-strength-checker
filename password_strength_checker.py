# This program checks password strength and suggest any missing criteria
import string 
import getpass

# Pass user entered password as a parameter to passwordStrength function 
def passwordStrength(secret_password):
    
    #Open a common password file 
    with open('common_password.txt', 'r') as common_password_file:
        common_password = common_password_file.read().splitlines()
    
    #If the password is in the common password file,     
    if secret_password in common_password:
       print("Password is found in common password list, please try another complex password")
       exit() 
    
    #caseCheck function returns true if there is any uppercase, lowercase, number or special character
    def caseCheck(parameter): 
        return any([1 if x in parameter else 0 for x in secret_password])
    #End of caseCheck function
    
    upper_case = caseCheck(string.ascii_uppercase)
    lower_case = caseCheck(string.ascii_lowercase)
    special_character = caseCheck(string.punctuation)
    number = caseCheck(string.digits)
    
    #Check password length
    password_length = len(secret_password)
    
    password_score = 0
    #If password length is less than 8
    if password_length < 8:
       password_score = 1 
    #If password length is between 8 and 12
    elif password_length >= 8 and password_length < 12 :
       password_score = 2
    #If password length is between 12 and 18
    elif password_length >= 12 and password_length < 18:
       password_score = 3
    #If password length is between 18 and 24
    elif password_length >= 18 and password_length < 24:
       password_score = 4
    #If password length is more than 24
    elif password_length >= 24:
       password_score = 5
        
    #Create warning messages if the password doesn't meet all the criteria
    password_case = '\n'
    if upper_case == False:
        password_case += 'Please add atleast one upper case in the password\n'
    else:
        password_score += 1
    if lower_case == False:
        password_case += 'Please add atleast one lower case in the password\n'
    else:
        password_score += 1
    if special_character == False:
        password_case += 'Please add atleast one special character in the password\n'
    else:
        password_score += 1
    if number == False:
        password_case += 'Please add atleast one number in the password\n'
    else:
        password_score += 1
        
    if password_case != '':    
        print(f"{password_case}")
# End of passwordStrength function 

    print(f"\nPassword Length is {str(password_length)}, password score is {password_score} / 9")

#User prompt to enter a password   
secret_password = getpass.getpass(prompt="please enter password:", stream=None)

#Function call and pass the user password as a parameter
passwordStrength(secret_password)