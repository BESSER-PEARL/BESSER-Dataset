from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class USUARIO:

    def __init__(self, ID: str, Nombre: str, Contrase_a: str, cUENTA0: set["CUENTA"] = None):
        self.ID = ID
        self.Nombre = Nombre
        self.Contrase_a = Contrase_a
        self.cUENTA0 = cUENTA0 if cUENTA0 is not None else set()
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Contrase_a(self):
        return self.__Contrase_a
    @Contrase_a.setter
    def Contrase_a(self, Contrase_a: str):
        self.__Contrase_a = Contrase_a

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def cUENTA0(self):
        return self.__cUENTA0
    @cUENTA0.setter
    def cUENTA0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_USUARIO__cUENTA0", None)
        self.__cUENTA0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uSUARIO1"):
                    opp_val = getattr(item, "uSUARIO1", None)
                    
                    if opp_val == self:
                        setattr(item, "uSUARIO1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uSUARIO1"):
                    opp_val = getattr(item, "uSUARIO1", None)
                    
                    setattr(item, "uSUARIO1", self)
                    



class CUENTA:

    def __init__(self, Nombre: str, Tipo_de_Cuenta: str, Balance: int, uSUARIO1: "USUARIO" = None):
        self.Nombre = Nombre
        self.Tipo_de_Cuenta = Tipo_de_Cuenta
        self.Balance = Balance
        self.uSUARIO1 = uSUARIO1
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: int):
        self.__Balance = Balance

    @property
    def Tipo_de_Cuenta(self):
        return self.__Tipo_de_Cuenta
    @Tipo_de_Cuenta.setter
    def Tipo_de_Cuenta(self, Tipo_de_Cuenta: str):
        self.__Tipo_de_Cuenta = Tipo_de_Cuenta

    @property
    def uSUARIO1(self):
        return self.__uSUARIO1
    @uSUARIO1.setter
    def uSUARIO1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CUENTA__uSUARIO1", None)
        self.__uSUARIO1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cUENTA0"):
                opp_val = getattr(old_value, "cUENTA0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cUENTA0"):
                opp_val = getattr(value, "cUENTA0", None)
                if opp_val is None:
                    setattr(value, "cUENTA0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

