def palindromic():
    number_list = []
    for a in range(100,1000):
        for b in range(100,1000):
            x = a * b
            if str(x) == str(x)[::-1]:
                number_list.append(x)
    number_list = sorted(number_list)
    return number_list[-1]
print(palindromic())