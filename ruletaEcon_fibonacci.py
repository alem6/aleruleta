import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math
from tkinter import *

def getNthFib(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n > 2:
		return getNthFib(n-1) + getNthFib(n-2)

def getColor(numero):
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10 , 11 , 13 , 15 , 17 ,20 , 22 , 24 ,26, 28, 29 , 31 , 33 , 35]
    if numero == 0: 
        return "V"
    if numero in rojos:
        return "R"
    else:
        return "N"

def getParidad(numero):
    if (numero % 2 == 0): 
        return "P" 
    else:
        return "I"

def opcionMenu():
    for i in opciones.pack_slaves():
            i.destroy() 
    if opcion.get() == 1: # Numero
        #Limpia        
        Label(opciones , text = "Ingrese el numero al que desea apostar").pack()
        Entry(opciones , textvariable = num ).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apue ).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()

    elif opcion.get() == 2: # Color
        #Limpia
        Label(opciones , text = "Ingrese el color al que desea apostar (R ,N)").pack()
        Entry(opciones , textvariable = col).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apue).pack()

        Button(opciones , command = apostar , text = "Apostar").pack()


    elif opcion.get() == 3: # Paridad
        #Limpia
        Label(opciones , text = "Ingrese si desea apostar a par o impar (I , P)").pack()
        Entry(opciones , textvariable = par).pack()
        Label(opciones , text = "Ingrese cuanto desea apostar").pack()
        Entry(opciones , textvariable = apue).pack()

        Button(opciones , command = apostar, text = "Apostar").pack()
        

def getGano(modo, numero_random , apuesta , color_apostado , numero_apostado , paridad_apostado):
    gano = 0

    if modo == 1: # Numero
        if numero_apostado == numero_random:
            gano = apuesta * 36     
    elif modo == 2: #Color
        if color_apostado == getColor(numero_random):
            gano = apuesta * 2
    elif modo == 3: #Par/Impar
        if paridad_apostado == getParidad(numero_random):
            gano = apuesta * 2
    
    return gano

def apostar(): 
    cantVeces = 1000
    modo = opcion.get()  # 1 2 3
    plata = 100
    infinito = False
    debug = False
 # Busca los parametros de la apuesta que puede   

    try:
        numero = int(num.get())
    except:
        numero = 0
    try:
        color = str(col.get())
    except:
        color = ""
    try:
        paridad = str(par.get())
    except:
        paridad = ""
    
    n = 1
    apuesta = getNthFib(n)
    altura = plata
    cant_capital = []
    c=0  

    for i in range(1 , cantVeces + 1):
        nroaleatorio = random.randrange( 00, 37)
        apuesta = getNthFib(n)
        if apuesta > plata: 
            print("HAS PERDIDO")
            break
        gano = getGano(modo , nroaleatorio , apuesta , color , numero , paridad)
        
        if gano == 0:
            n += 1
            if not infinito:
                plata -= apuesta
                c+=1
                
               
        if gano > 0:
            plata += gano
            c+=1
            
            if n > 3:
                n -= 2
            else:
                n = 1

        cant_capital.append(plata)
        if debug : print(f"Aposto {apuesta} y tiene {plata}")
        

    
    #Grafica de Capital
    
    plt.axhline(altura)
    plt.ylabel("CC(Cantidad de Capital)")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , max(cant_capital)])
    plt.plot(cant_capital, "-r")
    plt.show()

    #grafica barras
    X=0
    datos1=[]
    datos1=[cant_capital,plata]
    X=np.arange(c) 
    plt.bar(X+0.00,datos1[0],color='g',width=0.25)
    plt.bar(X+0.25,datos1[1],color='b',width=0.25)
    plt.ylabel("CC(Cantidad de Capital)")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , c, 0 , max(cant_capital)])
    plt.show()    
   
      
     

#region Menu
#Menu
root = Tk()
root.title("Ruleta")

opcion  = IntVar()
num  = StringVar()
apue = StringVar()
col   = StringVar()
par = StringVar()


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

#endregion
