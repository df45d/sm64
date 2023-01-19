"""
A class for basic cubes within OH19.
"""

import pygame

from .baseobject import object

# create mesh for 3D cube
class Prism(object):
	def __init__(self, vector: pygame.Vector3, color: tuple, size):
		super().__init__(vector, color)
		self.vertices = [
		[pygame.Vector3(-size[0]/2, -size[1]/2, -size[2]/2),   pygame.Vector3(-size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, -size[2]/2)],
		[pygame.Vector3(-size[0]/2, -size[1]/2, -size[2]/2),   pygame.Vector3(size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(size[0]/2, -size[1]/2, -size[2]/2)],
													
		[pygame.Vector3(size[0]/2, -size[1]/2, -size[2]/2),   pygame.Vector3(size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, size[2]/2)],
		[pygame.Vector3(size[0]/2, -size[1]/2, -size[2]/2),   pygame.Vector3(size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(size[0]/2, -size[1]/2, size[2]/2)],
													
		[pygame.Vector3(size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, size[2]/2)],
		[pygame.Vector3(size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, -size[1]/2, size[2]/2)],
														
		[pygame.Vector3(-size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, -size[2]/2)],
		[pygame.Vector3(-size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(-size[0]/2, -size[1]/2, -size[2]/2)],
													
		[pygame.Vector3(-size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(-size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, size[2]/2)],
		[pygame.Vector3(-size[0]/2, size[1]/2, -size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, size[2]/2),    pygame.Vector3(size[0]/2, size[1]/2, -size[2]/2)],
													
		[pygame.Vector3(size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, -size[1]/2, -size[2]/2)],
		[pygame.Vector3(size[0]/2, -size[1]/2, size[2]/2),    pygame.Vector3(-size[0]/2, -size[1]/2, -size[2]/2),    pygame.Vector3(size[0]/2, -size[1]/2, -size[2]/2)]]
    
	def __getattr__(self, name: str):
		if name == "max":
			return self.vertices[2][2] + self.position
		elif name == "min":
			return self.vertices[0][0] + self.position