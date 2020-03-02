#importancion del modulo de limpieza de la consola
import os
import datetime 
import time


#importancion de las clases 
from gato import Gato
from pajaro import Pajaro
from lista import Lista

#declaracion de variables contenedoras del archivo de salida
edu_result = " "
cadena = []

#declaracion de las estructuras de datos
lista = Lista()


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

    #guardado de la ruta dl archivo de mascotas
    path = input("\nIngrese la ruta del archivo: ")

    #vaciado del arreglo de mascotas y el contenido del archivo de salida
    mascotas = []
    mascotas_result = " "

    #validando que la extension del archivo sea la correcta
    while True:
        nombre,extension = os.path.splitext(path)
        if extension == ".mascotas":
            break
        else:
            path = input("\nIngrese la ruta del archivo: ")

    #apertura y lectura del contenido del archivo de las instrucciones 
    archivo_mascotas = open(path,"r")
    contenido = archivo_mascotas.read()

    #division del archivo en lineas
    division = contenido.split("\n")

    #recorrido de las lineas del archivo
    for linea in division:
        #division del archivo en tipo de instruccion(0) y contenido(1) 
        instruccion = linea.split(":")
        fecha = datetime.datetime.now()

        if instruccion[0] == "Crear_Pajaro":
            #eliminacion del "" en el nombre de la mascota
            nombre = instruccion[1].strip('"')
            
            #creacion del objeto
            p1 = Pajaro(nombre,1,True,0,0)

            #agregando el objeto creado al arreglo
            mascotas.append(p1)
            
            #generacion del reporte
            if mascotas_result != " ":
                mascotas_result = mascotas_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el pajaro " + nombre +"\n"
            else:
                mascotas_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el pajaro " + nombre + "\n"
        elif instruccion[0] == "Puede_Entregar_Mensaje":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                #validando el tipo de objeto que se encuentra en el arreglo
                if type(animal) == Pajaro:
                    if animal.nombre == nick:
                        if mascotas_result != " ":
                            mascotas_result = mascotas_result + animal.validarMensaje( int(ar1[1]) , int(ar1[2])) + "\n" 
                        else:
                            mascotas_result = animal.validarMensaje( int(ar1[1]) , int(ar1[2])) + "\n" 
        elif instruccion[0] == "Enviar_Mensaje":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                if type(animal) == Pajaro:
                    if animal.nombre == nick:
                        if mascotas_result != " ":
                            mascotas_result = mascotas_result + animal.enviarMensaje( int(ar1[1]) , int(ar1[2])) + "\n" 
                        else:
                            mascotas_result = animal.enviarMensaje( int(ar1[1]) , int(ar1[2])) + "\n" 
        elif instruccion[0] == "Crear_Gato":
            nombre = instruccion[1].strip('"')
            g1 = Gato(nombre,1,True,0,0)
            mascotas.append(g1)

            if mascotas_result != " ":
                mascotas_result = mascotas_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el gato " + nombre +"\n"
            else:
                mascotas_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el gato " + nombre + "\n"
        elif instruccion[0] == "Conviene_Comer_Raton":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                if type(animal) == Gato:
                    if animal.nombre == nick:
                        if mascotas_result != " ":
                            mascotas_result = mascotas_result + animal.validarComerRaton( int(ar1[1]) , int(ar1[2]) , int(ar1[3]) ) + "\n" 
                        else:
                            mascotas_result = animal.validarComerRaton( int(ar1[1]) , int(ar1[2]) , int(ar1[3]) ) + "\n" 
        elif instruccion[0] == "Enviar_Comer_Raton":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                if type(animal) == Gato:
                    if animal.nombre == nick:
                        if mascotas_result != " ":
                            mascotas_result = mascotas_result + animal.cazarRaton( int(ar1[1]) , int(ar1[2]) , int(ar1[3]) ) + "\n" 
                        else:
                            mascotas_result = animal.cazarRaton( int(ar1[1]) , int(ar1[2]) , int(ar1[3]) ) + "\n" 
        elif instruccion[0] == "Dar_de_Comer":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                if animal.nombre == nick:
                    if mascotas_result != " ":
                        mascotas_result = mascotas_result +  animal.comer(int(ar1[1])) + "\n" 
                    else:
                        mascotas_result = mascotas_result +  animal.comer(int(ar1[1])) + "\n" 
        elif instruccion[0] == "Resumen_Mascota":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in mascotas:
                if animal.nombre == nick:
                    if mascotas_result != " ":
                        mascotas_result = mascotas_result +  animal.resumen() + "\n" 
                    else:
                        mascotas_result = mascotas_result +  animal.resumen() + "\n" 
        elif linea == "Resumen_Global":
            fecha = datetime.datetime.now()
            if mascotas_result != " ":
                mascotas_result = mascotas_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "----------------- Resumen global -----------------\n"
            else:
                mascotas_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "----------------- Resumen global -----------------"

            for animal in mascotas:
                    if mascotas_result != " ":
                        mascotas_result = mascotas_result +  animal.resumen() + "\n" 
                    else:
                        mascotas_result = mascotas_result +  animal.F() + "\n" 

            mascotas_result = mascotas_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "--------------------------------------------------\n"

    #creacion e impresion del archivo.mascotas_result
    resultado = open("C:/Users/chepe/Desktop/archivo.mascotas_result","w")
    resultado.write(mascotas_result)
    resultado.close()
    os.system("C:/Users/chepe/Desktop/archivo.mascotas_result")
    menuPrincipal()

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
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                menuEntretenimiento()
            elif lectura == 2:
                menuEducacion()
            elif lectura == 0:
                print("Hasta la proxima c:")
                exit(0)
            else:
                print("\nIngrese una opcion valida\n")
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
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                mascotas()
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida \n")
        else:
            print("\nIngrese una opcion valida \n")

def traduccion(expresion):

    #arreglo para la traduccion y una pila para el almacenamiento de los operadores
    postfija = []
    pilaAux = []

    #recorrido de la expresion infija
    for it in range(0,len(expresion)):
        #si viene un numero en la expresion meterlo al arreglo de la traduccion
        if expresion[it].isdigit() == True or expresion[it].isalpha() == True:
            postfija.append(expresion[it])
        #si viene un operador meterlo a la pila de operadores
        else:
            #si la pila esta vacia insertar el operador
            if len(pilaAux) == 0:
                pilaAux.append(expresion[it])
            else:
                #si la pila no esta vacia, verificar cada caso para los operadores posibles
                if expresion[it] == "*":
                    #recorrer la pila de operadores
                    for ite in range(0,(len(pilaAux))):

                        #obtener el ultimo valor de la pila
                        aux1 = pilaAux[len(pilaAux)-1]
                        #si la pila esta vacia insertar el valor
                        if len(pilaAux) == 0:
                            pilaAux.append(expresion[it])
                        else:
                            """
                            si la prioridad del operador en la infija es mayor que la prioridad en la pila
                            se inserta en la pila, si la prioridad es menor se saca el valor del tope y se sigue 
                            preguntado hasta que la pila este vacia
                            
                            Operador|Prioridad infija|Prioridad en la pila
                                ^   |       4        |         3
                               *,/  |       2        |         2
                               +,-  |       1        |         1
                                (   |       5        |         0
                                )   |       NA       |         NA
                            """
                            if aux1 == "*":
                                """
                                como la prioridad es igual se saca de la pila de 
                                operadores y se agrega a la notacion postfija
                                """
                                postfija.append(pilaAux.pop())
                                #se verifica si la pila esta vacia para ingresar el operador que viene
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "/":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])                                  
                            #como la prioridad es mayor solo se agrega a la pila de operadores   
                            elif aux1 == "+":
                                pilaAux.append(expresion[it])
                            elif aux1 == "-":
                                pilaAux.append(expresion[it])
                            elif aux1 == "(":
                                pilaAux.append(expresion[it])
                elif expresion[it] == "/":
                    for ite in range(0,(len(pilaAux))):
                        aux1 = pilaAux[len(pilaAux)-1]
                        if len(pilaAux) == 0:
                            pilaAux.append(expresion[it])
                        else:
                            """
                            si la prioridad del operador en la infija es mayor que la prioridad en la pila
                            se inserta en la pila, si la prioridad es menor se saca el valor del tope y se sigue 
                            preguntado hasta que la pila este vacia
                            """
                            if aux1 == "*":
                                postfija.append(pilaAux.pop())
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "/":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])                                     
                            elif aux1 == "+":
                                pilaAux.append(expresion[it])
                            elif aux1 == "-":
                                pilaAux.append(expresion[it])
                            elif aux1 == "(":
                                pilaAux.append(expresion[it])
                elif expresion[it] == "+":
                    for ite in range(0,(len(pilaAux))):
                        aux1 = pilaAux[len(pilaAux)-1]
                        if len(pilaAux) == 0:
                            pilaAux.append(expresion[it])
                        else:
                            """
                            si la prioridad del operador en la infija es mayor que la prioridad en la pila
                            se inserta en la pila, si la prioridad es menor se saca el valor del tope y se sigue 
                            preguntado hasta que la pila este vacia
                            """
                            if aux1 == "*":
                                postfija.append(pilaAux.pop())
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "/":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])                                     
                            elif aux1 == "+":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "-":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "(":
                                pilaAux.append(expresion[it])
                elif expresion[it] == "-":
                    for ite in range(0,(len(pilaAux))):
                        aux1 = pilaAux[len(pilaAux)-1]
                        if len(pilaAux) == 0:
                            pilaAux.append(expresion[it])
                        else:
                            """
                            si la prioridad del operador en la infija es mayor que la prioridad en la pila
                            se inserta en la pila, si la prioridad es menor se saca el valor del tope y se sigue 
                            preguntado hasta que la pila este vacia
                            """
                            if aux1 == "*":
                                postfija.append(pilaAux.pop())
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "/":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])                                     
                            elif aux1 == "+":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "-":
                                postfija.append(pilaAux.pop())   
                                if len(pilaAux) == 0:
                                    pilaAux.append(expresion[it])
                            elif aux1 == "(":
                                pilaAux.append(expresion[it])
                elif expresion[it] == "(":
                    #al ser siempre la prioridad mayor solo se agrega
                    pilaAux.append(expresion[it])
                elif expresion[it] == ")":
                    #se recorre la pila hasta que encuentre el parentesis de apertura
                    while True:
                        valor = pilaAux.pop()
                        """
                        se verifica el valor que se extrajo de la pila si es el de 
                        apertura se termina de recorrer    
                        """
                        if valor == "(":
                            break
                        #luego de verificar el valor extraido se agrega al postfijo
                        postfija.append(valor)

    #se recorre la pila por si quedo algun operador dentro de el y se agrega al postfijo                    
    while len(pilaAux) != 0:
        postfija.append(pilaAux.pop())

    #regreso del arreglo en notacion postfija
    return postfija
    
def calculo(expresion,variables):
    #pila para el calculo de la expresion
    operacion = []
    print(expresion)
    #recorrido del arreglo de la expresion postfija
    for valor in expresion:
        #si viene un digito que lo agregue a la pila del calculo
        if valor.isdigit() == True:
            operacion.append(valor)
        elif valor.isalpha() == True:
            for var in variables:
                var = var.split(",")
                if valor == var[0]:
                    operacion.append(var[1])
        else:
            #si viene un operador que saque los dos numeros anteriores
            segundo = float(operacion.pop()) 
            primero = float(operacion.pop())
            """
            dependiendo del tipo de ooperador realizar la operacion 
            y regresar el resultado a la pila
            """
            if valor == "+":
                resultado = primero + segundo
                operacion.append(resultado)
            elif valor == "-":
                resultado = primero - segundo
                operacion.append(resultado)
            elif valor == "/":
                resultado = primero / segundo
                operacion.append(resultado)
            elif valor == "*":
                resultado = primero * segundo
                operacion.append(resultado)

    #regreso del valor de la operacion
    return round(float( operacion.pop() ) )

def calculadora():
    #guardado de la ruta del archivo 
    path = input("\nIngrese la ruta del archivo: ")

    #vaciado del arreglo de variables y el contenido del archivo de salida
    edu_result = " "
    variables = []

    #validando que la extension del archivo sea la correcta
    while True:
        nombre,extension = os.path.splitext(path)
        if extension == ".edu":
            break
        else:
            path = input("\nIngrese la ruta del archivo: ")

    #apertura y lectura del contenido del archivo de las instrucciones 
    archivo_edu = open(path,"r")
    contenido = archivo_edu.read()

    #division del archivo en lineas
    division = contenido.split("\n")

    #recorrido de las lineas del archivo
    for linea in division:
        #division del archivo en tipo de instruccion(0) y contenido(1) 
        instruccion = linea.split(":")
        fecha = datetime.datetime.now()

        if instruccion[0] == "Variable":
            #separacion de los parametros de la instruccion
            valor = instruccion[1].split(",")
            
            #traduccion y calculo del resultado de la operacion 
            infija = []
            print(valor[1].split(" "))
            for it in valor[1].split(" "):
                if it != "":
                    infija.append(it)

            resultado = calculo(traduccion(infija) ,variables)

            #cracion de una nueva cadena para alamacenaje y guardado en el arreglo
            cadena = valor[0]+","+str(resultado)
            variables.append(cadena)

        elif instruccion[0] == "Postfija":
            #traduccion de infijo a postfijo
            infija = []
            for it in instruccion[1].split(" "):
                if it != "":
                    infija.append(it)

            postfijo = traduccion(infija)
            print(postfijo)            

            #paso de un arreglo a un string
            cadena = " "
            for elemento in postfijo:
                cadena = cadena + elemento + " "

            if edu_result != " ":
                edu_result = edu_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Postfijo: " + cadena +"\n"
            else:
                edu_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Postfijo: " + cadena +"\n"
        
        elif instruccion[0] == "Incrementar":
            #creacion de una variable para el guardar el resultado
            resultado = 0

            #recorrido del arreglo de variables
            for valor in variables:
                #separacion de los elementos del arreglo por ","
                cadena = valor.split(",")

                #si se encuentra coincidencia con los nombres de las variables traducir y calcular el nuevo valor
                if cadena[0] == instruccion[1]:
                    resultado = calculo(traduccion([cadena[1],'+','1']),variables)

            #reemplazar el nuevo valor en el arreglo de variables
            for it in range(0,len(variables)):
                cadena = variables[it].split(",")
                if cadena[0] == instruccion[1]:
                    variables[it] = str(cadena[0]) + "," + str(resultado)
            
        elif instruccion[0] == "Mitad":
            #creacion de una variable para el guardar el resultado
            resultado = 0

            #recorrido del arreglo de variables
            for valor in variables:
                #separacion de los elementos del arreglo por ","
                cadena = valor.split(",")

                #si se encuentra coincidencia con los nombres de las variables traducir y calcular el nuevo valor
                if cadena[0] == instruccion[1]:
                    resultado = calculo(traduccion([cadena[1],'/','2']),variables)

            #reemplazar el nuevo valor en el arreglo de variables
            for it in range(0,len(variables)):
                cadena = variables[it].split(",")
                if cadena[0] == instruccion[1]:
                    variables[it] = str(cadena[0]) + "," + str(resultado)

        elif instruccion[0] == "Triple":
            #creacion de una variable para el guardar el resultado
            resultado = 0

            #recorrido del arreglo de variables
            for valor in variables:
                #separacion de los elementos del arreglo por ","
                cadena = valor.split(",")

                #si se encuentra coincidencia con los nombres de las variables traducir y calcular el nuevo valor
                if cadena[0] == instruccion[1]:
                    resultado = calculo(traduccion([cadena[1],'*','3']),variables)

            #reemplazar el nuevo valor en el arreglo de variables
            for it in range(0,len(variables)):
                cadena = variables[it].split(",")
                if cadena[0] == instruccion[1]:
                    variables[it] = str(cadena[0]) + "," + str(resultado)
        
        elif instruccion[0] == "Positivo":
            #creacion de una variable para el guardar el resultado
            resultado = 0

            #recorrido del arreglo de variables
            for valor in variables:
                #separacion de los elementos del arreglo por ","
                cadena = valor.split(",")

                #si se encuentra coincidencia con los nombres de las variables obtener el valor absoluto
                if cadena[0] == instruccion[1]:
                    resultado = abs(int(cadena[1]))

            #reemplazar el nuevo valor en el arreglo de variables
            for it in range(0,len(variables)):
                cadena = variables[it].split(",")
                if cadena[0] == instruccion[1]:
                    variables[it] = str(cadena[0]) + "," + str(resultado)

        elif instruccion[0] == "Negativo":
            #creacion de una variable para el guardar el resultado
            resultado = 0

            #recorrido del arreglo de variables
            for valor in variables:
                #separacion de los elementos del arreglo por ","
                cadena = valor.split(",")

                #si se encuentra coincidencia con los nombres de las variables obtener el valor negativo
                if cadena[0] == instruccion[1]:
                    resultado = abs(int(cadena[1])) * -1

            #reemplazar el nuevo valor en el arreglo de variables
            for it in range(0,len(variables)):
                cadena = variables[it].split(",")
                if cadena[0] == instruccion[1]:
                    variables[it] = str(cadena[0]) + "," + str(resultado)
        
        elif instruccion[0] == "Potencia":
            #separacion de ambas expresiones matematicas
            expresiones = instruccion[1].split(",")

            #traduccion y calculo de la primer expresion 

            infija = []
            for it in expresiones[0].split(" "):
                if it != "":
                    infija.append(it)

            base = calculo( traduccion( infija ),variables )

            #traduccion y calculo de la segunda expresion

            infija = []
            for it in expresiones[1].split(" "):
                if it != "":
                    infija.append(it)

            exponente = calculo( traduccion( infija ),variables )

            #arreglo para el calculo de la potencia
            operacion = []

            #conversion a notacion de potencia en formato postfijo
            for it in range(0,exponente):
                operacion.append(str(base)) 
            for it in range(1,exponente):
                operacion.append("*")

            if edu_result != " ":
                edu_result = edu_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Potencia: " +  str(calculo(operacion,variables)) +"\n"
            else:
                edu_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Potencia: " + str(calculo(operacion,variables)) +"\n"

        elif instruccion[0] == "Imprimir":
            #si los nombres de las variables coinciden imprimir su valor
            for valor in variables:
                cadena = valor.split(",")
                if cadena[0] == instruccion[1]:
                    if edu_result != " ":
                        edu_result = edu_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + " , " +  cadena[1]  +"\n"
                    else:
                        edu_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + cadena[0] + " , " +  cadena[1] +"\n"

        elif instruccion[0] == "Imprimir_Mensaje":
            #obtener el mensaje eliminarle las comillas e imprimirlo
            if edu_result != " ":
                edu_result = edu_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + instruccion[1].strip('"') + "\n"
            else:
                edu_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + instruccion[1].strip('"') +"\n"

    #creacion e impresion del archivo.edu_result
    resultado = open("C:/Users/chepe/Desktop/archivo.edu_result","w")
    resultado.write(edu_result)
    resultado.close()
    os.system("C:/Users/chepe/Desktop/archivo.edu_result")
    menuPrincipal()

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
    
    #validando que la extension del archivo sea la correcta
    while True:
        titulo,extension = os.path.splitext(path)
        if extension == ".almacen":
            break
        else:
            path = input("\nIngrese la ruta del archivo: ")

    #read() lectura del archivo en su totalidad
    contenido = archivo_almacen.read()
    division = contenido.split("\n")
    almacen_result = " "

    for linea in division:  
        instruccion = linea.split(":")
        fecha = datetime.datetime.now()

        if instruccion[0] == "Declarar":
            #agregar las palabras a un arreglo auxiliar
            ar1 = instruccion[1].split(",")
            completo = ar1[0]+","+ar1[1].strip('"') 
            palabras.append(completo)
           
            #separar el ID de la palabra y su contenido
            palabra = instruccion[1].split(",")
            
            #obtención del contenido
            asignacion = palabra[1].strip('"')

            """agregar longitud de la palabra eliminando la longitud que presentan las "" por la forma del 
            archivo de entrada"""
            lista.agregar(len(asignacion))
            
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
            
            #solo realiza esta instruccion si hay como minimo dos palabras en el almacen
            if len(palabras) >= 2:

                #extraccion de las ultimas dos palabras
                ultima = palabras.pop()
                penultima = palabras.pop()
                palabras.append(ultima)
                palabras.append(penultima)


                #obtencion del identificador y la palabra
                ultima = ultima.split(",")
                penultima = penultima.split(",")

                #concatenacion para la nueva palabra
                nueva_palabra = penultima[1]+ultima[1]


                #creacion y agregacion de la nueva palabra
                nuevo_valor = penultima[0]+","+nueva_palabra
                palabras.append(nuevo_valor)

                lista.agregar(len(nueva_palabra))
            
                #recorriendo la palabra para agregar los caracteres de la misma a la lista
                for iteracion in nueva_palabra:
                    if iteracion != '"':
                        lista.agregar(iteracion)
            
                #modificando la siguiente posicion vacia disponible
                lista.cabeza.objeto = lista.tamanyo

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
                contador = contador + (len(cadena[1]))    
        elif instruccion[0] == "Tamanio":
            #recorrido del arreglo auxiliar
            for i in palabras:
                #separacion del contenido del arreglo auxiliar
                identificador = i.split(",")
                #buscar conincidencia con el id ingresado y el del arreglo auxiliar
                if instruccion[1] == identificador[0]:
                    #generacion de reporte
                    if len(almacen_result) != 0:
                        almacen_result = almacen_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + identificador[0] + ", Tam: " + str(len(identificador[1])) + "\n"
                    else:
                        almacen_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + identificador[0] + ", Tam: " + str(len(identificador[1])) + "\n"
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
                contador = contador + (len(cadena[1]))   
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
            parte1 = instruccion[1].strip('"')
            parte2 = instruccion[2].strip('"')
            path_dot = parte1 +":"+ parte2
            path_dot = os.path.join(path_dot,"//grafo.dot") 
            path_dot = "C://Users//chepe//Desktop//grafo.dot"
            path_imagen = parte1 +":"+ parte2 + "//grafo.png"
            path_imagen = "C://Users//chepe//Desktop//grafo.png"

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
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                calculadora()
            elif lectura == 2:
                almacenCaracteres()
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida \n")
        else:
            print("\nIngrese una opcion valida \n")

menuPrincipal()