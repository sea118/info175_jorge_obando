# -*- coding: utf-8 -*-

class Auto(object):
  
    def __init__(self, kilometraje=0, bencina=0, rendimiento=10 ,encendido=False):
        self.kilometraje = kilometraje
        self.bencina = bencina
        self.rendimiento = rendimiento
        self.encendido = encendido
        
    def encender(self):
        if self.encendido:
           print "Motor ya está encendido."
        else:
            self.encendido = not self.encendido

    def apagar(self):
        if not self.encendido:
           print "Motor ya está apagado."
        else:
            self.encendido = not self.encendido

    def mover(self,kilometros):
        if not self.encendido:
            print "Motor apagado."
        elif self.bencina*self.rendimiento <= kilometros:
            print "Bencina insuficiente"
        else:
            print "sumaremos kilometraje y quitaremos bencina  "
            self.kilometraje += kilometros
            print self.kilometraje
            self.bencina -=  kilometros/self.rendimiento
            print self.bencina
            
    def obtener_kilometraje(self):
        print self.kilometraje

    def obtener_bencina(self):
        print self.bencina

    def cargar_bencina(self, bencina):
        if self.encendido:
            print "Primero debe apagar el motor."
        else:
            self.bencina += bencina
            
if __name__=="__main__":
    print ("***Comenzemos***")
    auto_a = Auto()
    auto_a.encender()
    auto_a.cargar_bencina(35)
    auto_a.mover(45)
    auto_a.apagar()
    auto_a.cargar_bencina(35)
    auto_a.obtener_bencina()
    auto_a.encender()
    auto_a.mover(5)
    auto_a.obtener_kilometraje()
    auto_a.mover(100)
    auto_a.apagar()



######
    
class Acoplado(object):
        def __init__(self,peso,ruedas,carga):
                self.peso = peso 
                self.ruedas = ruedas 
                self.carga = carga 

class Camion(Auto):
        def __init__(self,kilometraje,bencina,rendimiento,encendido,peso,ruedas,acoplados):
                super(Camion,self).__init__(kilometraje,bencina,rendimiento,encendido)
                self.peso = peso
                self.ruedas = ruedas
                self.acoplados = acoplados
	

        def agregar_acoplado(self,acoplado):
                self.acoplados.append(acoplado)
                print "Acoplado exitoso "

        def quitar_acoplado(self,acoplado):
                self.acoplados.remove(acoplado)
                print "El acoplado ha sido eliminado"

        def obtener_acoplados(self):
                for i in range(len(self.acoplados)):
                        print "Acoplado: "+str(i)
                        print "Peso: "+ str(self.acoplados[i].peso)
                        print "Ruedas: "+str(self.acoplados[i].ruedas)
                        print self.acoplados[i].carga
                        print

        def obtener_ruedas(self):
                return self.ruedas

        def obtener_peso(self):
                return self.peso



acoplado1 = Acoplado(7,4,"Petroleo")
acoplado2 = Acoplado(4,6,"Acido")
acoplado3 = Acoplado(2,3,"Leche")
acoplado4 = Acoplado(1,6, "Porche")

 

camion1 = Camion(1,30,70,False,40,2,[acoplado3,acoplado4]) 

print camion1.obtener_acoplados()

camion1.agregar_acoplado(acoplado1)
camion1.agregar_acoplado(acoplado2)

print camion1.obtener_acoplados()

print camion1.quitar_acoplado(acoplado3)

print camion1.quitar_acoplado(acoplado4)

print camion1.obtener_acoplados()

print "Peso del camion: "+str(camion1.obtener_peso())
print "Ruedas del camion: "+str(camion1.obtener_ruedas())
