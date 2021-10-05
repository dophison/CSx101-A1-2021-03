from decimal import*

a = float(input())
a= (a-32)/1.8
getcontext().a= 6

print(Decimal(a).normalize())