import hashlib
# 100 rounds of MD5 aka "stretching"
# find password that result in hash of c09145ad46b058fba82e4218169c7121
# password is between 000 and 999

for p1 in "0123456789":
  for p2 in "0123456789":
    for p3 in "0123456789":
      password = p1 + p2 + p3
      h = password
      for i in range(100):
        h = hashlib.new("md5", h).hexdigest()
      # print password, h
      if h == "c09145ad46b058fba82e4218169c7121":
        print password, h
