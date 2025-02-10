# Password Generator & Manager

## Overview
A secure password generator and manager built using Python. This application allows users to generate strong passwords, securely store them in an encrypted database, and retrieve them when needed.

## Features
- **Secure Password Generation**: Generates random, strong passwords.
- **Encrypted Storage**: Uses AES encryption (`cryptography` library) to store passwords securely.
- **SQLite Database**: Stores passwords locally in a structured format.
- **Retrieve Stored Passwords**: Fetch and decrypt stored passwords easily.
- **User-Friendly CLI**: Simple command-line interface for ease of use.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.7 or later recommended). Install the required dependencies using:
```sh
pip install cryptography sqlite3
```

## Setup
1. **Generate Encryption Key (Run Once)**
   ```sh
   python -c "import password_manager; password_manager.generate_key()"
   ```
   This will create a `key.key` file used for encrypting/decrypting passwords.

2. **Run the Password Manager**
   ```sh
   python main.py
   ```

## Usage
Upon running, you will see a menu with the following options:

1. **Generate Password**: Create a strong password of specified length.
2. **Save Password**: Store credentials securely in the database.
3. **Retrieve Password**: Fetch stored credentials and decrypt them.
4. **Exit**: Close the application.

## Example Usage
### Generate a Password
```sh
Choose an option: 1
Enter password length: 16
Generated Password: Xy7!jP9@qWs2K$%e
```

### Save a Password
```sh
Choose an option: 2
Enter website: example.com
Enter username: user@example.com
Enter password (or type 'gen' to generate one): gen
Generated Password: Hs@4G$kP
Password for example.com saved successfully.
```

### Retrieve a Password
```sh
Choose an option: 3
Enter website: example.com
Website: example.com
Username: user@example.com
Password: Hs@4G$kP
```

## Security Considerations
- Store the `key.key` file securely; losing it will prevent password decryption.
- The database (`passwords.db`) is encrypted but should still be stored securely.
- Do not share your encryption key with others.

## Future Enhancements
- **Master Password**: Adding authentication to prevent unauthorized access.
- **Browser Integration**: Auto-fill passwords in web browsers.



