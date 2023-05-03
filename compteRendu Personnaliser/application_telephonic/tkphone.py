''' on se propose de crer un scipt de gestion d'un carnet telephonique.
on peut consevoir 3 zone
fame superieur :dediée a l'affichage
frame(zone)médiane contenant une liste alphabetique ordonnée 
frame inferieu de bouton de gesion de la liste
positionner l'une sous l'autre grace au packer
'''
#importation des bibliothque specifique qui va nous aider a faire l'application
#importe le module Tkinter sous le  cette  bibliothèque dans le reste du code
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Allo_Ameni(tk.Tk): # type: ignore
    def __init__(self):#constructeur
        self.root=tk.Tk()# fenetre de l'application
        self.root.title("Repertoire Telephonique")
        self.root.config(relief=tk.RAISED,bd=3)
        self.construireWidgets()

    def boucleEvennementielle(self):
        self.champNom.focus()# focus => le curseur sera automatiquement sur le chmpNom
        self.root.mainloop()# demarer le boucle principale

    def construireWidgets(self):
        """configuration et positionnement des widgets
        conception du frame superieur"""
        frameH = ttk.Frame(self.root)
        #crer une frame a l'interieur de la fenetre principal self.root
        frameH.pack(fill=tk.X)
        # prendre tt largeur x de la fenetre parent
        frameH.columnconfigure(1,weight=0)# le colonne 1 de la frame des champ de text sont fix
                                           #weight peux prendre 0(champ_fixe) ou1(champs redimentionnable)

        ttk.Label(frameH,text="nom:").grid(row=0,column=0 ,sticky=tk.E)
        self.champNom=tk.Entry(frameH)
        self.champNom.grid(row=0, column=1, sticky=tk.EW,padx=5,pady=10)

        ttk.Label(frameH,text="Tel:").grid(row=1,column=0 ,sticky=tk.E)
        self.champTel=tk.Entry(frameH)
        self.champTel.grid(row=1, column=1, sticky=tk.EW,padx=5,pady=10)

        b=ttk.Button(frameH,text="effacer",command=self.effaceChamps)
        b.grid(row=2 ,column=0 , columnspan=2 ,pady=3)
        
        #conception de la zone médiane
        #creation d'un frame associer au fenetre principal
        frameM=ttk.Frame(self.root)

        frameM.pack(fill=tk.BOTH ,expand=True)
           # frame.pack => l'apparence dans la fenetre
           #ajouter le frame a la fenetre et elargir dans les deux sens horizontal et vertical
        self.scroll=ttk.Scrollbar(frameM)
         #crer un scrollbar et ajouter au frame
        self.listeSelection= tk.Listbox(frameM , yscrollcommand=self.scroll.set, height=6)
          # crer un nouveau listebox et ajouter au frameM
        self.scroll.config(command=self.listeSelection.yview)
         #configurer le scrollbar en utilisant yview qui permet faire la mouvement en haut et en bas
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y,pady=5)
        self.listeSelection.pack(side=tk.LEFT, fill=tk.BOTH,expand=True,pady=5)
        self.listeSelection.bind("<Double-Button-1>", lambda event:self.cb_afficher())
        
        #conception de la zone infeieu qui contient les boutons
        frameB=ttk.Frame(self.root)
        frameB.pack(pady=3, side=tk.BOTTOM , fill=tk.NONE) 

        b1=ttk.Button(frameB, text="Ajouter", command=self.cb_ajouter)
        b2=ttk.Button(frameB, text="Supprimer", command=self.cb_supprimer)
        b3=ttk.Button(frameB, text="Afficher", command=self.cb_afficher)
        b1.pack(side=tk.LEFT, pady=3)
        b2.pack(side=tk.LEFT, pady= 3)
        b3.pack(side=tk.LEFT, pady=2)
    #creation des methodes d'échange d'information de l'application
    def majlistselectionner(self, lstnoms):
        #remplissage compet de la liste de selection par les nom
        self.listeSelection.delete(0,tk.END)
        for nom in lstnoms:
            self.listeSelection.insert(tk.END, nom)
    def indexselection(self):
        #retourner le numero de la ligne selectionner
        return int(self.listeSelection.curselection()[0])         
    def changeChamps(self, nom, tel):
        #modification d'affichage dans le champ de saisi
        self.champNom.delete(0,tk.END)
        self.champNom.insert(0,nom) # type: ignore
        self.champTel.delete(0,tk.END)
        self.champTel.insert(0,tel)
        self.champNom.focus()

    def effaceChamps(self):
        #effacer des champs de saisi
        self.changeChamps('','')
    
    def valeurChamps(self):
        nom=self.champNom.get()
        tel=self.champTel.get()
        return nom ,tel
    def alerte(self , titre, message):
        messagebox.showinfo(titre,message)

 #methode a redefinir dans l'application
 #action liée aux boutons
    def cb_ajouter(self):
          #ajout dans la liste de contenue dans le champs de saisi
          raise NotImplementedError("cb_ajouter a redefinir")
    def cb_supprimer(self):
          #ajout dans la liste de contenue dans le champs de saisi
          raise NotImplementedError("cb_supprimer a redefinir")
    def cb_afficher(self):
          #ajout dans la liste de contenue dans le champs de saisi
          raise NotImplementedError("cb_afficher a redefinir")
    # autotest
if __name__=='__main__':
    app =Allo_Ameni()
    app.boucleEvennementielle()