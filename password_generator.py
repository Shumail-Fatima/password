import random
import string

def gen_password(length, lower_let = True, upper_let = True, num= True, sp_chars = True):
    lower_letter = string.ascii_lowercase
    upper_letter = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    chars = ""

    if lower_let:
        chars += lower_letter
    if upper_let:
        chars += upper_letter
    if num:
        chars += digits
    if sp_chars:
        chars += special_chars
    
    password = "".join(random.sample(chars,length))

    return password

print(gen_password(10))