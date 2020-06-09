#imports
import random
import math
import matplotlib.pyplot as plt
from scipy.stats import *
from scipy.stats import kstest, ks_2samp, chisquare
from scipy.stats import uniform
from scipy.stats import norm, gamma, binom, hypergeom
import numpy as np
import seaborn as sns
from decimal import Decimal

#Generadores
def uni(a, b):
    r = random.random()
    x = a + (b - a) * r 
    return x

def exp(ex):
    r = random.random()
    x = -ex * math.log(r)
    return x

def gamma(k, a):
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

def poisson(p):
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
    tabla_acumulada = [0.273, 0.31, 0.505, 0.514, 0.638, 0.696, 0.758, 0.909, 0.956, 1]
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
    data_statsgamma = stats.gamma.rvs(size= n, a= k, loc= 0, scale= 1/a)
    data_gamma     = np.array([gamma(k, a) for u in range(n)])
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
    data_poisson = stats.poisson.rvs(mu = mu, size=n)
    data_poiss   = np.array([poisson(mu) for u in range(n)])
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
    n = 1000000
    data_uni        = np.array([uni(a, b) for u in range(n)])
    m = 1000
    intervalos = []
    longitud_intervalo = (b - a) / m
    for x in range(int(m)):
        intervalo = [] 
        intervalo.append(float(x * Decimal(str(longitud_intervalo))))
        intervalo.append(float(int(x + 1) * Decimal(str(longitud_intervalo))))
        intervalo.append(0)
        intervalos.append(intervalo)
    data_uni = sorted(data_uni)
    for n in data_uni:
        for intervalo in intervalos:
            if  intervalo[0] < n <= intervalo[1]:
                #Numero adentro del intervalo
                intervalo[2] += 1
                break
    contadores = [q[2] for q in intervalos]
    print("-------------TEST UNIFORME-------------")
    print(chisquare(contadores))
    #print(kstest(data_uni, 'uniform', args=(0, 10)))    
    #graph(None, data_uni, False)

    #data_uniform = uniform.rvs(size=n, loc= a, scale=b)
    #print(kstest(data_uniform, 'uniform', args=(0, 10)))
    #print(ks_2samp(data_uni, data_uniform))


def testNormal(mu, sigma, n):
    data_norm = norm.rvs(size= n, loc= mu, scale= sigma )
    #data_normal = np.array([normal(mu, sigma) for u in range(n)])
    #graph(data_norm, data_normal, False)
    print("-------------TEST normal-------------")
    #print("Ks ",kstest(data_normal, 'norm', args=(mu, sigma)))
    print("Ks ",kstest(data_norm, 'norm', args=(mu, sigma)))
    #print(normaltest(data_norm))

if __name__ == "__main__":
    #generateUniform(1000000, 0, 10, False)
    #generateExp(5000, 1, True)
    #generateNormal(1000000, 10, 2, True)
    #generateGamma(10000, 1, 2, True)
    #generatePoisson(1000, 5, False)
    #generateBinomial(1000, 10, 0.2, False)
    #generateHypgeo(40, 20, 0.1, 1000000, False)
    #generatePascal(1000, 2 , 3, False)
    #generateEmpirica(1000, False)
    for x in range(10):
        testUniform(0, 1)
        #testNormal(0, 1, 1000000)