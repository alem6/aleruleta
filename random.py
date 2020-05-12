## Random number generator

from math import sqrt

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
        random_numbers.append(float("0."+ str(n_i)))
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

cant_numeros = 100
numero1 = glc(7**5 , (2**31)-1 , 0, 12, cant_numeros) # a , m , seed
numero2 = sng(2222, cant_numeros)
print(numero1)
print(numero2)
m = sqrt(cant_numeros)
intervalos = cant_numeros / 10 