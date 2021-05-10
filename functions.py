
import openpyxl
#from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx
import math                             # Nos permite usar funciones matemáticas
from pylab import *                     # Nos permite crear gráficos


## ISO 717-1
# Array con las frecuencias correspondientes al rango 100 Hz - 3150 Hz:
FR = [100, 126, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150]
# Array con las frecuencias correspondientes al rango ampliado 50-5000Hz:
FR_A = [50, 63, 80, 100, 126, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]
# Valores de referencia, en dB, según la norma:
arrayREF = [33, 36, 39, 42, 45, 48, 51, 52, 53, 54, 55, 56, 56, 56, 56, 56]
# Valores del espectro n1, para el rango 100-3150Hz:
arrayC = [-29, -26, -23, -21, -19, -17, -15, -13, -12, -11, -10, -9, -9, -9, -9, -9]
# Valores del espectro n1, para el rango ampliado 50-5000Hz:
arrayC_A = [-41, -37, -34, -30, -27, -24, -22, -20, -18, -16, -14, -13, -12, -11, -10, -10, -10, -10, -10, -10, -10]
# Valores del espectro n2, para el rango 100-3150Hz:
arrayCtr = [-20, -20, -18, -16, -15, -14, -13, -12, -11, -9, -8, -9, -10, -11, -13, -15]
# Valores del espectro n2, para el rango ampliado 50-5000Hz:
arrayCtr_A = [-25, -23, -21, -20, -20, -18, -16, -15, -14, -13, -12, -11, -9, -8, -9, -10, -11, -13, -15, -16, -18]

# CÁLCULO DE MAGNITUDES GLOBALES Y TÉRMINOS DE ADAPTACIÓN
# SEGÚN ISO 717-1 PARA LOS RESULTADOS DE LAS NORMA ISO 140-4 E ISO 16283-1

# Calcula la desviación favorable en función del desplazamiento escogido,
# donde A = valor de referencia i , B = desplazamiento, C = magnitud
def toCalcDesv (A, B, C):
    desv = A - B - C
    return(desv)

# Calcula el nivel sonoro del espectro n,
# donde A = espectro n, B = magnitud
def toCalcEsp (A, B):
    esp = A - B
    esp = 10**(esp/10)        # dB x 10**(-5)
    return(esp)

# Calcula la desviación favorable con el desplazamiento 'elegido', y calcula dicha desviación
# donde A = valor de referencia i , B = desplazamiento, C = magnitud
def toPrintDesv(A, B, C):
    i = 0                                           # Iterador
    total = 0                                       # Variable que almacena la desviación total

    for value in A:
        desv = toCalcDesv(A[i], B, C[i])            # Accede al elemento [i] de los arrays

        if desv > 0:
            total = total + desv                    # Sumatorio de las desviaciones SOLO favorables
        i = i + 1                                   # Siguiente elemento

    if total < 32:
        print('desv. favorable: ', round(total, 1), '< 32')     # Imprime mensaje que de que la desviación total favorable
    else:
        print(round(total, 1), '> 32')             # Imprime que el desplazamiento elegido no es correcto

# Bucle que recorre los arrays A y B, llamando a una función, e imprimiendo los resultados:
def toPrintEsp (A, B):
    i = 0                                          # Iterador
    sum = 0                                        # Variable que almacena los niveles sonoros
    for value in A:
        esp = toCalcEsp(A[i], B[i])                # Accede al elemento [i] de los arrays
        sum = sum + esp                            # Sumatorio de los niveles de sonoros

        i = i + 1                                  # Siguiente elemento

    myEsp = (-10)*math.log(sum,(10))
    return(round(myEsp))

# Imprime la magnitud global del término, donde
# A: es el desplazamiento elegido,  B: array de valores de 100-3150 Hz;
# C: array de valores de 50-5000 Hz, D: nombre de la magnitud
def toPrint717(A, B, D, E):
    toPrintDesv(arrayREF, A, B)                 # Según el desplazamiento, calcula la desviación favorable
    X = 52 - A                                  # Valor de la magnitud = 52 - desplazamiento
    C = toPrintEsp(arrayC, B)                   # Calculo del nivel sonoro del espectro, C en el rango 100-3150 Hz
    Ctr = toPrintEsp(arrayCtr, B)               # Calculo del nivel sonoro del espectro, Ctr en el rango 100-3150 Hz
    print(E, 'w(C, Ctr) =', X, '(', C - X, ';', Ctr - X, ')')

    C_A = toPrintEsp(arrayC_A, D)              # Calculo del nivel sonoro del espectro, C en el rango 50-5000 Hz
    Ctr_A = toPrintEsp(arrayCtr_A, D)          # Calculo del nivel sonoro del espectro, Ctr en el rango 50-5000 Hz
    print(E, 'w(C, Ctr, C50-5K, Ctr50-5K) =', X, '(', C - X, ';', Ctr - X, ';', C_A - X, ';', Ctr_A - X, ')')
