# CALCULOS PRINCIPALES
## CÁLCULO de DnT y R' - ISO 16283-1
# Carpeta: Documents/ISAM/TFG/PYTHON/

from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx
import math                             # Nos permite usar funciones matemáticas
from pylab import *                     # Nos permite crear gráficos
from pressure140 import *               # Importamos funciones del archivo pressure140

# Variables globales
SHEET = 'Hoja 1'        # Hoja del archivo XLSX
FILE  = 'datos2.xlsx'   # Variable para el fichero principal
FILE_TR = 'TR.xlsx'     # Variable para un segundo fichero (TR)
T = 0.5                 # Tiempo de referencia = 0.5s
V = 46.3                # Volumen del recinto receptor
S = 15.4                # Área del elemento separador


# Arrays vacíos
LpE_A1 = []           # Array para los resultados del nivel de presión en emisión , LpE-A1
LpR_A1 = []           # Array para los resultados del nivel de presión en recepción, LpR-A1
LpE_A2 = []           # Array para los resultados del nivel de presión en emisión , LpE-A2
LpR_A2 = []           # Array para los resultados del nivel de presión en recepción, LpR-A2
TR = []               # Array para los resultados del tiempo de reverberación en recepción, TR
DnT_A1 = []           # Array para los resultados del nivel de diferencia normalizada, DnT-A1
DnT_A2 = []           # Array para los resultados del nivel de diferencia normalizada, DnT-A2
myDnT = []            # Array para los resultados del nivel de diferencia normalizada global, DnT
R_A1 = []             # Array para los resultados del índice de reducción sonora aparente, R'- A1
R_A2 = []             # Array para los resultados del índice de reducción sonora aparente, R'- A2
myR = []              # Array para los resultados del índice de reducción sonora aparente global, R'

## PROCEDIMIENTOS ESPECÍFICOS DE LA ISO 16283-1
# Cálculo del sumatorio de las magnitudes en función de la posición de altavoz:
# donde A y B son los resultados por cada posición de altavoz respectivamente para cada banda de frecuencias.
def toSum(A, B, myArray):
    i = 0
    for num in A:
        sum = 10**(-A[i]/10) + 10**(-B[i]/10)       # Hacemos el cálculo tal y como indica la norma
        X = -10*math.log(sum/2,(10))                # Dividimos entre 2, el número de pos de altavoz, A1 y A2
        i = i + 1
        myArray.append(round(X,1))

if __name__ == "__main__":
    print()
    print('NIVELES EN EMISIÓN A1')
    print('---------------------')
    toCalc(8, 28, 3, 7, 5, LpE_A1)
    toPrint(LpE_A1, 'dB - ')

    print()
    print('NIVELES EN RECEPCIÓN A1')
    print('-----------------------')
    toCalc(8, 28, 16, 20, 5, LpR_A1)
    toPrint(LpR_A1, 'dB - ')

    print()
    print('TIEMPO DE REVERBERACIÓN')
    print('-----------------------')
    toRT(6, 26, 3, 8, TR)
    toPrint(TR, 's - ')

    print()
    print('DIFERENCIA ESTANDARIZADA A1')
    print('---------------------------')
    toDnT(LpE_A1, LpR_A1, TR, DnT_A1)
    toPrint(DnT_A1, 'dB - ')

    print()
    print('ÍNDICE DE REDUCCIÓN SONORA APARENTE A1')
    print('--------------------------------------')
    toR(LpE_A1, LpR_A1, TR, R_A1)
    toPrint(R_A1, 'dB - ')

    print()
    print('NIVELES EN EMISIÓN A2')
    print('---------------------')
    toCalc(8, 28, 8, 12, 5, LpE_A2)
    toPrint(LpE_A2, 'dB - ')

    print()
    print('NIVELES EN RECEPCIÓN A2')
    print('-----------------------')
    toCalc(8, 28, 21, 25, 5, LpR_A2)
    toPrint(LpR_A2, 'dB - ')

    print()
    print('DIFERENCIA ESTANDARIZADA A2')
    print('---------------------------')
    toDnT(LpE_A2, LpR_A2, TR, DnT_A2)
    toPrint(DnT_A2, 'dB - ')

    print()
    print('ÍNDICE DE REDUCCIÓN SONORA APARENTE A2')
    print('--------------------------------------')
    toR(LpE_A2, LpR_A2, TR, R_A2)
    toPrint(R_A2, 'dB - ')

    print()
    print('DIFERENCIA ESTANDARIZADA')
    print('------------------------')
    toSum(DnT_A1, DnT_A2, myDnT)
    toPrint(myDnT, 'dB - ')

    print()
    print('ÍNDICE DE REDUCCIÓN SONORA APARENTE')
    print('-----------------------------------')
    toSum(R_A1, R_A2, myR)
    toPrint(myR, 'dB - ')
