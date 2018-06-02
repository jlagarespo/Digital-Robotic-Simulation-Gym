import numpy as np

class ProblemMap():
    def __init__(self):
        #Init stuff
        print("init map")
        self.w = None
        self.h = None

        self.map = None
    
    def setMapSize(self, w, h):
        '''
        Generate a zero map with of size w, h.
        We fill the borders with ones.
        '''

        self.w = w
        self.h = h

        # set a full map
        self.map = np.ones((w, h))
        # fill interior with zeros
        self.map[1:w - 1, 1:h - 1] = 0
        # print(self.map.shape)

    def setObstacle(self, x, y, w, h):
        self.map[int(x):int(x + w), int(y):int(y + h)] = 1

    def getMap(self, x, y, w, h):
        return self.map[int(x):int(x + w), int(y):int(y + h)]

    def getSize(self):
        return self.w, self.h