import numpy as np

class ProblemMap():
    def __init__(self):
        #Init stuff
        print("init map")

    def setMapSize(self, w, h):
        self.w = w
        self.h = h

        self.map = np.zeros((w, h))

    def setObstacle(self, x, y, w, h):
        self.map[int(x), int(y)] = 1

    def getMap(self, x, y):
        return self.map[int(x), int(y)]