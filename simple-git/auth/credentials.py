import getpass
import base64

def get_credentials():
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    return base64.b64encode(f"{user}:{password}".encode()).decode()