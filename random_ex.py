import tkinter as tk
import random
import math

labels = []
bars = []
canvas_height = 200
canvas_width = 360

def afficher(resultats,nb):

    pourcents = []

    for i in range(6):
        p = resultats[i] * 100 / nb
        pourcents.append(p)

        labels[i]["text"] = f"{i+1} : {p:.2f} %"

        h = p/30 * canvas_height

        x1 = 10 + i*60
        x2 = x1 + 40

        canvas.coords(bars[i],x1,canvas_height-h,x2,canvas_height)

    # calcul écart-type
    moyenne = sum(pourcents)/6
    variance = sum((p-moyenne)**2 for p in pourcents)/6
    ecart = math.sqrt(variance)

    label_std["text"] = f"écart-type des % : {ecart:.3f}"


def lancer(methode):

    nb = int(entry_nb.get())

    res = [0]*6

    for _ in range(nb):

        if methode=="randint":
            n = random.randint(1,6)

        elif methode=="choice":
            n = random.choice([1,2,3,4,5,6])

        elif methode=="randrange":
            n = random.randrange(1,7)

        res[n-1]+=1

    afficher(res,nb)


root = tk.Tk()
root.title("Simulation de dé")

frame = tk.Frame(root)
frame.pack(padx=10,pady=10)

tk.Label(frame,text="Nombre de tirages").grid(row=0,column=0)

entry_nb = tk.Entry(frame,width=8)
entry_nb.insert(0,"1000")
entry_nb.grid(row=0,column=1)

tk.Button(frame,text="randint()",width=12,
          command=lambda:lancer("randint")).grid(row=1,column=0,padx=5)

tk.Button(frame,text="choice()",width=12,
          command=lambda:lancer("choice")).grid(row=1,column=1,padx=5)

tk.Button(frame,text="randrange()",width=12,
          command=lambda:lancer("randrange")).grid(row=1,column=2,padx=5)

canvas = tk.Canvas(frame,width=canvas_width,height=canvas_height,bg="white")
canvas.grid(row=2,column=0,columnspan=6,pady=10)

for i in range(6):
    bar = canvas.create_rectangle(0,0,0,0,fill="steelblue")
    bars.append(bar)

for i in range(6):
    lab = tk.Label(frame,text=f"{i+1} : 0 %",width=10)
    lab.grid(row=3,column=i)
    labels.append(lab)

label_std = tk.Label(frame,text="écart-type : 0")
label_std.grid(row=4,column=0,columnspan=6,pady=5)

root.mainloop()