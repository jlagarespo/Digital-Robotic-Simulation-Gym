import numpy as np


class ProblemMap():
    """
    to doc
    """
    def __init__(self):
        # Init stuff
        print("init map")
        self.w = None
        self.h = None

        self.map = None

    def setMapSize(self, w, h):
        """
        Build a map with size w, h
        The map is initialized with zeros. Obtacles and borders
        are filled with ones on the map
        """
        self.w = w
        self.h = h

        # build the map
        self.map = np.ones((w, h)) * 3
        self.map[1:w-1, 1:h-1] = 0

    def setGoal(self, x, y, w, h):
        """
        Goal to reach.
        This element is filled with 2 on the map.
        """
        self.map[int(x):int(x + w), int(y):int(y + h)] = 2

    def setObstacle(self, x, y, w, h):
        self.map[int(x):int(x + w), int(y):int(y + h)] = 1

    def getMap(self, x, y, w, h):
        """
        Return the part of the map seen by the agent's sensory
        system. The reference system is taken from the center of the
        agent
        """
        return self.map[int(x - (w / 2.0)):int(x + (w / 2.0)), int(y):int(y + h)]


    def getSize(self):
        return self.w, self.h

    def evaluate_map(self, x, y, w, h):
        """
        evaluate the current agent position
        Return True if the agent is overlapping one of
        the defined obstacles and False otherwise

        x, y, w and h are the agent coordenates and size,
        respectively.
        """

        return np.sum(self.map[int(x):int(x + w), int(y):int(y + h)] == 1) > 10
