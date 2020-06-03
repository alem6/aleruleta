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
    for i in range(5):
        r = random.random()
        tr *= r
    x = -math.log(tr)
    