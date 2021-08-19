flist = input('Числа с пробеами - ').split()

for i in range(1, len(flist), 2):
    flist.insert(i - 2, flist.pop(i))
print(flist)

