"""Plot grafa krivulje drugog reda, te analiza o kojoj se krivulji radi isprintano na prikazu"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageTk,Image
from tkinter import *

root = Tk()
background = "#DDE0A9"
entry_background = "#F1F1F1"
root.title("Graf krivulje drugog reda")
root.geometry("1280x720+1+1")
root.configure(background=background)
def quit():
    root.quit()
    root.destroy()
def plot_graph():
    A = A_entry.get()
    C = C_entry.get()
    D = D_entry.get()
    E = E_entry.get()
    F = F_entry.get()

    if A != '' and C !='' and D != '' and E != '' and F != '':
        A = int(A)
        C = int(C)
        D = int(D)
        F = int(F)
        E = int(E)
        if (A == 0 or C == 0):
            object_type = "Parabola"
        elif (A == C):
            object_type = "Kruznica"
        elif (A * C < 0):
            object_type = "Hiperbola"
        elif (A * C > 0):
            object_type = "Elipsa"

        x = np.linspace(-10, 10, 500)
        y = np.linspace(-10, 10, 500)
        X, Y = np.meshgrid(x, y)

        G = A*X*X + C*Y*Y + D*X + E*Y + F
        fig,ax = plt.subplots()
        ax.contour(X, Y, G, levels=[15], colors='red') # take level set corresponding to 0
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        plt.title(str(object_type))
        plt.grid()
        plt.show()
    return

func_label = Label(root, text='F(x,y)=Ax^2 + Cy^2 + Dx + Ey + F', font=('Helvetica', 15), bg=background)
func_label.place(x=10, y=50, width=350, height=25)
A_label = Label(root, text='A',bg=background).place(x=60, y=150, width=10, height=25)
A_entry = Entry(root, bg=entry_background)
A_entry.place(x=75, y=150, width=100, height=25)
C_label = Label(root, text='C',bg=background).place(x=60, y=180, width=10, height=25)
C_entry = Entry(root, bg=entry_background)
C_entry.place(x=75, y=180, width=100, height=25)
D_label = Label(root, text='D',bg=background).place(x=60, y=210, width=10, height=25)
D_entry = Entry(root, bg=entry_background)
D_entry.place(x=75, y=210, width=100, height=25)
E_label = Label(root, text='E',bg=background).place(x=60, y=240, width=10, height=25)
E_entry = Entry(root, bg=entry_background)
E_entry.place(x=75, y=240, width=100, height=25)
F_label = Label(root, text='F',bg=background).place(x=60, y=270, width=10, height=25)
F_entry = Entry(root, bg=entry_background)
F_entry.place(x=75, y=270, width=100, height=25)
graph_button = Button(root, command=plot_graph, text='graph', font=('Helvetica', 12), bg='#58E56B').place(x=60, y=330, width=120, height=45)
graph_quit = Button(root, command=quit, text='quit', font=('Helvetica', 12), bg='#EE452A').place(x=60, y=400, width=120, height=45)
root.mainloop()
