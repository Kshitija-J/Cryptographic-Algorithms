import math

n = 68102916241556953901301068745501609390192169871097881297
e = 36639088738407540894550923202224101809992059348223191165
matrixgiven = [
    [' ', '!', '\"', '#', '$', '%', '&', '\'', '(', ')'],
    ['*', '+', ',', '-', '.', '/', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9', ':', ';', '<', '='],
    ['>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
    ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
    ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '['],
    ['?', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
    ['z', '{', '|', '}', '~', ' ', ' ', '\n', '\r', ' ']
]
B = 2000

# Function to perform Pollard's p-1 algorithm
def pollard_p1(n, B):
    a = 2
    for i in range(2, B + 1):
        a = pow(a, i, n)
    d = math.gcd(a - 1, n)
    if 1 < d < n:
        return d
    else:
        return None

p = pollard_p1(n, B)
print("P:", p)
q = n // p
print("q:", q)

phi = (p - 1) * (q - 1)
print("phi value:", phi)

# Calculate d, the modular multiplicative inverse of e modulo phi
d = pow(e, -1, phi)
print("d:", d)

# Function to decrypt the ciphertext
def decrypt_cipher(ciphertext, d, n, matrix):
    finalanswer = ""
    for i in ciphertext:
        formula = pow(int(i), d, n)
        formulastr = str(formula)
        # Adjust formulastr to have even length
        if len(formulastr) % 2 != 0:
            formulastr = "0" + formulastr
        for j in range(0, len(formulastr), 2):
            rowvalue = int(formulastr[j])
            columnvalue = int(formulastr[j+1])
            finalanswer += matrix[rowvalue][columnvalue]
    return finalanswer

# Reading ciphertext from a file and decrypting it
with open('rsacipher.txt', 'r') as file:
    ciphertext = [line.strip() for line in file.readlines()]

decrypted_message = decrypt_cipher(ciphertext, d, n, matrixgiven)
print("Decrypted message:", decrypted_message)
