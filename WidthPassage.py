from HashTable import *
from Deque import *
def WidthPassage(dictionary):
    frm = int(input())
    to = int(input())
    res = 0
    deque = Deque()
    for i in dictionary.keys():
        if i != frm:
            deque.add(i)
    deque.showdeque()
    if frm in dictionary and to in dictionary:
        while deque.getLength() > 0:
            res += 1
            temp = deque.get()
            if temp == to:
                return res
            else:
                if dictionary.get(temp):
                    for i in dictionary.get(temp):
                        deque.add(i)







