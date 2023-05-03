import tkinter as tk
from tkinter import messagebox

class Allo_Ameni_test(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Annuaire")
        self.geometry("300x200")

        # Création des champs de saisi
        self.champNom = tk.Entry(self)
        self.champNom.pack()
        self.champTel = tk.Entry(self)
        self.champTel.pack()

        # Création des boutons
        self.boutonAjouter = tk.Button(self, text="Ajouter", command=self.cb_ajouter)
        self.boutonAjouter.pack(side=tk.LEFT)

        self.boutonSupprimer = tk.Button(self, text="Supprimer", command=self.cb_supprimer)
        self.boutonSupprimer.pack(side=tk.LEFT)

        self.boutonAfficher = tk.Button(self, text="Afficher", command=self.cb_afficher)
        self.boutonAfficher.pack(side=tk.LEFT)

    def changeChamps(self, nom, tel):
        # Modification d'affichage dans le champ de saisi
        self.champNom.delete(0,tk.END)
        self.champNom.insert(0,nom)
        self.champTel.delete(0,tk.END)
        self.champTel.insert(0,tel)
        self.champNom.focus()

    def effaceChamps(self):
        # Effacer des champs de saisi
        self.changeChamps('','')

    def valeurChamps(self):
        nom = self.champNom.get()
        tel = self.champTel.get()
        return nom, tel

    def alerte(self, titre, message):
        messagebox.showinfo(titre, message)

    # Méthodes à redéfinir dans l'application
    # Action liée aux boutons
    def cb_ajouter(self):
        # Ajout dans la liste de contenu dans le champ de saisi
        raise NotImplementedError("cb_ajouter a redefinir")

    def cb_supprimer(self):
        # Suppression dans la liste de contenu dans le champ de saisi
        raise NotImplementedError("cb_supprimer a redefinir")

    def cb_afficher(self):
        # Affichage dans la liste de contenu dans le champ de saisi
        raise NotImplementedError("cb_afficher a redefinir")

    # Autotest
if __name__=='__main__':
        app =Allo_Ameni_test()
        app.mainloop()
