import random
nroVecesGanados=0
cantTiros=0
resultados=[]
print('\tJUEGO DE RULETA\t ')
rta=input('ingrese s para comenzar a jugar: ')
while rta=='s':
    nume=int(input('INGRESE UN NUMERO PARA JUGAR: '))
    if (0<=nume <=36):
            nroaleatorio=random.randrange( 00, 36)
            cantTiros+=1
            if (nume!=nroaleatorio):
                print('Lo siento, cayó en el numero ' + str(nroaleatorio))
                rta=input('DESEA SEGUIR JUGANDO?: ')
            else:
                 print(' ..¡¡ FELICITACIONES GANASTE !!..')
                 rta=input('DESEA SEGUIR JUGANDO?: ')
                 nroVecesGanados=+1
            resultados.append(nroaleatorio)             
    else:
            print("el numero ingresado no esta en el rango vuelve a ingresar nro") 
            
print('cantidad de veces que ganaste:' + str (nroVecesGanados))   
print('cantidad de tiros jugados:' + str (cantTiros))   
print(resultados)      
  