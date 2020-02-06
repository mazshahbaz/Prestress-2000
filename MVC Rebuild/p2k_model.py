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
        self.callback[func] = 1
        
    def delCallback(self, func):
        del self.callback[func]
        
    def doCallbacks(self):
        for func in self.callbacks:
            func(self.data)
            
    def update(self, data):
        self.data = data
        self.doCallbacks()
                       

        
class Model():
    def __init__(self):
        self.materials_types = Observable(["Steel", "Concrete"])
        self.materials = Observable({})
        self.sections = Observable({})
        self.girders = Observable({})
        return
    
    
class materials():
    def __init__(self, master):
        self.materials_types = []



#if __name__ == "__main__":
