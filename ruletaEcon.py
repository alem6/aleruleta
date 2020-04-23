import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math
from tkinter import *

def asignar():
    pass
def opcionMenu():
    for i in opciones.pack_slaves():
            i.destroy() 
    if opcion.get() == 1: # Numero
        #Limpia        
        Label(opciones , text = "Ingrese el numero al que desea apostar").pack()
        Entry(opciones , textvariable = numero ).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apuesta ).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()

    elif opcion.get() == 2: # Color
        #Limpia
        Label(opciones , text = "Ingrese el color al que desea apostar (R ,N)").pack()
        Entry(opciones , textvariable = color).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apuesta).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()


    elif opcion.get() == 3: # Paridad
        #Limpia
        Label(opciones , text = "Ingrese si desea apostar a par o impar (I , P)").pack()
        Entry(opciones , textvariable = paridad).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apuesta).pack()

        Button(opciones , command = apostar, text = "Apostar").pack()
        
    
def apostar():
    cantVeces = 100
    modo = opcion.get()
    #print(modo)
    try:
        num = int(numero.get())
        print(num)
    except:
        pass

    col = str(color.get())
    print(col)
    try:
        par = str(paridad.get())
        print(par)
    except:
        pass
    
    
    
    
    
    
    print()

    for i in range(1 , cantVeces + 1):
        nroaleatorio = random.randrange( 00, 37) 
        #gano = determinarGanado(nroaleatorio , numero, color, paridad , apuesta, modo)
        #perdio = determinarPerdido(nroaleatorio , numero, color, paridad, apuesta, modo)


#Menu
root = Tk()
root.title("Ruleta")

opcion  = IntVar()
numero  = StringVar()
apuesta = StringVar()
color   = StringVar()
paridad = StringVar()


# Labels
frame = Frame(root, width = 600 , height = 600)
frame.pack()
label = Label(frame, text = "Bienvenido a la ruleta")
label.config(font = ("Verdana", 20))
label.grid(row = 0 , column = 1, pady = 20)
label = Label(frame, text = "Elija a que desea apostar")
label.config(font = ("Verdana", 16))
label.grid(row = 1 , column = 1 , pady = 5 , padx = 20)

Radiobutton(frame , text = "Numero     "    ,variable = opcion , value = 1, command = opcionMenu).grid(row = 2 ,column = 1)
Radiobutton(frame , text = "Color\t"        ,variable = opcion , value = 2, command = opcionMenu).grid(row = 3 ,column = 1)
Radiobutton(frame , text = "Par / Impar"    ,variable = opcion , value = 3, command = opcionMenu).grid(row = 4 ,column = 1)

opciones = Frame(root)
opciones.pack()

#Loop principal
root.mainloop()

