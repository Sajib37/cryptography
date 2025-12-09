import string

# Function to generate Playfair Key Matrix
def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Treat I and J as same

    matrix = []
    used = set()

    for char in key:
        if char not in used and char in string.ascii_uppercase:
            used.add(char)
            matrix.append(char)

    for char in string.ascii_uppercase:
        if char not in used and char != 'J':
            used.add(char)
            matrix.append(char)

    key_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


# Function to preprocess plaintext
def prepare_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")

    prepared = ""
    i = 0
    while i < len(text):
        prepared += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared += 'X'
            i += 1
        else:
            if i + 1 < len(text):
                prepared += text[i + 1]
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared


# Find position of character in key matrix
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


# Encrypt pair
def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]

    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

    else:  # Rectangle Rule
        return matrix[row1][col2] + matrix[row2][col1]


# Decrypt pair
def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]

    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]

    else:
        return matrix[row1][col2] + matrix[row2][col1]


# Full Encryption
def encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(plaintext)

    ciphertext = ""
    for i in range(0, len(text), 2):
        ciphertext += encrypt_pair(matrix, text[i], text[i + 1])

    return ciphertext


# Full Decryption
def decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(matrix, ciphertext[i], ciphertext[i + 1])

    return plaintext


# Driver Code
while True:
    choice = input("Encrypt (E), Decrypt (D), Quit (Q): ").upper()

    if choice == 'E':
        text = input("Enter plaintext: ")
        key = input("Enter key: ")
        print("Ciphertext:", encrypt(text, key))

    elif choice == 'D':
        text = input("Enter ciphertext: ")
        key = input("Enter key: ")
        print("Plaintext:", decrypt(text, key))

    elif choice == 'Q':
        print("Exiting.")
        break

    else:
        print("Invalid choice!")
