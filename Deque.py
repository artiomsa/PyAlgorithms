class Deque:
    __length = 0
    __data = []

    def __init__(self):
        self.__length = 0
        self.__data = []

    def add(self, key):
        self.__length += 1
        self.__data.append(key)

    def get(self):
        if self.__length != 0:
            res = self.__data.pop(0)
            self.__length -= 1
            return res

    def showdeque(self):
        for i in range(len(self.__data)):
            print(self.__data[i])

    def getLength(self):
        return self.__length