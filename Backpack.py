def GetUnits(count):
    units = []
    for i in range(count):
        print('Enter name')
        name = input()
        print('Enter value')
        value = int(input())
        print('Enter size')
        size = int(input())
        units.append([name, value, size])
    return units


def FindSmallest(units):
    smallest = float('inf')
    for i in range(len(units)):
        if units[i][2] < smallest:
            smallest = units[i][2]
    return smallest


def MakeDynamicTable(units):
    print('Enter size of Backpack')
    sizeBackPack = int(input())
    smallest = FindSmallest(units)
    columns = sizeBackPack // smallest
    table = []
    for i in range(len(units) + 1):
        table.append([])
        for j in range(columns + 1):
            table[i].append(0)

    for i in range(1, len(units) + 1):
        for j in range(1, columns + 1):
            if units[i - 1][2] <= j:
                table[i][j] = max(table[i-1][j], units[i - 1][1] + table[i-1][j - units[i - 1][2]])
            else:
                table[i][j] = table[i-1][j]


    return table, table[len(units)][columns]


def MakeBackpack():
    print('Enter count of units')
    count = int(input())
    units = GetUnits(count)
    print(units)
    table, answer = MakeDynamicTable(units)
    print(answer)
