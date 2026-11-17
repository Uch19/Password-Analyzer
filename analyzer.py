import getpass

password = getpass.getpass("Password: ") #Read the password from the user without echoing it to the console

print("Length: ", len(password)) #Print the length of the password

def check_policy(password):
    problems = []
    if len(password) < 12:
        problems.append("Password must be at least 12 characters long")
    if not any (c.islower() for c in password):
        problems.append("Password must contain at least one lowercase letter")
    if not any (c.isupper() for c in password):
        problems.append("Password must contain at least one uppercase letter")
    if set(password).isdisjoint(set("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?")):
        problems.append("Password must contain at least one special character")
    if any(a==b for a,b in zip(password, password[1:])):
        problems.append("Password must not contain any repeated characters")
    if any(ord(b) - ord(a) == 1 for a,b in zip(password, password[1:])):
        problems.append("Password must not contain any sequential characters")
    return problems

 