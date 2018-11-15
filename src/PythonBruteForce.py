# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import itertools #libreria de python para poder usar iteradores
import timeit #libreria python para poder utilizar el timer
import sys #libreria python para usar argumentos por consola

#BIBLIOGRAFIA CONSULTADA
#Class itertools: https://docs.python.org/3/library/itertools.html#itertools.count
#Video tutorial: https://www.youtube.com/watch?v=fDlg3DTzHrk
#Make your own iterator: https://stackoverflow.com/questions/19151/build-a-basic-python-iterator
#Operate with string: https://www.learnpython.org/en/Basic_String_Operations
#Read-Write files: https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#Python iterators examples: https://www.w3schools.com/python/python_iterators.asp
#Python timer https://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python
#Python tuples elements: https://www.tutorialspoint.com/python/python_tuples.htm
#Python concatenate str and float: https://stackoverflow.com/questions/16948256/cannot-concatenate-str-and-float-objects
#Python command line: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

__author__ = "Andres Cabrera, Alberto Ramos, Karan Sainani"
__date__ = "$11-nov-2018 11:31:17$"

#1- Leemos el fichero de datos
file = open(sys.argv[1], "r") #abrir fichero en modo lectura
number = int(file.readline()) #Leer numero de combinaciones a conformar
codigo = file.readline() #codigo leeido del fichero

#2- Mostrar datos a ejecutar
print("El codigo a obtener es: " + codigo)

#3- Llamada al metodo combinations_with_replacement() de la clase itertools
permut = itertools.product("0123456789", repeat=number)

#variable para saber si has encontrado la combinacion
found = False

#Inicializar timer
start = timeit.default_timer()

#2- Obtener tuplas y consultar con el codigo
for i in permut: #"i" son las tuplas ya obtenidas
    if(number != len(codigo)):
        break
    pos = 0
    #print(i) #tuplas
    tuple_values = ""
    while pos != number: #acceder a los elementos de las tuplas
        tuple_values = tuple_values + i[pos]
        pos = pos+1
    if(tuple_values == codigo):
        found = True
        break
        
#Parar timer
stop = timeit.default_timer()

if found:
    print("ENCONTRADO " + tuple_values)
else:
    print("CODIGO NO ENCONTRADO")

#Obtener tiempo medio
tiempoMedio = float(stop - start) #calculo del tiempo medio
msgTiempoMedio = str(tiempoMedio) #no se puede imprimir strig + float (casteo del tiempo a string)
print("El tiempo medio ha sido " + msgTiempoMedio + " milisegundos\n")