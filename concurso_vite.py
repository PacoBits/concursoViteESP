################################################################
####### Design & Develop by @Pacobits - fjducha@yahoo.es
####### Use for free
################################################################
#import hashlib
import sha3


#variables de parametrizacion.
_ficheroentrada='concurso_vite.txt'
_ficherosalida='resultado_concurso_vite.txt'
_iteraciones=999
_lista={}

#funcion que realiza las iteraciones del Hash
def iteradorhash(iteraciones,cadena):
    i=0
    #k = hashlib.sha3_256()
    k = sha3.keccak_256()
    oper=cadena
    oper2=b""
    while i<iteraciones:        
        k.update(oper.encode())
        oper2= bytes(k.digest() + oper2)
        oper=oper2.hex()
        i+=1      
    return k.hexdigest()


#proceso principal
with  open(_ficheroentrada, 'r')  as fr:
    lines = list(line for line in (l.strip() for l in fr) if line)
    for line in lines:
        parametros=line.split(',')
        valor=iteradorhash(_iteraciones,parametros[0])
        _lista[('0X' +valor).encode()]=parametros[0]
        print('procesado: ' +parametros[0])

# Ordenamos de mayor a menor y escribimos el resultado        
resultado=list(reversed((sorted(_lista.items()))))
fw = open(_ficherosalida,'w')
for item in resultado:
    print(item[0],item[1])
    fw.write(str(item[0]) + ','+str(item[1]) +'\n')
fr.close()
fw.close()
