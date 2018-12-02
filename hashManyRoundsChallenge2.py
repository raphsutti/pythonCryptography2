import hashlib
import time
# Upto 5000 rounds of SHA-1 hashing
# find password that result in hash of f6dc23c15a1d0c64e8d1c53cd95adc346ceeccbe
# password is between 000 and 999

startTime = time.time()

for p1 in "0123456789":
  for p2 in "0123456789":
    for p3 in "0123456789":
      password = p1 + p2 + p3
      h = password
      for i in range(5000):
        h = hashlib.new("sha1", h).hexdigest()
        if h == "f6dc23c15a1d0c64e8d1c53cd95adc346ceeccbe":
          print password, h

print "Time taken: %.03f seconds" % (time.time() - startTime)