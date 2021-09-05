class Examples:
    #arrays of ANGLES!!!!!
    one = [[0,"e",0,0],["e",0,"e",0],[0,"e",0,"e"],[0,0,"e",0]]
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []


class Digit:
    dots = []
    vectors = []
    angles = []
    count = 2

    def __makeVector(self):
        for i in range(self.count):
            x = - self.dots[i][0][0] + self.dots[i][1][0]
            y = - self.dots[i][0][1] + self.dots[i][1][1]
            z = - self.dots[i][0][2] + self.dots[i][1][2]
            self.vectors.append([x,y,z])
        print(self.vectors)

    def __init__(self):
        print('Enter dots coordinates')
        for i in range(self.count):
            self.dots.append([])
            for j in range(2):
                self.dots[i].append([])
                for k in range(3):
                    print('For vector', i + 1,'for dot', j + 1,'1-x 2-y 3-z')
                    kdot = int(input())
                    self.dots[i][j].append(kdot)
        print(self.dots)
        self.__makeVector()

#def GetAngles(digit1, digit2):

