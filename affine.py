def mod_inverse(a, m=26):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(ciphertext, a, b, m=26):
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - 65
            x = (a_inv * (y - b)) % m
            plaintext += chr(x + 65)
        else:
            plaintext += char
    return plaintext

def brute_force_decrypt(ciphertext):
    possible_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    for a in possible_keys:
        for b in range(26):
            decrypted_message = decrypt(ciphertext, a, b)
            if decrypted_message:
                print(f"Decrypted with a={a}, b={b}: {decrypted_message}")

# Reading the encrypted message from a file
file_path = 'ciphertext6.txt'
with open(file_path, 'r') as file:
    encrypted_message = file.read()

brute_force_decrypt(encrypted_message)
