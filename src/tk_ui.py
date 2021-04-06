import tkinter as tk 
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 
from resizer import resizer_fun

class Image_Resizer_UI():
    def __init__(self):

        self.root=tk.Tk() 
        
        # setting the windows size 
        self.root.geometry("350x150") 
        self.root.title('IMAGE RESIZER')
        # declaring string variable 
        # for storing name and count 
        self.Width=tk.StringVar() 
        self.Height=tk.StringVar() 
        self.folder_path = tk.StringVar()
    def main(self):
        # creating a label for  
        # name using widget Label Width
        self.width_label = tk.Label(self.root, text = 'Enter Width:', 
                            font=('calibre', 
                                    10, 'bold')) 
        
        # creating a entry for input Width
        # name using widget Entry 
        self.width_entry = tk.Entry(self.root, 
                            textvariable = self.Width,font=('calibre',10,'normal')) 
        
        # creating a label for Height 
        self.height_label = tk.Label(self.root, 
                            text = 'Enter Height:', 
                            font = ('calibre',10,'bold')) 
        
        # creating a entry for Height 
        self.height_entry=tk.Entry(self.root, 
                            textvariable = self.Height, 
                            font = ('calibre',10,'normal')) 

        # creating a label for Directory 
        self.loc_lab = tk.Label(self.root, 
                            text = 'Select_Directory', 
                            font = ('calibre',10,'bold')) 
        
        # creating a entry for Location 
        self.loc_entry=tk.Entry(self.root, 
                            textvariable = self.folder_path, 
                            font = ('calibre',10,'normal')) 
        
        # creating a button using the widget  
        # Button that will call the submit function  
        self.submit_button=tk.Button(self.root,text = 'Submit', 
                        command = self.submit) 
        
        # placing the label and entry in 
        # the required position using grid 
        # method 
        self.width_label.grid(row=4,column=1) 
        self.width_entry.grid(row=4,column=2) 
        self.height_label.grid(row=5,column=1) 
        self.height_entry.grid(row=5,column=2) 
        self.loc_lab.grid(row=2,column=1) 
        self.loc_entry.grid(row=2,column=2) 
        self.submit_button.grid(row=6,column=2) 

        self.button2 = Button(text="Browse", command=self.browse_button)
        self.button2.grid(row=2, column=3)
        # performing an infinite loop  
        # for the window to display 
        self.root.mainloop()


    # defining a function that will 
    # get the name and count and  
    # print them on the screen 
    def submit(self): 
    
        width=int(self.width_entry.get() )
        height=int(self.Height.get()) 
        loc = self.loc_entry.get()
        

        if len(loc) >3: 
            loc = loc+"/"
        
            print("file directory : ",loc)
            if width>1 and height>1     :
                resizer_fun(loc,width,height)
                tk.messagebox.showinfo("Submitted", "completed") 
                self.root.quit()
            else:
                print("Enter width :")
                print("Enter height :")
                tk.messagebox.askretrycancel("Enter width & height", "Try again?")


        else:
            print("select file location first")
            tk.messagebox.askretrycancel("select file location first", "Try again?")

        self.Width.set("") 
        self.Height.set("") 
    
    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called self.folder_path
        # global self.folder_path
        filename = filedialog.askdirectory()
        self.folder_path.set(filename)
    
        
