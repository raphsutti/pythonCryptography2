import hashlib

p = "password"
h = p
for i in range(10):
  h = hashlib.new("md5", h).hexdigest()
  print i+1, h