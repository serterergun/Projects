def is_prime(n:int)->bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 2
max = 1
while max < 10001:
    n += 1
    if is_prime(n):
        max += 1

print(n)