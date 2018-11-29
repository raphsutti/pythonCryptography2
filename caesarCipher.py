#Python 2.7

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = raw_input("Enter text: ")
shift = int(raw_input("Enter shift value: "))
cipher = ""

for i in range(len(text)):
  loc = alpha.find(text[i]) # position of text in the alphabet
  newLoc = loc + shift
  cipher += alpha[newLoc]

print "Original text:", text
print "Cipher text:", cipher