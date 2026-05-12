from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Calcular_el_primedio_de_edad_de_los_ejemplares__UseCase:

    pass


class Calcular_el_numero_ejemplar_por_raza__UseCase:

    pass


class Calcular_el_ejemplear_por_nombre__UseCase:

    pass


class Desplazarse_hasta_el_ultimo_ejemplar_UseCase:

    pass


class Desplazarse_hasta_el_primer_ejemplar__UseCase:

    pass


class Regresar_hacia_el_anterior_ejemplar_UseCase:

    pass


class Avanzar_hasta_el_siguiente_ejemplar__UseCase:

    pass


class Visualizar_Hoja_de_vida_de_los_caninos__UseCase:

    pass


class Usuario__Actor:

    pass





class Caninos2:

    pass


class Empresa2:

    pass


class Caninos1:

    def __init__(self, nombre: str, raza: str, edad: int, peso: int, altura: double, observaciones: str, empresa25: "Empresa1" = None, empresa27: "Empresa1" = None, empresa29: "Empresa1" = None, empresa23: "Empresa1" = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.empresa25 = empresa25
        self.empresa27 = empresa27
        self.empresa29 = empresa29
        self.empresa23 = empresa23
        
        pass
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: int):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: double):
        self.__altura = altura

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def empresa29(self):
        return self.__empresa29
    @empresa29.setter
    def empresa29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos1__empresa29", None)
        self.__empresa29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos28"):
                opp_val = getattr(old_value, "caninos28", None)
                if opp_val == self:
                    setattr(old_value, "caninos28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos28"):
                opp_val = getattr(value, "caninos28", None)
                setattr(value, "caninos28", self)

    @property
    def empresa23(self):
        return self.__empresa23
    @empresa23.setter
    def empresa23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos1__empresa23", None)
        self.__empresa23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos22"):
                opp_val = getattr(old_value, "caninos22", None)
                if opp_val == self:
                    setattr(old_value, "caninos22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos22"):
                opp_val = getattr(value, "caninos22", None)
                setattr(value, "caninos22", self)

    @property
    def empresa25(self):
        return self.__empresa25
    @empresa25.setter
    def empresa25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos1__empresa25", None)
        self.__empresa25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos24"):
                opp_val = getattr(old_value, "caninos24", None)
                if opp_val == self:
                    setattr(old_value, "caninos24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos24"):
                opp_val = getattr(value, "caninos24", None)
                setattr(value, "caninos24", self)

    @property
    def empresa27(self):
        return self.__empresa27
    @empresa27.setter
    def empresa27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos1__empresa27", None)
        self.__empresa27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos26"):
                opp_val = getattr(old_value, "caninos26", None)
                if opp_val == self:
                    setattr(old_value, "caninos26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos26"):
                opp_val = getattr(value, "caninos26", None)
                setattr(value, "caninos26", self)



class Empresa1:

    pass


class double:

    pass


class int:

    pass


class Caninos:

    def __init__(self, nombre: str, raza: str, edad: int, peso: int, altura: double, observaciones: str, empresa39: "Empresa" = None, veterinaria17: "Empresa" = None, veterinaria19: "Empresa" = None, veterinaria21: "Empresa" = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.empresa39 = empresa39
        self.veterinaria17 = veterinaria17
        self.veterinaria19 = veterinaria19
        self.veterinaria21 = veterinaria21
        
        pass
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: int):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: double):
        self.__altura = altura

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def veterinaria19(self):
        return self.__veterinaria19
    @veterinaria19.setter
    def veterinaria19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__veterinaria19", None)
        self.__veterinaria19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caninos18"):
                opp_val = getattr(old_value, "Caninos18", None)
                if opp_val == self:
                    setattr(old_value, "Caninos18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caninos18"):
                opp_val = getattr(value, "Caninos18", None)
                setattr(value, "Caninos18", self)

    @property
    def veterinaria17(self):
        return self.__veterinaria17
    @veterinaria17.setter
    def veterinaria17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__veterinaria17", None)
        self.__veterinaria17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caninos16"):
                opp_val = getattr(old_value, "Caninos16", None)
                if opp_val == self:
                    setattr(old_value, "Caninos16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caninos16"):
                opp_val = getattr(value, "Caninos16", None)
                setattr(value, "Caninos16", self)

    @property
    def veterinaria21(self):
        return self.__veterinaria21
    @veterinaria21.setter
    def veterinaria21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__veterinaria21", None)
        self.__veterinaria21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caninos20"):
                opp_val = getattr(old_value, "Caninos20", None)
                if opp_val == self:
                    setattr(old_value, "Caninos20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caninos20"):
                opp_val = getattr(value, "Caninos20", None)
                setattr(value, "Caninos20", self)

    @property
    def empresa39(self):
        return self.__empresa39
    @empresa39.setter
    def empresa39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__empresa39", None)
        self.__empresa39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos38"):
                opp_val = getattr(old_value, "caninos38", None)
                if opp_val == self:
                    setattr(old_value, "caninos38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos38"):
                opp_val = getattr(value, "caninos38", None)
                setattr(value, "caninos38", self)



class Empresa:

    def __init__(self, getImagen: int, setImagen: str, nuevoCanino: str, agregarCaninos: str, cantidadRazaCanina: double, Caninos_BuscarCanino: str, ArrayList: Caninos, Empresa: str, Caninos_informacion: str, getCaninos: str, getCaninos1: int, getCaninos2: str, getCaninos3: str, getCaninos4: str, getCaninos5: str, caninos38: "Caninos" = None, Caninos16: "Caninos" = None, Caninos18: "Caninos" = None, Caninos20: "Caninos" = None):
        self.getImagen = getImagen
        self.setImagen = setImagen
        self.nuevoCanino = nuevoCanino
        self.agregarCaninos = agregarCaninos
        self.cantidadRazaCanina = cantidadRazaCanina
        self.Caninos_BuscarCanino = Caninos_BuscarCanino
        self.ArrayList = ArrayList
        self.Empresa = Empresa
        self.Caninos_informacion = Caninos_informacion
        self.getCaninos = getCaninos
        self.getCaninos1 = getCaninos1
        self.getCaninos2 = getCaninos2
        self.getCaninos3 = getCaninos3
        self.getCaninos4 = getCaninos4
        self.getCaninos5 = getCaninos5
        self.caninos38 = caninos38
        self.Caninos16 = Caninos16
        self.Caninos18 = Caninos18
        self.Caninos20 = Caninos20
        
        pass
    @property
    def getCaninos5(self):
        return self.__getCaninos5
    @getCaninos5.setter
    def getCaninos5(self, getCaninos5: str):
        self.__getCaninos5 = getCaninos5

    @property
    def getCaninos(self):
        return self.__getCaninos
    @getCaninos.setter
    def getCaninos(self, getCaninos: str):
        self.__getCaninos = getCaninos

    @property
    def ArrayList(self):
        return self.__ArrayList
    @ArrayList.setter
    def ArrayList(self, ArrayList: Caninos):
        self.__ArrayList = ArrayList

    @property
    def cantidadRazaCanina(self):
        return self.__cantidadRazaCanina
    @cantidadRazaCanina.setter
    def cantidadRazaCanina(self, cantidadRazaCanina: double):
        self.__cantidadRazaCanina = cantidadRazaCanina

    @property
    def getImagen(self):
        return self.__getImagen
    @getImagen.setter
    def getImagen(self, getImagen: int):
        self.__getImagen = getImagen

    @property
    def agregarCaninos(self):
        return self.__agregarCaninos
    @agregarCaninos.setter
    def agregarCaninos(self, agregarCaninos: str):
        self.__agregarCaninos = agregarCaninos

    @property
    def getCaninos1(self):
        return self.__getCaninos1
    @getCaninos1.setter
    def getCaninos1(self, getCaninos1: int):
        self.__getCaninos1 = getCaninos1

    @property
    def Empresa(self):
        return self.__Empresa
    @Empresa.setter
    def Empresa(self, Empresa: str):
        self.__Empresa = Empresa

    @property
    def getCaninos3(self):
        return self.__getCaninos3
    @getCaninos3.setter
    def getCaninos3(self, getCaninos3: str):
        self.__getCaninos3 = getCaninos3

    @property
    def nuevoCanino(self):
        return self.__nuevoCanino
    @nuevoCanino.setter
    def nuevoCanino(self, nuevoCanino: str):
        self.__nuevoCanino = nuevoCanino

    @property
    def getCaninos4(self):
        return self.__getCaninos4
    @getCaninos4.setter
    def getCaninos4(self, getCaninos4: str):
        self.__getCaninos4 = getCaninos4

    @property
    def getCaninos2(self):
        return self.__getCaninos2
    @getCaninos2.setter
    def getCaninos2(self, getCaninos2: str):
        self.__getCaninos2 = getCaninos2

    @property
    def Caninos_informacion(self):
        return self.__Caninos_informacion
    @Caninos_informacion.setter
    def Caninos_informacion(self, Caninos_informacion: str):
        self.__Caninos_informacion = Caninos_informacion

    @property
    def Caninos_BuscarCanino(self):
        return self.__Caninos_BuscarCanino
    @Caninos_BuscarCanino.setter
    def Caninos_BuscarCanino(self, Caninos_BuscarCanino: str):
        self.__Caninos_BuscarCanino = Caninos_BuscarCanino

    @property
    def setImagen(self):
        return self.__setImagen
    @setImagen.setter
    def setImagen(self, setImagen: str):
        self.__setImagen = setImagen

    @property
    def Caninos18(self):
        return self.__Caninos18
    @Caninos18.setter
    def Caninos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__Caninos18", None)
        self.__Caninos18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria19"):
                opp_val = getattr(old_value, "veterinaria19", None)
                if opp_val == self:
                    setattr(old_value, "veterinaria19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria19"):
                opp_val = getattr(value, "veterinaria19", None)
                setattr(value, "veterinaria19", self)

    @property
    def caninos38(self):
        return self.__caninos38
    @caninos38.setter
    def caninos38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__caninos38", None)
        self.__caninos38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "empresa39"):
                opp_val = getattr(old_value, "empresa39", None)
                if opp_val == self:
                    setattr(old_value, "empresa39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "empresa39"):
                opp_val = getattr(value, "empresa39", None)
                setattr(value, "empresa39", self)

    @property
    def Caninos16(self):
        return self.__Caninos16
    @Caninos16.setter
    def Caninos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__Caninos16", None)
        self.__Caninos16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria17"):
                opp_val = getattr(old_value, "veterinaria17", None)
                if opp_val == self:
                    setattr(old_value, "veterinaria17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria17"):
                opp_val = getattr(value, "veterinaria17", None)
                setattr(value, "veterinaria17", self)

    @property
    def Caninos20(self):
        return self.__Caninos20
    @Caninos20.setter
    def Caninos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__Caninos20", None)
        self.__Caninos20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria21"):
                opp_val = getattr(old_value, "veterinaria21", None)
                if opp_val == self:
                    setattr(old_value, "veterinaria21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria21"):
                opp_val = getattr(value, "veterinaria21", None)
                setattr(value, "veterinaria21", self)

