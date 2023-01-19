"""
A module for implementing physics within OH19.
//Fix up slow collisions
"""

import pygame

def AABB_collision(box1, box2):
    var = (box1.min.x <= box2.max.x and box1.max.x >= box2.min.x) and \
          (box1.min.y <= box2.max.y and box1.max.y >= box2.min.y) and \
          (box1.min.z <= box2.max.z and box1.max.z >= box2.min.z)
    return var

def group_collision(box, group):
      for item in group:
            if AABB_collision(box, item): return True
      return False
            
            
            
def rigidbody_collision(box1, box2, vector):
      touched = [False, False, False]
      for i in range(int(abs(vector.x/0.001))):
            if group_collision(box1, box2):
                  box1.position.x -= 0.001 * vector.x/abs(vector.x)
                  touched[0] = True
                  break
            box1.position.x += 0.001 * vector.x/abs(vector.x)
      
      for i in range(int(abs(vector.y/0.001))):
            if group_collision(box1, box2):
                  box1.position.y -= 0.001 * vector.y/abs(vector.y)
                  touched[1] = True
                  break
            box1.position.y += 0.001 * vector.y/abs(vector.y)
            
      for i in range(int(abs(vector.z/0.001))):
            if group_collision(box1, box2):
                  box1.position.z -= 0.001 * vector.z/abs(vector.z)
                  touched[2] = True
                  break
            box1.position.z += 0.001 * vector.z/abs(vector.z)
      
      return touched
            
            
