# Password strength checker

password = input("Enter your password\n")
has_uppercase = input("Does your password have an uppercase? Type 1 for yes and 2 for no:\n") == "1"
has_lowercase = input("Does your password have a lowercase? Type 1 for yes and 2 for no:\n") == "1"
has_digit = input("Does your password have a digit? Type 1 for yes and 2 for no:\n") == "1"
has_special_char = input("Does your password have a special character (e.g. !, #, @)? Type 1 for yes and 2 for no:\n") == "1"

# Check password strength
if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
    print("Strong password")
elif len(password) >= 8 and (has_uppercase or has_lowercase or has_digit or has_special_char):
    print("Moderate password.")
else:
    print("Weak password")

# # Password strength checker
# password = input("Enter your password\n")

# has_uppercase = any(char.isupper() for char in password)
# has_lowercase = any(char.islower() for char in password)
# has_digit = any(char.isdigit() for char in password)
# has_special_char = any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for char in password)

# # Check password strength
# if len(password) >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
#     print("Strong password")
# elif len(password) >= 8 and (has_uppercase or has_lowercase or has_digit or has_special_char):
#     print("Moderate password. Consider adding more complexity.")
# else:
#     print("Weak password. It should be at least 8 characters long.")