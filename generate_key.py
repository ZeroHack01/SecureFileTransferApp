from cryptography.fernet import Fernet

def generate_key():
    # Generate a symmetric encryption key
    key = Fernet.generate_key()
    
    # Save the key to a file
    with open("filekey.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Symmetric encryption key generated and saved to filekey.key")

if __name__ == "__main__":
    generate_key()
