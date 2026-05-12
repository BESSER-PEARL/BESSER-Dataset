from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Desplazarse_hasta_el__ltimo_ejemplar_UseCase:

    pass


class Desplazarse_hasta_el_primer_ejemplar_UseCase:

    pass


class _Regresar_hacia_el_anterior_ejemplar_UseCase:

    pass


class Avanzar_hacia_el_siguiente_ejemplar_UseCase:

    pass


class _Calcular_el_promedio_de_edad_de_todos_los_ejemplares_caninos__UseCase:

    pass


class Calcular_el_n_mero_de_ejemplares_caninos_por_raza_UseCase:

    pass


class _Buscar_un_ejemplar_por_su_nombre___UseCase:

    pass


class Usuario_Actor:

    pass





class Caninos:

    def __init__(self, nombre: str, raza: str, edad: str, altura: str, peso: str, observaciones: str, Empresa_Class_115: set["Empresa"] = None, Empresa________________________Caninos2_119: set["Empresa"] = None, Empresa________________________Caninos3_121: set["Empresa"] = None, Empresa________________________Caninos_117: "Empresa" = None):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.observaciones = observaciones
        self.Empresa_Class_115 = Empresa_Class_115 if Empresa_Class_115 is not None else set()
        self.Empresa________________________Caninos2_119 = Empresa________________________Caninos2_119 if Empresa________________________Caninos2_119 is not None else set()
        self.Empresa________________________Caninos3_121 = Empresa________________________Caninos3_121 if Empresa________________________Caninos3_121 is not None else set()
        self.Empresa________________________Caninos_117 = Empresa________________________Caninos_117
        
        pass
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

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
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
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
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def Empresa________________________Caninos2_119(self):
        return self.__Empresa________________________Caninos2_119
    @Empresa________________________Caninos2_119.setter
    def Empresa________________________Caninos2_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__Empresa________________________Caninos2_119", None)
        self.__Empresa________________________Caninos2_119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "canino_318"):
                    opp_val = getattr(item, "canino_318", None)
                    
                    if opp_val == self:
                        setattr(item, "canino_318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "canino_318"):
                    opp_val = getattr(item, "canino_318", None)
                    
                    setattr(item, "canino_318", self)
                    

    @property
    def Empresa_Class_115(self):
        return self.__Empresa_Class_115
    @Empresa_Class_115.setter
    def Empresa_Class_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__Empresa_Class_115", None)
        self.__Empresa_Class_115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "canino_114"):
                    opp_val = getattr(item, "canino_114", None)
                    
                    if opp_val == self:
                        setattr(item, "canino_114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "canino_114"):
                    opp_val = getattr(item, "canino_114", None)
                    
                    setattr(item, "canino_114", self)
                    

    @property
    def Empresa________________________Caninos_117(self):
        return self.__Empresa________________________Caninos_117
    @Empresa________________________Caninos_117.setter
    def Empresa________________________Caninos_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__Empresa________________________Caninos_117", None)
        self.__Empresa________________________Caninos_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "canino_216"):
                opp_val = getattr(old_value, "canino_216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "canino_216"):
                opp_val = getattr(value, "canino_216", None)
                if opp_val is None:
                    setattr(value, "canino_216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Empresa________________________Caninos3_121(self):
        return self.__Empresa________________________Caninos3_121
    @Empresa________________________Caninos3_121.setter
    def Empresa________________________Caninos3_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Caninos__Empresa________________________Caninos3_121", None)
        self.__Empresa________________________Caninos3_121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "canino_420"):
                    opp_val = getattr(item, "canino_420", None)
                    
                    if opp_val == self:
                        setattr(item, "canino_420", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "canino_420"):
                    opp_val = getattr(item, "canino_420", None)
                    
                    setattr(item, "canino_420", self)
                    



class Empresa:

    pass
