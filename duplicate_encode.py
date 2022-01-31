def duplicate_encode(word):
    word = word.lower()
    lst_ch = []
    for char in word.lower():
        if word.count(char) == 1:
            lst_ch.append("(")
        elif word.count(char) > 1:
            lst_ch.append(")")
    return "".join(lst_ch).lower()


print('"{}"'.format(duplicate_encode("din"))) # returns "((("
print('"{}"'.format(duplicate_encode("recebe"))) # returns "()()()"
print('"{}"'.format(duplicate_encode("Success"))) # returns ")())())"
print('"{}"'.format(duplicate_encode("(( @"))) # returns "(())""