letters='abcdefghijklmnopqrstuvwxyz'
def mod_inverse(key):
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            return i
    return None

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        char = char.lower()
        if char in letters:
            position = letters.find(char)
            new_position = (position * key) % 26
            new_char = letters[new_position]
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    mod_inv = mod_inverse(key)
    for char in ciphertext:
        if char in letters:
            position = letters.find(char)
            new_position = (position * mod_inv) % 26
            new_char = letters[new_position]
            plaintext += new_char
        else:
            plaintext += char
    return plaintext
  
def main():
    while True:
        choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
        if choice == 'e':
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key (number): "))
            mod_inverse = mod_inverse(key)
            if mod_inverse is None:
                print("Key has no modular inverse. Choose a different key.")
                continue
            ciphertext = encrypt(plaintext, key)
            print("Ciphertext:", ciphertext)
        elif choice == 'd':
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key (number): "))
            mod_inverse = mod_inverse(key)
            if mod_inverse is None:
                print("Key has no modular inverse. Choose a different key.")
                continue
            plaintext = decrypt(ciphertext, key)
            print("Plaintext:", plaintext)
        elif choice == 'q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()