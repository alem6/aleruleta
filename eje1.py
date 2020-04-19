import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import seaborn as sns
import math

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
cantItemX = []
cantItemY = []
quartil1=[]

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

    

        
# Pongo estilo por default de seaborn
sns.set()

#Grafica de Frecuencia Relativa
#altura = 1 / 37
#plt.axhline(altura)
#plt.ylabel("FR(Frecuencia Relativa)")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 1])
#plt.plot(frecRelativas, "-r")
#plt.show()
#
##Grafica de Frecuencia Relativa
#altura = np.mean(resultados)
#plt.axhline(altura)
#plt.ylabel("VP(Valor Promedio de las tiradas")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 200])
#plt.plot(media, "-r")
#plt.show()
#
##Grafica de Desvio Estandar
#altura = np.std(resultados)
#plt.axhline(altura)
#plt.ylabel("VD(Valor del Desvio)")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 200])
#plt.plot(desvio, "-r")
#plt.show()
#
##Grafica de Varianza
#altura = np.var(resultados)
#plt.axhline(altura)
#plt.ylabel("VV(Valor de la Varianza)")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 200])
#plt.plot(varianza, "-r")
#plt.show()

#Grafica de la Moda
#plt.ylabel("Moda")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 36])
#plt.plot(moda, "-r")
#plt.show()
#
##Grafica de la Mediana
#altura = np.median(resultados)
#plt.axhline(altura)
#plt.ylabel("Mediana")
#plt.xlabel("Numero de tiradas")
#plt.axis([ 0 , cantVeces , 0 , 36])
#plt.plot(mediana, "-r")
#plt.show()

#Grafica de histograma de cantidad de apariciones de cada numero
counter = Counter(resultados)
counter = sorted(counter.items())
index = 0
for x in range(37):
    if index < len(counter):
        if counter[index][0] == x:
            cantItemX.append(counter[index][0])
            cantItemY.append(counter[index][1])
            index += 1
        else:
            cantItemX.append(x)
            cantItemY.append(0)
    else:
        cantItemX.append(x)
        cantItemY.append(0)

if len(cantItemX) < 37:
    print("Ha ocurrido un error")
    
print(cantItemX)
print(cantItemY)
plt.bar(cantItemX,cantItemY,label = "Cant Apariciones")
plt.xlabel("Numbers")
plt.ylabel("Quantity")
plt.legend()
plt.axis([ 0 , 36 , 0 , max(cantItemY)])
plt.show()

## Grafica de caja y bigotes
#plt.ylabel('Quartiles')
#quartil1=(np.quantile(resultados,0.25), np.quantile(resultados,0.50), np.quantile(resultados,0.75))
## Creando el objeto figura
#fig = plt.figure(1, figsize=(9, 6))
##  Creando el subgrafico
#ax = fig.add_subplot(111)
## creando el grafico de cajas
#bp = ax.boxplot(quartil1)
#for flier in bp['fliers']:
#   flier.set(marker='o', color='blue', alpha=0.5)
##plt.savefig("varianzaFiguras.pdf")
#print(quartil1)
#plt.show()
#
