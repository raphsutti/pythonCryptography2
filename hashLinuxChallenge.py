from passlib.hash import sha512_crypt
import time
# hash starts with = "PcSL"
# salt = "penguins"
# password ranges from 000 to 999

startTime = time.time()
s = "penguins"
for password in range(1000,2000):
  p = str(password)[1:]
  h = sha512_crypt.using(salt=s, rounds=5000).hash(p)
  if h[12:16] == "PcSL":
    print p, h
print "Time taken: %0.4f seconds" % (time.time() - startTime)