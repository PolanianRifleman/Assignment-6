import math

while True:
    s = int(0)
    n = int(0)
    k = input("Input Upper Limit: ")

    try:
        k = int(k)
    except ValueError:
        print("INVALID INPUT. ENTER A NUMBER")
        continue

    for n in range(k):
        s += (((-1)**n)*4)/(2*n+1)

    print(s)
    break
