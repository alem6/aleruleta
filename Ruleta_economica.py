import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math
import tkinter

#Declaracion de Variables
juego = False
numElegido = 5
cantVeces = 1500

# main
if juego:
    while True:
        numElegido = int(input('INGRESE UN NUMERO PARA JUGAR: (Del 0 al 36): '))
        if numElegido < 36 or numElegido > 0:
            break 

for i in range(1 , cantVeces + 1):
    nroaleatorio = random.randrange( 00, 37) 
    
    if (nume == nroaleatorio):
        nroVecesGanados += 1 
    resultados.append(nroaleatorio)