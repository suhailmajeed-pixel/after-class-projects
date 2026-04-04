import random
import string

length = 10

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits

all_chars = lower + upper + numbers

password = ''.join(random.choice(all_chars) for i in range(length))

password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)

print("Generated Password:", final_password)