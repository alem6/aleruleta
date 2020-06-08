#imports
import random
import math
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import uniform
from scipy.stats import norm, gamma
import numpy as np
import seaborn as sns

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
    qr = math.log10(q)
    for i in range(k):
        r = random.random()
        tr *= r
    nx = math.log10(tr) / qr
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
    data_statsgamma = stats.gamma.rvs(size= n, a= a, loc= 0, scale= 1)
    data_gamma     = np.array([gamma(k, a) for u in range(n)])
    graph(data_statsgamma, data_gamma, linea)
def generateNormal(n, mu, sigma, linea):
    #Generamos Normal
    data_norm = norm.rvs(size= n, loc= mu, scale= sigma )
    data_normal = np.array([normal(mu, sigma) for u in range(n)])
    graph(data_norm, data_normal, linea)
def generatePascal(n):
    pass
def generateBinomial(n):
    pass
def generateHypgeo(n):
    pass
def generatePoisson(n, mu,linea):
    # generamos poisson
    data_poisson = stats.poisson.rvs(mu = mu, size=n)
    data_poiss   = np.array([poisson(mu) for u in range(n)])
    graph(data_poisson, data_poiss, linea)
def generateEmpirica(n):
    pass
    


def graph(data1, data2, linea):
    """
        Mandar como primer argumento un array de np con el generador de Scipy
        Y segundo argumento otro array de np con el generador que creamos nosotros
    """
    #Generador de Scipy
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

    
if __name__ == "__main__":
    generateUniform(1000000, 0, 10, False)
    generateExp(5000, 1, True)
    generateNormal(1000000, 10, 2, True)
    generateGamma(10000, 1, 2, True)
    generatePoisson(1000, 5, False)