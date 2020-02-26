#importancion del modulo de limpieza de la consola
import os
import datetime 
import time


#importancion de las clases 
from gato import Gato
from pajaro import Pajaro
from lista import Lista
from pila import Pila

#declaracion de arreglos para el almacenamiento de los valores
gatos = []
pajaros = []
palabras = []

#declaracion de variables contenedoras del archivo de salida
mascotas_result = " "
edu_result = " "

#declaracion de las estructuras de datos
lista = Lista()
pila = Pila()


print(" ")
print("----------Datos del estudiante----------")
print("|                                      |")
print("| Lenguajes formales y de programacion |")
print("|              Seccion: B-             |")
print("|           Carne: 201700965           |")
print("|                                      |")
print("----------------------------------------")
print(" ")
input("Presione enter para continuar")
# Recibir un enter, limpiar pantalla y mostrar el menu principal

def mascotas():
    pass

def menuPrincipal():
    os.system("cls")
    print(" ")
    print("------Menu Principal-------")
    print("|                         |")
    print("| 1. Menu Entretenimiento |")
    print("| 2. Menu Educacion       |")
    print("| 0. Salir                |")
    print("|                         |")
    print("---------------------------")
    print(" ")
    while True:
        lectura = int(input('Presione el numero de la accion a realizar: '))
        #lectura = int(lectura)
    #    if type(lectura) == int:
        if lectura == 1:
            menuEntretenimiento()
        elif lectura == 2:
            menuEducacion()
        elif lectura == 0:
            print("Hasta la proxima c:")
            exit(0)
        else:
            print("\nIngrese una opcion valida \n")
     #   else: 
      #      print("ingrese unicamente numeros")

def menuEntretenimiento():
    os.system("cls")
    print(" ")
    print("-------Menu Entretenimiento-------")
    print("|                                |")
    print("| 1. Carga del archivo .mascotas |")
    print("| 0. Regresar al menu principal  |")
    print("|                                |")
    print("----------------------------------")
    print(" ")
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        lectura = int(lectura)
        if lectura == 1:
            print("carga del archivo")
        elif lectura == 0:
            menuPrincipal()
        else:
            print("\nIngrese una opcion valida \n")

def almacenCaracteres():
    path = input("\n Ingrese la ruta del archivo: ")  
    
    #limpiando la lista y el arreglo
    palabras = []
    lista.limpiar()
    lista.agregar(1)

    #"r" es para dar permisos de lectura y "w" es para dar permisos de lectura y escritura
    archivo_almacen = open(path,"r")
   
    """ readlines() lee linea por linea pero agrega un salto de linea al final de cada
        lectura """
    
    #read() lectura del archivo en su totalidad
    contenido = archivo_almacen.read()
    division = contenido.split("\n")
    almacen_result = " "

    for linea in division:  
        instruccion = linea.split(":")
        fecha = datetime.datetime.now()

        if instruccion[0] == "Declarar":
            #agregar las palabras a un arreglo auxiliar
            palabras.append(instruccion[1])
           
            #separar el ID de la palabra y su contenido
            palabra = instruccion[1].split(",")
            
            #obtención del contenido
            asignacion = palabra[1]

            """agregar longitud de la palabra eliminando la longitud que presentan las "" por la forma del 
            archivo de entrada"""
            lista.agregar(len(asignacion)-2)
            
            #generacion del reporte
            if len(almacen_result) != 0:
                almacen_result = almacen_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + palabra[0] + ", " + palabra[1] + "\n"
            else:
                almacen_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + palabra[0] + ", " + palabra[1] + "\n"


            #recorriendo la palabra para agregar los caracteres de la misma a la lista
            for iteracion in asignacion:
                if iteracion != '"':
                    lista.agregar(iteracion)
            
            #modificando la siguiente posicion vacia disponible
            lista.cabeza.objeto = lista.tamanyo
        elif instruccion[0] == "Concatenar":
            pass
        elif instruccion[0] == "Posicion_cadena":
            
            #contadores para medir longitud de palabras y cantidad de palabras que se han recorrido
            contador = 0
            contador_2 = 0

            #recorrido del arreglo auxiliar para las palabras
            for i in palabras:

                #division del contenido del arreglo para buscar coincidencias con la palabra a buscar
                cadena = i.split(",")

                #aumento del contador de palabras ya recorridas
                contador_2 = contador_2 + 1

                #buscar coincidencia en el ID de la palabra del arreglo y la ingresada
                if cadena[0] == instruccion[1]:
                    #suma de las posiciones recorridas y las longitudes de las palabras
                    contador = contador + contador_2
                    
                    #generacion del reporte
                    if len(almacen_result) != 0:
                        almacen_result = almacen_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + ", Pos: " + str(contador) + "\n"
                    else:
                        almacen_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + ", Pos: " + str(contador) + "\n"

                #aumento del contador de la longitud de las palabras
                contador = contador + (len(cadena[1])-2)    
        elif instruccion[0] == "Tamanio":
            #recorrido del arreglo auxiliar
            for i in palabras:
                #separacion del contenido del arreglo auxiliar
                identificador = i.split(",")
                #buscar conincidencia con el id ingresado y el del arreglo auxiliar
                if instruccion[1] == identificador[0]:
                    #generacion de reporte
                    if len(almacen_result) != 0:
                        almacen_result = almacen_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + identificador[0] + ", Tam: " + str(len(identificador[1])-2) + "\n"
                    else:
                        almacen_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + identificador[0] + ", Tam: " + str(len(identificador[1])-2) + "\n"
        elif instruccion[0] == "Imprimir":
             #contadores para medir longitud de palabras y cantidad de palabras que se han recorrido
            contador = 0
            contador_2 = 0

            #recorrido del arreglo auxiliar para las palabras
            for i in palabras:

                #division del contenido del arreglo para buscar coincidencias con la palabra a buscar
                cadena = i.split(",")

                #aumento del contador de palabras ya recorridas
                contador_2 = contador_2 + 1

                #buscar coincidencia en el ID de la palabra del arreglo y la ingresada
                if cadena[0] == instruccion[1]:
                    #suma de las posiciones recorridas y las longitudes de las palabras
                    contador = contador + contador_2 + 1
                    for j in cadena[1]:
                        if j != '"':
                             #generacion de reporte
                            if len(almacen_result) != 0:
                                almacen_result = almacen_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + ", " + str(contador) + ", "+ j +"\n"
                            else:
                                almacen_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + ", " + str(contador) + ", "+ j  + "\n"
                            contador = contador + 1 

                #aumento del contador de la longitud de las palabras
                contador = contador + (len(cadena[1])-2)   
        elif instruccion[0] == "Generar_grafo":
            #inicio del codigo del grafo
            dot = "digraph G{ \n"
            dot = dot + "\nnode [shape=box];\nnode [style=filled];\nnode [fillcolor=\"#EEEEEE\"];\nnode [color=\"#EEEEEE\"];\nedge [color=\"#31CEF0\"]; \n"
           
            #recorrido del grafo obteniendo sus elementos y asignandoles un identificador
            aux = lista.cabeza 
            identificador = 0
            while aux != None:
                dot = dot + str(identificador) + " [label= "+ '"'+ str(identificador) +") " +str(aux.objeto)+'"'+"];\n"   
                identificador = identificador + 1
                aux = aux.siguiente
            
            #reinicio de identificadores
            identificador = 0
            identificador_2 = 0
            aux = lista.cabeza

            #recorrido para hacer enlaces entre nodos del grafo
            while aux != None:
                if identificador < (lista.tamanyo-1):
                    identificador_2 = identificador + 1
                    dot = dot + str(identificador) + "->" + str(identificador_2) + ";\n"
                    identificador = identificador + 1
                aux = aux.siguiente

            #finalizacion del codigo del grafo    
            dot = dot + "}"
            
            #rutas del .dot y la imagen
            path_dot = instruccion[1]+":"+instruccion[2] + "//grafo.dot"
            path_imagen = instruccion[1]+":"+instruccion[2] + "//grafo.png"
            
            #escritura del .dot
            archivo_dot = open(path_dot,"w")
            archivo_dot.write(dot)
            archivo_dot.close()

            #compilacion del .dot
            os.system('dot {} -Tpng -o {}'.format(path_dot,path_imagen))
            
            #apertura de la imagen generada
            os.system(path_imagen)
    
    resultado = open("C:/Users/chepe/Desktop/archivo.almacen_result","w")
    resultado.write(almacen_result)
    resultado.close()
    os.system("C:/Users/chepe/Desktop/archivo.almacen_result")
    menuPrincipal()

def menuEducacion():
    os.system("cls")
    print(" ")
    print("---------Menu Educacion----------")
    print("|                               |")
    print("| 1. Carga del archivo .edu     |")
    print("| 2. Carga del archivo .almacen |")
    print("| 0. Regresar al menu principal |")
    print("|                               |")
    print("---------------------------------")
    print(" ")
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        lectura = int(lectura)
        if lectura == 1:
            print("carga del archivo")
        elif lectura == 2:
            almacenCaracteres()
        elif lectura == 0:
            menuPrincipal()
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()


