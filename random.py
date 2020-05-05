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

ret = glc(7 , 11 , 12 , 5) # a , m , seed
print(ret)

    
    