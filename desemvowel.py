def disemvowel(string_):
    for ch in 'aeiouAEIOU':
        string_ = string_.replace(ch, '')
    return string_


print(disemvowel('Loser LOL!')) #retorna "LsrLL!"
