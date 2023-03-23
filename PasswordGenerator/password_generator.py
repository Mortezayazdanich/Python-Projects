import secrets #It is advised by PEP506 to use "secrets" to create cryptographically secure sequence
import string
import random
#adding different character types to have a character dictionary to work with
letters = string.ascii_letters
digits = string.digits
punctuations = string.punctuation

char_alphabet = letters + digits + punctuations

pwd_lenght = random.randint(12, 16)

#The loop Generates password meeting the requirements
while True:
    password = ""
    for index in range(pwd_lenght):
        password += secrets.choice(char_alphabet)
    #Requirements:
    if (any(chars in punctuations for chars in password) and
        sum(chars in digits for chars in password) >= 2):
        break


print(password)
