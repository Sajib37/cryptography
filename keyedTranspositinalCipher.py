def encrypt(plaintext, key_matrix):
  plaintext=plaintext.replace(" ","").upper()
  key_length=len(key_matrix)
  while len(plaintext)%key_length !=0:
    plaintext+='X'
  ciphertext=''
  for i in range(0,len(plaintext),key_length):
    block=plaintext[i:i+key_length]
    new_block=['']*key_length
    for index in range(key_length):
      new_block[index]=block[key_matrix[index]]
    ciphertext+=''.join(new_block)
  return ciphertext

def decrypt(ciphertext, key_matrix):
  ciphertext=ciphertext.replace(" ","").upper()
  key_length=len(key_matrix)
  while len(ciphertext)%key_length !=0:
    ciphertext+='X'
  plaintext=''
  for i in range(0,len(ciphertext),key_length):
    block=ciphertext[i:i+key_length]
    new_block=['']*key_length
    for index in range(key_length):
      new_block[key_matrix[index]]=block[index]
    plaintext+=''.join(new_block)
  return plaintext

while True:
  choice=input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
  if choice=='e':
    plaintext=input("Enter plaintext: ")
    ciphertext=encrypt(plaintext,[2,0,3,4,1])
    print("Ciphertext:",ciphertext)
  elif choice=='d':
    ciphertext=input("Enter ciphertext: ")
    plaintext=decrypt(ciphertext,[2,0,3,4,1])
    print("Plaintext:",plaintext)
  elif choice=='q':
    print("Exiting program.")
    break
      
    