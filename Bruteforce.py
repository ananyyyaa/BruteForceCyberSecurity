import hashlib
import itertools

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def brute_force_attack(target_hash):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+' 
    password_length = 8 

    for length in range(1, password_length + 1):
        for guess in itertools.product(characters, repeat=length):
            password = ''.join(guess)
            hashed_guess = hash_password(password)
            if hashed_guess == target_hash:
                return password

    return None

target_hash ='your targetted hash paswrod'

cracked_password = brute_force_attack(target_hash)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found")
