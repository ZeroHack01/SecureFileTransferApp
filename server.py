import socket
import os
import argparse
from encryption import decrypt_data, verify_hmac, load_key

def receive_file(port, save_dir, keyfile):
    key = load_key(keyfile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen(1)
        print(f"[+] Server listening on port {port}...")

        conn, addr = s.accept()
        with conn:
            print(f"[+] Connection from {addr}")

            # Read file info until two '|' are found
            file_info = b""
            pipe_count = 0
            while pipe_count < 2:
                byte = conn.recv(1)
                file_info += byte
                if byte == b'|':
                    pipe_count += 1

            file_info = file_info.decode()
            filename, encrypted_size = file_info.strip().split('|')[:2]
            encrypted_size = int(encrypted_size)

            # Read the encrypted file content
            encrypted_data = b""
            while len(encrypted_data) < encrypted_size:
                encrypted_data += conn.recv(min(4096, encrypted_size - len(encrypted_data)))

            # Read the HMAC
            hmac_value = conn.recv(32)  # SHA-256 = 32 bytes

            # Verify HMAC
            if not verify_hmac(encrypted_data, hmac_value, key):
                print("[-] HMAC verification failed. File integrity compromised.")
                return

            # Decrypt and save
            decrypted_data = decrypt_data(encrypted_data)
            os.makedirs(save_dir, exist_ok=True)
            filepath = os.path.join(save_dir, filename)

            with open(filepath, "wb") as f:
                f.write(decrypted_data)

            print(f"[+] Received and verified file saved to {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--save-dir", required=True)
    parser.add_argument("--key", default="filekey.key")
    args = parser.parse_args()
    receive_file(args.port, args.save_dir, args.key)
