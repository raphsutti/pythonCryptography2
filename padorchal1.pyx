from os import system

def decr(c):
  cmd = "curl -s http://ad.samsclass.info/141/Padchal1.php?c=" + c + ">padorchal1.out"
  res = system(cmd)

  with open("padorchal1.out", "r") as f:
    data = f.read()

  if data == "":
    print "Error: no response from server!  Are you online?"
    exit()

  a = data.find("Decryption result:")
  if a < 0:
    print "Error: no decryption result from server!"
    exit()

  b = data.find("<", a)
  if b < 0:
    print "Error: invalid response from server!"
    exit()

  return data[a+19 : b]
