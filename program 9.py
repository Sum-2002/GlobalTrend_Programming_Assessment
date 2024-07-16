import string
import secrets

def generate_password(length: int = 12) -> str:
    """
    Generate a random password with a mix of uppercase letters, lowercase letters, digits, and special characters.

    Args:
        length (int): The length of the password. Default is 12.

    Returns:
        str: A random password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) 
                and any(c.isupper() for c in password) 
                and any(c.isdigit() for c in password) 
                and any(c in string.punctuation for c in password)):
            return password

x=int(input("enter the length of password"))
password = generate_password(x)
print(password)
