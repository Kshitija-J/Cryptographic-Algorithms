import string


with open('Ciphertext5.txt', 'r') as file:
    ciphertext_str = file.read()

def decrypt_caesar(text, shift=3):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

decrypted_text = decrypt_caesar(ciphertext_str).lower()


print(decrypted_text)
