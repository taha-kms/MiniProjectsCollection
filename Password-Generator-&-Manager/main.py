import sqlite3
import secrets
import string
import os
import hashlib
import getpass
from cryptography.fernet import Fernet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

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

# Hash passwords securely using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize database
def init_db():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    
    # Create table for passwords
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_hash TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create table for master password
    c.execute("""
        CREATE TABLE IF NOT EXISTS master_password (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password_hash TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# Set up the master password (Run once)
def setup_master_password():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT * FROM master_password")
    
    if c.fetchone() is None:
        print(Fore.YELLOW + "No master password found. Please set up a master password.")
        master_password = getpass.getpass(Fore.CYAN + "Enter a new master password: ")
        confirm_password = getpass.getpass(Fore.CYAN + "Confirm master password: ")
        
        if master_password == confirm_password:
            hashed_password = hash_password(master_password)
            c.execute("INSERT INTO master_password (password_hash) VALUES (?)", (hashed_password,))
            conn.commit()
            print(Fore.GREEN + "Master password set successfully!")
        else:
            print(Fore.RED + "Passwords do not match. Try again.")
            setup_master_password()
    
    conn.close()

# Verify master password at program start
def verify_master_password():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT password_hash FROM master_password")
    stored_hash = c.fetchone()
    
    if stored_hash:
        attempts = 3
        while attempts > 0:
            entered_password = getpass.getpass(Fore.YELLOW + "Enter Master Password: ")
            if hash_password(entered_password) == stored_hash[0]:
                print(Fore.GREEN + "Access Granted!")
                conn.close()
                return True
            else:
                attempts -= 1
                print(Fore.RED + f"Incorrect password. {attempts} attempts left.")
        
        conn.close()
        print(Fore.RED + "Too many failed attempts. Exiting.")
        exit()
    else:
        print(Fore.RED + "Master password not set up. Exiting.")
        exit()

# Save password to database
def save_password(website, username, password, key):
    encrypted_password = encrypt_password(password, key)
    website_hash = hash_password(website)

    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    
    # Check if a password already exists for this website
    c.execute("SELECT * FROM passwords WHERE website_hash=?", (website_hash,))
    existing = c.fetchone()
    
    if existing:
        confirm = input(Fore.YELLOW + f"A password for {website} already exists. Overwrite? (y/n): ").lower()
        if confirm != 'y':
            print(Fore.RED + "Operation cancelled.")
            conn.close()
            return

    c.execute("INSERT OR REPLACE INTO passwords (website_hash, username, password) VALUES (?, ?, ?)", 
              (website_hash, username, encrypted_password))
    
    conn.commit()
    conn.close()
    print(Fore.GREEN + f"Password for {website} saved successfully.")

# Retrieve password
def get_password(website, key):
    website_hash = hash_password(website)

    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT username, password FROM passwords WHERE website_hash=?", (website_hash,))
    result = c.fetchone()
    conn.close()
    
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password, key)
        return Fore.CYAN + f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}"
    else:
        return Fore.RED + "No password found for this website."

# Generate a secure password
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# Main function
def main():
    key = load_key()
    init_db()
    setup_master_password()
    verify_master_password()  # Ask for authentication at startup

    while True:
        print("\n" + Fore.YELLOW + "Password Manager Menu:")
        print(Fore.BLUE + "1. Generate Password")
        print(Fore.BLUE + "2. Save Password")
        print(Fore.BLUE + "3. Retrieve Password")
        print(Fore.RED + "4. Exit")

        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == "1":
            length = int(input(Fore.CYAN + "Enter password length: "))
            print(Fore.GREEN + "Generated Password:", generate_password(length))

        elif choice == "2":
            website = input(Fore.CYAN + "Enter website: ")
            username = input(Fore.CYAN + "Enter username: ")
            password = getpass.getpass(Fore.CYAN + "Enter password (or type 'gen' to generate one): ")
            if password.lower() == "gen":
                password = generate_password()
                print(Fore.GREEN + f"Generated Password: {password}")
            save_password(website, username, password, key)

        elif choice == "3":
            website = input(Fore.CYAN + "Enter website: ")
            print(get_password(website, key))

        elif choice == "4":
            print(Fore.RED + "Exiting...")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
