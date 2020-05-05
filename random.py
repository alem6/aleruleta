## Random number generator

def glc(a, m , seed, n):
    """
        a,m son los factores del generador,
        seed es la semilla,
        n es el numero aleatorio en la posicion n 
    """
    random_numbers = []
    n_i = seed
    if n == 1:
        return seed
    for i in range(n):
        n_i = a * n_i % m 
        random_numbers.append(n_i)
    print(random_numbers)
    return(random_numbers[-1])

def sng(number):#Square Number Generator
    """
        number debe ser un numero 2n
    """

    number_4n = str(number ** 2)

    while True:
        if len(number_4n) % 2 != 0:
            number_4n += "0"
        else:
            break
    half = int(len(number_4n) / 2)
    random_number = number_4n[half-2:half+2]
    return float("0." + random_number)


#ret = glc(7 , 11 , 12 , 5) # a , m , seed

print(sng(2222))    
    