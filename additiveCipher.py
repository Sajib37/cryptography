letters= 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext,key):
  ciphertext=''
  for char in plaintext:
    char=char.lower()
    if char in letters:
      position=letters.find(char)
      new_position=(position+key)%26
      new_char=letters[new_position]
      ciphertext+=new_char
    else:
      ciphertext+=char
  return ciphertext.upper()
def decrypt(ciphertext,key):
  plaintext=''
  for char in ciphertext:
    if char in letters:
      position=letters.find(char)
      new_position=(position-key)%26
      new_char=letters[new_position]
      plaintext+=new_char
    else:
      plaintext+=char
  return plaintext.upper()

def main():
  while True:
    choice=input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice=='e':
      plaintext=input("Enter plaintext: ")
      key=int(input("Enter key (number): "))
      ciphertext=encrypt(plaintext,key)
      print("Ciphertext:",ciphertext)
    elif choice=='d':
      ciphertext=input("Enter ciphertext: ")
      key=int(input("Enter key (number): "))
      plaintext=decrypt(ciphertext,key)
      print("Plaintext:",plaintext)
    elif choice=='q':
      print("Exiting program.")
      break
    else:
      print("Invalid choice. Please try again.")
  

main()