import math

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (e * d) % phi == 1:
            return d
    return None
  
def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
  
def generate_keypair(p, q):
    if not (isprime(p) and isprime(q)):
        print("Both numbers must be prime.")
    elif p == q:
        print("p and q cannot be the same.")
  
    n = p * q
    phi = (p - 1) * (q - 1)
  
    e = 3
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 2
  
    d = mod_inverse(e, phi)
  
    return e, d, n
  
def encrypt(message, e, n):
  cipher= message**e %n
  return cipher
  
def decrypt(ciphertext, d, n):
  message = ciphertext**d %n
  return message

while True:
  choice=input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
  if choice=='e':
    message=int(input("Enter message (number): "))
    p=int(input("Enter prime number p: "))
    q=int(input("Enter prime number q: "))
    e,d,n=generate_keypair(p,q)
    print("Public key: ",(e,n))
    print("Private key: ",(d,n))
    cipher=encrypt(message,e,n)
    print("Cipher:",cipher)
  elif choice=='d':
    cipher=int(input("Enter cipher (number): "))
    d=int(input("Enter private exponent d: "))
    n=int(input("Enter modulus n: "))
    message=decrypt(cipher,d,n)
    print("Message:",message)
  elif choice=='q':
    print("Exiting program.")
    break
