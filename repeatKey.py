# repeat key n times

key = raw_input("Enter key: ")
times = raw_input("Enter times: ")
paddedKey = ""

for i in range(int(times)):
  paddedKey += key[i%len(key)]

print "Key: %s \nPadded Key: %s" % (key, paddedKey)