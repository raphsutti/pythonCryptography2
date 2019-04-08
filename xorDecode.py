# try out every possible key from 0-9
# decode snw{fzs
# decode kquht}
# decode

text = raw_input("Enter text: ")
n = len(text)

for k in "0123456789":
  cipher = ""
  for i in range(n):
    t = text[i]
    x = ord(k) ^ ord(t)
    cipher += chr(x)
  print k, cipher
