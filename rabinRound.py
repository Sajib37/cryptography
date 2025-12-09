import math

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_keys():
    while True:
        p = int(input("Enter prime p (p % 4 == 3): "))
        q = int(input("Enter prime q (q % 4 == 3): "))

        if is_prime(p) and is_prime(q) and p % 4 == 3 and q % 4 == 3:
            break
        else:
            print("Both must be primes and ≡ 3 (mod 4). Try again.")

    n = p * q
    return p, q, n

def encrypt(plaintext, n):
    ciphertext = []
    for char in plaintext.replace(" ", "").upper():
        if char in letters:
            m = letters.find(char)
            c = pow(m, 2, n)
            ciphertext.append(str(c))
    return " ".join(ciphertext)

def decrypt(ciphertext, p, q):
    n = p * q
    cipher_nums = list(map(int, ciphertext.split()))
    plaintext = ""

    for c in cipher_nums:
        # Compute square roots mod p and mod q
        r = pow(c, (p + 1) // 4, p)
        s = pow(c, (q + 1) // 4, q)

        # Chinese Remainder Theorem combinations
        inv_q = pow(q, -1, p)
        inv_p = pow(p, -1, q)

        x = (r * q * inv_q + s * p * inv_p) % n
        y = (r * q * inv_q - s * p * inv_p) % n
        z = (-r * q * inv_q + s * p * inv_p) % n
        w = (-r * q * inv_q - s * p * inv_p) % n

        candidates = [x, y, z, w]

        # Pick the candidate within 0–25 (valid letter range)
        valid = [num for num in candidates if 0 <= num < 26]

        if valid:
            plaintext += letters[valid[0]]  # choose the correct one
        else:
            plaintext += "?"

    return plaintext

while True:
    choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")

    if choice == 'e':
        p, q, n = generate_keys()
        print("Public Key:", n)
        plaintext = input("Enter plaintext: ")
        cipher = encrypt(plaintext, n)
        print("Ciphertext:", cipher)

    elif choice == 'd':
        p = int(input("Enter private p: "))
        q = int(input("Enter private q: "))
        ciphertext = input("Enter ciphertext (space-separated numbers): ")
        print("Plaintext:", decrypt(ciphertext, p, q))

    elif choice == 'q':
        break
