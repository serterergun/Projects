def dividerCounter(n:int)->int:
    divider = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divider += 1
    return divider*2

def dividers(n:int)->list:
    a = [1, int(n)]
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            a.append(i)

    return sorted(a)

n = 1 
while True:
    num = (n*(n+1))/2
    if dividerCounter(num) > 500:
        break
    n += 1

print(int(num))
print(dividers(num))