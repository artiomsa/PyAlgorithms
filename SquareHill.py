# Задача о разбмении прямоугольного поля длиной х и шириной у на квадраты максимальных размеров
import time
def GetSquare(x, y):
    if (abs(x - y) == min(x, y)) or (x == y):
        return min(x, y)
    else:
        if max(x, y) - 2 * min(x, y) > 0:
            return GetSquare(max(x, y) - 2 * min(x, y), min(x, y))
        else:
            return GetSquare(max(x, y) - min(x, y), min(x, y))



def GetSquareNod(x, y):
    nod = 0
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0 and i > nod:
            nod = i
    return nod

def init():
    x = int(input())
    y = int(input())
    print(GetSquare(x, y))
    print(GetSquareNod(x, y))