def my_func(x):
    total = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
print(my_func(1000))