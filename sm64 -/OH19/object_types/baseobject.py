"""
A base class for object creation within OH19.
"""
import pygame

class object:
    def __init__(self, position: pygame.Vector3, color: tuple):
        self.position = position
        self.color = color
        self.rot_x, self.rot_y = 0, 0
    
    def change_center(self, vector: pygame.Vector3):
        for triangle in range(len(self.vertices)):
            for vertex in range(3):
                self.vertices[triangle][vertex] += vector
                
    def transform(self, vector: pygame.Vector3) -> None:
        vec = vector
        vec.rotate_y_ip(self.rotY)
        self.position += vec

    def rotate_y(self, angle: float) -> None:
        self.rot_y += angle
        for triangle in range(len(self.vertices)):
            for vertex in range(3):
                self.vertices[triangle][vertex].rotate_y_ip(angle)
    
    def scale(self, scale: pygame.Vector3) -> None:
        for triangle in range(len(self.vertices)):
            for vertex in range(3):
                self.vertices[triangle][vertex].x *= scale[0]
                self.vertices[triangle][vertex].y *= scale[1]
                self.vertices[triangle][vertex].z *= scale[2]
                

    