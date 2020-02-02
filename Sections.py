# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:14:23 2020

@author: Mazen
"""


import tkinter as tk
from Fonts import LARGE_FONT as LARGE_FONT
from Fonts import MEDIUM_FONT as MEDIUM_FONT
from Fonts import SMALL_FONT as SMALL_FONT
from Canvas_Settings import canvas_width
from Canvas_Settings import canvas_height


section_types = ["Rectangle",
                 "AASTHO"]



class RectangleSectionInputs(tk.Frame):
    """
    Need docstring explaiing how this page works and variables
    
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
    
        section_label = tk.Label(self, text="Rectangular Section Input", font=MEDIUM_FONT)
        section_label.grid(row=0, column=0, sticky = "W")
    
        section_name = tk.Label(self, text="Section Name:", font=MEDIUM_FONT)
        section_name.grid(row=1, column=0, sticky = "W")
        self.section_name_entry = tk.Entry(self)
        self.section_name_entry.grid(row=1, column=1)
    
        #Girder Material Selection
        girder_material_label = tk.Label(self, text="Girder Material Selection:", font=MEDIUM_FONT)
        girder_material_label.grid(row=2, column=0, sticky = "W")
        
        self.girder_material = tk.StringVar(self)
        self.girder_material.set("Select")
        self.girder_material_types = self.controller.get_materials_list()
        self.girder_material_om = tk.OptionMenu(self, self.girder_material, self.girder_material_types)         #add material_dropdown to the material dropdown list in the controller
        self.controller.add_material_om(self.girder_material_om, self.girder_material)
        self.girder_material_om.grid(row=2, column=1)
        
        #Deck Material Selection
        deck_material_label = tk.Label(self, text="Deck Material Selection:", font=MEDIUM_FONT)
        deck_material_label.grid(row=3, column=0, sticky = "W")
        
        self.deck_material = tk.StringVar(self)
        self.deck_material.set("Select")
        self.deck_material_types = self.controller.get_materials_list()
        self.deck_material_om = tk.OptionMenu(self, self.deck_material, self.deck_material_types)               #add material_dropdown to the material dropdown list in the controller
        self.controller.add_material_om(self.deck_material_om, self.deck_material)
        self.deck_material_om.grid(row=3, column=1)

    
        self.width_label = tk.Label(self, text="Width: (mm)", font=MEDIUM_FONT)
        self.width_label.grid(row=4, column=0, sticky = "W")
        self.width_entry = tk.Entry(self)
        self.width_entry.grid(row=4, column=1,)

        self.height_label = tk.Label(self, text="Height: (mm)", font=MEDIUM_FONT)
        self.height_label.grid(row=5, column=0, sticky = "W")
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=5, column=1)
        
    def create_section(self):
        name = self.section_name_entry.get()
        girder_material = self.girder_material.get()
        deck_material = self.deck_material.get()
        width = self.width_entry.get()
        height = self.height_entry.get()
        return Rectangle_Section(name, girder_material, deck_material, height, width)
            



class Rectangle_Section():
    def __init__(self, name, girder_material, deck_material, height, width):
        self.type = "Rectangle"
        self.name = name
        self.girder_material = girder_material
        self.deck_material = deck_material
        self.height = int(height)
        self.width = int(width)
    
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.coordinates = self.coordinates()
      
    def coordinates(self):
        center_x = self.canvas_width/2
        center_y = self.canvas_height/2
        
        min_multiplier = 1
        if self.height >= self.canvas_height or self.width >= self.canvas_width:
            height_multiplier = self.height/self.canvas_height
            width_multiplier = self.width/self.canvas_width
            min_multiplier = min(1/(height_multiplier*0.9), 1/(width_multiplier*0.9))
            
        origin_x = center_x - self.width/2 * min_multiplier
        origin_y = center_y - self.height/2 * min_multiplier
        height = self.height*min_multiplier
        width = self.width*min_multiplier
        
        
        p1 = [origin_x, origin_y]
        p2 = [origin_x + width, origin_y]
        p3 = [origin_x + width, origin_y + height]
        p4 = [origin_x, origin_y + height]
        p5 = [origin_x, origin_y]
        
        coordinates = [p1, p2, p3, p4, p5]
        min_multiplier = 1
        
#        if self.height >= self.canvas_height or self.width >= self.canvas_width:
#            height_multiplier = self.height/self.canvas_height
#            width_multiplier = self.width/self.canvas_width
#            min_multiplier = min(1/(height_multiplier*0.9), 1/(width_multiplier*0.9))
#        
#        scaled_coordinates = [[min_multiplier*p for p in coord] for coord in coordinates]
#        print(coordinates)
#        print(scaled_coordinates)
        return coordinates
        
    def section_properties(self):
        return
        
    def assign_reinforcement():
        return
    
    
    
    
class AASHTOSectionInputs(tk.Frame):
    """
    Need docstring explaiing how this page works and variables
    
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
    
        section_label = tk.Label(self, text="AASHTO Section Input", font=MEDIUM_FONT)
        section_label.grid(row=0, column=0, sticky = "W")
    
        section_name = tk.Label(self, text="Section Name:", font=MEDIUM_FONT)
        section_name.grid(row=1, column=0, sticky = "W")
        section_name_entry = tk.Entry(self)
        section_name_entry.grid(row=1, column=1)
    
        #Girder Material Selection
        girder_material_label = tk.Label(self, text="Girder Material Selection:", font=MEDIUM_FONT)
        girder_material_label.grid(row=2, column=0, sticky = "W")
        
        self.girder_material = tk.StringVar(self)
        self.girder_material.set("Select")
        self.girder_material_types = self.controller.get_materials_list()
        self.girder_material_om = tk.OptionMenu(self, self.girder_material, self.girder_material_types)         #add material_dropdown to the material dropdown list in the controller
        self.controller.add_material_om(self.girder_material_om, self.girder_material)
        self.girder_material_om.grid(row=2, column=1)
        
        #Deck Material Selection
        deck_material_label = tk.Label(self, text="Deck Material Selection:", font=MEDIUM_FONT)
        deck_material_label.grid(row=3, column=0, sticky = "W")
        
        self.deck_material = tk.StringVar(self)
        self.deck_material.set("Select")
        self.deck_material_types = self.controller.get_materials_list()
        self.deck_material_om = tk.OptionMenu(self, self.deck_material, self.deck_material_types)               #add material_dropdown to the material dropdown list in the controller
        self.controller.add_material_om(self.deck_material_om, self.deck_material)
        self.deck_material_om.grid(row=3, column=1)

    
        self.width_label = tk.Label(self, text="Width: (mm)", font=MEDIUM_FONT)
        self.width_label.grid(row=4, column=0, sticky = "W")
        self.width_entry = tk.Entry(self)
        self.width_entry.grid(row=4, column=1)

      
        self.height_label = tk.Label(self, text="Width: (mm)", font=MEDIUM_FONT)
        self.height_label.grid(row=5, column=0, sticky = "W")
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=5, column=1)
        
        
class AASHTO_Section():
    def __init__(self, name, girder_material, deck_material, height, width):
        self.type = "AASHTO"
        self.name = name
        self.girder_material = girder_material
        self.deck_material = deck_material
        self.height = height
        self.width = width
    
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        
    def assign_reinforcement():
        return