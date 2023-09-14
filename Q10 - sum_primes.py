def isPrime(n:int)->bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

total = 2
n = 1
while n < 2000000:
    n += 2
    if isPrime(n):
        total += n
print(total)

