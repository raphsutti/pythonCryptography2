# try out every possible key from 01-99
# decode hex 70155d5c45415d5011585446424c

text = "70155d5c45415d5011585446424c"
textHex = text.decode("hex")

for k1 in range(10):
  for k2 in range(10):
    key = str(k1) + str(k2)
    cipher = ""
    for i in range(len(textHex)):
      currChar = textHex[i]
      currKey = key[i%2]
      currCipherChar = ord(currChar) ^ ord(currKey)
      cipher += chr(currCipherChar)
    print key, cipher