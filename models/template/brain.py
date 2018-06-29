from agent import Agent
import numpy as np
import pygame

class Brain(Agent):
    """
    Class Brain

    The Brain class inherits the Agent class. We use it to implement
    our navigation algorithms. See agent.py to see the available methods.
    """

    def __init__(self, w, h, step):
        Agent.__init__(self, w, h, step)

    # *********************************************************
    # Behaviour controller  
    # *********************************************************

    def nextState(self, speed):
        # NEXT STATE
        pass