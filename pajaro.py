from animal import Animal 
import datetime

class Pajaro(Animal):

    def resumen(self):
        fecha = datetime.datetime.now()
        
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + self.energia + ", X: " + self.posicion_x + ", Y: " + self.posicion_y + ", Pajaro , vivo." 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + self.energia + ", X: " + self.posicion_x + ", Y: " + self.posicion_y + ", Pajaro , muerto." 

    def comer(self,gramos):
        self.energia = self.energia + (gramos*4)

    def comidaNecesaria(self, energia):
        return energia/4

    def enviarMensaje(self,x,y):
        energia_necesaria = self.calcularDistancia(x,y) + 10
        fecha = datetime.datetime.now()

        if self.estado == True:
            if self.energia >= energia_necesaria: 

                #modificando posicion, energia y estado
                self.posicion_x = x
                self.posicion_y = y
                self.energia = self.energia - energia_necesaria
                self.verificarEstado()

                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya fui a dejar el mensaje a: (x:" + x + ",y:"+y+")."
            elif self.energia < energia_necesaria:
                comida_necesaria = self.comidaNecesaria( energia_necesaria - self.energia )
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + self.nombre + ", Estoy exhausto. Dame de comer " + comida_necesaria + "gramos para ir."
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre+", Ya me mori."       

    def validarMensaje(self,x,y):
        energia_necesaria = self.calcularDistancia(x,y) + 10
        fecha = datetime.datetime.now()
        if self.estado == True:
            if self.energia >= energia_necesaria: 
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Si puedo ir a dejar el mensaje."
            else:
                comida_necesaria = self.comidaNecesaria( energia_necesaria - self.energia )
                self.estado = False               
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + self.nombre + ", Estoy exhausto. Dame de comer " + comida_necesaria + "gramos para ir."
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre+", Ya me mori."       