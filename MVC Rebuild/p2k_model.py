# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:29:18 2020

@author: Mazen
"""
class Observable:
    """
    The Observable class is used to allow data in the model be accessed by ANY listner. IF the Observable data is modified, all subscribed objects
    will execute their respective callback functions with the new data
    
    
    """
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}
        
    def addCallback(self, func):
        self.callbacks[func] = 1
        
    def delCallback(self, func):
        del self.callbacks[func]
        
    def doCallbacks(self):
        for func in self.callbacks:
            func(self.data)
            
    def addData(self, value):
        if value.name not in self.data.keys():
            self.data[value.name] = value
            self.doCallbacks()
                       

        
class Model():
    def __init__(self):
        self.materials_types = Observable(["Steel", "Concrete"])
        self.materials = Observable({})
        self.sections = Observable({})
        self.girders = Observable({})
        
    def create_material(self, material_type, inputs):
        if material_type == "Concrete":
            material = Concrete_Material(inputs)
        elif material_type == "Steel":
            material = Steel_Material(inputs)
        self.materials.addData(material)
    
    
class materials():
    def __init__(self, master):
        self.materials = {}
        
        

class Concrete_Material():
    def __init__(self,name, fc, fu, Ec, eu):
        self.type = "Concrete"
        self.name = name
        self.fc = fc
        self.fu = fu
        self.Ec = Ec
        self.eu = eu        

class Steel_Material():
    def __init__(self,name, fy, fu, Es, ey, eu):
        self.type = "Steel"
        self.name = name
        self.fy = fy
        self.fu = fu
        self.Es = Es
        self.ey = ey
        self.eu = eu 

#if __name__ == "__main__":
