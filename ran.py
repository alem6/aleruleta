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
def histogram(n, number_array):
    """
    Genera el histograma de frecuencia
    """
    m = int(sqrt(n))
    longitud_intervalo = 1 / m

    intervalos = []
    for x in range(int(m)):
        intervalo = [] 
        intervalo.append(float(x * Decimal(str(longitud_intervalo))))
        intervalo.append(float(int(x + 1) * Decimal(str(longitud_intervalo))))
        # Agregamos contador
        intervalo.append(0)

        intervalos.append(intervalo)

    for numero in number_array:
        for intervalo in intervalos:
            if  intervalo[0] < numero < intervalo[1]:
                #Numero adentro del intervalo
                intervalo[2] += 1
                break
    contadores = []
    for i in intervalos:
        contadores.append(i[2])
    x_coords = np.arange(len(intervalos)) 
    plt.bar(x_coords, contadores , color = 'r'  , label = f"FA intervalo")
    plt.xlabel("Intervalos")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.show()
    return contadores

def chi(n , contadores):
    ei = n / len(contadores)
    
    chi_cuadr = 0

    # Calcula chi cuadrado
    for c in contadores:
        chi_cuadr += (c - ei) ** 2
    chi_cuadr = chi_cuadr / ei

    chi_table = stats.chi2.ppf(q = 0.95, df = len(contadores) - 1)

    # Evalua
    if chi_cuadr < chi_table:
        print("Paso la prueba de Chi-Cuadrado")

def bitmap(numeros):
    m = int(sqrt(len(numeros)))
    img = Image.new(  size = (m, m), color =(0, 0, 0), mode = "RGB") # Create a new black image
    pixels = img.load() # Create the pixel map
    for i in range(img.size[0]):    # For every pixel:
        for j in range(img.size[1]):
            if(numeros[i * j] > 0.5):
                pixels[i, j] = (i, j, 1000)
    img.show()

def monobit():
    pass

"""
    Comienzo del programa principal
"""
# Declaro variables
cant_numeros = 1000000

# Genero numeros
numeros_glc = glc(7**5 , (2**31)-1 , 0, 12, cant_numeros) # a , m , seed
#numeros_sng = sng(2222, cant_numeros)


# Variable a Cambiar depende de que generador queremos testear
numeros = numeros_glc

# Comienzo tests
contadores = histogram(n = cant_numeros , number_array = numeros )

chi(n = cant_numeros , contadores = contadores)

bitmap(numeros = numeros)

