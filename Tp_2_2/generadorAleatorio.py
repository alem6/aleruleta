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


