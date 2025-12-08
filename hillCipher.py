import numpy as np

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def text_to_numbers(text):
    return [letters.index(c) for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join([letters[n % 26] for n in numbers])

def mod_inv_matrix(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  
    det_inv = pow(det, -1, modulus)         
    adj = np.round(det * np.linalg.inv(matrix)).astype(int)  
    return (det_inv * adj) % modulus

def encrypt(plaintext, key_matrix):
    numbers = text_to_numbers(plaintext)
    n = key_matrix.shape[0]
    # Padding if needed
    while len(numbers) % n != 0:
        numbers.append(23)  # 'X'
    ciphertext_numbers = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        cipher_block = key_matrix.dot(block) % 26
        ciphertext_numbers.extend(cipher_block)
    return numbers_to_text(ciphertext_numbers)

def decrypt(ciphertext, key_matrix):
    numbers = text_to_numbers(ciphertext)
    n = key_matrix.shape[0]
    key_inv = mod_inv_matrix(key_matrix, 26)
    plaintext_numbers = []
    for i in range(0, len(numbers), n):
        block = np.array(numbers[i:i+n])
        plain_block = key_inv.dot(block) % 26
        plaintext_numbers.extend(plain_block)
    return numbers_to_text(plaintext_numbers)


key_matrix = np.array([[3, 2],
                       [5, 7]])

while True:
    choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        plaintext = input("Enter plaintext: ")
        ciphertext = encrypt(plaintext, key_matrix)
        print("Ciphertext:", ciphertext)
    elif choice == 'd':
        ciphertext = input("Enter ciphertext: ")
        plaintext = decrypt(ciphertext, key_matrix)
        print("Plaintext:", plaintext)
    elif choice == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
