import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
# Declaro variables
nroVecesGanados = 0
cantTiros = 0
resultados = []
cantVeces = int(input("Cuantas iteraciones desea realizar?"))
frecRelativas = []
media = []
desvio = []
varianza = []
moda = []
mediana = []
valoresAcumulados = 0
acumDesvio = 0

# Comienza el programa
print('\tJUEGO DE RULETA\t ')
while True:
    nume = int(input('INGRESE UN NUMERO PARA JUGAR: (Del 0 al 36): '))#5
    if nume < 36 or nume > 0:
        break 

for i in range(1 , cantVeces + 1):
    nroaleatorio = random.randrange( 00, 37) # 5
    valoresAcumulados += nroaleatorio
    
    if (nume == nroaleatorio):
        nroVecesGanados += 1 # 1
    resultados.append(nroaleatorio)
    #Calcula Frecuencia Relativa     
    frecRelativas.append(nroVecesGanados / i)
    #Calcula medias
    media.append(valoresAcumulados/i)    
    # Calcula Desvio Estandar
    desvio.append(np.std(resultados))
    # Calcula Varianza
    varianza.append(np.var(resultados))
    # Calcula Moda
    c = Counter(resultados)
    mod = c.most_common(1)
    moda.append(mod[0][0])
    # Calcula mediana
    mediana.append(np.median(resultados))

    

## [5, 3, 4, 4]
## Frecuencia relativa,  valor promedio, valor del desvio y valor de la varianza
## [3 , 8 , 19, 3 ] 2 veces de las 4 veces que tiramos salio 3... fr(3) = 2/4

print(moda)
opcion = input("""Que desea graficar?
    a - Fr
    b - Promedio
    c - Desvio
    d - Varianza
    e - Moda
    f - Mediana""")
if opcion == "a":
    altura = 1 / 37
    #print(altura)
    plt.axhline(altura)
    plt.ylabel("FR(Frecuencia Relativa)")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 1])
    #frecRelativas = [0.02, 0.03, 0.04]
    plt.plot(frecRelativas, "-r")# [1 , 2 , 3 , 4]
    print(frecRelativas[-1])
    #plt.savefig("frecuenciaFiguras.pdf")
    plt.show()

if opcion == "b":
    altura = np.median(resultados)
    plt.axhline(altura)
    plt.ylabel("VP(Valor Promedio de las tiradas")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 200])
    plt.plot(media, "-r")# [1 , 2 , 3 , 4]
    print(media[-1])
    plt.show()
    #plt.savefig("promedioFiguras.pdf")

if opcion == "c":
    altura = np.std(resultados)
    plt.axhline(altura)
    plt.ylabel("VD(Valor del Desvio)")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 200])
    plt.plot(desvio, "-r")# [1 , 2 , 3 , 4]
    print(desvio[-1])
    #plt.savefig("desvioFiguras.pdf")
    plt.show()


if opcion == "d":
    altura = np.var(resultados)
    plt.axhline(altura)
    plt.ylabel("VV(Valor de la Varianza)")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 200])
    plt.plot(varianza, "-r")# [1 , 2 , 3 , 4]
    #plt.savefig("varianzaFiguras.pdf")
    print(varianza[-1])
    plt.show()

if opcion == "e":
    
    plt.ylabel("Moda")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 36])
    plt.plot(moda, "-r")# [1 , 2 , 3 , 4]
    #plt.savefig("varianzaFiguras.pdf")
    plt.show()

if opcion == "f":
    
    plt.ylabel("Mediana")
    plt.xlabel("Numero de tiradas")
    plt.axis([ 0 , cantVeces , 0 , 36])
    plt.plot(mediana, "-r")# [1 , 2 , 3 , 4]
    #plt.savefig("varianzaFiguras.pdf")
    plt.show()
#if opcion == "g":
#    
#    plt.ylabel("Moda")
#    plt.xlabel("Numero de tiradas")
#    plt.axis([ 0 , cantVeces , 0 , 36])
#    plt.plot(moda, "-r")# [1 , 2 , 3 , 4]
#    #plt.savefig("varianzaFiguras.pdf")
#    plt.show()
