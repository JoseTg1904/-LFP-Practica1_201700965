from animal import Animal 
import datetime

class Pajaro(Animal):

    def resumen(self):
        fecha = datetime.datetime.now()
        
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia) + ", X: " + str(self.posicion_x) + ", Y: " + str(self.posicion_y) + ", Pajaro , vivo." 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Energia: " + str(self.energia) + ", X: " + str(self.posicion_x) + ", Y: " + str(self.posicion_y) + ", Pajaro , muerto." 

    def comer(self,gramos):
        self.energia = self.energia + (gramos*4)
        fecha = datetime.datetime.now()
        print("si entro a esta instruccion")
        if self.estado == True: 
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Gracias. Ahora mi energia es: " + str(self.energia) 
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+ self.nombre + ", Muy tarde. Ya me mori" 

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
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre + ", Ya fui a dejar el mensaje a: (x:" + str(x) + ",y:"+str(y)+")."
            elif self.energia < energia_necesaria:
                comida_necesaria = self.comidaNecesaria( energia_necesaria - self.energia )
                self.energia = 0
                self.posicion_x = x
                self.posicion_y = y
                self.verificarEstado()
                texto = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + self.nombre + ", Estoy exhausto. Dame de comer " + str(comida_necesaria) + " gramos para ir. \n" + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre+", Ya me mori." 
                return texto
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
                return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + self.nombre + ", Estoy exhausto. Dame de comer " + str(comida_necesaria) + " gramos para ir."
        else:
            return "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] "+self.nombre+", Ya me mori."       