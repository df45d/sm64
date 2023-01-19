"""
A class for creating an axis aligned plane.
"""

import pygame

from .baseobject import object

class Plane(object):
    def __init__(self, vector: pygame.Vector3, size: float, color: tuple):
        super().__init__(vector, color)
        self.vertices = [
            pygame.math.Vector3(0, 0, 0),
            pygame.math.Vector3(size, 0, 0),
            pygame.math.Vector3(size, 0, size),
            pygame.math.Vector3(0, 0, 0),
            pygame.math.Vector3(0, 0, size),
            pygame.math.Vector3(size, 0, size),
        ]

