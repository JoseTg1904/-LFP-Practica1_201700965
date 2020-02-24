from nodo import Nodo

class Pila():

    def __init__(self):
        self.tamanyo = 0
        self.cabeza = None

    def agregar(self,objeto):
        if self.cabeza == None:
            self.cabeza = Nodo(objeto,None)
            self.tamanyo = self.tamanyo + 1
        else:
            aux = self.cabeza
            self.cabeza = Nodo(objeto,aux) 
            self.tamanyo = self.tamanyo + 1
    
    def imprimir(self):
        aux = self.cabeza
        while aux != None:
            print(aux.resumen())
            aux = aux.siguiente