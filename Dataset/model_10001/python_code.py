from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Genero(Enum):
    Lirico = "Lirico"
    Epico = "Epico"
    Narrativo = "Narrativo"
    Dramatico = "Dramatico"
    Didactico = "Didactico"
    Terror = "Terror"
class Estado(Enum):
    Bueno = "Bueno"
    Malo = "Malo"


############################################
# Definition of Classes
############################################

class Biblioteca_Multa:

    def __init__(self, fecha: date, monto: int, diasExcedidos: int, fechaDePago: date, Biblioteca_Multa: "Biblioteca_Socio" = None, Biblioteca_Multa21: "Biblioteca_Prestamo" = None):
        self.fecha = fecha
        self.monto = monto
        self.diasExcedidos = diasExcedidos
        self.fechaDePago = fechaDePago
        self.Biblioteca_Multa = Biblioteca_Multa
        self.Biblioteca_Multa21 = Biblioteca_Multa21
        
        pass
    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto: int):
        self.__monto = monto


    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha: date):
        self.__fecha = fecha


    @property
    def diasExcedidos(self):
        return self.__diasExcedidos

    @diasExcedidos.setter
    def diasExcedidos(self, diasExcedidos: int):
        self.__diasExcedidos = diasExcedidos


    @property
    def fechaDePago(self):
        return self.__fechaDePago

    @fechaDePago.setter
    def fechaDePago(self, fechaDePago: date):
        self.__fechaDePago = fechaDePago


    @property
    def Biblioteca_Multa(self):
        return self.__Biblioteca_Multa

    @Biblioteca_Multa.setter
    def Biblioteca_Multa(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Multa__Biblioteca_Multa", None)
        self.__Biblioteca_Multa = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Socio16"):
                opp_val = getattr(old_value, "Biblioteca_Socio16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Socio16"):
                opp_val = getattr(value, "Biblioteca_Socio16", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Socio16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Biblioteca_Multa21(self):
        return self.__Biblioteca_Multa21

    @Biblioteca_Multa21.setter
    def Biblioteca_Multa21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Multa__Biblioteca_Multa21", None)
        self.__Biblioteca_Multa21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Prestamo22"):
                opp_val = getattr(old_value, "Biblioteca_Prestamo22", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Prestamo22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Prestamo22"):
                opp_val = getattr(value, "Biblioteca_Prestamo22", None)
                setattr(value, "Biblioteca_Prestamo22", self)

class Biblioteca_Ejemplar:

    def __init__(self, numeroDeEjemplar: int, estado: str, Biblioteca_Ejemplar: "Biblioteca_Prestamo" = None):
        self.numeroDeEjemplar = numeroDeEjemplar
        self.estado = estado
        self.Biblioteca_Ejemplar = Biblioteca_Ejemplar
        
        pass
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado


    @property
    def numeroDeEjemplar(self):
        return self.__numeroDeEjemplar

    @numeroDeEjemplar.setter
    def numeroDeEjemplar(self, numeroDeEjemplar: int):
        self.__numeroDeEjemplar = numeroDeEjemplar


    @property
    def Biblioteca_Ejemplar(self):
        return self.__Biblioteca_Ejemplar

    @Biblioteca_Ejemplar.setter
    def Biblioteca_Ejemplar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Ejemplar__Biblioteca_Ejemplar", None)
        self.__Biblioteca_Ejemplar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Prestamo"):
                opp_val = getattr(old_value, "Biblioteca_Prestamo", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Prestamo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Prestamo"):
                opp_val = getattr(value, "Biblioteca_Prestamo", None)
                setattr(value, "Biblioteca_Prestamo", self)

class Biblioteca_Prestamo:

    def __init__(self, fechaDeInicio: date, fechaDeFin: date, fechaDeDevolucion: date, Biblioteca_Prestamo: "Biblioteca_Ejemplar" = None, Biblioteca_Prestamo10: "Biblioteca_Socio" = None, Biblioteca_Prestamo19: "Biblioteca_Socio" = None, Biblioteca_Prestamo22: "Biblioteca_Multa" = None):
        self.fechaDeInicio = fechaDeInicio
        self.fechaDeFin = fechaDeFin
        self.fechaDeDevolucion = fechaDeDevolucion
        self.Biblioteca_Prestamo = Biblioteca_Prestamo
        self.Biblioteca_Prestamo10 = Biblioteca_Prestamo10
        self.Biblioteca_Prestamo19 = Biblioteca_Prestamo19
        self.Biblioteca_Prestamo22 = Biblioteca_Prestamo22
        
        pass
    @property
    def fechaDeFin(self):
        return self.__fechaDeFin

    @fechaDeFin.setter
    def fechaDeFin(self, fechaDeFin: date):
        self.__fechaDeFin = fechaDeFin


    @property
    def fechaDeInicio(self):
        return self.__fechaDeInicio

    @fechaDeInicio.setter
    def fechaDeInicio(self, fechaDeInicio: date):
        self.__fechaDeInicio = fechaDeInicio


    @property
    def fechaDeDevolucion(self):
        return self.__fechaDeDevolucion

    @fechaDeDevolucion.setter
    def fechaDeDevolucion(self, fechaDeDevolucion: date):
        self.__fechaDeDevolucion = fechaDeDevolucion


    @property
    def Biblioteca_Prestamo19(self):
        return self.__Biblioteca_Prestamo19

    @Biblioteca_Prestamo19.setter
    def Biblioteca_Prestamo19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Prestamo__Biblioteca_Prestamo19", None)
        self.__Biblioteca_Prestamo19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Socio18"):
                opp_val = getattr(old_value, "Biblioteca_Socio18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Socio18"):
                opp_val = getattr(value, "Biblioteca_Socio18", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Socio18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Biblioteca_Prestamo(self):
        return self.__Biblioteca_Prestamo

    @Biblioteca_Prestamo.setter
    def Biblioteca_Prestamo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Prestamo__Biblioteca_Prestamo", None)
        self.__Biblioteca_Prestamo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Ejemplar"):
                opp_val = getattr(old_value, "Biblioteca_Ejemplar", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Ejemplar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Ejemplar"):
                opp_val = getattr(value, "Biblioteca_Ejemplar", None)
                setattr(value, "Biblioteca_Ejemplar", self)

    @property
    def Biblioteca_Prestamo10(self):
        return self.__Biblioteca_Prestamo10

    @Biblioteca_Prestamo10.setter
    def Biblioteca_Prestamo10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Prestamo__Biblioteca_Prestamo10", None)
        self.__Biblioteca_Prestamo10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Socio11"):
                opp_val = getattr(old_value, "Biblioteca_Socio11", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Socio11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Socio11"):
                opp_val = getattr(value, "Biblioteca_Socio11", None)
                setattr(value, "Biblioteca_Socio11", self)

    @property
    def Biblioteca_Prestamo22(self):
        return self.__Biblioteca_Prestamo22

    @Biblioteca_Prestamo22.setter
    def Biblioteca_Prestamo22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Prestamo__Biblioteca_Prestamo22", None)
        self.__Biblioteca_Prestamo22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Multa21"):
                opp_val = getattr(old_value, "Biblioteca_Multa21", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Multa21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Multa21"):
                opp_val = getattr(value, "Biblioteca_Multa21", None)
                setattr(value, "Biblioteca_Multa21", self)

class Biblioteca_Socio:

    def __init__(self, numeroDeSocio: int, nombreCompleto: str, telefono: str, direccion: str, edad: int, fechaDeNacimiento: date, Biblioteca_Socio: "Biblioteca_Biblioteca" = None, Biblioteca_Socio11: "Biblioteca_Prestamo" = None, Biblioteca_Socio16: set["Biblioteca_Multa"] = None, Biblioteca_Socio18: set["Biblioteca_Prestamo"] = None):
        self.numeroDeSocio = numeroDeSocio
        self.nombreCompleto = nombreCompleto
        self.telefono = telefono
        self.direccion = direccion
        self.edad = edad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.Biblioteca_Socio = Biblioteca_Socio
        self.Biblioteca_Socio11 = Biblioteca_Socio11
        self.Biblioteca_Socio16 = Biblioteca_Socio16 if Biblioteca_Socio16 is not None else set()
        self.Biblioteca_Socio18 = Biblioteca_Socio18 if Biblioteca_Socio18 is not None else set()
        
        pass
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad


    @property
    def nombreCompleto(self):
        return self.__nombreCompleto

    @nombreCompleto.setter
    def nombreCompleto(self, nombreCompleto: str):
        self.__nombreCompleto = nombreCompleto


    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono: str):
        self.__telefono = telefono


    @property
    def numeroDeSocio(self):
        return self.__numeroDeSocio

    @numeroDeSocio.setter
    def numeroDeSocio(self, numeroDeSocio: int):
        self.__numeroDeSocio = numeroDeSocio


    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion


    @property
    def fechaDeNacimiento(self):
        return self.__fechaDeNacimiento

    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, fechaDeNacimiento: date):
        self.__fechaDeNacimiento = fechaDeNacimiento


    @property
    def Biblioteca_Socio18(self):
        return self.__Biblioteca_Socio18

    @Biblioteca_Socio18.setter
    def Biblioteca_Socio18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Socio__Biblioteca_Socio18", None)
        self.__Biblioteca_Socio18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Prestamo19"):
                    opp_val = getattr(item, "Biblioteca_Prestamo19", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Prestamo19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Prestamo19"):
                    opp_val = getattr(item, "Biblioteca_Prestamo19", None)
                    
                    setattr(item, "Biblioteca_Prestamo19", self)
                    

    @property
    def Biblioteca_Socio16(self):
        return self.__Biblioteca_Socio16

    @Biblioteca_Socio16.setter
    def Biblioteca_Socio16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Socio__Biblioteca_Socio16", None)
        self.__Biblioteca_Socio16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Multa"):
                    opp_val = getattr(item, "Biblioteca_Multa", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Multa", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Multa"):
                    opp_val = getattr(item, "Biblioteca_Multa", None)
                    
                    setattr(item, "Biblioteca_Multa", self)
                    

    @property
    def Biblioteca_Socio11(self):
        return self.__Biblioteca_Socio11

    @Biblioteca_Socio11.setter
    def Biblioteca_Socio11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Socio__Biblioteca_Socio11", None)
        self.__Biblioteca_Socio11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Prestamo10"):
                opp_val = getattr(old_value, "Biblioteca_Prestamo10", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Prestamo10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Prestamo10"):
                opp_val = getattr(value, "Biblioteca_Prestamo10", None)
                setattr(value, "Biblioteca_Prestamo10", self)

    @property
    def Biblioteca_Socio(self):
        return self.__Biblioteca_Socio

    @Biblioteca_Socio.setter
    def Biblioteca_Socio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Socio__Biblioteca_Socio", None)
        self.__Biblioteca_Socio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Biblioteca4"):
                opp_val = getattr(old_value, "Biblioteca_Biblioteca4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Biblioteca4"):
                opp_val = getattr(value, "Biblioteca_Biblioteca4", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Biblioteca4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def uniqueID(self):
        # TODO: Implement uniqueID method
        pass

    def generarMulta(self, Biblioteca_prestamo) :
        # TODO: Implement generarMulta method
        pass

    def solicitarEjemplar(self, Biblioteca_codigo) :
        # TODO: Implement solicitarEjemplar method
        pass

    def existeSocio(self, Biblioteca_nombreDeSocio) :
        # TODO: Implement existeSocio method
        pass

    def devolverEjemplar(self, Biblioteca_codigo, Biblioteca_fechaActual) :
        # TODO: Implement devolverEjemplar method
        pass

class Biblioteca_Autor:

    def __init__(self, nombreCompleto: str, nacionalidad: str, fechaDeNacimiento: date, Biblioteca_Autor: "Biblioteca_Biblioteca" = None, Biblioteca_Autor7: "Biblioteca_Libro" = None, Biblioteca_Autor13: set["Biblioteca_Libro"] = None):
        self.nombreCompleto = nombreCompleto
        self.nacionalidad = nacionalidad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.Biblioteca_Autor = Biblioteca_Autor
        self.Biblioteca_Autor7 = Biblioteca_Autor7
        self.Biblioteca_Autor13 = Biblioteca_Autor13 if Biblioteca_Autor13 is not None else set()
        
        pass
    @property
    def nombreCompleto(self):
        return self.__nombreCompleto

    @nombreCompleto.setter
    def nombreCompleto(self, nombreCompleto: str):
        self.__nombreCompleto = nombreCompleto


    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad: str):
        self.__nacionalidad = nacionalidad


    @property
    def fechaDeNacimiento(self):
        return self.__fechaDeNacimiento

    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, fechaDeNacimiento: date):
        self.__fechaDeNacimiento = fechaDeNacimiento


    @property
    def Biblioteca_Autor(self):
        return self.__Biblioteca_Autor

    @Biblioteca_Autor.setter
    def Biblioteca_Autor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Autor__Biblioteca_Autor", None)
        self.__Biblioteca_Autor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Biblioteca2"):
                opp_val = getattr(old_value, "Biblioteca_Biblioteca2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Biblioteca2"):
                opp_val = getattr(value, "Biblioteca_Biblioteca2", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Biblioteca2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Biblioteca_Autor13(self):
        return self.__Biblioteca_Autor13

    @Biblioteca_Autor13.setter
    def Biblioteca_Autor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Autor__Biblioteca_Autor13", None)
        self.__Biblioteca_Autor13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Libro14"):
                    opp_val = getattr(item, "Biblioteca_Libro14", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Libro14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Libro14"):
                    opp_val = getattr(item, "Biblioteca_Libro14", None)
                    
                    setattr(item, "Biblioteca_Libro14", self)
                    

    @property
    def Biblioteca_Autor7(self):
        return self.__Biblioteca_Autor7

    @Biblioteca_Autor7.setter
    def Biblioteca_Autor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Autor__Biblioteca_Autor7", None)
        self.__Biblioteca_Autor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Libro6"):
                opp_val = getattr(old_value, "Biblioteca_Libro6", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Libro6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Libro6"):
                opp_val = getattr(value, "Biblioteca_Libro6", None)
                setattr(value, "Biblioteca_Libro6", self)

class Biblioteca_Libro:

    def __init__(self, ISBN: str, titulo: str, editorial: str, anioDeEdicion: int, genero: str, activo: bool, Biblioteca_Libro: "Biblioteca_Biblioteca" = None, Biblioteca_Libro6: "Biblioteca_Autor" = None, Biblioteca_Libro14: "Biblioteca_Autor" = None):
        self.ISBN = ISBN
        self.titulo = titulo
        self.editorial = editorial
        self.anioDeEdicion = anioDeEdicion
        self.genero = genero
        self.activo = activo
        self.Biblioteca_Libro = Biblioteca_Libro
        self.Biblioteca_Libro6 = Biblioteca_Libro6
        self.Biblioteca_Libro14 = Biblioteca_Libro14
        
        pass
    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN: str):
        self.__ISBN = ISBN


    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, activo: bool):
        self.__activo = activo


    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo


    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        self.__genero = genero


    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial: str):
        self.__editorial = editorial


    @property
    def anioDeEdicion(self):
        return self.__anioDeEdicion

    @anioDeEdicion.setter
    def anioDeEdicion(self, anioDeEdicion: int):
        self.__anioDeEdicion = anioDeEdicion


    @property
    def Biblioteca_Libro6(self):
        return self.__Biblioteca_Libro6

    @Biblioteca_Libro6.setter
    def Biblioteca_Libro6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Libro__Biblioteca_Libro6", None)
        self.__Biblioteca_Libro6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Autor7"):
                opp_val = getattr(old_value, "Biblioteca_Autor7", None)
                if opp_val == self:
                    setattr(old_value, "Biblioteca_Autor7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Autor7"):
                opp_val = getattr(value, "Biblioteca_Autor7", None)
                setattr(value, "Biblioteca_Autor7", self)

    @property
    def Biblioteca_Libro14(self):
        return self.__Biblioteca_Libro14

    @Biblioteca_Libro14.setter
    def Biblioteca_Libro14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Libro__Biblioteca_Libro14", None)
        self.__Biblioteca_Libro14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Autor13"):
                opp_val = getattr(old_value, "Biblioteca_Autor13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Autor13"):
                opp_val = getattr(value, "Biblioteca_Autor13", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Autor13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Biblioteca_Libro(self):
        return self.__Biblioteca_Libro

    @Biblioteca_Libro.setter
    def Biblioteca_Libro(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Libro__Biblioteca_Libro", None)
        self.__Biblioteca_Libro = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Biblioteca_Biblioteca"):
                opp_val = getattr(old_value, "Biblioteca_Biblioteca", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Biblioteca_Biblioteca"):
                opp_val = getattr(value, "Biblioteca_Biblioteca", None)
                if opp_val is None:
                    setattr(value, "Biblioteca_Biblioteca", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Biblioteca_Biblioteca:

    def __init__(self, direccion: str, Biblioteca_Biblioteca: set["Biblioteca_Libro"] = None, Biblioteca_Biblioteca2: set["Biblioteca_Autor"] = None, Biblioteca_Biblioteca4: set["Biblioteca_Socio"] = None):
        self.direccion = direccion
        self.Biblioteca_Biblioteca = Biblioteca_Biblioteca if Biblioteca_Biblioteca is not None else set()
        self.Biblioteca_Biblioteca2 = Biblioteca_Biblioteca2 if Biblioteca_Biblioteca2 is not None else set()
        self.Biblioteca_Biblioteca4 = Biblioteca_Biblioteca4 if Biblioteca_Biblioteca4 is not None else set()
        
        pass
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion: str):
        self.__direccion = direccion


    @property
    def Biblioteca_Biblioteca(self):
        return self.__Biblioteca_Biblioteca

    @Biblioteca_Biblioteca.setter
    def Biblioteca_Biblioteca(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Biblioteca__Biblioteca_Biblioteca", None)
        self.__Biblioteca_Biblioteca = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Libro"):
                    opp_val = getattr(item, "Biblioteca_Libro", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Libro", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Libro"):
                    opp_val = getattr(item, "Biblioteca_Libro", None)
                    
                    setattr(item, "Biblioteca_Libro", self)
                    

    @property
    def Biblioteca_Biblioteca4(self):
        return self.__Biblioteca_Biblioteca4

    @Biblioteca_Biblioteca4.setter
    def Biblioteca_Biblioteca4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Biblioteca__Biblioteca_Biblioteca4", None)
        self.__Biblioteca_Biblioteca4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Socio"):
                    opp_val = getattr(item, "Biblioteca_Socio", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Socio", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Socio"):
                    opp_val = getattr(item, "Biblioteca_Socio", None)
                    
                    setattr(item, "Biblioteca_Socio", self)
                    

    @property
    def Biblioteca_Biblioteca2(self):
        return self.__Biblioteca_Biblioteca2

    @Biblioteca_Biblioteca2.setter
    def Biblioteca_Biblioteca2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biblioteca_Biblioteca__Biblioteca_Biblioteca2", None)
        self.__Biblioteca_Biblioteca2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Biblioteca_Autor"):
                    opp_val = getattr(item, "Biblioteca_Autor", None)
                    
                    if opp_val == self:
                        setattr(item, "Biblioteca_Autor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Biblioteca_Autor"):
                    opp_val = getattr(item, "Biblioteca_Autor", None)
                    
                    setattr(item, "Biblioteca_Autor", self)
                    
