def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        lst_digits = []
        for digit in str(n):
            lst_digits.append(int(digit))
            n = sum(lst_digits)
        return digital_root(n)

print(digital_root(16)) # retorna 7
print(digital_root(942)) # retorna 6
print(digital_root(132189)) # retorna 6
print(digital_root(493193)) # retorna 2
