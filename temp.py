# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

Le but est de pouvoir ouvrir une nouvelle fenêtre contenant
les infos de l'élément sélectionné dans la liste_box...

Ensuite , on doit pouvoir trier la liste en fonction du texte entré dans
la barre entry...
"""

from tkinter import *

princip = Tk()

princip.geometry("500x200+200+100")

princip.title("Temporaire")

ev_label = Frame(princip, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)

tex = Label(ev_label , text ="test raising")
tex.pack()

def click(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    ev_label.pack(side = "right")
    print('You have selected  : "%s" ' % (value))
    

def chercher():
    if(entVal.get()!=""):
        titre.set(entVal.get())
        
    else :
        titre.set("")
        for x in range(10):
            liste.insert(END, "Livre" +str(x))
    
def create(evt):
    
    top = Toplevel(princip)
    top.geometry("500x200+200+100")
    lbl = Label(top, text = 'ok ! ')
    lbl.pack()

    
    
    
    
tFrame = Frame(princip, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
tFrame.pack()

tFrame2 = Frame(princip, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
tFrame2.pack(side = "bottom")

listFrame = Frame(princip, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
listFrame.pack( side = "left")

listFrame1 = Frame(princip, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
listFrame1.pack( side = "bottom")


entVal= StringVar()



tEntry = Entry(tFrame , textvariable =entVal, width =30)
tEntry.grid( row = 5 , column = 20)


SButton = Button(tFrame2, text = "Chercher" ,width =30, bg='#DAA520',relief =FLAT,fg='white')
SButton.pack()
titre = StringVar()
liste = Listbox(listFrame , width = 40 , listvariable = titre)
liste1 = Listbox(listFrame1 , width = 40 , listvariable = titre)

for x in range(10):
    liste.insert(END, "Livre" +str(x))

liste.pack() 

liste.bind('<<ListboxSelect>>' , click)
SButton.config(command = chercher)


for x in range(10):
    liste1.insert(END, "Livre" +str(x))

liste1.pack() 

liste1.bind('<<ListboxSelect>>' , create )


      


princip.mainloop()