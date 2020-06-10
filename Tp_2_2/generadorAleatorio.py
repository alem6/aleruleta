#imports
import random
import math
import matplotlib.pyplot as plt
from scipy.stats import *
from scipy.stats import kstest, ks_2samp, chisquare
from scipy.stats import uniform
from scipy.stats import norm, gamma, binom, hypergeom
from scipy.stats import chi
from scipy import stats
import numpy as np
import seaborn as sns
from decimal import Decimal
from collections import Counter

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

#Generadores
def uni(a, b):
    r = random.random()
    x = a + (b - a) * r 
    return x

def exp(ex):
    r = random.random()
    x = -ex * math.log(r)
    return x

def gamm(k, a):
    tr = 1
    for i in range(k):
        r = random.random()
        tr = tr * r
    x = -math.log(tr) / a
    return x

def normal(ex ,stdx):
    
    sum = 0
    for i in range(12):
        r = random.random()
        sum += r
    x = stdx * (sum - 6) + ex
    return x

def pascal(k,q):
    tr = 1.0
    qr = math.log(q)
    for i in range(k):
        r = random.random()
        tr *= r
    nx = math.log(tr) / qr
    return nx

def binomial(n, p):
    x = 0
    for i in range(n):
        r = random.random()
        if (r - p) <= 0 :
            x += 1
    return x

def hypgeo(tn, ns, p):
    x = 0
    for i in range(ns):
        r = random.random()
        if (r - p) <= 0 :
            s = 1
            x += 1
        else:
            s = 0
        p = (tn * p - s) / (tn - 1)
        tn = tn - 1
    return x # algo

def poiss(p):
    x = 0
    b = math.exp(-p)
    tr = 1
    while True:
        r = random.random()
        tr = tr * r
        if (tr - b) <= 0:
            break
        else:
            x += 1
    return x

def empirica():
    tabla = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    tabla_acumulada = [0, 0.273, 0.31, 0.505, 0.514, 0.638, 0.696, 0.758, 0.909, 0.956, 1]
    x = 0
    b = list(range(10))
    r = random.random()
    for index, t in enumerate(tabla_acumulada):

        if tabla_acumulada[index] <= r < tabla_acumulada[index + 1 ]:
            x = b[index]
            break
    return x

def generateUniform(n, a, b, linea):
    #Generamos uniforme
    data_uniform = uniform.rvs(size=n, loc= a, scale=b)
    data_uni     = np.array([uni(a, b) for u in range(n)])
    graph(data_uniform, data_uni, linea)

def generateExp(n, ex, linea):
    #Generamos Exponencial
    data_expon = np.array([random.expovariate(ex) for i in range(n)])
    data_exp   = np.array([exp(ex) for u in range(n)])
    graph(data_expon, data_exp, linea)
    

def generateGamma(n, k, a, linea):
    #generamos gamma
    data_statsgamma = gamma.rvs(size= n, a= k, loc= 0, scale= 1/a)
    data_gamma     = np.array([gamm(k, a) for u in range(n)])
    graph(data_statsgamma, data_gamma, linea)
def generateNormal(n, mu, sigma, linea):
    #Generamos Normal
    data_norm = norm.rvs(size= n, loc= mu, scale= sigma )
    data_normal = np.array([normal(mu, sigma) for u in range(n)])
    graph(data_norm, data_normal, linea)
def generatePascal(n,k, q, linea):
    data_pascal = np.array([pascal(k ,q) for u in range(n)])
    graph(None, data_pascal, linea)
def generateBinomial(n, k, p, linea):
    data_binom = binom.rvs(k, p , size= n)
    data_binomial = np.array([binomial(k, p) for u in range(n)])
    graph(data_binom, data_binomial, linea)
def generateHypgeo(k, m, n, size, linea):
    
    data_hypgeo = np.array([hypgeo(k, m, n) for u in range(size)])
    graph(None, data_hypgeo, linea)
def generatePoisson(n, mu,linea):
    # generamos poisson
    data_poisson = np.random.poisson(lam= mu, size=n)
    data_poiss   = np.array([poiss(mu) for u in range(n)])
    graph(data_poisson, data_poiss, linea)
def generateEmpirica(n, linea):
    data_empirica = np.array([empirica() for u in range(n)])
    graph(None, data_empirica, linea)
    


def graph(data1, data2, linea):
    """
        Mandar como primer argumento un array de np con el generador de Scipy
        Y segundo argumento otro array de np con el generador que creamos nosotros
    """
    #Generador de Scipy
    if data1 is not None:
        data1graph = sns.distplot(data1,
                                bins=100,
                                kde=linea,
                                color='green',
                                hist_kws={"linewidth": 15,'alpha':0.5},
                                label = "Generador Python",)
        data1graph.set(xlabel='Distr', ylabel='Frecuencia')
    
    
    #Nuestro generador
    data2graph = sns.distplot(data2,
                        bins=100,
                        kde=linea,
                        color='red',
                        hist_kws={"linewidth": 15,'alpha':0.5},
                        label = "Generador Nuestro",)
    data2graph.set(xlabel='Distr', ylabel='Frecuencia')
    plt.legend()
    plt.show()
def testUniform(a, b):
    n = 200 * 200
    data_uni        = np.array([uni(a, b) for u in range(n)])
    data_uniform    = uniform.rvs(loc= a, scale= b, size= n)

    print("-------------TEST UNIFORME-------------")
    print(ks_2samp(data_uni, data_uniform))


def testNormal(mu, sigma, n):
    data_norm = norm.rvs(size= n, loc= mu, scale= sigma )
    data_normal = [normal(mu, sigma) for u in range(n)]   
    print("-------------TEST normal-------------")
    print(ks_2samp(data_norm, data_normal, alternative='two-sided', mode= 'asymp'))
    #print(anderson(data_normal, dist='norm')) # Segun Wikipedia este test es el mas "fuerte"
    #print(shapiro(data_normal))
        
    # - ------ Probados --------l
    #graph(data_norm, data_normal, False)
    #print(kstest(data_normal,'norm', alternative='greater', mode= 'auto',))
    #print(jarque_bera(data_normal))
    #print(normaltest(data_normal))

def testPoisson(n, mu):
    data_poiss   = np.array([poiss(mu) for u in range(n)])
    data_poisson = np.random.poisson(lam= mu, size= n)
    print(ks_2samp(data_poiss, data_poisson, alternative='two-sided', mode= 'asymp'))
    
    

def testExp(n , l):
    data_exp   = np.array([exp(1/l) for u in range(n)])
    data_expon = np.array([random.expovariate(l) for i in range(n)])
    data_exp = sorted(data_exp)
    print("-------------TEST EXPON-------------")
    print("TEST ANDERSON: ", anderson(data_exp, dist= 'expon'))
    print("KS2: ", ks_2samp(data_exp, data_expon))
    
def testBinomial(n, k, p):
    data_binomial = [binomial(k, p) for u in range(n)]
    total = 0
    for d in data_binomial:
        total += d
    print(f"Probabilidad de que la distribucion tenga la probabilidad {p}", binom_test(x= total, n= k * n, p= p, alternative='greater'))
def testEmpirica(n):
    data_empirica = np.array([empirica() for x in range(n)])
    f_exp = [273, 37, 195, 9, 124, 58, 62, 151, 47, 44]
    counter = Counter(data_empirica)
    sorted_occurrences = list(dict(sorted(counter.items())).values())

    chi_cuadr = chisquare(sorted_occurrences, f_exp)[0]
    chi_table = stats.chi2.ppf(q = 0.95, df = len(sorted_occurrences) - 1)
    if chi_cuadr < chi_table:
        print(f"Chi vale {chi_cuadr} y paso el test")
    else:
        print(f"Chi vale {chi_cuadr} y no paso el test")


if __name__ == "__main__":
    generateUniform(100000, 0, 10, False)
    generateExp(100000, 1, True)
    generateNormal(100000, 10, 2, True)
    generateGamma(100000, 1, 2, True)
    generatePoisson(100000, 8, False)
    generateBinomial(100000, 10, 0.2, False)
    generateHypgeo(40, 30, 0.1, 100000, False)
    generatePascal(100000, 2 , 3, False)
    generateEmpirica(100000, False)
    for x in range(1):
        testUniform(0, 1)
        testNormal(5, 2, 2000)
        testExp(2000, 3)
        testBinomial(2000, 10, 0.2)
        testPoisson(10000, 8)
        testEmpirica(1000)
    
    
    
    
    #Test normal con GLC
    #nums = glc(7**5 , (2**31)-1 , 0, 12, 10000)
    #normalnums = []
    #for n in nums:
    #    sum = 0
    #    for i in range(12):
    #        r = random.random()
    #        sum += r
    #    x = 1 * (sum - 6) + 0
    #    normalnums.append(x)
    #graph(None, normalnums, True)
    #print(normaltest(normalnums))