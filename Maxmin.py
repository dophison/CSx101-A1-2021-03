from decimal import*

a, b = list(map(int,input().split()))

max = ((a+b)+ abs(a-b))/2 
min = ((a+b)-abs(a-b))/2

print("max = ",int(max))
print("max = ",int(min))
