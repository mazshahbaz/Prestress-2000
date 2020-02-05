# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:29:18 2020

@author: Mazen
"""
import tkinter as tk


class Controller():
    def __init__(self):
        self.View = View()
        self.Model = Model()
        self.View.mainloop()
        return
    
    
    
class Model():
    def __init__(self):
        self.materials = 1
        self.sections = 1
        self.girder = 1
        return

class View(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "PreStress-2000")
        root = tk.Frame(self)                                   #Displaying the startpage
        
        #Initalize Pages
        self.frames = {}                                        #Dictionary to contain all the frame created in our GUI, Each page is a frame
        for F in (StartPage, PageOne, PageTwo):
            frame = F(root, self)                               #Creating the Start Page
            self.frames[F] = frame                              #Placing frames in the frames dictionary
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)                              #Displaying the stratpage
        
    def show_frame(self, cont):
        """
        bring the desired frame (cont) to the front
        """
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self):
        return


class materials():
    def __init__(self, master):
        self.materials_types = []
        self.materials_list = {}
        



if __name__ == "__main__":
    Controller()