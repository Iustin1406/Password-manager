import random
import pyperclip
special_characters = "!@#$%&*_+=?"


def enough_letters(password):
    num = 0
    for character in password:
        if character.isalpha():
            num += 1
    if num >= 5:
        return True
    return False


def generate_password():
    length = random.randint(8, 16)
    good = False
    while not good:
        good = True
        password = ""
        for i in range(0, length):
            password += (chr(random.randint(33, 122)))

        has_special_char = any(char in special_characters for char in password)
        has_uppercase = any('A' <= char <= 'Z' for char in password)

        if not has_uppercase and not has_special_char or not enough_letters(password):
            good = False
        if good:
            pyperclip.copy(password) # after we created the password we copy it on clipboard
            return password
