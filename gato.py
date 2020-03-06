from animal import Animal
import datetime


class Gato(Animal):

    def resumen(self):
        fecha = datetime.datetime.now()
        
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia) + ", X: " + str(self.posicion_x) + ", Y: " + str(self.posicion_y) + ", Gato , vivo." 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia) + ", X: " + str(self.posicion_x) + ", Y: " + str(self.posicion_y) + ", Gato , muerto." 

    def comer(self,gramos):
        self.energia = self.energia + (12 + gramos)
        fecha = datetime.datetime.now()
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Gracias. Ahora mi energia es: " + str(self.energia) 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Muy tarde. Ya me mori" 
    
    def validarComerRaton(self,x,y,gramos):
        energia_consumida = int(self.calcularDistancia(x,y)/2)
        fecha = datetime.datetime.now()
        if self.estado == True:
            if self.energia >= energia_consumida:
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Si me conviene comerme al raton."
            else:
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Esta muy lejos. No me conviene."
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya me mori."

    def energiaNecesaria(self,distancia):
        aux = distancia - 12
        if aux >= 12:
            return aux
        else:
            return 13

    def cazarRaton(self,x,y,gramos):
        energia_consumida = int(self.calcularDistancia(x,y)/2)
        fecha = datetime.datetime.now()
       
        if self.estado == True:
            if self.energia >= energia_consumida:
                #modificando posicion, energia y estado
                self.posicion_x = x
                self.posicion_y = y
                self.energia = self.energia - energia_consumida + 12 + gramos
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya me comi al raton, ahora mi energia es: " + str(self.energia) + " Joules."   
            else:
                gramos_necesarios = self.energiaNecesaria(energia_consumida)
                self.energia = 0
                self.verificarEstado()
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Estoy exhausto. Dame de comer " + str(gramos_necesarios) + " gramos, para ir. \n" + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya me mori."
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya me mori."