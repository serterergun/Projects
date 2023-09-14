for a in range(1,1001):
    for b in range(1,1001):
        c = (a**2 + b**2)**0.5
        x = a + b + c
        if x == 1000 and a < b < c:
            print(int(a*b*c))