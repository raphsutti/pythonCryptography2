# caesar cipher with shift value of 3
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message: ")

n = len(str_in)
str_out = ""

for i in range(n):
  c = str_in[i] # character
  loc = alpha.find(c) # index of character
  print (i,c,loc)
  newloc = loc + 3
  str_out += alpha[newloc]  # collect new character
  print(newloc, str_out)
print("Obfuscated version:",str_out)