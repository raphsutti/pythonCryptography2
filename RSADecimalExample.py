from decimal import *

a = 10**100 + 1
b = a * a
print Decimal(b).sqrt()
getcontext().prec = 200
print Decimal(b).sqrt()