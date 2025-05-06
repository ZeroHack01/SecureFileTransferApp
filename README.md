🔐 SecureFileTransferApp

[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-brightgreen)](https://github.com/ZeroHack01/SecureFileTransferApp)
[![Status](https://img.shields.io/badge/Project-Stable-success)](https://github.com/ZeroHack01/SecureFileTransferApp)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)](https://github.com/ZeroHack01/SecureFileTransferApp/pulls)


A command-line Python tool for secure, encrypted file transfer across networks using AES-256 encryption and HMAC for integrity verification.  
Ideal for professionals who need lightweight, CLI-based, and private file exchange.


 🚀 Features

- ✅ AES-256 Encryption – End-to-end confidentiality  
- ✅ HMAC (SHA-256) – Integrity verification  
- ✅ File sender/receiver modes  
- ✅ Simple CLI interface  
- ✅ Cross-platform & lightweight  
- ✅ Ready for network environments  


🛠️ Project Structure

SecureFileTransferApp/
├── client.py # Client-side file receiver
├── server.py # Server-side file sender
├── encryption.py # AES encryption/decryption
├── hmac_verify.py # HMAC functions
├── utils.py # Key & utility functions
├── requirements.txt # Python dependencies
└── README.md # Documentation



📦 Installation
,,bash
git clone https://github.com/ZeroHack01/SecureFileTransferApp.git
cd SecureFileTransferApp
,,bash
python3 -m venv venv
source venv/bin/activate

,,bash
pip install -r requirements.txt

🔑 Key Generation
The encryption key is derived from a user-defined passphrase using SHA-256.

python
from utils import derive_key
key = derive_key("your_secure_passphrase")
Or: Enter the same passphrase on both machines. It will be internally converted.

⚠️ Use the same passphrase on both sender and receiver to ensure successful encryption/decryption.

📡 Usage
📤 Sender (Host):
,,bash
python server.py --port 4444 --key your_secure_passphrase

📥 Receiver (Client):
,,bash
python client.py --host 192.168.x.x --port 4444 --key your_secure_passphrase
Replace 192.168.x.x with the IP address of the host (e.g., your VM or LAN system).

🛡️ Security Overview
AES-256 in CBC mode with a random IV

SHA-256 HMAC for file integrity

Key derived from passphrase (SHA-256)

No plaintext file written or stored during transfer

🧠 Future Enhancements
🔄 Asymmetric key exchange (Diffie-Hellman)

🗂️ Multi-file/directory support

📉 Progress bar & transfer stats

🖼️ GUI (Tkinter or PyQt)

🤝 Contributing
Got ideas? Open a pull request or start a discussion!

👨‍💻 Author
Mongwoiching Marma
📧 mongwoiching2080@gmail.com
🔗 GitHub Profile
