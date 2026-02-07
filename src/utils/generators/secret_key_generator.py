from cryptography.fernet import Fernet

def get_secret_key():
    # Generate a new, cryptographically strong key
    key = Fernet.generate_key()
    return key

if __name__=="__main__":
    print(get_secret_key().decode())


