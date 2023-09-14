def my_func(x):
    for i in range(2,x):
        while x > i:
            if x % i == 0:
                x = x / i
            else:
                i = i + 1
        else:
            return x
print(my_func(int(600851475143)))