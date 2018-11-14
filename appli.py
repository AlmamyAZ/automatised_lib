#*******************Autonomous library project*************************#
# Author : Almamy Amadou Kanté
# College : Polytech Nancy
# Teamates : Christian  Ulrich Tchounke & Thibaut Jimenez
#**********************************************************************#
from tkinter import *
from datetime import datetime
from time import strftime

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

        for F in (BibliothequeUL, Mathématiques, Physique, Electromagnetique, Optique):
            page_name=F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name]= frame

            #faire apparaitre les pages au même endroit
            frame.grid(row=0, column=0, sticky="nsew")

        self.affich_fenetre("BibliothequeUL")

    
            
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

class BibliothequeUL(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller

        
        #===================canvas de 'arrière plan ====================================
        w,h = 800, 500

        self.image = PhotoImage(file='female.png', master=self)

        self.canvas = Canvas(self, width = w, height = h, scrollregion = (0, 0, 1000,1000 ))

        self.canvas.pack(fill ="both" , expand=True)

        self.canvas.create_image((w//2 , h//2), image = self.image)

        self.logo = PhotoImage(file='logo1.png', master = self)
        logo_label= Label(self.canvas , image = self.logo)
        logo_label.place( y = 650)

          #===================création d'un scrollbar pour le canva===============================

        #scl = Scrollbar(self.canvas, orient ="vertical")
        #scl.config(command = self.canvas.yview)
        #self.canvas.config(yscrollcommand = scl.set)
        #scl.pack(side ="right", fill="y")
        
        
        

       

       
        #creation d'un label et placement dans la page 
        label1 = Label(self.canvas, text="Matières" , font = 'corbel',fg='white',bg='#DAA520')
        label1.pack(side = "top" , fill = "x")                                     
        #label1.grid(row = 0 , sticky ="nsew")
        #self.labPlace(label1)
      
        #===================creation des boutons============================
        mathButton = Button(self.canvas, text ="Mathematiques", width = 30 ,command =lambda: controller.affich_fenetre("Mathématiques"),bg ="#DAA520")
        phyButton = Button(self.canvas, text ="Physique", width=30 ,command =lambda: controller.affich_fenetre("Physique"),bg ="#DAA520")
        elecButton = Button(self.canvas, text ="Electromagnetisme", width =30, command =lambda: controller.affich_fenetre("Electromagnetique"),bg ="#DAA520")
        optButton = Button(self.canvas, text ="Optique",width=30, command =lambda: controller.affich_fenetre("Optique"),bg ="#DAA520")

        #===================placement des boutons avec l'instruction grid=================
        
        #mathButton.grid(row = 300 , sticky = E)
        #phyButton.grid(row =301 , sticky =E)
        #elecButton.grid(row = 302, sticky=E)
        #optButton.grid(row = 303, sticky = E)

        mathButton.place( x = 600 , y = 30)
        phyButton.place( x = 600 , y = 60)
        elecButton.place( x = 600 , y = 90)
        optButton.place( x = 600 , y = 120)

        #====================Affichage de la date courante et du temps====================
        Dframe = Frame(self.canvas, borderwidth = 2, relief = GROOVE, bg="black")
        Dframe.pack(side = "bottom")
        #label_date= Label(Dframe, text = "Date "+strftime('%Y-%m-%d' , datetime.now()))
        label_date = Label(Dframe , text = datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        label_date.pack()
       

class Mathématiques(Frame):
     def __init__(self, parent, controller):    
        Frame.__init__(self,parent)
        self.controller = controller
        Mathentree = StringVar()
       

       #===================canvas de 'arrière plan ====================================
        w,h = 800, 500

        self.image = PhotoImage(file='female.png', master=self)

        self.canvas = Canvas(self, width = w, height = h)

        self.canvas.pack(fill ="both" , expand=True)

        self.canvas.create_image((w//2 , h//2), image = self.image)

        self.logo = PhotoImage(file='logo1.png', master = self)
        logo_label= Label(self.canvas , image = self.logo)
        logo_label.place( y = 650)

        
        list_frame = Frame(self.canvas)
        list_frame.place(x=300, y=100)
       
        #=======================Listebox pour les livres====================================
        liste1 = Listbox(list_frame, width =50)
        for x in range(100):
            liste1.insert(END, "Livre "+str(x))
        liste1.pack( side = "left" , fill ="y")
        #==========================scrollbar pour la page et la liste========================
        list_scroll = Scrollbar(list_frame, orient ="vertical")
        list_scroll.config(command = liste1.yview)
        list_scroll.pack(side ="right", fill ="y")
        
        #===============configiration du scrollbar============================
        liste1.config(yscrollcommand = list_scroll.set)
        #===============================================================================================================================
        labelm = Label(self.canvas, text="Mathématiques", bg='#DAA520')
        labelm.pack(side = "top", fill = "x")
        tframe = Frame(self.canvas, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105) #frame pour la zone de texte
        tframe.place( x = 300 , y = 20)
        requete = Entry(tframe, textvariable = Mathentree , width = 50).pack()#zone de texte pour la recherche
        #=============================================boutons recherche & retour==============================================================
        bframe = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520') #frame pour le bouton de recherche
        bframe.place(x =0 , y =20)
        sButton = Button(bframe, text = "Rechercher" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack() #bouton de recherche
        rButton = Button(bframe, text = "Retour" ,width =30, bg='#DAA520',relief =FLAT,fg='white', command = lambda:controller.affich_fenetre("BibliothequeUL")).pack(side = "bottom")#bouton de retour
        #============================================boutons Emprunter & Reserver==============================================================
        b1frame = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520') #frame pour le bouton de recherche
        b1frame.place(x = 100,y = 450)
        eButton = Button(b1frame, text = "Emprunter" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack(side="left" ,padx = 5)
        lButton = Button(b1frame, text ="Réserver" , width = 30, bg ='#DAA520', relief = FLAT, fg = 'white').pack(side = "right", padx = 5)
        #==================================================================Frame de description de livres======================================
        Bframe = Frame(self.canvas , borderwidth = 2 , width = 500 , height = 300  , relief = GROOVE , bg = 'red')
        #Bframe.place(x = 500 ,y = 500)
        Bframe.pack(side = "right")
        author_label = Label(Bframe , text = "Auteur : " , bg = '#DAA520')
        author_label.place(  y = 5 )
        
        
      
  
        
class Physique(Frame):
     def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        Phyentree= StringVar()
        #===================canvas de 'arrière plan ====================================
        w,h = 800, 500

        self.image = PhotoImage(file='female.png', master=self)

        self.canvas = Canvas(self, width = w, height = h)

        self.canvas.pack(fill ="both" , expand=True)

        self.canvas.create_image((w//2 , h//2), image = self.image)

        self.logo = PhotoImage(file='logo1.png', master = self)
        logo_label= Label(self.canvas , image = self.logo)
        logo_label.place( y = 650)

        
        
        #==================================================================================================================
        labelm = Label(self.canvas, text="Physique", bg='#DAA520')
        labelm.pack(side = "top", fill = "x")
        tframe = Frame(self.canvas, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
        tframe.place( x = 300 , y = 20)
        requete = Entry(tframe, textvariable = Phyentree , width = 50).pack()
        bframe = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520',)
        bframe.place(x =0 , y =20)
        sButton = Button(bframe, text = "Rechercher" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack()
        rButton = Button(bframe, text = "Retour" ,width =30, bg='#DAA520',relief =FLAT,fg='white', command = lambda:controller.affich_fenetre("BibliothequeUL")).pack(side = "bottom")
        b1frame = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520') #frame pour le bouton de recherche
        b1frame.place(x = 100,y = 450)
        eButton = Button(b1frame, text = "Emprunter" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack(side="left" ,padx = 5)
        lButton = Button(b1frame, text ="Réserver" , width = 30, bg ='#DAA520', relief = FLAT, fg = 'white').pack(side = "right", padx = 5)
      


        

        list_frame = Frame(self.canvas)
        list_frame.place(x=300, y=100)
       
        #=======================Listebox pour les livres====================================
        liste1 = Listbox(list_frame, width =50)
        for x in range(100):
            liste1.insert(END, "Livre "+str(x))
        liste1.pack( side = "left" , fill ="y")
        #==========================scrollbar pour la page et la liste========================
        list_scroll = Scrollbar(list_frame, orient ="vertical")
        list_scroll.config(command = liste1.yview)
        list_scroll.pack(side ="right", fill ="y")
         #===============configiration du scrollbar============================
        liste1.config(yscrollcommand = list_scroll.set)

class Electromagnetique(Frame):
    
     def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        Elentree = StringVar()

         #===================canvas de 'arrière plan ====================================
        w,h = 800, 500

        self.image = PhotoImage(file='female.png', master=self)

        self.canvas = Canvas(self, width = w, height = h)

        self.canvas.pack(fill ="both" , expand=True)

        self.canvas.create_image((w//2 , h//2), image = self.image)

        self.logo = PhotoImage(file='logo1.png', master = self)
        logo_label= Label(self.canvas , image = self.logo)
        logo_label.place( y = 650)
        

        labelm = Label(self.canvas, text="Electromagnetique", bg='#DAA520')
        labelm.pack(side = "top", fill = "x")
        tframe = Frame(self.canvas, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
        tframe.place( x = 300 , y = 20)
        requete = Entry(tframe, textvariable = Elentree , width = 50).pack()
        bframe = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520',)
        bframe.place(x =0 , y =20)
        sButton = Button(bframe, text = "Rechercher" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack()
        rButton = Button(bframe, text = "Retour" ,width =30, bg='#DAA520',relief =FLAT,fg='white', command = lambda:controller.affich_fenetre("BibliothequeUL")).pack(side = "bottom")
        b1frame = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520') #frame pour le bouton de recherche
        b1frame.place(x = 100,y = 450)
        eButton = Button(b1frame, text = "Emprunter" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack(side="left" ,padx = 5)
        lButton = Button(b1frame, text ="Réserver" , width = 30, bg ='#DAA520', relief = FLAT, fg = 'white').pack(side = "right", padx = 5)

        list_frame = Frame(self.canvas)
        list_frame.place(x=300, y=100)
       
        #=======================Listebox pour les livres====================================
        liste1 = Listbox(list_frame, width =50)
        for x in range(100):
            liste1.insert(END, "Livre "+str(x))
        liste1.pack( side = "left" , fill ="y")
        #==========================scrollbar pour la page et la liste========================
        list_scroll = Scrollbar(list_frame, orient ="vertical")
        list_scroll.config(command = liste1.yview)
        list_scroll.pack(side ="right", fill ="y")
         #===============configiration du scrollbar============================
        liste1.config(yscrollcommand = list_scroll.set)

class Optique(Frame):
     def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        Opentree= StringVar()

         #===================canvas de 'arrière plan ====================================
        w,h = 800, 500

        self.image = PhotoImage(file='female.png', master=self)

        self.canvas = Canvas(self, width = w, height = h)

        self.canvas.pack(fill ="both" , expand=True)

        self.canvas.create_image((w//2 , h//2), image = self.image)

        self.logo = PhotoImage(file='logo1.png', master = self)
        logo_label= Label(self.canvas , image = self.logo)
        logo_label.place( y = 650)

        
        labelm = Label(self.canvas, text="Optique", bg='#DAA520')
        labelm.pack(side = "top", fill = "x")
        tframe = Frame(self.canvas, borderwidth = 2 , relief = GROOVE , bg ='white', width = 105 , height =105)
        tframe.place( x = 300 , y = 20)
        requete = Entry(tframe, textvariable = Opentree , width = 50).pack()
        bframe = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520',)
        bframe.place(x =0 , y =20)
        sButton = Button(bframe, text = "Rechercher" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack()
        rButton = Button(bframe, text = "Retour" ,width =30, bg='#DAA520',relief =FLAT,fg='white', command = lambda:controller.affich_fenetre("BibliothequeUL")).pack(side = "bottom")
        b1frame = Frame(self.canvas, borderwidth = 2 , relief = FLAT , width = 20, height =100,bg='#DAA520') #frame pour le bouton de recherche
        b1frame.place(x = 100,y = 450)
        eButton = Button(b1frame, text = "Emprunter" ,width =30, bg='#DAA520',relief =FLAT,fg='white').pack(side="left" ,padx = 5)
        lButton = Button(b1frame, text ="Réserver" , width = 30, bg ='#DAA520', relief = FLAT, fg = 'white').pack(side = "right", padx = 5)
      


        list_frame = Frame(self.canvas)
        list_frame.place(x=300, y=100)
       
        #=======================Listebox pour les livres====================================
        liste1 = Listbox(list_frame, width =50)
        for x in range(100):
            liste1.insert(END, "Livre "+str(x))
        liste1.pack( side = "left" , fill ="y")
        #==========================scrollbar pour la page et la liste========================
        list_scroll = Scrollbar(list_frame, orient ="vertical")
        list_scroll.config(command = liste1.yview)
        list_scroll.pack(side ="right", fill ="y")
        #===============configiration du scrollbar============================
        liste1.config(yscrollcommand = list_scroll.set)
        
if __name__=="__main__":
    app = Fen_principale()
    app.title("Bibliothèque Universitaire")
    app.geometry("800x600+300+500")
    app.mainloop()
