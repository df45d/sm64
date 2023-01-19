"""
A module for rendering objects to screens. Still in Beta.
"""

import pygame
from .functions import *
from .camera import Camera
from .scene import Screen

    
def alpha_triangle(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)


def shader1(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker):

        triangle_midpoint = midpoints[midpoint_tracker][0]

        
        normal = find_normal(triangle)
        
        normal.scale_to_length(0.4)
        if (normal.dot(triangle_midpoint + obj.position - camera.position) < 0.0):
            
            if on_screen(pointlist):                
                # triangle
                pygame.draw.polygon(scene.screen, obj.color, (pointlist))
                pygame.draw.polygon(scene.screen, (0, 0, 0), (pointlist), 2)
                
                #pygame.draw.line(scene.screen, (255, 0, 0), project(
                #    rotate_round_point(triangle_midpoint + obj.position, camera), scene), 
                #project(rotate_round_point(normal + triangle_midpoint + obj.position, camera), scene), 2)
                
                
                
def shader2(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker):
        if on_screen(pointlist):                
            # triangle
            alpha_triangle(scene.screen, obj.color, (pointlist))

            pygame.draw.polygon(scene.screen, obj.color, (pointlist), 2)
                
        



def render_object(obj, camera: Camera, scene: Screen, shader=1):
    
    midpoints = [((
        (obj.vertices[triangle][0] + obj.vertices[triangle][1] + obj.vertices[triangle][2]) / 3), triangle )
                 for triangle in range(len(obj.vertices))]

    midpoints.sort(key=lambda x: rotate_round_point(x[0], camera).z, reverse=True)
    vertices = []
    
    for item in range(len(obj.vertices)):
        vertices.append(obj.vertices[midpoints[item][1]])
    
    midpoint_tracker = 0
    for triangle in vertices:
        pointlist = []
        render = 0
        for vertex in triangle:
            point = rotate_round_point(vertex + obj.position, camera)
            
            if point.z < 1:
                point.z = 1
                render += 1
            vector = project(point, scene)
            pointlist.append((vector[0], vector[1]))
        if render < len(triangle):
            if shader == 1:
                shader1(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker)
            elif shader == 2:
                shader2(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker)
                
        midpoint_tracker += 1
        
def render_all(objects, camera: Camera, scene: Screen, shader=1):
    
    midpoints = []
    for object in objects:    
        j_midpoints = [((
            (object.vertices[triangle][0] + object.vertices[triangle][1] + object.vertices[triangle][2]) / 3), 
                        triangle, object)
                 for triangle in range(len(object.vertices))]
        midpoints = midpoints + j_midpoints
    

    midpoints.sort(key=lambda x: camera.position.distance_to(x[0] + x[2].position), reverse=True)
    vertices = []
    
    for item in range(len(midpoints)):
        vertices.append((midpoints[item][2].vertices[midpoints[item][1]], midpoints[item][2]))
    
    midpoint_tracker = 0
    for tri in vertices:
        obj = tri[1]
        triangle = tri[0]
        pointlist = []
        render = 0
        for vertex in triangle:
            point = rotate_round_point(vertex + obj.position, camera)
                
            if point.z <= 0:
                render += 1


            pointlist.append(point)

        if render < 3:
            for item in range(len(pointlist)):
                if pointlist[item].z <= 1:
                    pointlist[item].z = 1
        
        
        if render < 3:
            for item in range(len(pointlist)):
                pointlist[item] = project(pointlist[item], scene)
                
            if shader == 1:
                shader1(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker)
            elif shader == 2:
                shader2(obj, camera, scene, pointlist, triangle, midpoints, midpoint_tracker)
                
        midpoint_tracker += 1     
        
        
        
    
    
