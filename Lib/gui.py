import tkinter as tk
from tkinter import *

class IDMGui(tk.Tk):
    def __init__(self,title="box") -> None:
        mywindow=tk.Tk()
        self.window=mywindow
        self.window.title(title)
        self.window.geometry("500x300")
    


    def resizeWindow(self,width=500,height=300):
        string= f"{width}x{height}"
        self.window.geometry(string)


    def createButton(self,function,text="",width=200,height=150,**kwargs):
        fg=kwargs.get('fg',None)
        bg=kwargs.get('bg',None)
        image=kwargs.get('image',None)
        activeback=kwargs.get("activebackground",None)
        activefore=kwargs.get("activeforeground",None)

        button=tk.Button(self.window,text=text,command=function,fg=fg,
                         background=bg,image=image,activebackground=activeback,activeforeground=activefore)
        return button
    
    def createLabel(self,labelText=""):
        label=Label(self.window,text=labelText)
        return label 
    

    def createInputField(self,labelText=""):
        entry=Entry(self.window)
        return entry


    def createDirectorySelector(self):
        pass

    def setPosition(self,object,x=0,y=0):
        object.place(x=x, y=y)

    def run(self):
        self.window.mainloop()

    

        

    

