mlist = [7, 6, 5, 3, 7, 3, 2, 0]
new_number = int(input('Новый элемент рейига в виде числа - '))
a = 0

for n in mlist:
    if new_number <= n:
        a += 1
mlist.insert(a, int(new_number))
print(mlist)