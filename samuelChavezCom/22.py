'''
Dadas cuatro tuplas (en ningun orden en particular) 
representando cuatro puntos en un espacio bidimensional, 
determine si en conjunto representan un cuadrado.

Condiciones
1. La distancia de dos puntos a 'P' es igual a 'd'
2. La distancia de un tercer punto restante 'q' a 'P' sqrt(2)*d
3. La distancia de 'q' hacia dos puntos debe ser igual a d 

'''

import math

coordinates = { 
    'uno' : (5, 10),
    'dos' : (10, 10),
    'tres' : (5, 5),
    'cuatro' : (10, 5)
}

def squareDet(d):
    # distance 1: point1 to point2
    d1 = distance(d['uno'], d['dos'])
    # distance 2: point1 to point3
    d2 = distance(d['uno'], d['tres'])
    # distance 3: point1 to point4
    d3 = distance(d['uno'], d['cuatro'])
    
    # if d1 y d2 are equal && d3^2 = 2*d1^2 && (d2-3)^2 = 2*(d2-4)^2  then it is a square
    if d1 == d2 and round(math.pow(d3, 2)) == round(2 * math.pow(d1, 2)) and round(math.pow(distance(d['dos'], d['tres']), 2)) == round(2 * math.pow(distance(d['dos'], d['cuatro']), 2)):
        return True
    
    # if d1 y d2 are equal && d1^2 = 2*d1^2 && (d2-3)^2 = 2*(d2-4)^2  then it is a square
    if d2 == d3 and round(math.pow(d1,2)) == round(2 * math.pow(d2, 2)) and round(math.pow(distance(d['tres'], d['cuatro']), 2)) == round(2 * math.pow(distance(d['tres'], d['dos']), 2)):
        return True
    # if d1 y d2 are equal && d2^2 = 2*d1^2 && (d2-3)^2 = 2*(d2-4)^2  then it is a square
    if d1 == d3 and round(math.pow(d2,2)) == round(2 * math.pow(d1, 2)) and round(math.pow(distance(d['dos'], d['cuatro']), 2)) == round(2 * math.pow(distance(d['dos'], d['tres']), 2)):
        return True
    
    return False

def distance(tuple1, tuple2):
    return math.sqrt( math.pow( tuple2[0]-tuple1[0], 2 ) + math.pow(tuple2[1]-tuple1[1], 2 ) ) 


print(squareDet(coordinates))