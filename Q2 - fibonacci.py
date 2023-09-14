def fibonacci(x):
    sum = 0
    a = 1
    b = 1
    c = a + b
    while c < x:
        sum = sum + c
        a = b + c
        b = c + a
        c = a + b
    else:
        return sum

print(fibonacci(4000000))