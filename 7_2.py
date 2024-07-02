ten = "hung"
num = 23
print(type(ten))
print(9//2) #chia lay phan nguyen
print(9%2) #chia lay phan du
print(9**2)# luy thua

from decimal import*
getcontext().prec = 10  # ko co cung dc
dec = Decimal(10)/3
print(dec)

from fractions import*
frac = Fraction(4,9)
print(frac)

c = complex(2,5)
print(c,"  ",c.real, "   ", c.imag)


