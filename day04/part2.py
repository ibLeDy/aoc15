import hashlib

with open('input.txt', 'r') as f:
    secret_key = f.read()

hashed = ''
number = -1
while not hashed.startswith('000000'):
    number += 1
    hashed = hashlib.md5(f'{secret_key}{str(number)}'.encode()).hexdigest()

print(number)
