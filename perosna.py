class persona(object):
    def__init__(self,rut,nombre,fecha,genero):
        self.rut=rut
        self.normbre=nombre
        self.fecha=fecha
        self.genero)genero
    def obtner_edad(self):
        fecha=time.strftime(%d %m %y)
        pass
class Nota(object):
    def__init__(self,valor,ponderacion,ramo,carrera):
        self.valor=valor
        self.ponderacion=ponderacion
        self.ramo=ramo
        self.carrera=carrera
    def obtener_valor(self):
        return self.valor
    def obtener_ponderacion(self):
        return self.ponderacion
    def modificar(self,valor,ponderacion):
        self.valor=valor
        self.ponderacion=ponderacion
    
class Alumno(persona,Nota):
    def__init__(self,rut,nombre,fecha,genero,correo,carrera,promicion,notas)
    super(Alumno,self).__init__(rut,nombre,fecha,genero)
    self.correo=correo
    self.carrera=carrera
    self.promocion=promocion
    self.notas=notas
    def agregar_notas(self,nota):
        return
    def pga(self,notas):
        return
    def promedioramos(self,notas):
        return
