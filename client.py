import socket
import os
import argparse
from encryption import encrypt_data, compute_hmac, load_key

def send_file(filename, host, port, keyfile):
    key = load_key(keyfile)
    
    with open(filename, "rb") as f:
        data = f.read()

    encrypted_data = encrypt_data(data)
    hmac_value = compute_hmac(encrypted_data, key)

    with socket.create_connection((host, port)) as s:
        file_info = f"{os.path.basename(filename)}|{len(encrypted_data)}|".encode()
        s.sendall(file_info + encrypted_data + hmac_value)

    print(f"[+] File '{filename}' encrypted, HMAC calculated, and sent.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--key", default="filekey.key")
    args = parser.parse_args()
    send_file(args.file, args.host, args.port, args.key)
