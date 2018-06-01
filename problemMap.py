import numpy as np

class ProblemMap():
    def __init__(self):
        #Init stuff
        print("init map")
        self.w = None
        self.h = None

        self.map = None

    def setMapSize(self, w, h):
        self.w = w
        self.h = h

        self.map = np.zeros((w, h))
        # print(self.map.shape)

    def setObstacle(self, x, y, w, h):
        self.map[int(x):int(x + w), int(y):int(y + h)] = 1

    def getMap(self, x, y, w, h):
        return self.map[int(x):int(x + w), int(y):int(y + h)]

    def getSize(self):
        return self.w, self.h