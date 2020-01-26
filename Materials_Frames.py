# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:04:51 2020

@author: Mazen
"""

import tkinter as tk
from Fonts import LARGE_FONT as LARGE_FONT
from Fonts import MEDIUM_FONT as MEDIUM_FONT
from Fonts import SMALL_FONT as SMALL_FONT






#def add_concrete_material(controller, parent, name, fc, fu, Ec, eu):
#    if name in parent.materials_dictionary:
#        return
#    else:
#        parent.materials_dictionary[name] = Concrete_Material(name, fc, Ec, eu)
#        parent.Lb.insert(tk.END, name)
#        controller.frames[PageTwo].update_material_dropdown()                             #Updates the dropdown menu on PgaeTwo
#        
#def add_steel_material(controller, parent, name, fy, fu, Es, ey, eu):
#    if name in parent.materials_dictionary:
#        return
#    else:
#        parent.materials_dictionary[name] = Steel_Material(name, fy, fu, Es, ey, eu)
#        parent.Lb.insert(tk.END, name)
#        controller.frames[PageTwo].update_material_dropdown()                           #Updates the dropdown menu on PgaeTwo


class ConcreteMaterialInputs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
    
        material_label = tk.Label(self, text="Concrete Material Input", font=MEDIUM_FONT)
        material_label.grid(row=0, column=0)
    
        material_name = tk.Label(self, text="Concrete Material Name:", font=MEDIUM_FONT)
        material_name.grid(row=1, column=0)
        material_name_entry = tk.Entry(self)
        material_name_entry.grid(row=1, column=1)
    
    
        fc_label = tk.Label(self, text="f'c (MPa):", font=MEDIUM_FONT)
        fc_label.grid(row=2, column=0)
        fc_entry = tk.Entry(self)
        fc_entry.grid(row=2, column=1)
    
    
        fu_label = tk.Label(self, text="f'u: (MPa)", font=MEDIUM_FONT)
        fu_label.grid(row=3, column=0)
        fu_entry = tk.Entry(self)
        fu_entry.grid(row=3, column=1)
        
        
        Ec_label = tk.Label(self, text="Ec: (MPa)", font=MEDIUM_FONT)
        Ec_label.grid(row=4, column=0)
        Ec_entry = tk.Entry(self)
        Ec_entry.grid(row=4, column=1)
        
        eu_label = tk.Label(self, text="e'u:", font=MEDIUM_FONT)
        eu_label.grid(row=5, column=0)
        eu_entry = tk.Entry(self)
        eu_entry.grid(row=5, column=1)
        
        add_material_button = tk.Button(self, text="Add Material", 
                                command=lambda: parent.add_concrete_material(material_name_entry.get(), fc_entry.get(), fu_entry.get(), Ec_entry.get(), eu_entry.get()))
        add_material_button.grid(row=6, column=0)



class SteelMaterialInputs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
    
        material_label = tk.Label(self, text="Steel Material Input", font=MEDIUM_FONT)
        material_label.grid(row=0, column=0)
    
        material_name = tk.Label(self, text="Steel Material Name:", font=MEDIUM_FONT)
        material_name.grid(row=1, column=0)
        material_name_entry = tk.Entry(self)
        material_name_entry.grid(row=1, column=1)
    
    
        fy_label = tk.Label(self, text="fy: (MPa)", font=MEDIUM_FONT)
        fy_label.grid(row=2, column=0)
        fy_entry = tk.Entry(self)
        fy_entry.grid(row=2, column=1)
    
    
        fu_label = tk.Label(self, text="fu: (MPa)", font=MEDIUM_FONT)
        fu_label.grid(row=3, column=0)
        fu_entry = tk.Entry(self)
        fu_entry.grid(row=3, column=1)
        
        
        Es_label = tk.Label(self, text="Es: (MPa)", font=MEDIUM_FONT)
        Es_label.grid(row=4, column=0)
        Es_entry = tk.Entry(self)
        Es_entry.grid(row=4, column=1)
        
        ey_label = tk.Label(self, text="e'y:", font=MEDIUM_FONT)
        ey_label.grid(row=5, column=0)
        ey_entry = tk.Entry(self)
        ey_entry.grid(row=5, column=1)
        
        eu_label = tk.Label(self, text="e'u:", font=MEDIUM_FONT)
        eu_label.grid(row=6, column=0)
        eu_entry = tk.Entry(self)
        eu_entry.grid(row=6, column=1)
        
        add_material_button = tk.Button(self, text="Add Material", 
                                command=lambda: parent.add_steel_material(material_name_entry.get(), fy_entry.get(), fu_entry.get(), Es_entry.get(), ey_entry.get() ,eu_entry.get()))
        add_material_button.grid(row=7, column=0)      
        
        
        
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