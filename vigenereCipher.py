letters='abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, keys):
  plaintext=plaintext.lower()
  keys=keys.lower()
  key_stream=''
  ciphertext=''
  for i in range(len(plaintext)):
    key_stream+=keys[i % len(keys)]
  print(f"Key Stream: {key_stream}")
  
  for letter, key in zip(plaintext,key_stream):
    plaintext=plaintext.lower()
    if letter in letters:
      position=letters.find(letter)
      key_position=letters.find(key)
      new_position=(position+ key_position)%26
      new_char=letters[new_position]
      ciphertext+=new_char
    else:
      ciphertext+=letter
  return ciphertext

def decrypt(ciphertext, keys):
  keys=keys.lower()
  ciphertext=ciphertext.lower()
  key_stream=''
  plaintext=''
  for i in range(len(ciphertext)):
    key_stream+=keys[i % len(keys)]
    
  for letter, key in zip(ciphertext,key_stream):
    if letter in letters:
      position=letters.find(letter)
      key_position=letters.find(key)
      new_position=(position - key_position)%26
      new_char=letters[new_position]
      plaintext+=new_char
    else:
      plaintext+=letter
  return plaintext

def main():
  while True:
    choice = input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
    if choice == 'e':
        plaintext = input("Enter plaintext: ")
        keys = input("Enter key (string): ")
        ciphertext = encrypt(plaintext, keys)
        print("Ciphertext:", ciphertext)
    elif choice == 'd':
        ciphertext = input("Enter ciphertext: ")
        keys = input("Enter key (string): ")
        plaintext = decrypt(ciphertext, keys)
        print("Plaintext:", plaintext)
    elif choice == 'q':
        print("Exiting program.")
        break


main()