class Nodo():

    def __init__(self,objeto,siguiente):
        self.objeto = objeto
        self.siguiente = siguiente

    def resumen(self):
        return self.objeto