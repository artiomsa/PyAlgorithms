class LinkedList:
    head = None
    length = 0

    class Node:
        value = None
        nodeNext = None

        def __init__(self, value):
            self.value = value
            self.nodeNext = None

    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        if self.head:
            node = self.head
            while node.nodeNext:
                node = node.nodeNext
            node.nodeNext = self.Node(value)
            self.length += 1
        else:
            self.head = self.Node(value)
            self.length += 1

    def print(self):
        if self.length != 0:
            node = self.head
            while node:
                print(node.value)
                node = node.nodeNext
