from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Selects_Operando:

    def __init__(self, columna: str, tabla: str, Selects_Operando: "Selects_Join" = None, Selects_Operando15: "Selects_Join" = None):
        self.columna = columna
        self.tabla = tabla
        self.Selects_Operando = Selects_Operando
        self.Selects_Operando15 = Selects_Operando15
        
    @property
    def tabla(self) -> str:
        return self.__tabla

    @tabla.setter
    def tabla(self, tabla: str):
        self.__tabla = tabla

    @property
    def columna(self) -> str:
        return self.__columna

    @columna.setter
    def columna(self, columna: str):
        self.__columna = columna

    @property
    def Selects_Operando15(self):
        return self.__Selects_Operando15

    @Selects_Operando15.setter
    def Selects_Operando15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Selects_Operando__Selects_Operando15", None)
        self.__Selects_Operando15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selects_Join14"):
                opp_val = getattr(old_value, "Selects_Join14", None)
                if opp_val == self:
                    setattr(old_value, "Selects_Join14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selects_Join14"):
                opp_val = getattr(value, "Selects_Join14", None)
                setattr(value, "Selects_Join14", self)

    @property
    def Selects_Operando(self):
        return self.__Selects_Operando

    @Selects_Operando.setter
    def Selects_Operando(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Selects_Operando__Selects_Operando", None)
        self.__Selects_Operando = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selects_Join12"):
                opp_val = getattr(old_value, "Selects_Join12", None)
                if opp_val == self:
                    setattr(old_value, "Selects_Join12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selects_Join12"):
                opp_val = getattr(value, "Selects_Join12", None)
                setattr(value, "Selects_Join12", self)

class Selects_Join:

    pass
class Selects_Where:

    pass
class Selects_From:

    pass
class Selects_Select:

    pass
class NamedElement:

    pass
class Selects_Tabla(NamedElement):

    def __init__(self, tabAlias: str, Selects_Tabla: "Selects_From" = None):
        self.tabAlias = tabAlias
        self.Selects_Tabla = Selects_Tabla
        
    @property
    def tabAlias(self) -> str:
        return self.__tabAlias

    @tabAlias.setter
    def tabAlias(self, tabAlias: str):
        self.__tabAlias = tabAlias

    @property
    def Selects_Tabla(self):
        return self.__Selects_Tabla

    @Selects_Tabla.setter
    def Selects_Tabla(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Selects_Tabla__Selects_Tabla", None)
        self.__Selects_Tabla = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Selects_From8"):
                opp_val = getattr(old_value, "Selects_From8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Selects_From8"):
                opp_val = getattr(value, "Selects_From8", None)
                if opp_val is None:
                    setattr(value, "Selects_From8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Selects_Fichero(NamedElement):

    pass
class Selects_Aplicacion:

    pass
class Selects_NamedElement(ABC):

    def __init__(self, nombre: str):
        self.nombre = nombre
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
