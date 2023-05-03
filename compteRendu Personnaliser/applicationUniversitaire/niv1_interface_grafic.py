import os
import sys
import customtkinter
import tkinter
print("bnj nv cour customtkinter")


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

def button_function2():
    print("button 2 pressed")

def afficher_liste_des_prof():
      professeurs_list = ['yohan Amar', 'Marie Martin', 'Pierre Durand', 'Lucie Dubois']
       # Utilisation de la liste à l'intérieur de la méthode
      for professeur in professeurs_list :
       print(professeur)

def afficher_dictionnaire_des_prof(professeurs):
     
       # Utilisation de la liste à l'intérieur de la méthode
      for professeur in professeurs : #comment utiliser un dictionnaire declarer en dehor de la methode
       print(professeur['yohan Amar'])

  
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Button de l'interface 1 ", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app, text="Button de l'interface 2 ", command=afficher_liste_des_prof)
button.place(relx=0.5, rely=0.7 , anchor=tkinter.CENTER)
app.mainloop()