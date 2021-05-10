# CALCULOS PRINCIPALES
## CÁLCULO de DnT y R' - ISO 16283-1
# Carpeta: Documents/ISAM/TFG/PYTHON/

from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx
import math                             # Nos permite usar funciones matemáticas
from pressure140 import *               # Importamos funciones del archivo pressure140
from pressure16283 import *             # Importamos funciones del archivo pressure16283

# Variables globales
SHEET = 'Hoja 1'        # Hoja del archivo XLSX
FILE  = 'datos2.xlsx'    # Variable para el fichero principal
FILE_TR = 'TR.xlsx'     # Variable para un segundo fichero (TR)
TR_BF = 1.5             # Valor del TR20 para baja frecuencia
nmicro = 5              # Posiciones de micrófono
T = 0.5                 # Tiempo de referencia = 0.5s
V = 46.3                # Volumen del recinto receptor
S = 15.4                # Área del elemento separador


## PROCEDIMIENTO ESPECÍFICO DE LA ISO 16283-1 PARA BAJA FRECUENCIA
# Cálculo del promedio de posiciones de micrófono para cada banda de frecuencia, Lp
# segun el procedimiento de baja frecuencia de la ISO 16283-1:
def toCalcBF(A, B, FR):
    Lbf = 10**(0.1*A) + 2*(10**(B*0.1))         # Hacemos el cálculo tal y como indica la norma
    Lbf = 10*math.log(Lbf/3, (10))

    print('Lp(' + FR + 'Hz) = ', B, 'dB')
    print('LpBF(' + FR + 'Hz) = ', round(Lbf,1), 'dB') # Imprimo en el terminal el resultado
                                                       # La función round(L,1) redondea L a 1 decimal.
    return (Lbf)

# Cálculo del tiempo de reverberación TR20 para cada banda de frecuencia:
def toRT(A, B, FR):
    wb = load_workbook(FILE_TR, read_only=True)      # Cargamos en wb el fichero
    sheet = wb[SHEET]                                # Cargamos la hoja del fichero de donde obtenemos los datos

    myrow = sheet[A:B]                               # Nos colocamos en la fila que va de celda A >> celda B.
    RT = 0                                           # Inicializo a cero.
    n = 0                                            # Contador de 'valores no nulos'

    #NOTA: Se añade un contadores de valores porque hay algunos resultados nulos, por lo que no todas las
    #medidas tienen el mismo número de promedios.

    for row in myrow:
        for cell in row:                             # Para cada celda de mi fila [A, B]:
            if cell.value != '*':                    # Cuando los valores  no son nulos:
                RT = RT + cell.value                 # calculo el promedio de los valores del TR por cada posición
                n = n + 1                            # Añado 1 a mis valores 'no nulos'
    RT = RT/n
    print('TR(' + FR + 'Hz) = ', round(RT,1))        # Imprimo en el terminal el resultado
    return (round(RT,1))

# Cálculo de la diferencia estandarizada, DnT por cada posición de altavoz:
# donde A y B representan los niveles de emisión y recepción respectivamente por cada banda de frecuencias.
def toDnT(A, B, TR, FR):
    DnT = A - B + 10*math.log(TR/T,(10))                     # Hacemos el cálculo tal y como indica la norma

    print('DnT(' + FR + 'Hz) = ', round(DnT,1), 'dB')   # Imprimo en el terminal el resultado
    return(DnT)

# Cálculo de la reducción sonora aparente, R' para cada posición de altavoz, A1 y A2:
# donde A y B representan los niveles de emisión y recepción respectivamente por cada banda de frecuencias.
def toR(A, B, TR, FR):
    Abs = (0.16*V)/TR                         # Calculo del área de absorción equivalente

    R = A - B + 10*math.log(S/Abs,(10))

    print('R(' + FR + 'Hz) = ', round(R,1), 'dB')   # Imprimo en el terminal el resultado
    return(round(R,1))


# Cálculo de la diferencia estandarizada DnT del sumatorio:
# donde A y B son el resultado de DnT_A por cada posición de altavoz respectivamente para cada banda de frecuencias.
def toSum(A, B, C, FR):
    DnT = 10**(-A/10) + 10**(-B/10)                     # Hacemos el cálculo tal y como indica la norma
    DnT = -10*math.log(DnT/2,(10))

    print(C, FR + 'Hz) = ', round(DnT,1), 'dB')   # Imprimo en el terminal el resultado
    return(DnT)


print()
print('NIVELES EN EMISIÓN A1')
print('---------------------')
A1_50 = 64.2                             # Promedio 50 Hz en A1
BF50_A1 = 78.6                           # Esquina más ruidosa en 50 Hz - A1
A1_50BF = toCalcBF(BF50_A1, A1_50, '50') # Promedio 50 Hz en A1 según Procedimiento BF

A1_63 = 64.0                             # Promedio 63 Hz en A1 en Emisión
BF63_A1 = 81.2                           # Esquina más ruidosa en 63 Hz - A1
A1_63BF = toCalcBF(BF63_A1, A1_63, '63') # Promedio 63 Hz en A1 según Procedimiento BF

A1_80 = 66.9                             # Promedio 80 Hz en A1 en Emisión
BF80_A1 = 82.1                           # Esquina más ruidosa en 83 Hz
A1_80BF = toCalcBF (BF80_A1, A1_80, '80')   # Promedio 80 Hz en A1 según Procedimiento BF

print()
print('NIVELES EN RECEPCIÓN A1')
print('-----------------------')

A1_50_R = 55.8                               # Promedio 50 Hz en A1
BF50_R1 = 59.3                               # Esquina más ruidosa en 50 Hz en Recepción - A1
A1_50BF_R = toCalcBF(BF50_R1, A1_50_R, '50') # Promedio 50 Hz en A1 según procedimiento BF

A1_63_R = 54.5                               # Promedio 63 Hz en A1
BF63_R1 = 64.1                               # Esquina más ruidosa en 63 Hz en Recepción - A1
A1_63BF_R = toCalcBF(BF63_R1, A1_63_R, '63') # Promedio 63 Hz en A1 según procedimiento BF

A1_80_R = 45.7                               # Promedio 80 Hz en A1
BF80_R1 = 62.6                               # Esquina más ruidosa en 80 Hz en Recepción - A1
A1_80BF_R = toCalcBF(BF80_R1, A1_80_R, '80') # Promedio 80 Hz en A1 según procedimiento BF

print()
print('TIEMPO DE REVERBERACIÓN')
print('-----------------------')

TR50 = toRT('C6', 'H6', '50')                         # TR 50 Hz
TR63 = toRT('C7', 'H7', '63')                         # TR 63 Hz
TR80 = toRT('C8', 'H8', '80')                         # TR 80 Hz

print()
print('DIFERENCIA ESTANDARIZADA A1')
print('---------------------------')

DnT50_A1 = toDnT(A1_50, A1_50_R, TR50, '50')              # DnT 50 Hz en A1
DnT50_A1BF = toDnT(A1_50BF, A1_50BF_R, TR_BF, '50-BF')     # DnT 50 Hz en A1 según Procedimiento BF
DnT63_A1 = toDnT(A1_63, A1_63_R, TR63, '63')              # DnT 63 Hz en A1
DnT63_A1BF = toDnT(A1_63BF, A1_63BF_R, TR_BF, '63-BF')     # DnT 63 Hz en A1 según Procedimiento BF
DnT80_A1 = toDnT(A1_80, A1_80_R, TR80, '80')              # DnT 80 Hz en A1
DnT80_A1BF = toDnT(A1_80BF, A1_80BF_R, TR_BF, '80-BF')     # DnT 80 Hz en A1 según Procedimiento BF

print()
print('ÍNDICE DE REDUCCIÓN SONORA APARENTE A1')
print('--------------------------------------')

R50_A1 = toR(A1_50, A1_50_R, TR50, '50')              # R' 50 Hz en A1
R50_A1BF = toR(A1_50BF, A1_50BF_R, TR_BF, '50-BF')     # R' 50 Hz en A1 según Procedimiento BF
R63_A1 = toR(A1_63, A1_63_R, TR63, '63')              # R' 63 Hz en A1
R63_A1BF = toR(A1_63BF, A1_63BF_R, TR_BF, '63-BF')     # R' 63 Hz en A1 según Procedimiento BF
R80_A1 = toR(A1_80, A1_80_R, TR80, '80')              # R' 80 Hz en A1
R80_A1BF = toR(A1_80BF, A1_80BF_R, TR_BF, '80-BF')     # R' 80 Hz en A1 según Procedimiento BF

print()
print()
print('NIVELES EN EMISIÓN A2')
print('---------------------')

A2_50 = 71.3                             # Promedio 50 Hz en A2;
BF50_A2 = 83.9                           # Esquina más ruidosa en 50 Hz - A2
A2_50BF = toCalcBF(BF50_A2, A2_50, '50') # Promedio 50 Hz en A2 según Procedimiento BF

A2_63 = 69.4                             # Promedio 63 Hz en A2
BF63_A2 = 85.1                           # Esquina más ruidosa en 50 Hz - A2
A2_63BF = toCalcBF(BF63_A2, A2_63, '63') # Promedio 63 Hz en A2 según Procedimiento BF

A2_80 = 67.9                             # Promedio 80 Hz en A2;
BF80_A2 = 84.7                           # Esquina más ruidosa en 50 Hz - A2
A2_80BF = toCalcBF(BF80_A2, A2_80, '80') # Promedio 80 Hz en A2 según Procedimiento BF


print()
print('NIVELES EN RECEPCIÓN A2')
print('-----------------------')

A2_50_R = 50.4                              # Promedio 50 Hz en A2
BF50_R2 = 59.9                              # Esquina más ruidosa en 50 Hz en Recepción - A2
A2_50BF_R = toCalcBF(BF50_R2, A2_50_R, '50')# Promedio 50 Hz en A2 según Procedimiento BF

A2_63_R = 51.9                              # Promedio 63 Hz en A2
BF63_R2 = 63.9                               # Esquina más ruidosa en 50 Hz en Recepción - A2
A2_63BF_R = toCalcBF(BF63_R2, A2_63_R, '63')# Promedio 63 Hz en A2 según Procedimiento BF

A2_80_R = 40.5                              # Promedio 80 Hz en A2
BF80_R2 = 58.4                              # Esquina más ruidosa en 50 Hz en Recepción - A2
A2_80BF_R = toCalcBF(BF80_R2, A2_80_R, '80')# Promedio 80 Hz en A2 según Procedimiento BF


print()
print('DIFERENCIA ESTANDARIZADA A2')
print('---------------------------')

# CALCULO DE LA DIFERENCIA ESTANDARIZADA de A2:
# Para cada fila de datos, se calcula DnT para cada banda de frecuencias, FR:

DnT50_A2 = toDnT(A2_50, A2_50_R, TR50, '50')              # DnT 50 Hz en A2
DnT50_A2BF = toDnT(A2_50BF, A2_50BF_R, TR_BF, '50-BF')    # DnT 50 Hz en A1 según Procedimiento BF
DnT63_A2 = toDnT(A2_63, A2_63_R, TR63, '63')              # DnT 63 Hz en A2
DnT63_A2BF = toDnT(A2_63BF, A2_63BF_R, TR_BF, '63-BF')    # DnT 63 Hz en A2 según Procedimiento BF
DnT80_A2 = toDnT(A2_80, A2_80_R, TR80, '80')              # DnT 80 Hz en A2
DnT80_A2BF = toDnT(A2_80BF, A2_80BF_R, TR_BF, '80-BF')    # DnT 80 Hz en A2 según Procedimiento BF

print()
print('ÍNDICE DE REDUCCIÓN SONORA APARENTE A2')
print('--------------------------------------')

R50_A2 = toR(A2_50, A2_50_R, TR50, '50')               # R' 50 Hz en A2
R50_A2BF = toR(A2_50BF, A2_50BF_R, TR_BF, '50-BF')     # R' 50 Hz en A2 según Procedimiento BF
R63_A2 = toR(A2_63, A2_63_R, TR63, '63')               # R' 63 Hz en A2
R63_A2BF = toR(A2_63BF, A2_63BF_R, TR_BF, '63-BF')     # R' 63 Hz en A2 según Procedimiento BF
R80_A2 = toR(A2_80, A2_80_R, TR80, '80')               # R' 80 Hz en A2
R80_A2BF = toR(A2_80BF, A2_80BF_R, TR_BF, '80-BF')     # R' 80 Hz en A2 según Procedimiento BF


print()
print('DIFERENCIA ESTANDARIZADA')
print('------------------------')


DnT50 = toSum(DnT50_A1, DnT50_A2,'DnT(', '50')              # DnT 50 Hz
DnT50_BF = toSum(DnT50_A1BF, DnT50_A2BF, 'DnT ','50-BF')    # DnT 50 Hz según Procedimiento BF
DnT63 = toSum(DnT63_A1, DnT63_A2, 'DnT(','63')              # DnT 63 Hz
DnT63_BF = toSum(DnT63_A1BF, DnT63_A2BF,'DnT ', '63-BF')    # DnT 63 Hz según Procedimiento BF
DnT80 = toSum(DnT80_A1, DnT80_A2, 'DnT(','80')              # DnT 80 Hz
DnT80_BF = toSum(DnT80_A1BF, DnT80_A2BF, 'DnT(','80-BF')    # DnT 80 Hz según Procedimiento BF

print()
print('ÍNDICE DE REDUCCIÓN SONORA APARENTE')
print('-----------------------------------')


R50 = toSum(R50_A1, R50_A2, "R'(",'50')              # R' 50 Hz
R50_BF = toSum(R50_A1BF, R50_A2BF, "R'(", '50-BF')    # R' 50 Hz según Procedimiento BF
R63 = toSum(R63_A1, R63_A2, "R'(",'63')              # R' 63 Hz
R63_BF = toSum(R63_A1BF, R63_A2BF, "R'(",'63-BF')    # R' 63 Hz según Procedimiento BF
R80 = toSum(R80_A1, R80_A2, "R'(", '80')              # R' 80 Hz
R80_BF = toSum(R80_A1BF, R80_A2BF, "R'(", '80-BF')    # R' 80 Hz según Procedimiento BF
