
import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from tkinter import *
from collections import namedtuple
from os.path import isfile
import clientCR

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

separateur='\t'
ligneRep= namedtuple("ligneRep","nom tel")
#creation du classe principale
class InterfaceClient(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Application de gestion des informations clientels")
        self.liste_clients = []
        self.create_Interface_ajout_client()

   
    def create_Interface_ajout_client(self):
        # Création des étiquettes et champs de saisie
                # Création des étiquettes et champs de saisie
        label_formulaire = tk.Label(
            self,
            text="Remplir le formulaire concernant votre client attentivement:",
            font=("arial", 20),
            bg="#1FB3AD",
            fg="white",
        )
        label_formulaire.grid(row=0, column=0)

        self.framec = tk.Frame(self)
        self.framec.grid(row=2, column=0)
        self.framec.config(width=250,height=50,bg='#1FB3AD')

        label_nom = tk.Label(
            self.framec, text="Nom du client:", font=("arial", 15), bg="#1FB3AD", fg="white"
        )
        label_nom.grid(row=1, column=0)
        self.framec.champ_nom = tk.Entry(self.framec, width=50)
        self.framec.champ_nom.grid(row=1, column=1)

        label_prenom = tk.Label(
            self.framec,
            text="Prénom:",
            width=20,
            font=("arial", 15),
            bg="#1FB3AD",
            fg="white",
        )
        label_prenom.grid(row=2, column=0)
        self.framec.champ_prenom = tk.Entry(self.framec, width=50)
        self.framec.champ_prenom.grid(row=2, column=1)

        label_age = tk.Label(
            self.framec, text="Âge:", font=("arial", 15), bg="#1FB3AD", fg="white"
        )
        label_age.grid(row=3, column=0)
        self.framec.champ_age = tk.Entry(self.framec, width=50)
        self.framec.champ_age.grid(row=3, column=1)

        label_tel = tk.Label(
            self.framec, text="Tel:", font=("arial", 15), bg="#1FB3AD", fg="white"
        )
        label_tel.grid(row=4, column=0)
        self.framec.champ_tel = tk.Entry(self.framec, width=50)
        self.framec.champ_tel.grid(row=4, column=1)

        label_adresse = tk.Label(
            self.framec, text="Adresse:", font=("arial", 15), bg="#1FB3AD", fg="white"
        )
        label_adresse.grid(row=5, column=0)
        self.framec.champ_adresse = tk.Entry(self.framec, width=50)
        self.framec.champ_adresse.grid(row=5, column=1)

        label_montantA = tk.Label(
            self.framec,
            text="Montant d'achat:",
            font=("arial", 15),
            bg="#1FB3AD",
            fg="white",
        )
        label_montantA.grid(row=6, column=0)
        self.framec.champ_montantA = tk.Entry(self.framec, width=50)
        self.framec.champ_montantA.grid(row=6, column=1)

        self.frameb = tk.Frame(self)
        self.frameb.grid(row=7, column=0)
        self.frameb.config(width=250,height=50,bg='#1FB3AD')

        self.frameb.bouton_ajouter = tk.Button(self.frameb, text="Ajouter", width=15, font=20, fg='#1FB3AD', command=self.ajouter_client)
        self.frameb.bouton_ajouter.grid(row=7, column=0, padx=10, pady=10)

        """self.frameb.bouton_modifier = tk.Button(self.frameb, text="Modifier", width=15, font=20, fg='#1FB3AD', command=self.modifier_client)
        self.frameb.bouton_modifier.grid(row=7, column=3, padx=10, pady=10)
        """
        self.frameb.bouton_supprimer = tk.Button(self.frameb, text="Supprimer", width=15, font=20, fg='#1FB3AD', command=self.supprimer_client)
        self.frameb.bouton_supprimer.grid(row=7, column=1, padx=10, pady=10)

        self.frameb.bouton_afficher = tk.Button(self.frameb, text="Afficher", width=15, font=20, fg='#1FB3AD', command=self.afficher_client)
        self.frameb.bouton_afficher.grid(row=7, column=2, padx=10, pady=10)

        
        self.framed = tk.Frame(self)
        self.framed.grid(row=8, column=0)
        self.framed.config(width=250,height=50,bg='#1FB3AD')

        self.framed.scroll = tk.Scrollbar(self.framed)

        self.framed.listeSelection = tk.Listbox(self.framed, yscrollcommand=self.framed.scroll.set, width=130, height=8)
        self.framed.scroll.config(command=self.framed.listeSelection.yview)
        self.framed.scroll.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
        self.framed.listeSelection.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)
        self.framed.listeSelection.bind("<Double-Button-1>", lambda event: self.framed.afficher_client())
    
        
    def ajouter_client(self):
            nom = self.framec.champ_nom.get()
            prenom = self.framec.champ_prenom.get()
            age = self.framec.champ_age.get()
            tel = self.framec.champ_tel.get()
            adresse = self.framec.champ_adresse.get()
            montantA = self.framec.champ_montantA.get()
            if nom == "" or prenom == "" or age == "" or tel == "" or adresse == "" or montantA == "":
             messagebox.showerror("Erreur", "Il faut remplir tous les champs")
            else:
                clt = clientCR.Clients(nom, prenom, age, tel, adresse, montantA)
                self.liste_clients.append(clt)
                messagebox.showinfo("Succès de l'ajout", "Le client a été ajouté avec succès")
                self.vider_champs()
                self.afficher_client()
    def supprimer_client(self):
            nom = self.framec.champ_nom.get()
            prenom = self.framec.champ_prenom.get()
            age = self.framec.champ_age.get()
            tel = self.framec.champ_tel.get()
            adresse = self.framec.champ_adresse.get()
            montantA = self.framec.champ_montantA.get()
            if nom == "" and prenom == "" and age == "" and tel == "" and adresse == ""and montantA == "":
             messagebox.showinfo("avertissement", " tous les champs sont vide deja")
            else:
                index = self.liste_clients.curselection()[0]
                clt = self.liste_clients[index]
                self.liste_clients.remove(clt)
                messagebox.showinfo("Succès de la suppression", "Le client {} a été supprimé avec succès de la liste des clients.".format(clt.nom))
                self.liste_clients.delete(0, tk.END)
                # Parcourir la liste des étudiants
                for clt in self.liste_clients:
                    # Ajouter le nom complet de l'étudiant à la listebox
                    self.liste_clients.insert(tk.END, f"{clt.nom} {clt.prenom}{clt.age} {clt.tel}{clt.adresse} {clt.montant}")

    
    def vider_champs(self):
                self.framec.champ_nom.delete(0, 'end')
                self.framec.champ_prenom.delete(0, 'end')
                self.framec.champ_age.delete(0, 'end')
                self.framec.champ_tel.delete(0, 'end')
                self.framec.champ_adresse.delete(0, 'end')
                self.framec.champ_montantA.delete(0, 'end')

   
        #effacer les champs de saisi
    def effaceChamps(self):
        #effacer des champs de saisi
        self.modifier_client('','','','','','')
   

    def afficher_client(self):
    
        if not self.liste_clients:
            messagebox.showwarning("Avertissement", "la liste des clients est vide.")
        else:
            message = "Liste des client :\n\n"
        for clt in self.liste_clients:
            message += f"Nom: {clt.nom} {clt.prenom}\n"
            message += f"Age: {clt.age} ans\n"
            message += f"n°TEl: {clt.tel}\n"
            message += f"adresse: {clt.adresse}\n"
            message += f"Montant D'achat effectuer: {clt.montant_achat}\n\n"
        messagebox.showinfo("Liste des clients", message)
            

    def modifier_client(self):
        #modification d'affichage dans le champ de saisi
        
        n=self.framec.champ_nom.get() 
        p=self.framec.champ_prenom.get()
        age=self.framec.champ_age.get()
        a=self.framec.champ_adresse.get()
        t=self.framec.champ_tel.get()
        m=self.framec.champ_montantA.get()
        # Vérifier si un client a été sélectionné
        if not self.listbox.curselection():
            return
        
        # Récupérer l'index du client sélectionné dans la listebox
        index = self.listbox.curselection()[0]
        
        # Récupérer le client correspondant à l'index
        client = self.clients[index]
        
        # Remplir les champs de saisie avec les données du client
        self.framec.champ_nom.delete(0, tk.END)
        if client.nom:
          self.framec.champ_nom.insert(0, client.nom)

        self.framec.champ_prenom.delete(0, tk.END)
        if client.prenom:
          self.framec.champ_prenom.insert(0, client.prenom)

        self.framec.champ_age.delete(0, tk.END)
        if client.age:
            self.framec.champ_age.insert(0, client.age)

        self.framec.champ_adresse.delete(0, tk.END)
        if client.adresse:
            self.framec.champ_adresse.insert(0, client.adresse)

        self.framec.champ_tel.delete(0, tk.END)
        if client.tel:
            self.framec.champ_tel.insert(0, client.tel)

        self.framec.champ_montantA.delete(0, tk.END)
        if client.montantA:
            self.framec.champ_montantA.insert(0, client.montantA)

        # Mettre le focus sur le premier champ de saisie
        self.after_idle(self.framec.champ_nom.focus)


           
   
#programme principale
if __name__ == "__main__":
        #app = customtkinter.CTk()  # create CTk window like you do with the Tk windowm
    app =InterfaceClient()
    app.geometry("850x450")
    app.config(background='#1FB3AD')
    app.mainloop()
