## GRÁFICOS 15168-1
# COMPARACIÓN DE RESULTADOS DnT y R'
# Carpeta: Documents/ISAM/TFG/PYTHON/

from pylab import *
from graphs import *

FR = ['50', '63', '80', '100', '125', '160', '200', '250', '315', '400', '500', '630', '800', '1000', '1250', '1600', '2000','2500', '3150', '4000', '5000']

## ARRAYS SUB-ÁREA 1:
H11 = [] ## BARRIDO HORIZONTAL - POSICIÓN A1
V11 = [] ## BARRIDO VERTICAL - POSICIÓN A1
H12 = [] ## BARRIDO HORIZONTAL - POSICIÓN A2
V12 = [] ## BARRIDO VERTICAL - POSICIÓN A2
## ARRAYS SUB-ÁREA 2:
H21 = [] ## BARRIDO HORIZONTAL - POSICIÓN A1
V21 = [] ## BARRIDO VERTICAL - POSICIÓN A1
H22 = [] ## BARRIDO HORIZONTAL - POSICIÓN A2
V22 = [] ## BARRIDO VERTICAL - POSICIÓN A2


## SUB1
toAdd('C42', 'C62', H11) ## BARRIDO HORIZONTAL - POSICIÓN A1
toAdd('D42', 'D62', V11) ## BARRIDO VERTICAL - POSICIÓN A1
toAdd('E42', 'E62', H12) ## BARRIDO HORIZONTAL - POSICIÓN A2
toAdd('F42', 'F62', V12) ## BARRIDO VERTICAL - POSICIÓN A2
##SUB2
toAdd('G42', 'G62', H21) ## BARRIDO HORIZONTAL - POSICIÓN A1
toAdd('H42', 'H62', V21) ## BARRIDO VERTICAL - POSICIÓN A1
toAdd('I42', 'I62', H22) ## BARRIDO HORIZONTAL - POSICIÓN A2
toAdd('J42', 'J62', V22) ## BARRIDO VERTICAL - POSICIÓN A2

## REPRESENTACIÓN DE RESULTADOS EN GRÁFICOS:

#REPRESENTACIÓN DE LOS NIVELES DE INTENSIDAD | SUB-ÁREA 1
figure()
subplot(3,1,1)
plot(FR, H11, 'co-', V11, 'bo-',H12, 'go-', V12, 'yo-')        # Genera el gráfico
toDraw('INTENSIDAD EN LA SUB-ÁREA 1 DE LA PARED DE SEPARACIÓN',
('Horizontal - A1', 'Vertical - A1','Horizontal - A2', 'Vertical - A2'))

subplot(3,1,3)
#falta añadir leyenda correcta
plot(FR, H21, 'co-', V21, 'bo-',H22, 'go-', V22, 'yo-')        # Genera el gráfico
toDraw('INTENSIDAD EN LA SUB-ÁREA 2 DE LA PARED DE SEPARACIÓN',
('Horizontal - A1', 'Vertical - A1','Horizontal - A2', 'Vertical - A2'))

tight_layout()        # Permite ajustar la leyenda fuera del gráfico
show()                # Muestra el gráfico
