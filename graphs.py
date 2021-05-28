## SCRIPT PARA LOS GRÁFICOS RELACIONADOS CON PRESIÓN
## ISO 140-4 E ISO 16283-1

from pylab import *                     # Nos permite crear gráficos
from openpyxl import load_workbook      # Nos permite leer de ficheros .xlsx

# VARIABLES GLOBALES
SHEET = 'Hoja 1'        # Hoja del archivo XLSX
FILE  = 'datos2.xlsx'    # Variable para el fichero principal

## RANGO DE FRECUENCIAS
FR = ['50', '63', '80', '100', '125', '160', '200', '250', '315', '400', '500', '630', '800', '1000', '1250', '1600', '2000','2500', '3150', '4000', '5000']

# 140-4:
LpE_140 = [69.1, 67.5, 67.4, 85.3, 85.7, 92.7, 96.5, 98.3, 100.4, 101.1, 100.3, 100.4, 99.6, 99.0, 98.8, 98.1, 99.1, 101.4, 99.7, 96.7, 95.5] ## EMISIÓN
LpR_140 = [47.9, 49.6, 41.0, 47.6, 52.0, 68.7, 66.4, 68.0, 68.2, 67.3, 63.9, 60.8, 59.3, 58.0, 56.5, 56.1, 57.2, 56.9, 52.8, 49.1, 47.8] ## RECEPCIÓN
RF = [33.4, 23.7, 14.9, 33.4, 19.1, 24.7, 35.2, 18.7, 16.5, 15.2, 28.5, 22.7, 18.5, 19.1, 19.7, 22.2, 18.0, 16.5, 13.1, 10.8, 9.4] ## RUIDO DE FONDO en RECEPCIÓN

## TR:
TR = [1.9, 1.5, 1.6, 1.1, 1.2, 1.1, 1.6, 1.3, 1.0, 1.0, 1.1, 1.0, 1.2, 1.1, 1.0, 0.8, 0.8, 0.9, 0.9, 0.8, 0.8]

#DATOS EN BAJA FRECUENCIA | ISO 16283-1
E_BF_A1 = [74.1, 76.6, 77.6]
R_BF_A1 = [54.7, 59.4, 57.9]
E_BF_A2 = [79.6, 80.6, 80.1]
R_BF_A2 = [56.0, 59.6, 53.8]

A1_LpE = [64.2, 64.0, 66.9, 84.9, 84.5, 91.8, 96.5, 97.5, 100.3, 100.6, 99.7, 100.1, 99.2, 98.9, 98.9, 98.2, 99.2, 101.5, 99.8, 96.7, 95.5]
A2_LpE = [71.3, 69.4, 67.9, 85.7, 86.6, 93.3, 96.5, 99.0, 100.6, 101.6, 100.8, 100.7, 99.9, 99.0, 98.7, 98.0, 98.9, 101.3, 99.6, 96.7, 95.4]
A1_LpR = [41.4, 44.2, 41.5, 48.0, 52.7, 69.2, 64.5, 67.4, 68.6, 66.0, 63.3, 60.7, 59.0, 58.1, 56.1, 55.9, 57.0, 56.5, 52.6, 49.4, 47.5]
A2_LpR = [50.4, 51.9, 40.5, 47.3, 51.3, 68.1, 67.7, 68.4, 67.7, 68.2, 64.4, 61.0, 59.6, 57.9, 56.9, 56.3, 57.3, 57.2, 53.0, 48.9, 48.0]

##DIFERENCIA SONORA APARENTE
DnT_140 = [27.0, 22.7, 31.5, 41.1, 37.5, 27.4, 35.2, 34.4, 35.2, 36.8, 39.8, 42.6, 44.1, 44.4, 45.3, 44.0, 43.9, 47.1, 49.5, 49.6, 49.7] # ISO 140-4
DnT_16283 = [27.5, 23.3, 31.4, 41.0, 37.0, 27.1, 35.2, 34.4, 35.3, 37.0, 39.8, 42.5, 44.0, 44.3, 45.3, 44.0, 43.9, 47.1, 49.5, 49.5, 49.7] # ISO 16283-1
DnT_BF = [24.8, 22.9, 26.8, 41.0, 37.0, 27.1, 35.2, 34.4, 35.3, 37.0, 39.8, 42.5, 44.0, 44.3, 45.3, 44.0, 43.9, 47.1, 49.5, 49.5, 49.7] # ISO 16283-1 | BF

##INDICE DE REDUCCION SONORA APARENTE
R_140 = [27.1, 22.8, 31.6, 41.3, 37.6, 27.6, 35.3, 34.6, 35.4, 37.0, 40.0, 42.8, 44.2, 44.6, 45.5, 44.2, 44.1, 47.2, 49.6, 49.8, 49.9] # ISO 140-4
R_16283 = [27.6, 23.4, 31.5, 41.2, 37.1, 27.3, 35.3, 34.6, 35.5, 37.2, 40.0, 42.7, 44.1, 44.5, 45.5, 44.2, 44.1, 47.2, 49.6, 49.7, 49.9] # ISO 16283-1
R_BF = [25.0, 23.0, 27.0, 41.2, 37.1, 27.3, 35.3, 34.6, 35.5, 37.2, 40.0, 42.7, 44.1, 44.5, 45.5, 44.2, 44.1, 47.2, 49.6, 49.7, 49.9] # ISO 16283-1 | BF

#ARRAYS VALORES MICRO:
M1 = []
M2 = []
M3 = []
M4 = []
M5 = []
M6 = []
M7 = []
M8 = []
M9 = []
M10 = []

RF1 = []
RF2 = []
RF3 = []
RF4 = []
RF5 = []
RF6 = []
RF7 = []
RF8 = []
RF9 = []
RF10 = []
RF11 = []

R1 = []
R2 = []
R3 = []
R4 = []
R5 = []
R6 = []
R7 = []
R8 = []
R9 = []
R10 = []

# Función que permite añadir datos desde el Excel en un array:
# A: inicio columna HORIZONTAL, B: fin columna HORIZONTALZ;
# C: inicio columna VERTICAL; D: fin columna VERTICAL
def toAdd(A, B, myArray):
    wb = load_workbook(FILE, read_only=True)        # Cargamos en wb el fichero
    sheet = wb[SHEET]                               # Cargamos la hoja del fichero de donde obtenemos los datos
    myrow = sheet[A:B]                              # Nos colocamos en la fila que va de celda A >> celda B.

    for row in myrow:
        for cell in row:
            L = cell.value
            myArray.append(round(L,1))

    return (L)

## REPRESENTACIÓN DE RESULTADOS EN GRÁFICOS:
def toDraw(A, B):
    title(A)
    xlabel('Frecuencia [Hz]')
    ylabel('Niveles [dB]')
    ylim(0,110)
    legend((B),
    prop = {'size': 10}, bbox_to_anchor=(1.05, 1.0), loc='best')
    grid()

def toDraw2(A):
    title(A)
    xlabel('Frecuencia [Hz]')
    ylabel('Tiempo[s]')
    ylim(0, 2)
    legend(('TR20'),
    prop = {'size': 10}, loc='best')
    grid()

## VALORES EN EMISIÓN
toAdd('C8', 'C28', M1)
toAdd('D8', 'D28', M2)
toAdd('E8', 'E28', M3)
toAdd('F8', 'F28', M4)
toAdd('G8', 'G28', M5)
toAdd('H8', 'H28', M6)
toAdd('I8', 'I28', M7)
toAdd('J8', 'J28', M8)
toAdd('K8', 'K28', M9)
toAdd('L8', 'L28', M10)

## VALORES DEL RUIDO DE FONDO EN EMISIÓN
toAdd('AE8', 'AE28', RF1)
toAdd('AH8', 'AH28', RF2)
toAdd('AK8', 'AK28', RF3)
toAdd('AN8', 'AN28', RF4)
toAdd('AQ8', 'AQ28', RF5)

## VALORES EN RECEPCIÓN
toAdd('P8', 'P28', R1)
toAdd('Q8', 'Q28', R2)
toAdd('R8', 'R28', R3)
toAdd('S8', 'S28', R4)
toAdd('T8', 'T28', R5)
toAdd('U8', 'U28', R6)
toAdd('V8', 'V28', R7)
toAdd('W8', 'W28', R8)
toAdd('X8', 'X28', R9)
toAdd('Y8', 'Y28', R10)

## RUIDO DE FONDO EN RECEPCIÓN
toAdd('BD8', 'BD28', RF11)

if __name__ == "__main__":

    figure('VALORES EN EMISIÓN')
    plot(FR, M1, 'co-', M2, 'bo-', M3, 'ro-', M4, 'mo-', M5, 'go-',
    M6, 'cs-', M7, 'bs-', M8, 'rs-', M9, 'ms-', M10, 'gs-',
    RF1, 'y*-', RF2, 'k*-', RF3, 'g*-', RF4, 'r*-', RF5, 'c*-')
    toDraw('NIVELES DE PRESIÓN EN LA SALA EMISORA',
    ('M1','M2','M3','M4','M5','M6','M7','M8','M9', 'M10', 'RF1', 'RF2', 'RF3', 'RF4', 'RF5'))

    figure('VALORES EN RECEPCIÓN')
    plot(FR, R1, 'co-', R2, 'bo-', R3, 'ro-', R4, 'mo-', R5, 'go-',
    R6, 'cs-', R7, 'bs-', R8, 'rs-', R9, 'ms-', R10, 'gs-',
    RF11,'y*-')
    toDraw('NIVELES DE PRESIÓN EN LA SALA RECEPTORA',
    ('M1','M2','M3','M4','M5','M6','M7','M8','M9', 'M10', 'RF'))

    #REPRESENTACIÓN DE LOS NIVELES EN EMISIÓN Y RECEPCIÓN
    figure('140-4')
    plot(FR, LpE_140, 'co-', LpR_140, 'bo-', RF, 'go-')        # Genera el gráfico
    toDraw('NIVELES PROMEDIADOS ENERGÉTICAMENTE PARA AMBAS SALAS', ('LpE', 'LpR', 'LpRF'))

    #REPRESENTACIÓN DEL TR
    figure('TR20')
    plot(FR, TR, 'ro-')        # Genera el gráfico
    toDraw2('TIEMPO DE REVERBERACIÓN EN LA SALA RECEPTORA')

    #REPRESENTACIÓN DE LOS NIVELES EN EMISIÓN Y RECEPCIÓN
    #subplot(3,1,1)
    figure('POR DEFECTO')
    plot(FR, A1_LpE, 'co-', A2_LpE, 'bo-', LpE_140, 'm*-',
    A1_LpR, 'go-', A2_LpR, 'yo-', LpR_140, 'r*-')
    leg1 = ('LpE_A1', 'LpE_A2', 'LpE_140',
    'LpR_A1','LpR_A2', 'LpR_140',)
    toDraw('PROCEDIMIENTO POR DEFECTO. 140-4 vs 16283-1', leg1)

    figure('POR DEFECTO VS BF')
    plot(FR, A1_LpE, 'co-', A2_LpE, 'bo-', LpE_140, 'm*-', E_BF_A1, 'ks-', E_BF_A2, 'ys-',
    A1_LpR, 'go-', A2_LpR, 'yo-', LpR_140, 'r*-', R_BF_A1, 'ks-', R_BF_A2, 'cs-')
    leg2 = ('LpE_A1', 'LpE_A2', 'LpE_140', 'LpE_BF_A1', 'LpE_BF_A2',
    'LpR_A1','LpR_A2', 'LpR_140', 'LpR_BF_A1', 'LpR_BF_A2',)
    toDraw('PROCEDIMIENTO POR DEFECTO vs PROCEDIMIENTO DE BAJA FRECUENCIA', leg2)

    #REPRESENTACIÓN DE LA DIFERENCIA SONORA APARENTE
    figure ("DnT")
    plot(FR, DnT_140, 'co-', DnT_16283, 'bo-', DnT_BF, 'go-')        # Genera el gráfico
    toDraw('DIFERENCIA NORMALIZADA', ('140-4', '16283-1', '16283-1 | BF'))

    #REPRESENTACIÓN DEL ÍNDICE DE REDUCCIÓN SONORA
    figure("R'")            # Tabla de 2x1; dibujamos en 2
    plot(FR, R_140, 'co-', R_16283, 'bo-', R_BF, 'go-')        # Genera el gráfico
    toDraw('ÍNDICE DE REDUCCIÓN SONORA', ('140-4', '16283-1', '16283-1 | BF'))

    tight_layout()          # Permite ajustar la leyenda fuera del gráfico
    show()
