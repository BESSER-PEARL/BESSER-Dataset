from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Personas:

    def __init__(self, Nombre: str, Direccion: str):
        self.Nombre = Nombre
        self.Direccion = Direccion
        
        pass
    @property
    def Direccion(self):
        return self.__Direccion
    @Direccion.setter
    def Direccion(self, Direccion: str):
        self.__Direccion = Direccion

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre



class Entrenador:

    def __init__(self, nivel_de_acreditaci_n: str, a_os_de_experiencia: int):
        self.nivel_de_acreditaci_n = nivel_de_acreditaci_n
        self.a_os_de_experiencia = a_os_de_experiencia
        
        pass
    @property
    def a_os_de_experiencia(self):
        return self.__a_os_de_experiencia
    @a_os_de_experiencia.setter
    def a_os_de_experiencia(self, a_os_de_experiencia: int):
        self.__a_os_de_experiencia = a_os_de_experiencia

    @property
    def nivel_de_acreditaci_n(self):
        return self.__nivel_de_acreditaci_n
    @nivel_de_acreditaci_n.setter
    def nivel_de_acreditaci_n(self, nivel_de_acreditaci_n: str):
        self.__nivel_de_acreditaci_n = nivel_de_acreditaci_n



class Partido:

    def __init__(self, resultado: int, localizaci_n: str, equipo7: set["Equipo"] = None):
        self.resultado = resultado
        self.localizaci_n = localizaci_n
        self.equipo7 = equipo7 if equipo7 is not None else set()
        
        pass
    @property
    def resultado(self):
        return self.__resultado
    @resultado.setter
    def resultado(self, resultado: int):
        self.__resultado = resultado

    @property
    def localizaci_n(self):
        return self.__localizaci_n
    @localizaci_n.setter
    def localizaci_n(self, localizaci_n: str):
        self.__localizaci_n = localizaci_n

    @property
    def equipo7(self):
        return self.__equipo7
    @equipo7.setter
    def equipo7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Partido__equipo7", None)
        self.__equipo7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "partido6"):
                    opp_val = getattr(item, "partido6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "partido6"):
                    opp_val = getattr(item, "partido6", None)
                    
                    if opp_val is None:
                        setattr(item, "partido6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Jugadores:

    def __init__(self, nombre: str, posicion: int, equipo3: "Equipo" = None, equipo4: "Equipo" = None):
        self.nombre = nombre
        self.posicion = posicion
        self.equipo3 = equipo3
        self.equipo4 = equipo4
        
        pass
    @property
    def posicion(self):
        return self.__posicion
    @posicion.setter
    def posicion(self, posicion: int):
        self.__posicion = posicion

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def equipo3(self):
        return self.__equipo3
    @equipo3.setter
    def equipo3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugadores__equipo3", None)
        self.__equipo3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugadores2"):
                opp_val = getattr(old_value, "jugadores2", None)
                if opp_val == self:
                    setattr(old_value, "jugadores2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugadores2"):
                opp_val = getattr(value, "jugadores2", None)
                setattr(value, "jugadores2", self)

    @property
    def equipo4(self):
        return self.__equipo4
    @equipo4.setter
    def equipo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jugadores__equipo4", None)
        self.__equipo4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jugadores5"):
                opp_val = getattr(old_value, "jugadores5", None)
                if opp_val == self:
                    setattr(old_value, "jugadores5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jugadores5"):
                opp_val = getattr(value, "jugadores5", None)
                setattr(value, "jugadores5", self)



class Equipo:

    def __init__(self, nombre: str, registro: str, partido6: set["Partido"] = None, liga1: "Liga" = None, jugadores2: "Jugadores" = None, jugadores5: "Jugadores" = None):
        self.nombre = nombre
        self.registro = registro
        self.partido6 = partido6 if partido6 is not None else set()
        self.liga1 = liga1
        self.jugadores2 = jugadores2
        self.jugadores5 = jugadores5
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def registro(self):
        return self.__registro
    @registro.setter
    def registro(self, registro: str):
        self.__registro = registro

    @property
    def partido6(self):
        return self.__partido6
    @partido6.setter
    def partido6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__partido6", None)
        self.__partido6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "equipo7"):
                    opp_val = getattr(item, "equipo7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "equipo7"):
                    opp_val = getattr(item, "equipo7", None)
                    
                    if opp_val is None:
                        setattr(item, "equipo7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def jugadores5(self):
        return self.__jugadores5
    @jugadores5.setter
    def jugadores5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__jugadores5", None)
        self.__jugadores5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo4"):
                opp_val = getattr(old_value, "equipo4", None)
                if opp_val == self:
                    setattr(old_value, "equipo4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo4"):
                opp_val = getattr(value, "equipo4", None)
                setattr(value, "equipo4", self)

    @property
    def jugadores2(self):
        return self.__jugadores2
    @jugadores2.setter
    def jugadores2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__jugadores2", None)
        self.__jugadores2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo3"):
                opp_val = getattr(old_value, "equipo3", None)
                if opp_val == self:
                    setattr(old_value, "equipo3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo3"):
                opp_val = getattr(value, "equipo3", None)
                setattr(value, "equipo3", self)

    @property
    def liga1(self):
        return self.__liga1
    @liga1.setter
    def liga1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Equipo__liga1", None)
        self.__liga1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equipo0"):
                opp_val = getattr(old_value, "equipo0", None)
                if opp_val == self:
                    setattr(old_value, "equipo0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equipo0"):
                opp_val = getattr(value, "equipo0", None)
                setattr(value, "equipo0", self)



class Liga:

    def __init__(self, nombre: str, datos_comienzo: str, datos_finalizaci_n: str, equipo0: "Equipo" = None):
        self.nombre = nombre
        self.datos_comienzo = datos_comienzo
        self.datos_finalizaci_n = datos_finalizaci_n
        self.equipo0 = equipo0
        
        pass
    @property
    def datos_finalizaci_n(self):
        return self.__datos_finalizaci_n
    @datos_finalizaci_n.setter
    def datos_finalizaci_n(self, datos_finalizaci_n: str):
        self.__datos_finalizaci_n = datos_finalizaci_n

    @property
    def datos_comienzo(self):
        return self.__datos_comienzo
    @datos_comienzo.setter
    def datos_comienzo(self, datos_comienzo: str):
        self.__datos_comienzo = datos_comienzo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def equipo0(self):
        return self.__equipo0
    @equipo0.setter
    def equipo0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Liga__equipo0", None)
        self.__equipo0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "liga1"):
                opp_val = getattr(old_value, "liga1", None)
                if opp_val == self:
                    setattr(old_value, "liga1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "liga1"):
                opp_val = getattr(value, "liga1", None)
                setattr(value, "liga1", self)

