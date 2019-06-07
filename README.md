# concursoViteESP
Programa para elegir al ganador del Concurso de Vite Spain de Junio 2019

El programa utiliza dos ficheros para identificar los datos de entrada y donde debe dejar los datos de salida. 

#variables de parametrizacion.
_ficheroentrada='concurso_vite.txt'
_ficherosalida='resultado_concurso_vite.txt'

Ademas usa una variable cuyo valor sera elegido por el administrador del sorteo para indicar el numero de iteraciones que se realizan.
_iteraciones=999

El proceso toma las direcciones de los wallets de los usuarios que se han apuntado al concurso, del _ficheroentrada y aplica sobre ellos un proceso de hashing iterativo sumando ademas a cada hash su ultimo valor calculado.

El resultado final será ordenado para obtener de mayor a menor para obtener al ganador

Dependencias: sha3 y hashlib


