import string
def valid_password(password):
    if len(password) < 10 or len(password) > 15:
        return "Password should be between 10 and 15 characters."
    if password.isupper() or password.islower() or password.isdigit() or password.isalpha():
        return "Password should have at least one uppercase letter, one lowercase letter, one digit, and one special character."
    for i in range(len(password)):
        if password[i] == ' ':
            return "Password should not contain spaces."
    if password.endswith('.') or password.endswith('@'):
        return "Password should not end with '.' or '@'."
    special_characters = string.punctuation
    if not any(char in special_characters for char in password):
        return "Password should contain at least one special character"
    return "Password is valid."
password = input("Enter password: ")
print(valid_password(password))