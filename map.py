import numpy as np

class Map():
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.map = np.zeros((w, h))

    def setObstacle(self, x, y):
        self.map[x, y] = 1