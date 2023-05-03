#importation des bibliothque
from collections import namedtuple
from os.path import isfile
from tkphone import Allo_Ameni
separateur='\t'
ligneRep= namedtuple("ligneRep","nom tel")
#definition de class
class Allo(Allo_Ameni):
    #repertoire telephonique
    def __init__(self,fic='phones.txt'):
        super().__init__()  #constructeur de class parent
        self.phoneList=[]
        self.fic=""
        self.chargerFichier(fic)

    def chargerFichier(self , nomfic):
        # chargement de la liste a partir d'un fichier repertoire
        self.fic=nomfic
        self.phoneList=[]
        if isfile(self.fic):
            with open(self.fic, encoding="utf8")as f:
                for line in f: 
                    nom, tel , *reste= line[:-1].split(separateur)[:2]
                    self.phoneList.append(ligneRep(nom , tel))
        else:
            with open(self.fic,"w", encoding="utf8"):
                pass
        self.phoneList.sort()
        self.majlistselectionner([x.nom for x in self.phoneList])
        
    def enregistrerFichier(self):
        """ engegistrer l'ensemble de la liste dans unn fichier"""
        with open(self.fic,"w",encoding="utf8")as f:
            for i in self.phoneList:
                f.write("%s%s%s\n" %(i.nom, separateur , i.tel))

    def ajouteFichier(self ,nom ,tel):
        # ajouter un enregistrement a la fin du fichier
        with open(self.fic,"a",encoding="utf8")as f: 
            f.write("%s%s%s\n"%(nom,separateur,tel))

    def cb_ajouter(self):
        nom , tel=self.valeurChamps()
        nom=nom.replace(separateur,'')
        tel=tel.replace(separateur,'')
        if(nom=="")or (tel==""):
            self.alerte("erreur", "il faut saisi le nom et le numero de telephone")
            return
        self.phoneList.append(ligneRep(nom,tel))
        self.phoneList.sort()
        self.majlistselectionner([x.nom for x in self.phoneList])
        self.ajouteFichier(nom , tel)
        self.effaceChamps()

    def cb_supprimer(self):
        nom , tel =self.phoneList[self.indexselection()]
        self.phoneList.remove(ligneRep(nom , tel))
        self.majlistselectionner([x.nom for x in self.phoneList])
        self.enregistrerFichier()
        self.effaceChamps()
    def cb_afficher(self):
        nom, tel= self.phoneList[self.indexselection()]
        self.changeChamps(nom , tel)
app=Allo()
app.boucleEvennementielle()


