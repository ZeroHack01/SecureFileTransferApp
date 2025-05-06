# 🔐 SecureFileTransferApp

![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-brightgreen)
![Status](https://img.shields.io/badge/Project-Stable-success)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)

A command-line Python tool for secure, encrypted file transfer across networks using AES-256 encryption and HMAC for integrity verification. Ideal for professionals who need lightweight, CLI-based, and private file exchange.

---

## 🚀 Features

- ✅ AES-256 Encryption – End-to-end confidentiality  
- ✅ HMAC (SHA-256) – Integrity verification  
- ✅ File sender/receiver modes  
- ✅ Simple CLI interface  
- ✅ Cross-platform & lightweight  
- ✅ Ready for network environments

---

## 🛠️ Project Structure

SecureFileTransferApp/
├── client.py # Client-side file receiver
├── server.py # Server-side file sender
├── encryption.py # AES encryption/decryption
├── hmac_verify.py # HMAC functions
├── utils.py # Key & utility functions
├── requirements.txt # Python dependencies
└── README.md # Documentation

yaml
Copy
Edit

---

## 📦 Installation

```bash
git clone https://github.com/ZeroHack01/SecureFileTransferApp.git
cd SecureFileTransferApp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🔑 Key Generation
python
Copy
Edit
from utils import derive_key
key = derive_key("your_secure_passphrase")
Or: Enter the same passphrase on both machines. It will be converted internally.

⚠️ Use the same passphrase on both sender and receiver to ensure proper encryption/decryption.

📡 Usage
📤 Sender (Host):

bash
Copy
Edit
python server.py --port 4444 --key your_secure_passphrase
📥 Receiver (Client):

bash
Copy
Edit
python client.py --host 192.168.x.x --port 4444 --key your_secure_passphrase
Replace 192.168.x.x with the IP of your host machine (VM or LAN).

🛡️ Security Overview
AES-256 in CBC mode with random IV

SHA-256 HMAC for file integrity

Key derived from passphrase (SHA-256)

No plaintext file stored or exposed during transfer

🧠 Future Enhancements
🔄 Asymmetric key exchange (Diffie-Hellman)

🗂️ Multi-file/directory support

📉 Progress bar & transfer stats

🖼️ GUI with Tkinter or PyQt

🤝 Contributing
Have ideas? Open a pull request or start a discussion!

👨‍💻 Author
Mongwoiching Marma
📧 mongwoiching2080@gmail.com
🔗 GitHub Profile
