
import getpass
import string

print("Password Strength Checker Started!")

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    print("\n--- PASSWORD STRENGTH REPORT ---")

    if score <= 2:
        print("Password Strength: WEAK")
    elif score <= 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")

password = input("Enter your password: ")
check_password(password)

print("\nPassword checking completed.")
