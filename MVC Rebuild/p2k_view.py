# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:29:18 2020

@author: Mazen
"""
import tkinter as tk
import Fonts


class NavigationBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Home_button = tk.Button(self, text="Home", 
                                command=lambda: controller.show_frame(self.controller.frames, StartPage))
        Home_button.grid(row=0, column=0)
        
        materials_button = tk.Button(self, text="Materials", 
                                command=lambda: controller.show_frame(self.controller.frames, PageOne))
        materials_button.grid(row=0, column=1)
        
        xsection_button = tk.Button(self, text="Cross Section", 
                                command=lambda: controller.show_frame(self.controller.frames, PageTwo))
        xsection_button.grid(row=0, column=2)
        
        graph_button = tk.Button(self, text="Graph", 
                                command=lambda: controller.show_frame(self.controller.frames, PageThree))
        graph_button.grid(row=0, column=3)
        
  

      
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Page One", font=Fonts.LARGE_FONT)
        label.grid(row=1, column=0)



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Materials Page", font=Fonts.LARGE_FONT)
        label.grid(row=1, column=0, sticky="W")
        
        #Materials inputs Frames
        self.input_frames = {}
        for F in [ConcreteMaterialInput, SteelMaterialInput]:
            frame = F(parent=self, controller=self.controller)
            self.input_frames[F] = frame
            frame.grid(row=3, column=0, sticky="NSEW")
            
            
        #Material Selection Dropdown
        material = tk.StringVar(self)
        material.set("Select")
        material_types = controller.get_material_types()
        self.material_dropdown = tk.OptionMenu(self, material, *material_types, 
                                               command = lambda material: self.show_frame(self.get_material_input_frame(material)))
        self.material_dropdown.grid(row=2, column=0)
        
    def get_material_input_frame(self, material):
        if material == "Concrete":
            return self.input_frames[ConcreteMaterialInput]
        if material == "Steel":
            return self.input_frames[SteelMaterialInput]
    
    def show_frame(self, frame):
        frame.tkraise()


class ConcreteMaterialInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
        
        material_label = tk.Label(self, text="Concrete Material Input", font=Fonts.MEDIUM_FONT)
        material_label.grid(row=0, column=0)
    
        material_name = tk.Label(self, text="Concrete Material Name:", font=Fonts.MEDIUM_FONT)
        material_name.grid(row=1, column=0)
        material_name_entry = tk.Entry(self)
        material_name_entry.grid(row=1, column=1)
    
    
        fc_label = tk.Label(self, text="f'c (MPa):", font=Fonts.MEDIUM_FONT)
        fc_label.grid(row=2, column=0)
        fc_entry = tk.Entry(self)
        fc_entry.grid(row=2, column=1)
    
    
        fu_label = tk.Label(self, text="f'u: (MPa)", font=Fonts.MEDIUM_FONT)
        fu_label.grid(row=3, column=0)
        fu_entry = tk.Entry(self)
        fu_entry.grid(row=3, column=1)
        
        
        Ec_label = tk.Label(self, text="Ec: (MPa)", font=Fonts.MEDIUM_FONT)
        Ec_label.grid(row=4, column=0)
        Ec_entry = tk.Entry(self)
        Ec_entry.grid(row=4, column=1)
        
        eu_label = tk.Label(self, text="e'u:", font=Fonts.MEDIUM_FONT)
        eu_label.grid(row=5, column=0)
        eu_entry = tk.Entry(self)
        eu_entry.grid(row=5, column=1)

class SteelMaterialInput(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
    
        material_label = tk.Label(self, text="Steel Material Input", font=Fonts.MEDIUM_FONT)
        material_label.grid(row=0, column=0)
    
        material_name = tk.Label(self, text="Steel Material Name:", font=Fonts.MEDIUM_FONT)
        material_name.grid(row=1, column=0)
        material_name_entry = tk.Entry(self)
        material_name_entry.grid(row=1, column=1)
    
    
        fy_label = tk.Label(self, text="fy: (MPa)", font=Fonts.MEDIUM_FONT)
        fy_label.grid(row=2, column=0)
        fy_entry = tk.Entry(self)
        fy_entry.grid(row=2, column=1)
    
    
        fu_label = tk.Label(self, text="fu: (MPa)", font=Fonts.MEDIUM_FONT)
        fu_label.grid(row=3, column=0)
        fu_entry = tk.Entry(self)
        fu_entry.grid(row=3, column=1)
        
        
        Es_label = tk.Label(self, text="Es: (MPa)", font=Fonts.MEDIUM_FONT)
        Es_label.grid(row=4, column=0)
        Es_entry = tk.Entry(self)
        Es_entry.grid(row=4, column=1)
        
        ey_label = tk.Label(self, text="e'y:", font=Fonts.MEDIUM_FONT)
        ey_label.grid(row=5, column=0)
        ey_entry = tk.Entry(self)
        ey_entry.grid(row=5, column=1)
        
        eu_label = tk.Label(self, text="e'u:", font=Fonts.MEDIUM_FONT)
        eu_label.grid(row=6, column=0)
        eu_entry = tk.Entry(self)
        eu_entry.grid(row=6, column=1)

#class ConcreteMaterialInput(tk.Frame):       
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        frame.grid(row=3, column=2, sticky="NSEW")
#        fy= tk.Label(parent, text="fy (MPa): " + str(material.fy), font=Fonts.MEDIUM_FONT)
#        fy.grid(row=0, column=0, sticky="w")
#        fu = tk.Label(parent, text="fu (MPa): " + str(material.fu), font=Fonts.MEDIUM_FONT)
#        fu.grid(row=1,column=0, sticky="w")
#        Ec = tk.Label(parent, text="Es (MPa): " + str(material.Es), font=Fonts.MEDIUM_FONT)
#        Ec.grid(row=2,column=0, sticky="w")
#        ey = tk.Label(parent, text="ey: " + str(material.ey), font=Fonts.MEDIUM_FONT)
#        ey.grid(row=3,column=0, sticky="w")
#        eu = tk.Label(parent, text="eu: " + str(material.eu), font=Fonts.MEDIUM_FONT)
#        eu.grid(row=4,column=0, sticky="w")        
#
#
#class SteelMaterialInput(tk.Frame):       
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        frame = tk.Frame(parent)
#        frame.grid(row=3, column=2, sticky="NSEW")
#        fc = tk.Label(frame, text="fc (MPa): " + str(material.fc), font=MEDIUM_FONT)
#        fc.grid(row=0,column=0, sticky="w")
#        fu = tk.Label(frame, text="fu (MPa): " + str(material.fu), font=MEDIUM_FONT)
#        fu.grid(row=1,column=0, sticky="w")
#        Ec = tk.Label(frame, text="Ec (MPa): " + str(material.Ec), font=MEDIUM_FONT)
#        Ec.grid(row=2,column=0)
#        eu = tk.Label(frame, text="eu : " + str(material.eu), font=MEDIUM_FONT)
#        eu.grid(row=3,column=0, sticky="w")


    
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        

#if __name__ == "__main__":