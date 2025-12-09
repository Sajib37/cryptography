import random
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_keys():
    p = int(input("Enter a prime number p: "))
    while not is_prime(p):
        print("Not a prime! Enter again.")
        p = int(input("Enter a prime number p: "))

    g = random.randint(2, p - 1)

    # Private key (a) choose randomly
    a = random.randint(2, p - 2)

    # Public key component h
    h = mod_exp(g, a, p)

    print("Public Key: (p =", p, ", g =", g, ", h =", h, ")")
    print("Private Key: a =", a)

    return p, g, h, a

# Encryption
def encrypt(plaintext, p, g, h):
    plaintext = plaintext.replace(" ", "").upper()
    cipher_pairs = []

    for char in plaintext:
        if char in letters:
            m = letters.index(char)

            k = random.randint(2, p - 2)  # Random session key

            c1 = mod_exp(g, k, p)
            c2 = (m * mod_exp(h, k, p)) % p

            cipher_pairs.append((c1, c2))

    return cipher_pairs

# Decryption
def decrypt(cipher_pairs, p, a):
    plaintext = ""

    for c1, c2 in cipher_pairs:
        s = mod_exp(c1, a, p)
        s_inv = pow(s, -1, p)  # modular inverse of s modulo p
        m = (c2 * s_inv) % p
        plaintext += letters[m]

    return plaintext


# Main Program Loop
while True:
    choice = input("\nType 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

    if choice == 'e':
        p, g, h, a = generate_keys()
        plaintext = input("Enter plaintext (A-Z only): ")
        cipher = encrypt(plaintext, p, g, h)
        print("Encrypted Cipher:", cipher)

    elif choice == 'd':
        p = int(input("Enter p: "))
        a = int(input("Enter private key a: "))
        cipher_input = input("Enter cipher as pairs (e.g., (c1,c2) (c1,c2)): ")

        # Parse input back into pairs
        pairs = eval("[" + cipher_input.replace(") (", "),(") + "]")
        decrypted = decrypt(pairs, p, a)
        print("Decrypted Plaintext:", decrypted)

    elif choice == 'q':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
