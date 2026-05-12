from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Calcular_promedio_edad_perros_UseCase:

    pass


class Calcular_cantidad_por_raza_UseCase:

    pass


class Buscar_perro_por_nombre_UseCase:

    pass


class Ir_al_ultimo_UseCase:

    pass


class Ir_al_primero_UseCase:

    pass


class Anterior_UseCase:

    pass


class Avanzar_UseCase:

    pass


class Interfaz_veterinaria_UseCase:

    pass


class Usuario__Actor:

    pass





class Caninos2:

    pass


class Empresa2:

    pass


class Caninos1:

    def __init__(self, nombre: str, raza: str, edad: int, peso: int, altura: double, observaciones: str, empresa25: "Empresa1" = None, empresa27: "Empresa1" = None, empresa29: "Empresa1" = None, empresa31: "Empresa1" = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.empresa25 = empresa25
        self.empresa27 = empresa27
        self.empresa29 = empresa29
        self.empresa31 = empresa31
        
        pass
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

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
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: double):
        self.__altura = altura

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

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
    def empresa31(self):
        return self.__empresa31
    @empresa31.setter
    def empresa31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos1__empresa31", None)
        self.__empresa31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caninos30"):
                opp_val = getattr(old_value, "caninos30", None)
                if opp_val == self:
                    setattr(old_value, "caninos30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caninos30"):
                opp_val = getattr(value, "caninos30", None)
                setattr(value, "caninos30", self)



class Empresa1:

    pass


class double:

    pass


class int:

    pass


class Caninos:

    def __init__(self, nombre: str, raza: str, edad: int, peso: double, altura: int, observaciones: str, attribute: str, veterinaria21: "Empresa" = None, veterinaria23: "Empresa" = None, veterinaria17: "Empresa" = None, veterinaria19: "Empresa" = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.attribute = attribute
        self.veterinaria21 = veterinaria21
        self.veterinaria23 = veterinaria23
        self.veterinaria17 = veterinaria17
        self.veterinaria19 = veterinaria19
        
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
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: int):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: double):
        self.__peso = peso

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

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
            if hasattr(old_value, "ejemplares_caninos18"):
                opp_val = getattr(old_value, "ejemplares_caninos18", None)
                if opp_val == self:
                    setattr(old_value, "ejemplares_caninos18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ejemplares_caninos18"):
                opp_val = getattr(value, "ejemplares_caninos18", None)
                setattr(value, "ejemplares_caninos18", self)

    @property
    def veterinaria23(self):
        return self.__veterinaria23
    @veterinaria23.setter
    def veterinaria23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__veterinaria23", None)
        self.__veterinaria23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ejemplares_caninos22"):
                opp_val = getattr(old_value, "ejemplares_caninos22", None)
                if opp_val == self:
                    setattr(old_value, "ejemplares_caninos22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ejemplares_caninos22"):
                opp_val = getattr(value, "ejemplares_caninos22", None)
                setattr(value, "ejemplares_caninos22", self)

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
            if hasattr(old_value, "ejemplares_caninos16"):
                opp_val = getattr(old_value, "ejemplares_caninos16", None)
                if opp_val == self:
                    setattr(old_value, "ejemplares_caninos16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ejemplares_caninos16"):
                opp_val = getattr(value, "ejemplares_caninos16", None)
                setattr(value, "ejemplares_caninos16", self)

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
            if hasattr(old_value, "ejemplares_caninos20"):
                opp_val = getattr(old_value, "ejemplares_caninos20", None)
                if opp_val == self:
                    setattr(old_value, "ejemplares_caninos20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ejemplares_caninos20"):
                opp_val = getattr(value, "ejemplares_caninos20", None)
                setattr(value, "ejemplares_caninos20", self)



class Empresa:

    def __init__(self, ArrayList: Caninos, Empresa: str, getCaninos: str, getCaninos1: str, getCaninos2: str, getCaninos3: str, Cantidad_razaCanina: str, Promedio_canino: str, buscarCaninos: str, ejemplares_caninos20: "Caninos" = None, ejemplares_caninos22: "Caninos" = None, ejemplares_caninos16: "Caninos" = None, ejemplares_caninos18: "Caninos" = None):
        self.ArrayList = ArrayList
        self.Empresa = Empresa
        self.getCaninos = getCaninos
        self.getCaninos1 = getCaninos1
        self.getCaninos2 = getCaninos2
        self.getCaninos3 = getCaninos3
        self.Cantidad_razaCanina = Cantidad_razaCanina
        self.Promedio_canino = Promedio_canino
        self.buscarCaninos = buscarCaninos
        self.ejemplares_caninos20 = ejemplares_caninos20
        self.ejemplares_caninos22 = ejemplares_caninos22
        self.ejemplares_caninos16 = ejemplares_caninos16
        self.ejemplares_caninos18 = ejemplares_caninos18
        
        pass
    @property
    def ArrayList(self):
        return self.__ArrayList
    @ArrayList.setter
    def ArrayList(self, ArrayList: Caninos):
        self.__ArrayList = ArrayList

    @property
    def buscarCaninos(self):
        return self.__buscarCaninos
    @buscarCaninos.setter
    def buscarCaninos(self, buscarCaninos: str):
        self.__buscarCaninos = buscarCaninos

    @property
    def getCaninos1(self):
        return self.__getCaninos1
    @getCaninos1.setter
    def getCaninos1(self, getCaninos1: str):
        self.__getCaninos1 = getCaninos1

    @property
    def getCaninos2(self):
        return self.__getCaninos2
    @getCaninos2.setter
    def getCaninos2(self, getCaninos2: str):
        self.__getCaninos2 = getCaninos2

    @property
    def getCaninos(self):
        return self.__getCaninos
    @getCaninos.setter
    def getCaninos(self, getCaninos: str):
        self.__getCaninos = getCaninos

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
    def Cantidad_razaCanina(self):
        return self.__Cantidad_razaCanina
    @Cantidad_razaCanina.setter
    def Cantidad_razaCanina(self, Cantidad_razaCanina: str):
        self.__Cantidad_razaCanina = Cantidad_razaCanina

    @property
    def Promedio_canino(self):
        return self.__Promedio_canino
    @Promedio_canino.setter
    def Promedio_canino(self, Promedio_canino: str):
        self.__Promedio_canino = Promedio_canino

    @property
    def ejemplares_caninos22(self):
        return self.__ejemplares_caninos22
    @ejemplares_caninos22.setter
    def ejemplares_caninos22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__ejemplares_caninos22", None)
        self.__ejemplares_caninos22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "veterinaria23"):
                opp_val = getattr(old_value, "veterinaria23", None)
                if opp_val == self:
                    setattr(old_value, "veterinaria23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "veterinaria23"):
                opp_val = getattr(value, "veterinaria23", None)
                setattr(value, "veterinaria23", self)

    @property
    def ejemplares_caninos18(self):
        return self.__ejemplares_caninos18
    @ejemplares_caninos18.setter
    def ejemplares_caninos18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__ejemplares_caninos18", None)
        self.__ejemplares_caninos18 = value
        
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
    def ejemplares_caninos20(self):
        return self.__ejemplares_caninos20
    @ejemplares_caninos20.setter
    def ejemplares_caninos20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__ejemplares_caninos20", None)
        self.__ejemplares_caninos20 = value
        
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

    @property
    def ejemplares_caninos16(self):
        return self.__ejemplares_caninos16
    @ejemplares_caninos16.setter
    def ejemplares_caninos16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Empresa__ejemplares_caninos16", None)
        self.__ejemplares_caninos16 = value
        
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

