letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def encrypt(plaintext, key):
  ciphertext=''
  for letter in plaintext:
    if letter.islower():
      position=letters.find(letter)
      new_position=(position+key)%26
      new_char=letters[new_position]
      ciphertext+=new_char
    elif letter.isupper():
      position=letters.find(letter.lower())
      new_position=(position+key)%26
      new_char=letters[new_position].upper()
      ciphertext+=new_char
    elif letter in digits:
      position=digits.find(letter)
      new_position=(position+key)%10
      new_char=digits[new_position]
      ciphertext+=new_char
    else:
      ciphertext+=letter
  return ciphertext

def decrypt(ciphertext, key):
  plaintext=''
  for letter in ciphertext:
    if letter.islower():
      position=letters.find(letter)
      new_position=(position - key)%26
      new_char=letters[new_position]
      plaintext+=new_char
    elif letter.isupper():
      position=letters.find(letter.lower())
      new_position=(position - key)%26
      new_char=letters[new_position].upper()
      plaintext+=new_char
    elif letter in digits:
      position=digits.find(letter)
      new_position=(position - key)%10
      new_char=digits[new_position]
      plaintext+=new_char
    else:
      plaintext+=letter
  return plaintext

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