from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Desplazarse_hasta_el__ltimo_ejemplar__UseCase:

    pass


class Desplazarse_hasta_el_primer_ejemplar__UseCase:

    pass


class Regresar_hacia_el_anterior_ejemplar__UseCase:

    pass


class Avanzar_hacia_el_siguiente_ejemplar__UseCase:

    pass


class Calcular_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase:

    pass


class Calcular_n_mero_de_ejemplares_caninos_por_raza__UseCase:

    pass


class Buscar_ejemplar_por_su_nombre__UseCase:

    pass


class Usuario_Actor:

    pass





class Caninos:

    def __init__(self, nombre: str, raza: str, edad: str, peso: str, altura: str, observaciones: str, Empresa_Caninos_115: set["Empresa"] = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        self.Empresa_Caninos_115 = Empresa_Caninos_115 if Empresa_Caninos_115 is not None else set()
        
        pass
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
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: str):
        self.__edad = edad

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def Empresa_Caninos_115(self):
        return self.__Empresa_Caninos_115
    @Empresa_Caninos_115.setter
    def Empresa_Caninos_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__Empresa_Caninos_115", None)
        self.__Empresa_Caninos_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caninos14"):
                    opp_val = getattr(item, "caninos14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caninos14"):
                    opp_val = getattr(item, "caninos14", None)
                    
                    if opp_val is None:
                        setattr(item, "caninos14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Empresa:

    pass
