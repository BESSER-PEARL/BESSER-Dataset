from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Calcular_el_promedio_de_edad_UseCase:

    pass


class Calcular_el_numero_de_ejemplares_UseCase:

    pass


class Buscar_un_ejemplar_por_su_nombre_UseCase:

    pass


class Desplazarse_hasta_el_ultimo_UseCase:

    pass


class Desplazarse_hasta_el_primer_UseCase:

    pass


class Regresar_hacia_el_anterior_UseCase:

    pass


class Avanzar_hacia_el_siguiente__UseCase:

    pass


class Usuario__Actor:

    pass





class Datos:

    def __init__(self, Edad: int, peso: str, altura: str, observacion: str, nombre: str, raza: str, veterinario15: set["Veterinario"] = None):
        self.Edad = Edad
        self.peso = peso
        self.altura = altura
        self.observacion = observacion
        self.nombre = nombre
        self.raza = raza
        self.veterinario15 = veterinario15 if veterinario15 is not None else set()
        
        pass
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def observacion(self):
        return self.__observacion
    @observacion.setter
    def observacion(self, observacion: str):
        self.__observacion = observacion

    @property
    def Edad(self):
        return self.__Edad
    @Edad.setter
    def Edad(self, Edad: int):
        self.__Edad = Edad

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def veterinario15(self):
        return self.__veterinario15
    @veterinario15.setter
    def veterinario15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Datos__veterinario15", None)
        self.__veterinario15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Veterinario_Datos_014"):
                    opp_val = getattr(item, "Veterinario_Datos_014", None)
                    
                    if opp_val == self:
                        setattr(item, "Veterinario_Datos_014", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Veterinario_Datos_014"):
                    opp_val = getattr(item, "Veterinario_Datos_014", None)
                    
                    setattr(item, "Veterinario_Datos_014", self)
                    



class Veterinario:

    pass
