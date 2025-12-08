import math
def encrypt(plaintext):
  plaintext=plaintext.replace(" ","").upper()
  rows= math.ceil(math.sqrt(len(plaintext)))
  columns=rows
  matrix=[]
  position=0
  
  for row in range(rows):
    row_data=[]
    for col in range(columns):
      if position<len(plaintext):
        row_data.append(plaintext[position])
        position+=1
      else:
        row_data.append('X')
    matrix.append(row_data)
    
  ciphertext=''
  for col in range(columns):
    for row in range(rows):
      ciphertext+=matrix[row][col]
  return ciphertext

def decrypt(ciphertext):
  ciphertext=ciphertext.replace(" ","").upper()
  rows= math.ceil(math.sqrt(len(ciphertext)))
  columns=rows
  matrix=[]
  position=0
  for row in range(rows):
    row_data=[]
    for col in range(columns):
      if position<len(ciphertext):
        row_data.append(ciphertext[position])
        position+=1
      else:
        row_data.append('X')
    matrix.append(row_data)
  plaintext=''
  for col in range(columns):
    for row in range(rows):
      plaintext+=matrix[row][col]
  return plaintext


while True:
  choice=input("Type 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ")
  if choice=='e':
    plaintext=input("Enter plaintext: ")
    ciphertext=encrypt(plaintext)
    print("Ciphertext:",ciphertext)
  elif choice=='d':
    ciphertext=input("Enter ciphertext: ")
    plaintext=decrypt(ciphertext)
    print("Plaintext:",plaintext)
  elif choice=='q':
    print("Exiting program.")
    break
    