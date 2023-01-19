"""
A basic scene required for all OH19 projects.
"""

import math, pygame

class Screen:
    def __init__(self, dimensions: tuple):
        self.WIDTH = dimensions[0]
        self.HEIGHT = dimensions[1]
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.FOV = 60
        self.distance = ((self.WIDTH / 2) / math.tan(
            (self.FOV / 2) * (math.pi / 180)
        ), (self.HEIGHT / 2) / math.tan(
            (self.FOV / 2) * (math.pi / 180)
        ))
        

    def fill(self, r, g, b):
        self.screen.fill((r, g, b))

    def change_fov(self, new):
        self.FOV = new
        self.distance = ((self.WIDTH / 2) / math.tan(
            (self.FOV / 2) * (math.pi / 180)
        ), (self.HEIGHT / 2) / math.tan(
            (self.FOV / 2) * (math.pi / 180)
        ))
        