# website requires the users to input username and password to register. Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
import re

pattern = re.compile(r'[a-zA-Z0-9#$@]{8,16}')
passwords = input('Please enter passwords separated by comma: ').split(',')

display_pass = []
for item in passwords:
    check = pattern.fullmatch(item)
    if check:
        display_pass.append(item)

print(','.join(display_pass))
