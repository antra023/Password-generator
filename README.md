Password Generator
================

This Python script generates strong, secure passwords that meet modern security standards. The passwords are a mix of uppercase and lowercase letters, numbers, and special characters.

Usage
-----

1. Run the script: `python password_generator.py`
2. Enter the length of the password (min 12, recommended 16+)
3. Enter the number of passwords to generate
4. The script will generate and print the specified number of passwords, each of the specified length.

Best Practices
-------------

* Use a password manager to store unique, complex passwords for each account.
* Avoid using the same password across multiple sites.
* Use a passphrase (a sequence of words) for added security.
* Change passwords regularly (every 60-90 days).

Security Notes
-------------

* Passwords are generated using Python's `random` library, which is suitable for cryptographic purposes.
* The script uses a combination of uppercase and lowercase letters, numbers, and special characters to ensure strong passwords.
* Passwords are not stored or transmitted anywhere; they are generated and printed locally.
