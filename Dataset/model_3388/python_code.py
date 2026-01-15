from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Fragmentos_Fichero:

    def __init__(self, nombre: str, Fragmentos_Fichero2: set["Fragmentos_Fragmento"] = None, Fragmentos_Fichero4: set["Fragmentos_Fragmento"] = None, Fragmentos_Fichero: "Fragmentos_Aplicacion" = None):
        self.nombre = nombre
        self.Fragmentos_Fichero2 = Fragmentos_Fichero2 if Fragmentos_Fichero2 is not None else set()
        self.Fragmentos_Fichero4 = Fragmentos_Fichero4 if Fragmentos_Fichero4 is not None else set()
        self.Fragmentos_Fichero = Fragmentos_Fichero
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def Fragmentos_Fichero(self):
        return self.__Fragmentos_Fichero

    @Fragmentos_Fichero.setter
    def Fragmentos_Fichero(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fichero__Fragmentos_Fichero", None)
        self.__Fragmentos_Fichero = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragmentos_Aplicacion"):
                opp_val = getattr(old_value, "Fragmentos_Aplicacion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragmentos_Aplicacion"):
                opp_val = getattr(value, "Fragmentos_Aplicacion", None)
                if opp_val is None:
                    setattr(value, "Fragmentos_Aplicacion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Fragmentos_Fichero2(self):
        return self.__Fragmentos_Fichero2

    @Fragmentos_Fichero2.setter
    def Fragmentos_Fichero2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fichero__Fragmentos_Fichero2", None)
        self.__Fragmentos_Fichero2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Fragmentos_Fragmento"):
                    opp_val = getattr(item, "Fragmentos_Fragmento", None)
                    
                    if opp_val == self:
                        setattr(item, "Fragmentos_Fragmento", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Fragmentos_Fragmento"):
                    opp_val = getattr(item, "Fragmentos_Fragmento", None)
                    
                    setattr(item, "Fragmentos_Fragmento", self)
                    

    @property
    def Fragmentos_Fichero4(self):
        return self.__Fragmentos_Fichero4

    @Fragmentos_Fichero4.setter
    def Fragmentos_Fichero4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fichero__Fragmentos_Fichero4", None)
        self.__Fragmentos_Fichero4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Fragmentos_Fragmento5"):
                    opp_val = getattr(item, "Fragmentos_Fragmento5", None)
                    
                    if opp_val == self:
                        setattr(item, "Fragmentos_Fragmento5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Fragmentos_Fragmento5"):
                    opp_val = getattr(item, "Fragmentos_Fragmento5", None)
                    
                    setattr(item, "Fragmentos_Fragmento5", self)
                    

class Fragmentos_Aplicacion:

    pass
class Fragmentos_Fragmento:

    def __init__(self, numLinea: int, posCaracter: int, texto: str, Fragmentos_Fragmento: "Fragmentos_Fichero" = None, Fragmentos_Fragmento5: "Fragmentos_Fichero" = None, Fragmentos_Fragmento8: "Fragmentos_Fragmento" = None, Fragmentos_Fragmento6: "Fragmentos_Fragmento" = None):
        self.numLinea = numLinea
        self.posCaracter = posCaracter
        self.texto = texto
        self.Fragmentos_Fragmento = Fragmentos_Fragmento
        self.Fragmentos_Fragmento5 = Fragmentos_Fragmento5
        self.Fragmentos_Fragmento8 = Fragmentos_Fragmento8
        self.Fragmentos_Fragmento6 = Fragmentos_Fragmento6
        
    @property
    def numLinea(self) -> int:
        return self.__numLinea

    @numLinea.setter
    def numLinea(self, numLinea: int):
        self.__numLinea = numLinea

    @property
    def texto(self) -> str:
        return self.__texto

    @texto.setter
    def texto(self, texto: str):
        self.__texto = texto

    @property
    def posCaracter(self) -> int:
        return self.__posCaracter

    @posCaracter.setter
    def posCaracter(self, posCaracter: int):
        self.__posCaracter = posCaracter

    @property
    def Fragmentos_Fragmento8(self):
        return self.__Fragmentos_Fragmento8

    @Fragmentos_Fragmento8.setter
    def Fragmentos_Fragmento8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fragmento__Fragmentos_Fragmento8", None)
        self.__Fragmentos_Fragmento8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragmentos_Fragmento6"):
                opp_val = getattr(old_value, "Fragmentos_Fragmento6", None)
                if opp_val == self:
                    setattr(old_value, "Fragmentos_Fragmento6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragmentos_Fragmento6"):
                opp_val = getattr(value, "Fragmentos_Fragmento6", None)
                setattr(value, "Fragmentos_Fragmento6", self)

    @property
    def Fragmentos_Fragmento5(self):
        return self.__Fragmentos_Fragmento5

    @Fragmentos_Fragmento5.setter
    def Fragmentos_Fragmento5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fragmento__Fragmentos_Fragmento5", None)
        self.__Fragmentos_Fragmento5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragmentos_Fichero4"):
                opp_val = getattr(old_value, "Fragmentos_Fichero4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragmentos_Fichero4"):
                opp_val = getattr(value, "Fragmentos_Fichero4", None)
                if opp_val is None:
                    setattr(value, "Fragmentos_Fichero4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Fragmentos_Fragmento(self):
        return self.__Fragmentos_Fragmento

    @Fragmentos_Fragmento.setter
    def Fragmentos_Fragmento(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fragmento__Fragmentos_Fragmento", None)
        self.__Fragmentos_Fragmento = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragmentos_Fichero2"):
                opp_val = getattr(old_value, "Fragmentos_Fichero2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragmentos_Fichero2"):
                opp_val = getattr(value, "Fragmentos_Fichero2", None)
                if opp_val is None:
                    setattr(value, "Fragmentos_Fichero2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Fragmentos_Fragmento6(self):
        return self.__Fragmentos_Fragmento6

    @Fragmentos_Fragmento6.setter
    def Fragmentos_Fragmento6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fragmentos_Fragmento__Fragmentos_Fragmento6", None)
        self.__Fragmentos_Fragmento6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fragmentos_Fragmento8"):
                opp_val = getattr(old_value, "Fragmentos_Fragmento8", None)
                if opp_val == self:
                    setattr(old_value, "Fragmentos_Fragmento8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fragmentos_Fragmento8"):
                opp_val = getattr(value, "Fragmentos_Fragmento8", None)
                setattr(value, "Fragmentos_Fragmento8", self)
