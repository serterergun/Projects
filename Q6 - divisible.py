def find_obeb(a:int, b:int)->int:
    while b:
        a, b = b, a % b
    return a

def find_okek(n:int)->int:
    okek = 1
    for i in range(1, n):
        okek = okek * i // find_obeb(okek, i)
    return okek

print(find_okek(20))

