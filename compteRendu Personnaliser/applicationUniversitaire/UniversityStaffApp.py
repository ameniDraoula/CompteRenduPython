import customtkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


class Etudiants:
    def __init__(self, nom, prenom, age ,niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.niveau=niveau

class UniversityStaffApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ajout d'étudiant a l'application UniversityStaffApp")
        self.liste_etudiants = []
        self.create_Interface_ajout_etudiant()

    def create_Interface_ajout_etudiant(self):
        # Création des étiquettes et champs de saisie
        label_nom = tk.Label(self, text=" donnez le nom de l'étudiant : ",
                              font=("arial", 15),
                                 bg="#250B6F",
                                 fg="white")
        label_nom.grid(row=0, column=0)
        self.champ_nom = tk.Entry(self,width=45)
        self.champ_nom.grid(row=0, column=1)

        label_prenom = tk.Label(self, text=" Donner le prénom de l'étudiant : ",
                                 font=("arial", 15),
                                 bg="#250B6F",
                                 fg="white")
        label_prenom.grid(row=1, column=0)
        self.champ_prenom = tk.Entry(self,width=45)
        self.champ_prenom.grid(row=1, column=1)

        label_age = tk.Label(self, 
                             text=" donnez l'Âge de l'étudiant : ",
                             font=("arial", 15),
                             bg="#250B6F",
                             fg="white"
                             )
        label_age.grid(row=2, column=0)
        self.champ_age = tk.Entry(self,width=45)
        self.champ_age.grid(row=2, column=1)

        label_niveau = tk.Label(self,
                                 text=" donnez le niveau de l'étudiant : ",
                                 font=("arial", 15),
                                 bg="#250B6F",
                                 fg="white")
        label_niveau.grid(row=3, column=0)
        self.champ_niveau = tk.Entry(self, width=45)
        self.champ_niveau.grid(row=3, column=1)

        # Création du bouton d'ajout et du bouton d'affichage
        bouton_ajouter = tk.Button(self, text="Buton Ajouter", width=30, font=20, fg='#250B6F', command=self.ajouter_etudiant)
        bouton_ajouter.grid(row=4, column=1 , padx=10, pady=10)

        bouton_afficher = tk.Button(self, text="Afficher la liste des étudiants", width=30, font=20, fg='#250B6F', command=self.afficher_etudiant)
        bouton_afficher.grid(row=5, column=1, padx=10, pady=10)
  

    def ajouter_etudiant(self):
        nom = self.champ_nom.get()
        prenom = self.champ_prenom.get()
        age = self.champ_age.get()
        niveau = self.champ_niveau.get()
        etudiant = Etudiants(nom, prenom, age, niveau)
        self.liste_etudiants.append(etudiant)
        messagebox.showinfo("Succès de l'ajout ", "L'étudiant {} a été ajouté avec succès a la liste des etudiant de cette univercité.".format(etudiant.nom))
    def supprimer_etudiant(self):
        index = self.listbox_etudiants.curselection()[0]
        etudiant = self.liste_etudiants[index]
        self.liste_etudiants.remove(etudiant)
        messagebox.showinfo("Succès de la suppression", "L'étudiant {} a été supprimé avec succès de la liste des étudiants de cette université.".format(etudiant.nom))
        self.actualiser_liste_etudiants()
        
    def afficher_etudiant(self):
        if not self.liste_etudiants:
            messagebox.showwarning("Avertissement", "la liste d'étudiant est vide.")
        else:
            message = "Liste des étudiants : \n"
            for etudiant in self.liste_etudiants:
               message += "nom: {} {},".format(etudiant.nom, etudiant.prenom)
               message += "Age: {} ans ,".format(etudiant.age)
               message += "De Niveau: {} \n".format(etudiant.niveau)
            messagebox.showinfo("Liste des étudiants", message)

if __name__ == "__main__":
    #app = customtkinter.CTk()  # create CTk window like you do with the Tk windowm
    app = UniversityStaffApp()
   
    app.geometry("850x250")
    app.config(background='#250B6F')
    app.mainloop()
    