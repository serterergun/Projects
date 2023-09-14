def square_(n:int)->int:
    sum = 0
    for i in range(0,n):
        sum += i*i
    return sum

def square(n:int)->int:
    sum = 0
    for i in range(0,n):
        sum = sum + i
    return sum**2

print(square(101) - square_(101))