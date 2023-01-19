"""
A class made to move within a scene with a camera.
"""

import pygame
import math
class Camera:
    def __init__(self, position: pygame.Vector3):
        self.position = position # camera position
        self.rot_y = 0  # camera rotation
        self.rot_x = 0
        self.direction = pygame.Vector3(0, 0, 1)

    def transform_z(self, amount: float):
        increment = pygame.math.Vector3(0, 0, amount)
        increment.rotate_y_ip(-self.rot_y)
        self.position += increment

    def transform_x(self, amount: float):
        increment = pygame.math.Vector3(amount, 0, 0)
        increment.rotate_y_ip(-self.rot_y)
        self.position += increment

    def transform_y(self, amount: float):
        self.position.y += amount

    def rotate_y(self, amount: float):
        self.rot_y -= amount
        self.rot_y = self.rot_y % 360
        self.direction.rotate_y_ip(amount)

    def rotate_x(self, amount: float):
        self.rot_x -= amount
        self.rot_x = self.rot_x % 360
        
    def set_direction(self):
        sphere = pygame.Vector3(self.direction.x, self.direction.y, self.direction.z)
        self.rot_x = math.degrees(math.tanh(sphere.y/sphere.z))

        
        self.rot_y = -math.degrees(math.atan(sphere.x/sphere.z))
        print(sphere)

