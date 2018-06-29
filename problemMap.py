import numpy as np

class ProblemMap():
    """
    Class Map

    The abstract map what determines where is what. Using a
    fragment of it as agent eyes.
    """

    def __init__(self):
        # Init stuff
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
        self.map = np.ones((h, w))
        # fill interior with zeros
        self.map[5:h - 5, 5:w - 5] = 0
        # print(self.map.shape)

        self.goal_id = 5

    def setObstacle(self, x, y, w, h):
        """
        Sets obstacle location in the map
        """
        self.map[int(y):int(y + h), int(x):int(x + w)] = 1

    def setGoal(self, x, y, w, h):
        """
        Sets obstacle location in the map
        """
        self.map[int(y):int(y + h), int(x):int(x + w)] = self.goal_id

    def getMap(self, x, y, w, h):
        """
        Return the part of the map seen by the agent's sensory
        system. The reference system is taken from the center of the
        agent
        """
        return self.map[int(x):int(x + h), int(y):int(y + w)]

    def getSize(self):
        return self.w, self.h

    def evaluate_map(self, x, y, w, h, min_res):
        """
        evaluate the current agent position
        Return True if the agent is overlapping one of
        the defined obstacles and False otherwise

        x, y, w and h are the agent coordenates (center of masses)
        and size, respectively.
        """

        next_map = np.sum(self.map[int(x - h/2):int(x + h/2),
                               int(y - w/2):int(y + w/2)] == 1)
    
        return next_map > min_res

    def evaluate_goal(self, x, y, w, h):
        """
        !!to doc
        """

        next_map = self.map[int(x - h/2):int(x + h/2),
                               int(y - w/2):int(y + w/2)]

        
        print(next_map)
    
        return self.goal_id in next_map
