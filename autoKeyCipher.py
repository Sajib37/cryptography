letters='abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext,keys):
  plaintext=plaintext.lower()
  ciphertext=''
  only_ltters=''
  for char in plaintext:
    if char in letters:
      only_ltters+=char
  key_stream=keys+only_ltters
  key_stream=key_stream[:len(plaintext)]
  print(f"Key Stream: {key_stream}")
  for letter , key in zip(plaintext,key_stream):
    if letter in letters:
      position=letters.find(letter)
      key_position=letters.find(key)
      new_position=(position+key_position)%26
      new_char=letters[new_position]
      ciphertext+=new_char
    else:
      ciphertext+=letter
  return ciphertext


def decrypt(ciphertext,key_stream):
  plaintext=''
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
        key_stream = keys + ciphertext
        key_stream = key_stream[:len(ciphertext)]
        plaintext = decrypt(ciphertext, key_stream)
        print("Plaintext:", plaintext)
    elif choice == 'q':
        print("Exiting program.")
        break

main()