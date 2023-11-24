


import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

password_to_hash = "MyCode1!"

hashed_password = hash_password(password_to_hash)

print("Original Password:", password_to_hash)
print("Hashed Password:", hashed_password)
