"""
A class that allows for objects to be derived from .obj files.
"""

from pygame import Vector3

from .baseobject import *

class BlenderObject(object):
    def __init__(self, position, color, file, hitbox):
        super().__init__(position, color)
        self.vertices = self.open(file)
        self.hitbox = hitbox # min, max
    
    def __getattr__(self, name: str):
        if name == "max":
            return self.hitbox[1] + self.position
        elif name == "min":
            return self.hitbox[0] + self.position

    def open(self, ifile):
        # open file efficiently 
        with open(ifile) as file:
            lines = file.read().splitlines()
        
        # change the file into a multidemonsional list
        plist = []
        for item in lines:
            string = item.replace("/", ",")
            string = string.replace(" ",",")
            plist.append(string.split(","))
            
        vertices = []
        faces = []
        for item in plist:
            if item[0] == "v":
                vertices.append((float(item[1]), float(item[2]), float(item[3])))
            elif item[0] == "f":
                faces.append((int(item[1]), int(item[4]), int(item[7])))
            
        # print(vertices, faces)
        
        returnlist = []
        for item in faces:
            returnlist.append([
                Vector3(vertices[item[0] - 1]),
                Vector3(vertices[item[1] - 1]),
                Vector3(vertices[item[2] - 1])
                ])
        
        return returnlist
    
        