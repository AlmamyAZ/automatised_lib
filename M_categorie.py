# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:00:44 2018

@author: Almamy
"""

"""
création des métaclasses pour les différentes catégories

"""

from tkinter import *



liste_classes ={} # dictionnaire de toutes les catégories

class Categorie(type):
    
    """ Repésente la classe mère
    de toute les catégories de livres
    qui seront instanciées plus tard"""
    
    def __new__(metacls, cat_name , cat_tup , cat_dico ):
        print("Appel de la Categorie: ".format(cat_name))
        return type.__new__(metacls,cat_name,cat_tup,cat_dico)

    def __init__(self, cat_name,cat_tup, cat_dico):

        type.__init__(self,cat_name,cat_tup,cat_dico)



    


"""class Cat_book(Frame,metaclass = Categorie):
    def __init__(self, name,id):
        Frame.__init__(self,id)
        #self.controller = controller
        self.name = name
        self.id = id"""





class Fen_principale(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #creation du container qui représente la page de base
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0 , weight=1)
        container.grid_columnconfigure(0, weight=1)
       #===============================creation d'un menu et sous menu=========================================
        self.biblio_menu = Menu(self)
        self.sous_men = Menu(self.biblio_menu, tearoff=0) #creation d'un sous menu
        self.biblio_menu.add_cascade(label="Menu",menu=self.sous_men) # ajout du sous menu au menu
        self.sous_men.add_command(label="Quitter", command = self.quitter) # ajout des commandes
        self.sous_men.add_command(label="Connexion Admin", command = self.admin)
        self.biblio_menu.add_command(label="Information",command=self.helpp)
        self.biblio_menu.add_command(label="Retour", command = self.retour_livre)
        self.config(menu = self.biblio_menu) # permet de configurer le menu
        # le menu doit toujours être defini dans une fenetre de Tk , jamais dans un Frame...
       
        self.frames = {}

        for F in (Bibliotheque, Mathematique):
            page_name=F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name]= frame

            #faire apparaitre les pages au même endroit
            frame.grid(row=0, column=0, sticky="nsew")

        self.affich_fenetre("Mathematique")

    
            
    def affich_fenetre(self,page_name):
        #affichage d'une fenêtre avec le nom donnee dans la fonction

        frame = self.frames[page_name]
        frame.tkraise()
        #======= definition des fonctions=====================================    
    def admin(self):
        pass

    def retour_livre(self):
        pass

    def quitter(self):
        self.destroy()

    def helpp(self):
        print("please place your student card")


def show(Mathematique):
    pass

def def_cat(self , name , id):
    self.name = name
    self.id = id

    print("Constructeur de la classe".format(Mathematique.name))

dic_Cat ={"__init__": def_cat, "affiche":show}

""" Création des classes dynamiques"""""""""""""""

#Cat_Book = Categorie("Cat_book",(Frame,),dic_Cat)
Bibliotheque = Categorie("Bibliotheque",(Frame,),dic_Cat)   
Mathematique = Categorie("Mathematique",(Frame,),dic_Cat)   

if __name__=="__main__":
    app = Fen_principale()
    app.title("Bibliothèque Universitaire")
    app.geometry("800x600+300+500")
    app.mainloop()

