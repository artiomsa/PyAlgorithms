from HashTable import *


def GetGraph(sizeOfPeak):
    dictionary = dict()
    for i in range(sizeOfPeak):
        values = []
        print("For", i + 1, "peak:")
        for j in range(sizeOfPeak):
            if j != i:
                print("to", j + 1, "?   y/n")
                hotkey = input()
                if hotkey == "y":
                    values.append(j+1)
        dictionary[i+1] = values
    return dictionary

