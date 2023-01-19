"""
A module for various mathmatical calculations.
"""

import pygame
from .scene import Screen
from .camera import Camera

def rect_collision(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h) -> bool:
    return (r1x + r1w >= r2x and 
           r1x <= r2x + r2w and 
           r1y + r1h >= r2y and 
           r1y <= r2y + r2h)


def on_screen(tri: tuple[pygame.Vector3]):
    x_list = sorted([tri[0][0], tri[1][0], tri[2][0]])
    y_list = sorted([tri[0][1], tri[1][1], tri[2][1]])
    
    rect = (x_list[0], y_list[0], x_list[2]-x_list[0], y_list[2]-y_list[0])
    return rect_collision(rect[0], rect[1], rect[2], rect[3], 0 , 0, 800, 600)


def conv_cartesian(x: float, y: float, screen: pygame.Surface) -> tuple:
    X = (screen[0] / 2) + x
    Y = (screen[1] / 2) - y
    return (X, Y)


def projectaroundpoint(vector, scene: Screen) -> tuple:
    X = (vector.x) * (scene.distance[0] / (vector.z + 0.0001))
    Y = (vector.y) * (scene.distance[0] / (vector.z + 0.0001))
    return conv_cartesian(X, Y, (scene.WIDTH, scene.HEIGHT))


def project(vector, scene: Screen) -> tuple:
    return projectaroundpoint(vector, scene)


def rotate_round_point(vector, camera: Camera) -> pygame.Vector3:
    vector = vector - camera.position
    vector.rotate_y_ip(camera.rot_y)
    vector.rotate_x_ip(camera.rot_x)
    return vector


def find_normal(triangle: tuple[pygame.Vector3]) -> pygame.Vector3:
    tri = triangle
                
    line1, line2 = pygame.Vector3(0, 0, 0), pygame.Vector3(0, 0, 0)
    line1.x = tri[1].x - tri[0].x
    line1.y = tri[1].y - tri[0].y
    line1.z = tri[1].z - tri[0].z

    line2.x = tri[2].x - tri[0].x
    line2.y = tri[2].y - tri[0].y
    line2.z = tri[2].z - tri[0].z

    normal = pygame.Vector3(0, 0, 0)
    normal.x = line1.y * line2.z - line1.z * line2.y
    normal.y = line1.z * line2.x - line1.x * line2.z
    normal.z = line1.x * line2.y - line1.y * line2.x
    
    return normal
