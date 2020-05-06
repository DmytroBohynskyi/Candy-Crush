""" Candy Crush

"""
from __future__ import barry_as_FLUFL

__version__ = '0.1'
__author__ = 'Dmytro Bohynskyi'

import time  # standard libraries
import random
from subprocess import call
from colr import Colr as C  # custom libraries
import numpy as np
import os


class Hexagon:
    """
    This class defines a hexagonal agent.
    """

    TYPE = ['FF0000', '555B6E', '4b88b0', "EAF4F4", "21FC0D", 'F6F786']

    def __init__(self):
        self.type = random.choice(Hexagon.TYPE)

    def delete(self):
        """

        :return:None
        """
        self.type = random.choice(Hexagon.TYPE)


class View:
    __POS = {
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

    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.n = width * height
        self.agents = np.array([Hexagon() for _ in range(self.n)]).reshape(width, height)
        [self.look_for((x, y)) for y in range(height - 1) for x in range(width - 1)]

    def algorithm(self, x_pos, y_pos, pos):
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
            function = View.__POS.get(pos)[y_pos % 2]  # get functions depending on the value [pos] and [y_pos % 2]
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
        position = {p: View.__POS.get(p)[y % 2](x, y, self.width, self.height) for p in position_list}
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


def print_view(view):
    x, y = view.agents.shape
    for y_ in range(y):
        print("\n " if y_ % 2 else "\n", end=" ")
        for x_, agent in enumerate(view.agents[:, y_]):
            if x > x_ + 1 and y > y_ + 1:
                view.look_for((x_, y_))
            print(C().hex(agent.type, "*", rgb_mode=True), end=" ")


if __name__ == '__main__':
    window = View()  # Create new windows
    game = True
    while game:
        print_view(window)
        try:
            x = int(input('\n podaj pozycje x : '))  # user input value of x
            y = int(input('podaj pozycje y : '))  # user input value of x
        except:
            game = False if x == 'end' else True  # if the user input "end" then finish the loops
        else:
            p = input('Gdzie: ')  # user input direction of shift
            window.algorithm(x - 1, y - 1, p)  # shifting algorithm
            os.system('cls')  # clear terminal
