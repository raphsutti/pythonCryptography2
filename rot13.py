alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message: ")
shift = 13

n = len(str_in)
str_out = ""

for i in range(n):
  c = str_in[i] # character
  loc = alpha.find(c) # index of character
  newloc = (loc + shift) % 26
  str_out += alpha[newloc]  # collect new character

print("Obfuscated version:", str_out)