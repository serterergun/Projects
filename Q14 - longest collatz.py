def evenOdd(x:int)->int:
    if x % 2 == 0:
        return int(x / 2)
    else:
        return int(3*x + 1)

print(evenOdd(13))

