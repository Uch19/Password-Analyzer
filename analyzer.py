import getpass

password = getpass.getpass("Password: ") #Read the password from the user without echoing it to the console

print("Length", len(password)) #Print the length of the password

def check_policy(password):
    problems = []
    if len(password) < 12:
        problems.append("Password must be atleast 12 characters long")
    if password.isLower():
        problems.append("Password must contain atleast one uppercase letter")
    
    
    return problems

 