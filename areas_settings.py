#klasicke sudoku 9x9

radky = []
for i in range(9):
    new_line = []
    for j in range(9):
        new_line.append((i, j))
    radky.append(new_line)

sloupce = []
for i in range(9):
    new_column = []
    for j in range(9):
        new_column.append((j, i))
    sloupce.append(new_column)

ctverce = []
for i, j in [(0, 3), (3, 6), (6, 9)]:
    for k, l in [(0, 3), (3, 6), (6, 9)]:
        ctverce.append([(x, y) for x in range(i, j) for y in range(k, l)])

'''
ctverce.append([(x, y) for x in range(3) for y in range(3)])
ctverce.append([(x, y) for x in range(3) for y in range(3,6)])
ctverce.append([(x, y) for x in range(3) for y in range(6,9)])
ctverce.append([(x, y) for x in range(3, 6) for y in range(3)])
ctverce.append([(x, y) for x in range(3, 6) for y in range(3, 6)])
ctverce.append([(x, y) for x in range(3, 6) for y in range(6, 9)])
ctverce.append([(x, y) for x in range(6, 9) for y in range(3)])
ctverce.append([(x, y) for x in range(6, 9) for y in range(3, 6)])
ctverce.append([(x, y) for x in range(6, 9) for y in range(6, 9)])
'''

hlavni_uhlopricka = [(i, i) for i in range(9)]
vedl_uhlopricka = [(i, 8-i) for i in range(9)]

uhlopricky = [hlavni_uhlopricka, vedl_uhlopricka]

areas_coords = radky + sloupce + ctverce  # + uhlopricky


