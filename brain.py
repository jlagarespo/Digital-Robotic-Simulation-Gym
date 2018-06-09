from agent import Agent
import numpy as np


class Brain(Agent):
    """
    Class Brain

    The Brain class inherits the Agent class. We use it to implement
    our navigation algorithms. See agent.py to see the available methods.

    """

    def __init__(self, w, h, step):
        Agent.__init__(self, w, h, step)
        self.prev_orientation = np.random.randint(1, 8)

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
        dir = ["NW", "NN", "NE", "WW", "EE", "SW", "SS", "SE"]

        if np.sum(sensor_data) == 0:
            next_orientation = self.prev_orientation
            step = 5
        else:
            max_loss = self.get_orientation_loss(sensor_data)
            next_orientation = self.get_next_orientation(max_loss)
            print('ORIENT:', next_orientation)
            print("obstacle direction", dir[next_orientation-1])
            self.prev_orientation = next_orientation
            step = 30

        # move the agent
        self.move_agent(next_orientation, step)

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

        sensor_mask[0:x_int, 0:y_int] = 1  # NW
        sensor_mask[x_int:x_int*2, 0:y_int] = 2  # NN
        sensor_mask[x_int*2:x_int*3, 0:y_int] = 3  # NE
        sensor_mask[0:x_int, y_int:y_int*2] = 4  # WW
        sensor_mask[0:x_int, y_int*2:y_int*3] = 6  # SW
        sensor_mask[x_int:x_int*2, y_int*2:y_int*3] = 7  # EE
        sensor_mask[x_int*2:x_int*3, y_int*2:y_int*3] = 8  # SE

        # compute loss for each direction (I'm using a list comprenhension
        # instead of a for loop)
        losses = np.array([np.sum(sensor_map * (sensor_mask == i))
                           for i in range(1, 9)])
        max_loss = np.where(losses == np.max(losses))[0]
        print(losses, max_loss)

        # only 1,2 or 3 directions can be detected at the same time
        # given the kind of sensor and the orientations employed.
        # if 2, 3 directions are detected, return the central one
        orientation = max_loss if len(max_loss) == 1 else max_loss[1]
        return orientation + 1

    def get_next_orientation(self, max_loss_direction):
        """
        return the opposite direction
        """

        return abs(max_loss_direction - 8) + 1

    def move_agent(self, orientation, step):
        """
        Move the agent taking into account each of the 8 possible
        positions

        """
        if orientation == 1:
            self.moveUp(step)
            self.moveLeft(step)
        if orientation == 2:
            self.moveUp(step)
        if orientation == 3:
            self.moveUp(step)
            self.moveRight(step)
        if orientation == 4:
            self.moveLeft(step)
        if orientation == 5:
            self.moveRight(step)
        if orientation == 6:
            self.moveDown(step)
            self.moveLeft(step)
        if orientation == 7:
            self.moveDown(step)
        if orientation == 8:
            self.moveDown(step)
            self.moveRight(step)
