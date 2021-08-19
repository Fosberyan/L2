listttt = [(-14 + 88), 1337, 3.14, True, None, 'Тут текст', [1, 2],

           (3, 4, 5.5), {11: 'Один и Один', 1: 'Просто один'}, {9, 10},

           frozenset(), range(100500), b'tnj', bytearray(b'texting'),

           zip(*[(4, 5), (6, 7), ('x', 'y')]), TypeError]

for l, item in enumerate(listttt, 1):

    print(f"{l}) {item} - {type(item)}")