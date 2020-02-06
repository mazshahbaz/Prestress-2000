# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:29:18 2020

@author: Mazen
"""
import tkinter as tk
import p2k_model as Model
import p2k_view as v
   

class Controller(tk.Tk):
    def __init__(self):
        self.model = Model.Model()
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "PreStress-2000")
        root = tk.Frame(self)                                                    #This is the mainframe where everything goes
        root.grid(row=0, column=0) 
        
        #Initalize Pages
        self.frames = {}                                                         #Dictionary to contain all the frame created in our GUI, Each page is a frame
        for F in (v.StartPage, v.PageOne, v.PageTwo):
            frame = F(parent=root, controller=self)                              #Creating the Start Page
            self.frames[F] = frame                                               #Placing frames in the frames dictionary
            frame.grid(row=1, column=0, sticky="nsew")
        
        ##Initalize Navigation Bar
        self.navbar = v.NavigationBar(parent=root, controller=self)
        self.navbar.grid(row=0, column=0, sticky="NSEW")
            
        self.show_frame(self.frames, v.StartPage)                                             #Displaying the startpage
        
    def show_frame(self, frames, F):
        """
        bring the desired frame (F) to the front
        """
        frame = frames[F]
        frame.tkraise()
        
    def show_material_input_frame(self, frames, F):
        """
        bring the desired frame (F) to the front
        """
        frame = frames[F]
        frame.tkraise()
    
    def get_material_types(self):
        return self.model.materials_types.data
    
    def get_materials_dic(self):
        return self.model.materials.data
    
    def get_sections_dic(self):
        return self.model.sections.data
        
        

class Observable:
    """
    
    """
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}
        
    def addCallback(self, func):
        self.callback[func]
        
    def delCallback(self, func):
        del self.callback[func]
        
    def doCallbacks(self):
        for func in self.callbacks:
            func(self.data)
            
    def update(self, data):
        self.data = data
        self.doCallbacks()
        




if __name__ == "__main__":
    app=Controller()
    app.mainloop()