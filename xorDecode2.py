# try out every possible key from 01-99
# decode hex 70155d5c45415d5011585446424c

text = raw_input("Enter text: ")
hex = text.decode("hex")
hexLen = len(hex)

for k1 in "0123456789":
  for k2 in "0123456789":
    key = k1 + k2 # key 01 - 99
    cipher = ""
    for i in range(hexLen):
      k = key[i%2] # alternate first and second key digit
      t = hex[i]
      x = ord(k) ^ ord(t)
      cipher += chr(x)
    print text, cipher

