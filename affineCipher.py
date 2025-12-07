letters= 'abcdefghijklmnopqrstuvwxyz'

def mod_inverse(key1):
    for i in range(1, 26):
        if (key1 * i) % 26 == 1:
            return i
    return None

def encrypt(plaintext, key1, key2):
    ciphertext = ''
    for char in plaintext:
        char = char.lower()
        if char in letters:
            position = letters.find(char)
            new_position = (position * key1 + key2) % 26
            new_char = letters[new_position]
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key1, key2):
    plaintext = ''
    mod_inv = mod_inverse(key1)
    for char in ciphertext:
        if char in letters:
            position = letters.find(char)
            new_position = (mod_inv * (position - key2)) % 26
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
        key1 = int(input("Enter multiplicative key (number): "))
        key2 = int(input("Enter additive key (number): "))
        mod_inverse_key = mod_inverse(key1)
        if mod_inverse_key is None:
            print("Multiplicative key has no modular inverse. Choose a different key.")
            continue
        ciphertext = encrypt(plaintext, key1, key2)
        print("Ciphertext:", ciphertext)
    elif choice == 'd':
        ciphertext = input("Enter ciphertext: ")
        key1 = int(input("Enter multiplicative key (number): "))
        key2 = int(input("Enter additive key (number): "))
        mod_inverse_key = mod_inverse(key1)
        if mod_inverse_key is None:
            print("Multiplicative key has no modular inverse. Choose a different key.")
            continue
        plaintext = decrypt(ciphertext, key1, key2)
        print("Plaintext:", plaintext)
    elif choice == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

main()