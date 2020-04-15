import random
import matplotlib.pyplot as plt
import numpy as np

nroVecesGanados = 0
cantTiros = 0
resultados = []
cantVeces = 20
frecRelativas = []

print('\tJUEGO DE RULETA\t ')
while True:
    nume = int(input('INGRESE UN NUMERO PARA JUGAR: (Del 0 al 36)'))#5
    if nume < 36 or nume > 0:
        break 

for i in range(1,cantVeces + 1):
    nroaleatorio=random.randrange( 00, 36) # 5
    
    if (nume == nroaleatorio):
                
        nroVecesGanados=+1 # 1
         
    frecRelativas.append(nroVecesGanados / i) #[0/1, 1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7] 

    resultados.append(nroaleatorio)             
        
#print('Cantidad de veces que ganaste: ' + str (nroVecesGanados))   

#print(resultados)      

## [5, 3, 4, 4]
## Frecuencia relativa,  valor promedio, valor del desvio y valor de la varianza
## [3 , 8 , 19, 3 ] 2 veces de las 4 veces que tiramos salio 3... fr(3) = 2/4

#nroVecesGanados es la cant de veces que salio el numero

## for f in frecRelativas:
##     # Para cada frecuencia relativa la mostramos
##     print("La frecuencia relativa es de " + str(f))

altura = 1 / 37
print(altura)
plt.axhline(altura)
plt.ylabel("Frecuencia")
plt.xlabel("Numero de tiradas")
plt.axis([ 0 , cantVeces , 0 , 1])
#frecRelativas = [0.02, 0.03, 0.04]
plt.plot(frecRelativas, "-r")# [1 , 2 , 3 , 4]
plt.show()
