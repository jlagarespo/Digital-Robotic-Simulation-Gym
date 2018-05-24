import numpy as np

class ProblemMap():
    def __init__(self):
        #Init stuff
        print("init map")

    def setMapSize(self, w, h):
        self.w = w
        self.h = h
    
        self.map = np.zeros(self.w, self.h)

    def setObstacle(self, x, y):
        self.map[x, y] = 1