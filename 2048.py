import tkinter as tk
import random

# création de la fenêtre principale
window = tk.Tk()

# titre de la fenêtre
window.title("2048")

# largeur et hauteur de la fenêtre
window_width = 600
window_height = 600

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


label = tk.Label(window, text="2048", font=("Arial", 15), bg="black", fg="green")
label.pack(pady=20)


label2 = tk.Label(window, text="score", font=("Arial", 15), bg="black", fg="yellow")
label2.pack(pady=10, padx=10)

label3 = tk.Label(window, text="Nouveau score", font=("Arial", 15), bg="black", fg="#008888")
label3.pack(pady=10, padx=10)

# classe qui contient les couleurs des tuiles
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

    # couleur du texte selon la valeur
    # blanc pour toutes les tuiles
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


# je crée la grille du jeu
grid = [[0 for _ in range(4)] for _ in range(4)]

# tableau qui contiendra les widgets Label pour afficher les tuiles
cells = [[None for _ in range(4)] for _ in range(4)]

# frame qui contient la grille visuelle
frame = tk.Frame(window, bg="white")
frame.pack(pady=0)


# création des cases visuelles (labels)
for i in range(4):
    for j in range(4):
        cell = tk.Label(
            frame,
            text="",               # texte vide au début
            width=6,               # largeur de la case
            height=3,              # hauteur de la case
            font=("Arial", 20, "bold"),     # police et taille du texte
            fg="white",            # couleur du texte
        )
        cell.grid(row=i, column=j, padx=1, pady=2)
        cells[i][j] = cell


# fonction qui ajoute une tuile (2 ou 4) dans une case vide
# cette fonction cherche une case vide au hasard et y place un 2 ou un 4
def add_tile():
    # liste des cases vides
    empty = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]

    # si il reste des cases vides
    if empty:
        i, j = random.choice(empty)   # choisir une case au hasard
        grid[i][j] = random.choice([2, 4])   # mettre un 2 ou un 4
        update_board()                # mettre à jour l'affichage


# fonction qui met à jour l'affichage des tuiles a chaque fois qu'on ouvre ou ferme la fenetre
# parcourt toutes les cases de la grille et applique les couleurs correspondantes
def update_board():
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


# placer tous les numéros dans la grille avec leurs couleurs
# on a tous les numéros du jeu a afficher
numeros = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

# remplir la grille avec tous les numéros
position = 0
for i in range(4):
    for j in range(4):
        if position < len(numeros):
            grid[i][j] = numeros[position]
            position += 1

# mettre a jour l affichage pour montrer tous les numéros
update_board()

# boucle principale Tkinter
window.mainloop()