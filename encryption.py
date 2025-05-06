from cryptography.fernet import Fernet
import hmac
import hashlib

# Function to load the symmetric key
def load_key(filename="filekey.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

# Function to encrypt data
def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data)

# Function to decrypt data
def decrypt_data(encrypted_data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)

# Function to compute HMAC of data
def compute_hmac(data, key):
    h = hmac.new(key, data, hashlib.sha256)
    return h.digest()

# Function to verify HMAC
def verify_hmac(data, received_hmac, key):
    h = hmac.new(key, data, hashlib.sha256)
    return hmac.compare_digest(h.digest(), received_hmac)

