#Farah
#2048
#10.03.206

import tkinter as tk
import random
import tkinter.messagebox as messagebox
import random
import copy

# création de la fenêtre principale
window = tk.Tk()

# titre de la fenêtre
window.title("2048")

# largeur et hauteur de la fenêtre
window_width = 800
window_height = 800

# couleur de fond de la fenêtre
window.configure(bg='black')
   
# récupération de la taille de l'écran pour centrer la fenêtre
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# calcul de la position pour centrer la fenêtre
x_left = int(screen_width/2 - window_width/2)
y_top = int(screen_height/2 - window_height/2)

# application de la taille et de la position
window.geometry(f"{window_width}x{window_height}+{x_left}+{y_top}")

# pour afficher le titre dans tkinter
lbl = tk.Label(window, text="2048", font=("Arial", 15), bg="black", fg="green")
lbl.pack(pady=20)

#pour afficher le score pour l instant y a rien dans le score
lbl2 = tk.Label(window, text="score", font=("Arial", 15), bg="black", fg="yellow")
lbl2.pack(pady=10, padx=10)


#le score sert a compter le nombre de point 
score = 0
deja_gagne = False

def recommencer():
    global grid
    global score
    global deja_gagne
    score = 0
    deja_gagne = False
    grid= [[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
    add_tile()
    add_tile()
    update_board()
#je fais le btn recommencer 
btn_recommencer = tk.Button (window,text="recommencer", font = ("arial",15), bg="black", fg="#008888", command=recommencer)
btn_recommencer.pack(pady=10)

#le btn quitter pour que je puisse quitter 
def quitter_le_jeu():
    sauvegarder_score()
    window.destroy()
    
# sur le bouton
btn_quitter = tk.Button(window, text="quitter", font=("arial", 15), bg="black", fg="red", command=quitter_le_jeu)
btn_quitter.pack(pady=10)




# classe de tableau qui contient les couleurs des tuiles
class board:
    # couleur de fond selon la valeur
    bg_color = {
        2: "#FFE6CC",
        4: "#FFCC99",
        8: "#FFB366",
        16: "#FF9933",
        32: "#FF8000",
        64: "#f67c5f",
        128: "#994C00",
        256: "#CC6600",
        512: "#663300",
        1024: "#331A00",
        2048: "#990000",
        4096: "#660000",
        8192: "#330000",
    }

    # blanc pour toutes les numéro de tuiles qui ecrit en blanc
    text_color = {
        2: "#FFFFFF",
        4: "#FFFFFF",
        8: "#FFFFFF",
        16: "#FFFFFF",
        32: "#FFFFFF",
        64: "#FFFFFF",
        128: "#FFFFFF",
        256: "#FFFFFF",
        512: "#FFFFFF",
        1024: "#FFFFFF",
        2048: "#FFFFFF",
        4096: "#FFFFFF",
        8192: "#FFFFFF",
    }


# tableau qui contiendra les widgets Label pour afficher les tuiles
cells = [[None, None, None, None],
         [None, None, None, None],
         [None, None, None, None],
         [None, None, None, None]]

# frame qui contient la grille visuelle
frame = tk.Frame(window, bg="white")
frame.pack(pady=0)



# création des cases visuelles (labels)
for col in range(4):
    for li in range(4):
        cell = tk.Label(
            frame,
            text="",               # texte vide au début
            width=6,               # largeur de la case
            height=3,              # hauteur de la case
            font=("Arial", 20, "bold"),     # police et taille du texte
            fg="white",            # couleur du texte
        )
        cell.grid(row=col, column=li, padx=1, pady=2)
        cells[col][li] = cell

# fonction qui ajoute une tuile (2 ou 4) dans une case vide
# cette fonction cherche une case vide au hasard et y place un 2 ou un 4
def add_tile():
    empty = [] #pour cette fonction je me suis aider avc l'ia
    for col in range(4):
        for li in range(4):
            if grid[col][li] == 0:
                empty.append((col, li))

    if empty:
        col, li = random.choice(empty)
        grid[col][li] = random.choice([2, 4])
        update_board()




# fonction qui met à jour l'affichage des tuiles a chaque fois qu'on ouvre ou ferme la fenetre
# parcourt toutes les cases de la grille et applique les couleurs correspondantes
def update_board():
    meilleur_score= lire_meilleur_score()
    lbl2.config(text=f"Score : {score}   | Meilleur_score : {meilleur_score}")
    for i in range(4):
        for j in range(4):
            value = grid[i][j]

            # si la case est vide
            if value == 0:
                cells[i][j].config(text="", bg="#616161")
            else:
                # couleur de fond selon la valeur
                bg = board.bg_color.get(value, "#616161")
                # couleur de texte selon la valeur
                fg = board.text_color.get(value, "#FFFFFF")
                # applique le texte et les couleurs a la case
                cells[i][j].config(text=str(value), bg=bg, fg=fg)

#permet de tasser les tuilles
def pack4(a, b, c, d):
    # on met les 4 éléments dans une liste
    global score
    if c == 0:
        c = d
        d = 0
    if b == 0:
        b = c
        c = d
        d = 0
    if a == 0:
        a = b
        b = c
        c = d
        d = 0
    if a == b and a !=0:
        a = 2*a
        score += a
        b = c
        c = d 
        d = 0   
    if b == c and b !=0:
        b = 2*b
        score += b
        c = d
        d = 0
    if c == d and c !=0:
        c = 2*c
        score += c
        d = 0

    return (a, b, c, d)
#tasser tout le jeu dans une direction 

print (pack4(0,0,0,2))  # devrait afficher (2, 0, 0, 0)
print (pack4(0,0,2,2))  # devrait afficher (4, 0, 0, 0)
print (pack4(2,0,2,2))  # devrait afficher (4, 2, 0, 0)
print (pack4(2,2,2,2))  # devrait afficher (4, 4, 0, 0)
print (pack4(2, 2, 4, 0))  # devrait afficher (4, 4, 0, 0)
print (pack4(8,8,8,8))  # devrait afficher (16, 16, 0, 0)
print (pack4(2,2,0,2))  # devrait afficher (4, 2, 0, 0)
print (pack4(16,4,0,8))  # devrait afficher (32, 8, 0, 0)

#faire la direction vers le bas il faut un pack4 entre le premier et le deuxieme faux qu ils soient identique sinon sa marche pas 
#j avais un bug c etais avc le tassement normale mtn ca marche 
def down():    #pour aller vers le bas
    for col in range(4):
        (grid[3][col], grid[2][col], grid[1][col], grid[0][col]) = pack4(grid[3][col], grid[2][col], grid[1][col], grid[0][col])
    update_board()
#pour aller vers le haut
def up():
    for col in range (4):
        (grid[0][col], grid[1][col], grid[2][col], grid[3][col]) = pack4(grid[0][col], grid[1][col], grid[2][col], grid[3][col])
    update_board()
#pour aller vers la gauche
def left():
    for ligne in range(4):
        (grid[ligne][0], grid[ligne][1], grid[ligne][2], grid[ligne][3]) = pack4(grid[ligne][0], grid[ligne][1], grid[ligne][2], grid[ligne][3])
    update_board()
#pour aller vers la droite
def right():
    for ligne in range(4):
        (grid[ligne][3], grid[ligne][2], grid[ligne][1], grid[ligne][0]) = pack4(grid[ligne][3], grid[ligne][2], grid[ligne][1], grid[ligne][0])
    update_board()



#affectation des touches aux fonctions, q pour quitter, le reste pour "tasser" dans une certaine direction
def key_pressed(event) :
    gagné=False
    touche=event.keysym #récupérer le symbole de la touche
    m_grid = copy.deepcopy(grid)#memoriser le tableau grid
    print(m_grid)
    if (touche=="Right" or touche=="d" or touche=="D"):
        right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        left()
    if (touche=="Up" or touche=="w" or touche=="W"):
        up()
    if (touche=="Down" or touche=="s" or touche=="S"):
        down()
    print(grid)
    print (m_grid)
    if m_grid != grid:#si le tableau a changer il fait apparaitre un 2 ou un 4
        apparition_de_tuiles()
        resultat = gagné_ou_perdu()
        if resultat == "gagné":
            recommencer()
        elif resultat ==True:
            update_board()
            perdu()
            recommencer()            
    update_board()
    if (touche=="Q" or touche=="q"):
        result=messagebox.askokcancel("Confirmation", "vraiment quitter ?")
        if result:
            quit()




#apparition aléatoire de tuiles de 2 ou de 4
def apparition_de_tuiles():
    # choisir si c'est un 2 ou un 4 (avecv 80% de chance pour le 2)
    tb= [2,2,2,2,4,]
    n=random.choice(tb)
    print(n)
#trouve toutes les case vides 
    case_vide = [] #la variable de la case vide
    for col in range (4):  # il parcourt la partie colonne
        for li in range (4): # il parcourt la partie ligne 
            if grid[li][col]==0: # la on fait si le grid li et col parcouru mettre 
                case_vide.append((li,col)) #la c est pour ajouter la case vide
                print(case_vide)  #c est pour voir dans la console

    (li,col)= random.choice(case_vide)  
    grid[li][col]=n




#maintenant je vais faire une fonction qui affiche quand le jeu est terminer

def gagné_ou_perdu():

    # vérifier si y a un 2048 dans la grille
    # par
    for li in range(4):
        for col in range(4):
            if grid[li][col] == 2048:
                global deja_gagne
                if deja_gagne == False:
                    deja_gagne = True
                    reponse = messagebox.askyesno("gagné", "bien joué t as gagné est ce que tu veux continuer?")
                    if reponse:
                     return False
                    else:
                        return "gagné"


    for li in range (4):   #il verifie les colonnes si elles sont vide ou pas
        for col in range (4):  # il verifie les ligne si elle sont vide ou pas 
            if grid [li][col] == 0: #et si le grid li et col est vide returne faux ducoup c est pas fini
                return False
      #on verifie si c est y a des possibilité de fusion en horizentale
    for li in range (4): #il verifie les lignes si elles sont vide ou pas
        for col in range (3): # il verifie les colonnes si elle sont vide ou pas 
            if grid [li][col] == grid [li][col +1]:  #et si le grid li et col est vide returne faux ducoup c est pas fini
                return False
          
    
#on verifie si c est y a des possibilité de fusion en horizentale
    for li in range (3): #il verifie les ligne si elles sont vide ou pas
        for col in range (4): # il verifie les colonnes si elle sont vide ou pas 
            if grid [li][col] == grid [li +1][col]:
                return False



    return True      #quand c est vrai 


    
def perdu():
    print("perdu")   # pour voir le msg perdu dans le terminal
    #c est le messagebox qui permet d affiche une quoi perdu et le jeux s arrete
    #quit ()      #le jeux s arrete 
    sauvegarder_score()
    meilleur_score= lire_meilleur_score()
    messagebox.showinfo("perdu", f"t as perdu nullllll\nTon score : {score}\nMeilleur score : {meilleur_score}")
    





def lire_meilleur_score():
    try:
        with open("meilleur_score.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def sauvegarder_score():
    meilleur = lire_meilleur_score()
    if score > meilleur:
        with open("meilleur_score.txt", "w") as f:
            f.write(str(score))










window.bind('<Key>', key_pressed) #on traite les touches clavier


# placer tous les numéros dans la grille avec leurs couleurs
# on a tous les numéros du jeu a afficher
#2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192

numeros = [2, 2, 2, 2,]

# remplir la grille avec tous les numéros
#grid= [[2,2,4,4],
        #[2,2,4,4],
       #[4,4,2,2],
       #[0,2,0,0]]
grid= [[2,2,4,4],
       [2,2,4,4],
       [4,4,2,2],
       [0,2,0,0]]

# mettre a jour l affichage pour montrer tous les numéros
update_board()
apparition_de_tuiles()

# boucle principale Tkinter
window.mainloop()