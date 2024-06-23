def string_merge(string1, string2, letter):
    lst1 = list(string1)
    lst2 = list(string2)
    idx1 = []
    idx2 = []
    for x in lst1:
        if x == letter:
            idx1.append(lst1.index(x))
    for v in lst2:
        if v == letter:
            idx2.append(lst2.index(v))
    return string1[0:idx1[0]] + string2[idx2[0]:]

print(string_merge("hello", "world", "l")) #"held"
print(string_merge("coding", "anywhere", "n")) #"codinywhere"
print(string_merge("jason", "samson", "s")) #"jasamson"