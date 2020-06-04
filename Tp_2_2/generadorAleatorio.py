#imports
import random
import math

#Generadores
def uniform(a, b):
    r = random.random()
    x = a + (b - a) * r 
    return x

def exp(ex):
    r = random.random()
    x = -ex * math.log(r , 10)
    return x

def gamma(k, a):
    tr = 1.0
    for i in range(k):
        r = random.random()
        tr *= r
    x = -math.log(tr)
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