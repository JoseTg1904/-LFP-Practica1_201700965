class Animal():

    def __init__(self,nombre,energia,estado,posicion_x,posicion_y):
        self.nombre = nombre
        self.energia = energia
        self.estado = estado
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

    def calcularDistancia(self,x,y):
         Px = abs(self.posicion_x - x) 
         Py = abs(self.posicion_y - y)
         return int((Px**2 + Py**2)**0.5)

    def verificarEstado(self):
        if self.energia == 0:
            self.estado = False
        else:
            self.estado = True

    def comer(self):
        pass