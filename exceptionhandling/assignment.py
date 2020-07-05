class InvalidPasswordException(Exception):
    pass

try:
    p=input("Enter password min. 8 characters: ")
    if len(p)<8:
        raise InvalidPasswordException
    
except InvalidPasswordException:
    print("Enter password with minimum 8 characters")
    
else:
    print("Access Granted!")