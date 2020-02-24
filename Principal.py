#importancion del modulo de limpieza de la consola
import os
import time

#importancion de las clases 
from gato import Gato
from pajaro import Pajaro

#declaracion de arreglos para el almacenamieno de las mascotas
gatos = []
pajaros = []

#declaracion de variables contenedoras del archivo de salida
mascotas_result = " "
edu_result = " "
almacen_result = " "


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
        lectura = input('Presione el numero de la accion a realizar: ')
        lectura = int(lectura)
        if lectura == 1:
            menuEntretenimiento()
        elif lectura == 2:
            menuEducacion()
        elif lectura == 0:
            print("Hasta la proxima c:")
            exit(0)
        else:
            print("\nIngrese una opcion valida \n")

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
            print("carga del archivo")
        elif lectura == 0:
            menuPrincipal()
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()


