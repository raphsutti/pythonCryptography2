from decimal import *
# RSA can be cracked if two prime numbers chosen are close together
# Find two primes that multply to be 10000000000000000016800000000000000005031


n = 10000000000000000016800000000000000005031
getcontext().prec = 50
print Decimal(n).sqrt() # 100000000000000000083.99999999999999998987500000000

for p in range (100000000000000000083, 100000000000000000030, -2):
  print p, n%p