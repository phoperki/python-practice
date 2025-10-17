# Build a password checker

#Define Function check_password_strength

def check_password_strength(password):
    checks=0
    # Check password length
    passlength = len(password)

    #Create check for uppercase
    if any(char.isupper() for char in password):
        checks=checks+1
    #Create check for lowercase
    if any(char.islower() for char in password):
        checks=checks+1
    #Create check for number
    if any(char.isdigit() for char in password):
        checks=checks+1
    #Create check for special character
    if any(not char.isalnum() for char in password):
        checks=checks+1

    # If password length >= 12 has uppercase, lowercase, number, and special character = strong
    if passlength >=12 and checks==4:
        return("Strong")
    # If password length >= 8 has atleast 3 
    elif passlength >= 8 & checks>=3:
        return("Medium")
    # Else false
    else:
        return("Weak")

print(check_password_strength("Example123!2"))