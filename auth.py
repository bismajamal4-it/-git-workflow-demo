# Authentication Module

def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False

def logout():
    return "User logged out"

