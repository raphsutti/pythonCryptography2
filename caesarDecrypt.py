# decrypting caesar cipher challenge
# decrypt: ABJLKPQOXQFLK
# decrypt: MYXQBKDEVKDSYXC

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = raw_input("Enter text: ")

print "Text:", text

for j in range(26):
  shift = j
  cipher = ""
  for i in range(len(text)):
    loc = alpha.find(text[i])
    newloc = (shift + loc) % 26
    cipher += alpha[newloc]

  # print "Shift value:", j, ";", "Cipher text:", cipher
  print "Shift value: %d, Cipher text: %s" % (j,cipher)