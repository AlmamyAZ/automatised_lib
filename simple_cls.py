# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:10:04 2018

@author: Almamy
"""
from abc import ABC , abstractmethod
from tkinter import *
from datetime import datetime
from time import strftime
import subprocess
import sys


class Category(ABC,Tk):
    def __init__(self,name,id):
        self.name=name
        self.id =id
        self.parent = "i'm a parent"
        Tk.__init__(self,self.parent)
        

    @abstractmethod
    def show(self):
        pass
    
class ImplCategory(Category): # héritage multiple
    
    def _init_(self,name,id):
        super(Category)
        #self.name = name
        #self.id=id
      

    def ouvrir(self,evt):
        
        #fle = subprocess.Popen([sys.executable(),temp.py])
        fle = subprocess.Popen("temp.py",shell=True) #executable pour tout compilateur et cherche le chemin du script
        N_cat.destroy()
        fle.communicate()
        
        
        
        
    
    
    def create_p(self,evt,name):
        
        name = ImplCategory("page",2)
        name.show()
        
   
       
         
    def show(self):
        
        
        titre = StringVar()
        Frame1 =Frame(self, borderwidth = 2 , relief =GROOVE, bg = "black") 
        Frame1.pack()
        
        B1 = Button(Frame1, text = "test", command = self.ouvrir)
        B1.pack()
        self.geometry("800x400+200+100")
        liste1 = Listbox(self, width = 40 , listvariable = titre)
        for x in range(10):
            liste1.insert(END, "Livre" +str(x))
            liste1.pack() 
            liste1.bind('<<ListboxSelect>>' , self.ouvrir )

        
        
        print("i'm a custom category")
        
      
         
        
        

    
        


if __name__=="__main__":
    
    N_cat=ImplCategory("name",1)
    N_cat.show()
    N_cat.mainloop()
    
    
