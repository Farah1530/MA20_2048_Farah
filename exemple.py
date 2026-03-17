# exemple d'utilisation des touches
# JCY jan 2024

from tkinter import *
from tkinter import messagebox

#affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction
def key_pressed(event) :

    touche=event.keysym #récupérer le symbole de la touche
    messagebox.showinfo("On bouge", "Et vous avez pressé la touche : " + touche)
    if (touche=="Right" or touche=="d" or touche=="D"):
        messagebox.showinfo("On va à droite", "Et vous avez pressé la touche : " + touche)
    if (touche=="Left" or touche=="a" or touche=="A"):
        messagebox.showinfo("On va à gauche", "Et vous avez pressé la touche : " + touche)
    if (touche=="Up" or touche=="w" or touche=="W"):
        messagebox.showinfo("On va en haut", "Et vous avez pressé la touche : " + touche)
    if (touche=="Down" or touche=="s" or touche=="S"):
        messagebox.showinfo("On va en bas", "Et vous avez pressé la touche : " + touche)
    if (touche=="Q" or touche=="q"):
        result=messagebox.askokcancel("Confirmation", "vraiment quitter ?")
        if result:
            quit()
    if (touche=="x"):
        messagebox.showinfo("On va en x", "Et vous avez pressé la touche : " + touche)
          
def key_unique(event):
    messagebox.showinfo("x","ça c'est le x")

# Construction de la fenêtre :
win = Tk()
win.geometry("600x200")
win.title('Utilisation des touches')

#Création du label arrière
label_back=Label(win,text="Essayez les flèches et asdw", width=40, height=2,  bg="lightblue")
label_back.pack()


win.bind('<Key>', key_pressed) #on traite les touches clavier

# traitement d'une touche unique
win.bind('x',key_unique)

win.mainloop()




















#mettre fin de jeux qaund c est fini
def jeu_fini():
    # vérifier si il y a encore des cases vides
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False  # encore des cases vides, pas fini
    
    # vérifier si des fusions sont encore possibles (horizontal)
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                return False  # fusion possible, pas game over
    
    # vérifier si des fusions sont encore possibles (vertical)
    for i in range(3):
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                return False  # fusion possible, pas fini
    
    return True  # grille pleine + aucune fusion possible = le jeux est terminer