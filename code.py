import math

s = int(0)
n = int(0)
k = int(input("Input Upper Limit: "))

for n in range(k):
    s += (((-1)**n)*4)/(2*n+1)

print(s)
