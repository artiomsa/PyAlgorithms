class HashTable:
    __data = dict()

    def __init__(self):
        self.__data = dict()

    def add(self, key, value):
        self.__data[key] = value

    def print(self):
        print(self.__data)