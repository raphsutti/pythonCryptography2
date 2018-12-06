from passlib.hash import sha512_crypt
s = "4S"
p = "password"
print sha512_crypt.using(salt=s, rounds=5000).hash(p)