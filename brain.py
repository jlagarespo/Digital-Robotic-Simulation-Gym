from agent import Agent
import numpy as np
import random as rand

class Brain(Agent):
    """
    Class Brain

    The Brain class inherits the Agent class. We use it to implement
    our navigation algorithms. See agent.py to see the available methods.

    """
    
    def __init__(self, w, h, step):
        Agent.__init__(self, w, h, step)
        np.set_printoptions(threshold=np.nan)
        self.prev_orientation = 2

    # *********************************************************
    # Behaviour controller
    # *********************************************************

    def nextState(self):
        """
        Here is where magic happens

        sensorMap has the available information about the enviroment.
        The agent will move using the available methods: moveDown, moveUp,
        moveLeft, moveRight
        """

        sensor_data = self.sensorMap
        step = 2

        if np.sum(sensor_data) == 0:
            orientation = self.prev_orientation
            step = 5
        else:
            orientation = self.get_orientation_loss(sensor_data)
            print("BEST OR", orientation)
            self.prev_orientation = orientation
            step = 30

        if orientation == 1:
            self.moveDown(step)
            self.moveRight(step)
        if orientation == 2:
            self.moveDown(step)
        if orientation == 3:
            self.moveDown(step)
            self.moveLeft(step)
        if orientation == 4:
            self.moveRight(step)
        if orientation == 5:
            self.moveLeft(step)
        if orientation == 6:
            self.moveUp(step)
            self.moveRight(step)
        if orientation == 7:
            self.moveUp(step)
        if orientation == 8:
            self.moveUp(step)
            self.moveLeft(step)
        
    def get_orientation_loss(self, sensor_map):
        """
        We get the best orientation by calculating the number of elements
        on each of the possible 8 directions. We assume the sensor shape is
        a square :(
 
        NW NN NE
        WW AG EE
        SW SS SE

        We generate a mask with the following values, which be translated
        as the best orientation to follow:

        NW = 1, NN = 2, NE = 3, WW = 4, EE = 5, SW = 6
        SS = 7 and SE = 8

        """

        # build the orientation mask:
        # IMPORTANT NOTE: this should be built into a separated method and
        # only be called once :)
        sensor_mask = np.zeros_like(sensor_map)

        x_size = sensor_mask.shape[0]
        y_size = sensor_mask.shape[1]
        
        x_int = int(x_size / 3)
        y_int = int(y_size / 3)

        dir = ["NW", "NN", "NE", "WW", "EE", "SW", "SS", "SE"]

        sensor_mask[0:x_int, 0:y_int] = 1
        sensor_mask[0:x_int, y_int:y_int*2] = 2
        sensor_mask[0:x_int, y_int*2:y_int*3] = 3
        sensor_mask[x_int:x_int*2, 0:y_int] = 4
        sensor_mask[x_int:x_int*2, y_int*2:y_int*3] = 5
        sensor_mask[x_int*2:x_int*3, 0:y_int] = 6
        sensor_mask[x_int*2:x_int*3, y_int:y_int*2] = 7
        sensor_mask[x_int*2:x_int*3, y_int*2:y_int*3] = 8

        # check the best orientation
        # here us the center of the brain
        # here is where you check what is your best possible direction to continue
        # do changes here
        print(sensor_mask)
        print(sensor_map)
        max_loss = 0
        max_loss_orientation = 0
        for i in range(1, 9):
            loss = np.sum(sensor_map * (sensor_mask == i))
            if loss > max_loss:
                max_loss_orientation = i
                max_loss = loss
            print(dir[i - 1], loss)


        print(max_loss_orientation)
        print(max_loss)
        # return the value
        return max_loss_orientation
        
#END#