
with open('ciphertext2.txt', 'r') as file:
    ciphertext_str = file.read()


dict1 = {
    'A': 'i', 'B': 'x', 'C': 'v', 'D': 'g', 'E': 'l', 'F': 'f', 'G': 'e', 'H': 'd', 
    'I': 'q', 'J': 'c', 'K': 'b', 'L': 'a', 'M': 'z', 'N': 'y', 'O': 'r', 'P': 's', 
    'Q': 'j', 'R': 'm', 'S': 'h', 'T': 'n', 'U': 'p', 'V': 'w', 'W': 'k', 'X': 'u', 
    'Y': 'o', 'Z': 't', ' ': ' '
}

def decrypt_substitution(ciphertext, mapping):
    decrypted_text = ""
    for char in ciphertext:
        
        if char.upper() in mapping:
            
            if char.islower():
                decrypted_text += mapping[char.upper()].lower()
            else:
                decrypted_text += mapping[char.upper()]
        else:
            
            decrypted_text += char
    return decrypted_text


decrypted_text = decrypt_substitution(ciphertext_str, dict1)

print(decrypted_text)
