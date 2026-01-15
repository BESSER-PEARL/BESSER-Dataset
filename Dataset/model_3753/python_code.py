from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TipoPrimitivo(Enum):
    String = "String"
    Integer = "Integer"
    Double = "Double"
    Date = "Date"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class BD_Columna:

    def __init__(self, nombre: str, tipo: str, BD_Columna: "BD_Tabla" = None):
        self.nombre = nombre
        self.tipo = tipo
        self.BD_Columna = BD_Columna
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def BD_Columna(self):
        return self.__BD_Columna

    @BD_Columna.setter
    def BD_Columna(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BD_Columna__BD_Columna", None)
        self.__BD_Columna = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BD_Tabla2"):
                opp_val = getattr(old_value, "BD_Tabla2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BD_Tabla2"):
                opp_val = getattr(value, "BD_Tabla2", None)
                if opp_val is None:
                    setattr(value, "BD_Tabla2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BD_Tabla:

    def __init__(self, nombre: str, BD_Tabla: "BD_EsquemaBD" = None, BD_Tabla2: set["BD_Columna"] = None):
        self.nombre = nombre
        self.BD_Tabla = BD_Tabla
        self.BD_Tabla2 = BD_Tabla2 if BD_Tabla2 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def BD_Tabla(self):
        return self.__BD_Tabla

    @BD_Tabla.setter
    def BD_Tabla(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BD_Tabla__BD_Tabla", None)
        self.__BD_Tabla = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BD_EsquemaBD"):
                opp_val = getattr(old_value, "BD_EsquemaBD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BD_EsquemaBD"):
                opp_val = getattr(value, "BD_EsquemaBD", None)
                if opp_val is None:
                    setattr(value, "BD_EsquemaBD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BD_Tabla2(self):
        return self.__BD_Tabla2

    @BD_Tabla2.setter
    def BD_Tabla2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BD_Tabla__BD_Tabla2", None)
        self.__BD_Tabla2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BD_Columna"):
                    opp_val = getattr(item, "BD_Columna", None)
                    
                    if opp_val == self:
                        setattr(item, "BD_Columna", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BD_Columna"):
                    opp_val = getattr(item, "BD_Columna", None)
                    
                    setattr(item, "BD_Columna", self)
                    

class BD_EsquemaBD:

    pass