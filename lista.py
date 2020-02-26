from nodo import Nodo

class Lista():

    def __init__(self):
        self.tamanyo = 0
        self.cabeza = None

    def imprimir(self):
        aux = self.cabeza
        while aux != None:
            print(aux.resumen())
            aux = aux.siguiente

    def agregar(self, objeto):
        if self.cabeza == None:
            self.cabeza = Nodo(objeto,None)
            self.tamanyo = self.tamanyo + 1
        else:
            aux = self.cabeza
            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = Nodo(objeto,None)
            self.tamanyo = self.tamanyo + 1

    def limpiar(self):
        if self.cabeza != None:
            self.cabeza = self.cabeza.siguiente
            self.limpiar()
        else:
            self.tamanyo = 0
            self.cabeza = None

           

