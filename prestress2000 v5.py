# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:48:08 2020

@author: Mazen
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk    #brings in the canvas we will use, and the navigation bar used in each plot!
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from Fonts import LARGE_FONT as LARGE_FONT
from Fonts import MEDIUM_FONT as MEDIUM_FONT
from Fonts import SMALL_FONT as SMALL_FONT
import Materials_Frames as MF
import Sections as sections
import Canvas_Settings

#LARGE_FONT = ("Verdana", 12)
#MEDIUM_FONT = ("Verdana", 10)
#SMALL_FONT = ("Verdana", 8)
style.use('ggplot')                         #can also use 'dark_background'



# create a figure to be used in our application
f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    """
    Continiously pulls x,y data from the specified file!
    """
    pulldata = open("sampleData.txt", "r").read()    
    dataList = pulldata.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()                                                    #if we dont clear, plot will continue to plot over eachother
    a.plot(xList, yList)

    
def NavigationBar(Parent, controller):
    f = tk.Frame(Parent)
    f.grid(row = 0, column = 0, sticky="W")
    
    Home_button = tk.Button(f, text="Home", 
                            command=lambda: controller.show_frame(StartPage))
    Home_button.grid(row=0, column=0)
    
    materials_button = tk.Button(f, text="Materials", 
                            command=lambda: controller.show_frame(PageOne))
    materials_button.grid(row=0, column=1)
    
    xsection_button = tk.Button(f, text="Cross Section", 
                            command=lambda: controller.show_frame(PageTwo))
    xsection_button.grid(row=0, column=2)
    
    graph_button = tk.Button(f, text="Graph", 
                            command=lambda: controller.show_frame(PageThree))
    graph_button.grid(row=0, column=3)
    
    

class Prestress2000(tk.Tk):

    def __init__(self):
        """
        root represents the main frame in our window. we inherit tk.TK in the class and then initalize it
        so that we can use all the functionality within our objects. when prestress2000 is called 'root'
        is what creates the tkinter window
        
        
        UPDATE ME, expalin the initializations and methods?
        """
        tk.Tk.__init__(self)                                    #Opens the application, and allows use of tk methods
#        tk.Tk.iconbitmap(self,default='clienticon.ico')        #Should be 16*16 the icon for our application! use GIMP to make .ico files
        tk.Tk.wm_title(self, "PreStress-2000")
        
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 3
        #Initalize Pages
        root = tk.Frame(self)                                   #Creating the MAIN FRAME wilth the application as the parent
        root.grid(row=0, column=0)                              #fill the main frame to fit entire window

        root.grid_rowconfigure(0, weight=1)                     #configure the grid in the main frame, 0 is the size of the row, weight represnts importance
        root.grid_columnconfigure(0, weight=1)                  #configure the grid in the main frame, 0 is the size of the column, weight represnts importance
        
        #Initalize Option Menus, these are used to update OM's effeciently. items in list structured as [OM , Var]
        self.materials_option_menus = []
        self.section_option_menus = []
        
        
        #Initalize Pages
        self.frames = {}                                        #Dictionary to contain all the frame created in our GUI, Each page is a frame
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(root, self)                               #Creating the Start Page
            self.frames[F] = frame                              #Placeing startpage in the frames dictionary
            frame.grid(row=0, column=0, sticky="nsew")          #Displaying the startpage
        
        
        self.show_frame(StartPage)                              #Displaying the stratpage


    def show_frame(self, cont):
        """
        bring the desired frame (cont) to the front
        """
        frame = self.frames[cont]
        frame.tkraise()
           
    
    def update_dropdown(self, new_choices, option_menu, var):
        """
        This function updates the materials OptionMenu on the cross section page. 
        whenever a material is added on PageOne (add_concrete_material, add_concrete_steel)
        this function is called.
        
        
        UPDATE ME
        """
        OptionMenu = option_menu["menu"]
        OptionMenu.delete(0, 'end')
        for choice in new_choices:
            print(new_choices)
            OptionMenu.add_command(label=choice, 
                                   command= lambda value=choice: var.set(value))
            
    def get_materials_list(self):
        return self.frames[PageOne].get_materials_list()
    
    def update_material_dropdown(self):
        """
        This function updates the materials OptionMenu on the cross section page. 
        whenever a material is added on PageOne (add_concrete_material, add_concrete_steel)
        this function is called.
        
        
        UPDATE ME
        """
        new_choices = self.get_materials_list()
        for om , var in self.materials_option_menus:
           self.update_dropdown(new_choices, om, var)

    
    def add_material_om(self, om, var):
        self.materials_option_menus.append([om, var])
        
    
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        # parent is the widget this is being placed in, and Controller is the main program
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 3
        
        NavigationBar(self, controller)
        
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.grid(row=1, column=0)
 


# =============================================================================
#  PAGE ONE - Materials
# =============================================================================

    
def remove_material(parent, name):
    if name in parent.materials_dictionary:
        parent.materials_dictionary.pop(name)
        parent.Lb.delete(tk.ANCHOR)
        
def material_properties(parent, name):
    if name in parent.materials_dictionary:
        material = parent.materials_dictionary[name]
        if material.type == "Steel":
            frame = tk.Frame(parent)
            frame.grid(row=3, column=2, sticky="NSEW")
            fy= tk.Label(frame, text="fy (MPa): " + str(material.fy), font=MEDIUM_FONT)
            fy.grid(row=0, column=0, sticky="w")
            fu = tk.Label(frame, text="fu (MPa): " + str(material.fu), font=MEDIUM_FONT)
            fu.grid(row=1,column=0, sticky="w")
            Ec = tk.Label(frame, text="Es (MPa): " + str(material.Es), font=MEDIUM_FONT)
            Ec.grid(row=2,column=0, sticky="w")
            ey = tk.Label(frame, text="ey: " + str(material.ey), font=MEDIUM_FONT)
            ey.grid(row=3,column=0, sticky="w")
            eu = tk.Label(frame, text="eu: " + str(material.eu), font=MEDIUM_FONT)
            eu.grid(row=4,column=0, sticky="w")
            frame.tkraise()
            print(name, "steel", material.fy)
        if material.type == "Concrete":
            frame = tk.Frame(parent)
            frame.grid(row=3, column=2, sticky="NSEW")
            fc = tk.Label(frame, text="fc (MPa): " + str(material.fc), font=MEDIUM_FONT)
            fc.grid(row=0,column=0, sticky="w")
            fu = tk.Label(frame, text="fu (MPa): " + str(material.fu), font=MEDIUM_FONT)
            fu.grid(row=1,column=0, sticky="w")
            Ec = tk.Label(frame, text="Ec (MPa): " + str(material.Ec), font=MEDIUM_FONT)
            Ec.grid(row=2,column=0)
            eu = tk.Label(frame, text="eu : " + str(material.eu), font=MEDIUM_FONT)
            eu.grid(row=3,column=0, sticky="w")
            frame.tkraise()

       
class PageOne(tk.Frame):
    """
    Material Definitions
    
    
    UPDATE ME
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
        
        NavigationBar(self, controller)
        
        label = tk.Label(self, text="Materials Page", font=LARGE_FONT)
        label.grid(row=1, column=0, sticky="W")
        
        self.materials_dictionary = {}
        
        #Material Selection Dropdown
        material = tk.StringVar(self)
        material.set("Select")
        material_types=["Concrete",
                        "Steel"]
        self.material_dropdown = tk.OptionMenu(self, material, *material_types, command = lambda material: self.show_frame(material))
        self.material_dropdown.grid(row=2, column=0)
        
        #Concrete material inputs frame
        self.concrete_input_frame = MF.ConcreteMaterialInputs(self, controller)
        self.concrete_input_frame.grid(row=3, column=0, sticky="NSEW")
        
        #Steel material inputs frame
        self.steel_input_frame = MF.SteelMaterialInputs(self, controller)
        self.steel_input_frame.grid(row=3, column=0, sticky="NSEW")
        
        #Added Materials List Box frame
        added_materials = tk.Frame(self)
        added_materials.grid(row=3, column=1, padx=10)
        self.Lb = tk.Listbox(added_materials)
        self.Lb.grid(row=0, column=0)
        
        def selected_material(evt):
            index = evt.widget.curselection()[0]
            name = self.Lb.get(index)
            print(name)
            material_properties(self, name)
                   
        self.Lb.bind('<<ListboxSelect>>', selected_material)
        remove_button = tk.Button(added_materials, text="Remove Material", 
                            command=lambda: remove_material(self, self.Lb.get(tk.ANCHOR)))
        remove_button.grid(row=1, column=0)
        
        
    def show_frame(self, material_type):
        """
        bring the desired frame to the front
        """
        if material_type == "Steel":
            self.steel_input_frame.tkraise()
        elif material_type == "Concrete":
            self.concrete_input_frame.tkraise()
        
    def add_concrete_material(self, name, fc, fu, Ec, eu):
        """
        Adds a concrete material to the materials listbox, and updates 
        ALL optionmenus that list materials from the listbox
        located on the materials page [PageTwo]
        """
        if name in self.materials_dictionary:
            return
        else:
            self.materials_dictionary[name] = MF.Concrete_Material(name, fc, fu, Ec, eu)
            self.Lb.insert(tk.END, name)
            self.controller.update_material_dropdown()
            
    def add_steel_material(self, name, fy, fu, Es, ey, eu):
        """
        Adds a concrete material to the materials listbox, and updates 
        ALL optionmenus that list materials from the listbox
        located on the materials page [PageTwo]
        """
        if name in self.materials_dictionary:
            return
        else:
            self.materials_dictionary[name] = MF.Steel_Material(name, fy, fu, Es, ey, eu)
            self.Lb.insert(tk.END, name)
            self.controller.update_material_dropdown() 
            
    def get_materials_list(self):
        """
        Returns an updated list of all materials as a lsit.
        """
        materials_list = self.materials_dictionary.keys()
        return list(materials_list)
        




# =============================================================================
#  PAGE TWO - Cross Section
# =============================================================================


#def get_materials(controller):
#controller.frames[PageOne]
#    materials_list = controller.frames[PageOne].materials_dictionary
#    return list(materials_list)

    
"""
To do, implement add section button/function, and implement drawing on the canvas!
"""
    
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 4
        self.controller = controller
        self.canvas_height = Canvas_Settings.canvas_height
        self.canvas_width = Canvas_Settings.canvas_width
        
        #General Page Parameters
        NavigationBar(self, controller)
        page_label = tk.Label(self, text="Cross-Section Page", font=LARGE_FONT)
        page_label.grid(row=1, column=0, sticky = "W", padx=10)
        
        # Initalize Sections Data
        self.sections = {}
        self.section_input_frames ={}
        self.section_types = ["Rectangle",
                              "AASHTO"]
        
        #Define Section input Frames and place them in the inputs_frames dictionary
        self.section_input_frames = {"Rectangle": sections.RectangleSectionInputs(self, self.controller),
                  "AASHTO": sections.AASHTOSectionInputs(self, self.controller)}
        for frame in self.section_input_frames.values():
            frame.grid(row=3, column=0, sticky = "NSEW", padx=10, pady=3)
        
        
        #Section Type Selection, will raise the input_frame of the section type selected in the option menu
        self.section_type = tk.StringVar(self)
        self.section_type.set("Select")
        self.section_OM = tk.OptionMenu(self, self.section_type, *self.section_types, command =  lambda section_type: self.show_frame(self.section_type.get()))
        self.section_OM.grid(row=2, column=0, sticky = "W", padx=10, pady=10)
        
        
        #Sections Listbox, created sections are added here
        sections_LB_frame = tk.Frame(self)
        sections_LB_frame.grid(row=3, column=1, padx=10)
        self.Lb = tk.Listbox(sections_LB_frame)
        self.Lb.grid(row=3, column=1)
        
        #Add Section Button
        add_section_button = tk.Button(self, text="Add Material", 
                                command=lambda: self.add_section())
        add_section_button.grid(row=4, column=0, sticky = "W", padx=10)
        
        #Remove Section Button
        remove_section_button = tk.Button(self, text="Remove Material", 
                            command=lambda: self.remove_section(self.Lb.get(tk.ANCHOR)))
        remove_section_button.grid(row=4, column=1, pady=10)
        
        #initalize Canvas
        self.canvas=tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, background="white")
        self.canvas.grid(row=5,column=0, pady=10, padx=10)
        
        
#    def create_section(self, section_type):
#        if 
    
    def get_input_frame(self, section_type):
        return self.section_input_frames[section_type]
    
    
    def show_frame(self, section_type):
        """
        bring the desired frame to the front
        """
        print(section_type)
        frame = self.get_input_frame(section_type)
        frame.tkraise()
        
    def add_section(self):
        """
        Creates a a cross-section based on the section_type selected
        the inputs are obtained from the section_input_frame, and a the corrseponding section is created
        
        The Created Section is then:
            - Added tp the sections dictionary in the Page2 Class
            - Added to the Sections Listbox
        
        Section_input_frame: The frame in which the user inputs the desired sections properties, based on the section type selected
        section: The created section object
        
        NEED TO ADD FUNCTIONALITY TP UPDATE ALL future optionmenus that reference this one 
        """
        section_input_frame = self.get_input_frame(self.section_type.get())
        section = section_input_frame.create_section()
        section_name = section.name
        if section_name in self.sections:
           print("This name has already been used for a section")
        else:
            self.sections[section_name] = section
            self.Lb.insert(tk.END, section.name)
            self.draw_section(section.coordinates)
    
    def draw_section(self, coordinates):
        self.canvas.delete("all")
        coord_list = [point for points in coordinates for point in points]
        print(coord_list)
        self.canvas.create_polygon(coord_list,
                                   )
#        i=0
#        while i<len(coordinates):
#            if i == len(coordinates)-1:
#                self.canvas.create_oval
#                line = [coordinates[i][0], coordinates[i][1], coordinate[0][0], coordinate[0][1]]
#            else:
#                line = [coordinates[i][0], coordinates[i][1],coordinate[i+1][0], coordinate[i+1][1]]
            
        
    def remove_section(self, section):
        if section in self.sections:
            self.sections.pop(section)
            self.Lb.delete(tk.ANCHOR)

        

        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #initialize number of rows and columns on this frame
        self.n_col = 3
        self.n_row = 3
        
        NavigationBar(self, controller)
        
        label = tk.Label(self, text="Graph page", font=LARGE_FONT)
        label.grid(row=1, column=0)
        
        canvas_frame=tk.Frame(self)
        canvas_frame.grid(row=2, column=0)
        canvas = FigureCanvasTkAgg(f, canvas_frame)                                         #Create the Figure
        canvas.draw()                                                               # Will Actually show the figure
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)       #places the figure where we want
        
        toolbar =  NavigationToolbar2Tk(canvas, canvas_frame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        #uses the animate function to do live updates of figure 'f' at interval of 1000 ms
        self.ani = animation.FuncAnimation(f, animate, interval=1000)
        



app = Prestress2000() #this is the main window
app.mainloop() #running the main window (the application)'