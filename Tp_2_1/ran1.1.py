## Random number generator

from math import sqrt,fsum
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare
from scipy import stats
from PIL import Image

def glc(a, m, c, seed, n):
    """
        a,m son los factores del generador,
        seed es la semilla,
        n es el numero aleatorio en la posicion n 
    """
    random_numbers = []
    n_i = seed
    if n == 1:
        return n_i
    
    for i in range(n):
        n_i = (a * n_i + c)  % m 
        random_numbers.append(n_i / m)
    return random_numbers 

def sng(seed , iteraciones):#Square Number Generator
    """

        Number debe ser un numero de 4 digitos

    """
    random_numbers = []
    x_i = seed
    for x in range(iteraciones):
        number_4n = str(x_i ** 2) 

        while True:
            if len(number_4n) < 8 :
                number_4n += "0"
            else: 
                break

        half = int(len(number_4n) / 2) 
        x_i = int(number_4n[half - 2 : half + 2]) 
        random_numbers.append(float("0." + str(x_i)))
    return random_numbers

cant_numeros = 1000000
numeros_glc = glc(7**5 , (2**31)-1 , 0, 12, cant_numeros) # a , m , seed
numeros_sng = sng(2222, cant_numeros)
# print(numero1)
# print(numero2)

m = int(sqrt(cant_numeros))

longitud_intervalo = 1 / m

intervalos = []
for x in range(int(m)):
    intervalo = [] #[0 , 0.2]
    intervalo.append(float(x * Decimal(str(longitud_intervalo))))
    intervalo.append(float(int(x + 1) * Decimal(str(longitud_intervalo))))
    # Agregamos contador
    intervalo.append(0)

    intervalos.append(intervalo)

for numero in numeros_sng:
    for intervalo in intervalos:
        if  intervalo[0] < numero < intervalo[1]:
            #Numero adentro del intervalo
            intervalo[2] += 1
            break
contadores = []
for i in intervalos:
    contadores.append(i[2])
#x_coords = np.arange(len(intervalos)) 
plt.bar(x_coords, contadores , color = 'r'  , label = f"FR intervalo")
plt.xlabel("Intervalos")
plt.ylabel("Cantidad")
plt.legend()
plt.show()
   
#Oi, contadores
# Ei, n / m
ei = cant_numeros / m
chi_cuadr = 0

# Calcula chi cuadrado
for c in contadores:
    chi_cuadr += (c - ei) ** 2
chi_cuadr = chi_cuadr / ei

chi_table = stats.chi2.ppf(q = 0.95, df = len(intervalos) - 1)

# Evalua
if chi_cuadr < chi_table:
    print("Paso la prueba de Chi-Cuadrado")




img = Image.new(  size = (m, m), color =(0, 0, 0), mode = "RGB") # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        if(numeros_glc[i * j] > 0.5):
            pixels[i, j] = (i, j, 1000)
        

img.show()

####prueba de poker####

#quintilla-todos iguales
#full- 1 trio y 1 par
#par - 1 par
#TP - 2 pares
#tercia - 3 iguales
#poker - 4 iguales
# TD - todos diferentes

def quintilla(nro):
    
    
    digito1 = nro[0]
    for digito in nro:
        if digito != digito1:
            return False
    return True
def full(nro):
    # Conteo
    guia = dict.fromkeys(nro, 0)
    for digito in nro:
        guia[digito]+=1
    if(2 in guia.values() and 3 in guia.values()):
        return True
    return False
def par(nro):
    #conteo
    
    guia = dict.fromkeys(nro, 0)
    for dig in nro:
        guia[digito]+=1
    # Par
    for conteo in guia.values():
        if conteo >= 2:
            return True
    return False

def Tp(nro):
    # Conteo
    
    guia = dict.fromkeys(nro, 0)
    for digito in nro:
        guia[digito]+=1
    # Primer par
    # Solo si sabemos que había uno
    if onep(nro):
        par = None
        for conteo in guia.items():
            if conteo[1] >= 2:
                par = conteo[0]
                break
        # Quitamos el que había
        del guia[par]
        # Segundo par
        for conteo in guia.values():
            if conteo >= 2:
                return True
        return False
    else:
        return False 
           
def tercia(nro):
    # Conteo
    guia = dict.fromkeys(nro, 0)
    for digito in nro:
        guia[digito]+=1
    # Impar
    for conteo in guia.values():
        if conteo >= 3:
            return True
    return False
def poker(nro):
    

    if(tercia(nro)):
        # Conteo
        guia = dict.fromkeys(nro, 0)
        for digito in nro:
            guia[digito]+=1
        for conteo in guia.values():
            if conteo >= 4:
                return True
        return False
    else:
        return False
def td(nro):

    return not (len(nro) != len(set(nro)))


def tipo(numeros):

      if quintilla(numeros):
        return 'quintilla'
      elif poker(numeros):
        return 'poker'
      elif full(numeros):
        return 'full'
      elif tercia(numeros):
        return 'tercia'
      elif twop(numeros):
        return '2p'
      elif onep(numeros):
        return '1p'
      else:
        return 'td'
  