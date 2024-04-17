# paso 1 : Crear un archivo llamado password.py LISTO
# paso2 : Solicitamos la clave. para ello, utilizaremos la librería getpass

import getpass

password = getpass.getpass("Ingrese la clave secreta:")

# Paso 3 Si la clave es correcta queremos que nuestro programa inicie, de lo contrario, queremos que vuelva a solicitar la clave. Dado que queremos que vuelva a realizar una acción de solicitar la clave hasta que se ingrese la clave correcta, es necesario utilizar el ciclo while:

while password != "123":
    password = getpass.getpass("La clave secreta no es correcta. Intenta otra vez:")

# Paso 4 Finalmente, podemos incluir el código final de nuestro programa. En este caso, solo agregaremos un código genérico que da inicio a nuestro programa.

    print("Clave Correcta. Puedes utilizar tu programa")
    print("Tu clave es :")
print("Tu clave es:" , (password))