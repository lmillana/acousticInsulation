# CALCULOS PRINCIPALES
## CÁLCULO de DnT y R' POR INTENSIMETRÍA - ISO 15186-2
## 10CM ENTRE SONDA Y PARED DE SEPARACIÓN + PANELES ABSORBENTES - EXPERIMENTO 2

from pylab import *                     # Nos permite crear gráficos
from int30 import *


## ARRAYS PARA TRATAR DATOS DE MANERA MÁS SENCILLA:
# Rango de frecuencias de interes:
FR = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]
# Valores en Emisión - SB:
E = [69.1, 67.5, 67.4, 85.3, 85.7, 92.7, 96.5, 98.3, 100.4, 101.1, 100.3, 100.4, 99.6, 99.0, 98.8, 98.1, 99.1, 101.4, 99.7, 96.7, 95.5]

## SUB-ÁREAS DEL ELEMENTO DE MEDICIÓN:
SUB11 = [] # Sub-área 1, posición de altavoz A1
SUB12 = [] # Sub-área 1, posición de altavoz A2
SUB21 = [] # Sub-área 2, posición de altavoz A1
SUB22 = [] # Sub-área 2, posición de altavoz A2

## SUB-ÁREAS LATERALES:
arrayS3 = [] # Array para los resultados de la sub-área 3
arrayS4 = [] # Array para los resultados de la sub-área 4
arrayS5 = [] # Array para los resultados de la sub-área 5
arrayS6 = [] # Array para los resultados de la sub-área 6

LIn = [] # Array para los resultados combinados de ambas sub-áreas
DIn = [] # Array para los resultados de la diferencia normalizada por intensimetría
RI = []  # Array para los resultados de R'I SIN influencia de paredes laterales
RI2 = []  # Array para los resultados de R'I CON influencia de paredes laterales


if __name__ == "__main__":
    print('SUB-ÁREA 1 - A1')
    print('---------------')
    toSUB(42, 62, 13, 14, SUB11)

    print('SUB-ÁREA 1 - A2')
    print('---------------')
    toSUB(42, 62, 15, 16, SUB12)

    print('SUB-ÁREA 2 - A1')
    print('---------------')
    toSUB(42, 62, 17, 18, SUB21)

    print('SUB-ÁREA 2 - A2')
    print('---------------')
    toSUB(42, 62, 19, 20, SUB22)

    print()
    print('COMBINACIÓN DE RESULTADOS - LIn')
    print('-------------------------------')
    toLIn(SUB11, SUB12, SUB21, SUB22, LIn)

    print('DIFERENCIA DE NIVEL NORMALIZADO POR INTENSIMETRÍA')
    print('-------------------------------------------------')
    toDIn(E, LIn, DIn)

    print("R'I SIN INFLUENCIA DE ELEMENTOS LATERALES")
    print('------------------------------------------')
    toRI(E, LIn, FR, RI)

"""
    print()
    print("R'I CON INFLUENCIA DE ELEMENTOS LATERALES")
    print('------------------------------------------')
    toAdd('I74','I94',arrayS3)                 # Creamos array con los valores SUB3
    toAdd('J74','J94', arrayS4)               # Creamos array con los valores SUB4
    toAdd('K74','K94',arrayS5)                 # Creamos array con los valores SUB5
    toAdd('L74','L94', arrayS6)               # Creamos array con los valores SUB6
    toPrint3(arrayE, arrayLIn, arrayS3, arrayS4, arrayS5, arrayS6, arrayFR, toRI2, arrayRI2)
"""
