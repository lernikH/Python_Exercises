def m(l):
    ls = [-x if 2 <= i <= 7 else x for i, x in enumerate(l)]
    return ls
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(m(ls))