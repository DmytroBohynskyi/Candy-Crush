""" Candy Crush

"""
from __future__ import barry_as_FLUFL

__version__ = '0.2'
__author__ = 'Dmytro Bohynskyi'

import random  # standard libraries
import os
from colr import Colr as C  # custom libraries
import numpy as np

# Static variables
POS = {
    "q": (lambda x, y, w, h: (x - 1, y - 1) if x > 0 and y > 0 else None,
          lambda x, y, w, h: (x, y - 1) if x >= 0 and y > 0 else None),

    "z": (lambda x, y, w, h: (x - 1, y + 1) if x >= 0 and y < h else None,
          lambda x, y, w, h: (x, y + 1) if x > 0 and y < h else None),

    "e": (lambda x, y, w, h: (x, y - 1) if x <= w and y > 0 else None,
          lambda x, y, w, h: (x + 1, y - 1) if x < w and y > 0 else None),

    "c": (lambda x, y, w, h: (x, y + 1) if x <= w and y < h else None,
          lambda x, y, w, h: (x + 1, y + 1) if x < w and y <= h else None),

    "d": (lambda x, y, w, h: (x + 1, y) if x < w else None,
          lambda x, y, w, h: (x + 1, y) if x < w else None),

    "a": (lambda x, y, w, h: (x - 1, y) if x > 0 else None,
          lambda x, y, w, h: (x - 1, y) if x > 0 else None)
}


class Hexagon:
    """
    This class defines a hexagonal agent.
    """
    TYPE = ['FF0000', '00FF00', '0000FF', "00FFFF", "FAEBD7", 'F6F786']

    def __init__(self):
        self.type = random.choice(Hexagon.TYPE)

    def delete(self):
        """

        :return:None
        """
        self.type = random.choice(Hexagon.TYPE)


class View:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.n = width * height
        self.agents = np.array([Hexagon() for _ in range(self.n)]).reshape(width, height)
        [self.look_for((x, y)) for y in range(height - 1) for x in range(width - 1)]

    def algorithm(self, x_y_pos, pos):
        """
        This function changes the agent's position
        :param x_y_pos: x position  is equal to [0 : width - 1]
                     y position  is equal to [0 : height - 1]
        :param pos: q  //\\  e
                    a ||  || d ->
                    z  \\//  c
        :return: None
        """
        try:
            x_pos, y_pos = x_y_pos
            function = POS.get(pos)[y_pos % 2]  # get functions depending on the value [pos] and [y_pos % 2]
            next_pos = function(x_pos, y_pos, self.width, self.height)
            if next_pos:
                self.agents[x_pos, y_pos], self.agents[next_pos] = self.agents[next_pos], self.agents[x_pos, y_pos]
        except TypeError:
            print("Nieznany kierunek!")

    def look_for(self, actual):
        """

        :param actual: actual position
        :return: None
        """
        x, y = actual
        # adjacent positions
        position_list = ['q', 'a', 'z', 'e', 'd', 'c', ]

        # Create dict with adjacent positions
        position = {p: POS.get(p)[y % 2](x, y, self.width, self.height) for p in position_list}
        # Create dict with adjacent positions (object)
        position = {p: self.agents[position[p]] for p in position if position[p]}
        # Create dict with adjacent positions (object type)
        position_type = {p: position[p].type for p in position if position[p]}

        actual = self.agents[actual]  # this is main object

        # if they are equal then delete
        if actual.type == position_type.get('a', None) == position_type.get('d', None):
            self.del_object(actual, position['a'], position['d'])
        elif actual.type == position_type.get('e', None) == position_type.get('z', None):
            self.del_object(actual, position['e'], position['z'])
        elif actual.type == position_type.get('q', None) == position_type.get('c', None):
            self.del_object(actual, position['q'], position['c'])

    @staticmethod
    def del_object(one, two, three):
        """
        Thia function delete agents
        :param one: main agent
        :param two: agent
        :param three: agent
        :return: None
        """
        one.delete()
        two.delete()
        three.delete()


class User:
    def __init__(self, act=True):
        self.position = (1, 1)
        self.act = act

    def algorithm(self, pos):
        """
        This function changes the agent's position
        :param x_pos: x position  is equal to [0 : width - 1]
        :param y_pos: y position  is equal to [0 : height - 1]
        :param pos: q  //\\  e
                    a ||  || d ->
                    z  \\//  c
        :return: None
        """
        try:
            x_pos, y_pos = self.position
            function = POS.get(pos)[y_pos % 2]  # get functions depending on the value [pos] and [y_pos % 2]
            position = function(x_pos, y_pos, 20, 15)
        except TypeError:
            print("Nieznany kierunek!")
        finally:
            self.position = position

    def __bool__(self):
        return self.act

    def __eq__(self, other):
        return True if self.position == other else False
