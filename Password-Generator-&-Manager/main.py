import sqlite3
import secrets
import string
import base64
import os
import hashlib
import getpass
from cryptography.fernet import Fernet

# Generate a secure encryption key (Run this once and store the key)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encrypt password
def encrypt_password(password, key):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()

# Hash website names for better security (prevents lookup attacks)
def hash_website(website):
    return hashlib.sha256(website.encode()).hexdigest()

# Generate a secure password
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# Initialize database
def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_hash TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Save password to database
def save_password(website, username, password, key):
    encrypted_password = encrypt_password(password, key)
    website_hash = hash_website(website)

    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    
    # Check if a password already exists for this website
    c.execute("SELECT * FROM passwords WHERE website_hash=?", (website_hash,))
    existing = c.fetchone()
    
    if existing:
        confirm = input(f"A password for {website} already exists. Overwrite? (y/n): ").lower()
        if confirm != 'y':
            print("Operation cancelled.")
            conn.close()
            return

    c.execute("INSERT OR REPLACE INTO passwords (website_hash, username, password) VALUES (?, ?, ?)", 
              (website_hash, username, encrypted_password))
    
    conn.commit()
    conn.close()
    print(f"Password for {website} saved successfully.")

# Retrieve password
def get_password(website, key):
    website_hash = hash_website(website)

    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT username, password FROM passwords WHERE website_hash=?", (website_hash,))
    result = c.fetchone()
    conn.close()
    
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password, key)
        return f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}"
    else:
        return "No password found for this website."

# Main function to interact
def main():
    key = load_key()
    init_db()
    
    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Retrieve Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            print("Generated Password:", generate_password(length))

        elif choice == "2":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password (or type 'gen' to generate one): ")
            if password.lower() == "gen":
                password = generate_password()
                print(f"Generated Password: {password}")
            save_password(website, username, password, key)

        elif choice == "3":
            website = input("Enter website: ")
            print(get_password(website, key))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
