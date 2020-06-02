import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math
from tkinter import *
class Menu():

    root = Tk()
    numero = IntVar()
    color = StringVar()
    paridad = StringVar()
    apuesta = IntVar()
    modo = "" 

    def mainMenu(self):
        #Elemento raiz
        
        self.root.title("Ruleta")

        frame = Frame(self.root, width = 600 , height = 600)
        frame.pack()

        label = Label(frame, text = "Bienvenido a la ruleta")
        label.config(font = ("Verdana", 20))
        label.grid(row = 0 , column = 1, pady = 20)
        label = Label(frame, text = "Elija a que desea apostar")
        label.config(font = ("Verdana", 16))
        label.grid(row = 1 , column = 1 , pady = 5 , padx = 20)

        Button(frame, command = self.menuNumero, text = "Numero" , width = 20).grid(row = 2 , column = 0 , padx = 25)

        Button(frame, command = self.menuColor, text = "Color" , width = 20 ).grid(row = 2 , column = 1 , pady = 25)

        Button(frame, command = self.menuParidad, text = "Par / Impar" , width = 20).grid(row = 2 , column = 2 , padx = 25)

        #Loop principal
        self.root.mainloop()



    def menuNumero(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title("Apuesta Numero")
        self.modo = "numero"
     

        frame = Frame(self.root, width = 600 , height = 600)
        frame.pack()

        label = Label(frame, text = "Apueste a un numero")
        label.config(font = ("Verdana", 18))
        label.place(x = 20 , y = 0)

        Label(frame, text = "Ingrese el numero al que desea apostar:").grid(row = 0, column = 0 ,padx = 25 , pady = (40 , 5))
        entryNumero = Entry(frame , width = 30 ,textvariable = self.numero)
        entryNumero.grid(row = 0, column = 1, padx = 25 , pady = (40, 5))
        
        Label(frame, text = "Ingrese su apuesta:").grid(row = 1, column = 0 , padx = 25 , pady = (5, 25))
        entryApuesta = Entry(frame , width = 30, textvariable = self.apuesta)
        entryApuesta.grid(row = 1, column = 1, padx = 25 , pady = (5, 25))

        Button(frame, command = main, text = "Apostar" , width = 20).grid(row = 2 , column = 2 , padx = 25)
        #Loop principal
        self.root.mainloop()

    def menuColor(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title("Apuesta color")
        self.modo = "color"

        frame = Frame(root, width = 600 , height = 600)
        frame.pack()

        label = Label(frame, text = "Apueste a un color")
        label.config(font = ("Verdana", 20))
        label.grid(row = 0 , column = 1)

        Label(frame, text = "Ingrese el color al que desea apostar: (R,N)").grid(row = 0, column = 0 ,padx = 25 , pady = (40 , 5))
        entryNumero = Entry(frame , width = 30 ,textvariable = self.color)
        entryNumero.grid(row = 0, column = 1, padx = 25 , pady = (40, 5))
        
        Label(frame, text = "Ingrese su apuesta:").grid(row = 1, column = 0 , padx = 25 , pady = (5, 25))
        entryApuesta = Entry(frame , width = 30, textvariable = self.apuesta)
        entryApuesta.grid(row = 1, column = 1, padx = 25 , pady = (5, 25))

        Button(frame, command = main, text = "Apostar" , width = 20).grid(row = 2 , column = 2 , padx = 25)

        #Loop principal
        self.root.mainloop()

    def menuParidad(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title("Apuesta Paridad")
        self.modo = "paridad"

        frame = Frame(root, width = 600 , height = 600)
        frame.pack()

        label = Label(frame, text = "Apueste a par o a impar")
        label.config(font = ("Verdana", 20))
        label.grid(row = 0 , column = 1)

        Label(frame, text = "Ingrese la opcion a la que desea apostar:(P,I)").grid(row = 0, column = 0 ,padx = 25 , pady = (40 , 5))
        entryNumero = Entry(frame , width = 30 ,textvariable = self.paridad)
        entryNumero.grid(row = 0, column = 1, padx = 25 , pady = (40, 5))
        
        Label(frame, text = "Ingrese su apuesta:").grid(row = 1, column = 0 , padx = 25 , pady = (5, 25))
        entryApuesta = Entry(frame , width = 30, textvariable = self.apuesta)
        entryApuesta.grid(row = 1, column = 1, padx = 25 , pady = (5, 25))

        Button(frame, command = main, text = "Apostar" , width = 20).grid(row = 2 , column = 2 , padx = 25)

        #Loop principal
        self.root.mainloop()

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

def determinarGanado(numeroRuleta, numero, color, paridad ,apuesta, modo):
    dineroGanado = 0

    if numero == numeroRuleta and modo == "numero":
        dineroGanado += apuesta * 36
    if getColor(numeroRuleta) == color and modo == "color":
        dineroGanado += apuesta * 2
    if getParidad(numeroRuleta == paridad) and modo == "paridad":
        dineroGanado += apuesta * 2

    if dineroGanado > 0: 
        return True, dineroGanado
    else:
        return False, dineroGanado

def determinarPerdido(numeroRuleta, numero, color, paridad ,apuesta, modo):
    dineroPerdido = 0
    if numero != numeroRuleta and modo == "numero":
        dineroPerdido += apuesta
    if getColor(numeroRuleta) != color and modo == "color":
        dineroPerdido += apuesta
    if getParidad(numeroRuleta) != paridad and modo == "paridad":
        dineroPerdido += apuesta
    
    

    if dineroPerdido > 0: 
        return True
    else:
        return False

def main():
    #Variables de Apuesta
    apuesta = menu.apuesta.get()
    numero = menu.numero.get()
    print(apuesta)


    for i in range(1 , cantVeces + 1):
        plata_ganada  = 0
        plata_perdida = 0
        nroaleatorio = random.randrange( 00, 37) 
        gano = determinarGanado(nroaleatorio , numero, color, paridad , apuesta, modo)
        perdio = determinarPerdido(nroaleatorio , numero, color, paridad, apuesta, modo )
        plata += plata_ganada
        plata -= plata_perdida
        if perdio:
            apuesta = apuesta * 2  

#Declaracion de Variables
juego = False
cantVeces = 1500
ganadosPorNro = 0
resultados = []



# Crea el menu
menu = Menu()
menu.mainMenu()
