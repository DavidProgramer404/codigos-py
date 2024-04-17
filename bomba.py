# Paso 1
# Crear el archivo bomba.py

# Paso 2
# En este caso podemos utilizar sys.argv para ingresar el número de segundos antes de explotar.

# Paso 3
# Creamos un ciclo que nos permita generar decremento, desde el valor inicial hasta cero.

# Paso 4
# Para que efectivamente i represente un segundo, podemos utilizar la librería time, la 
# que nos permitirá esperar un segundo entre cada decremento. La idea es que al 
# terminar el ciclo, la bomba explote, de manera que el código completo se vea así:

# Paso 5
# Si bien este ejercicio puede 
# parecer simple, no es tan 
# intuitivo entender el código. 
# A continuación, se muestra 
# cómo sería en caso de no utilizar 
# un ciclo, a través de un ejemplo 
# que demuestra el caso de 5 
# segundos:

import time
import sys


i = 5
print(i) # Muestra el valor 5
time.sleep(1) # espera un segundo
i = 4 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 4
time.sleep(1) # espera un segundo
i = 3 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 3
time.sleep(1) # espera un segundo
i = 2 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 2
time.sleep(1) # espera un segundo
i = 1 # Descuenta 1 al valor de i.
print(i) # Muestra el valor de i
time.sleep(1) # espera un segundo
i = 0
# En este punto se evalúa el fin de ciclo ya que i es cero.
print("BOOM!") # al salir del ciclo la bomba explota!!