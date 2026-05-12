from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class User_Actor:

    pass





class Foto_de_perfil:

    pass


class Telefono:

    def __init__(self, Codigo_de_Area: int, Prefijo: int, Numero: int):
        self.Codigo_de_Area = Codigo_de_Area
        self.Prefijo = Prefijo
        self.Numero = Numero
        
        pass
    @property
    def Numero(self):
        return self.__Numero
    @Numero.setter
    def Numero(self, Numero: int):
        self.__Numero = Numero

    @property
    def Prefijo(self):
        return self.__Prefijo
    @Prefijo.setter
    def Prefijo(self, Prefijo: int):
        self.__Prefijo = Prefijo

    @property
    def Codigo_de_Area(self):
        return self.__Codigo_de_Area
    @Codigo_de_Area.setter
    def Codigo_de_Area(self, Codigo_de_Area: int):
        self.__Codigo_de_Area = Codigo_de_Area



class Direccion:

    def __init__(self, Nombre: str, Codigo_Postal: int, Ciudad: str, Pais: str, contacto3: "Contacto" = None, contacto5: "Contacto" = None):
        self.Nombre = Nombre
        self.Codigo_Postal = Codigo_Postal
        self.Ciudad = Ciudad
        self.Pais = Pais
        self.contacto3 = contacto3
        self.contacto5 = contacto5
        
        pass
    @property
    def Ciudad(self):
        return self.__Ciudad
    @Ciudad.setter
    def Ciudad(self, Ciudad: str):
        self.__Ciudad = Ciudad

    @property
    def Codigo_Postal(self):
        return self.__Codigo_Postal
    @Codigo_Postal.setter
    def Codigo_Postal(self, Codigo_Postal: int):
        self.__Codigo_Postal = Codigo_Postal

    @property
    def Pais(self):
        return self.__Pais
    @Pais.setter
    def Pais(self, Pais: str):
        self.__Pais = Pais

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def contacto5(self):
        return self.__contacto5
    @contacto5.setter
    def contacto5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direccion__contacto5", None)
        self.__contacto5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direccion4"):
                opp_val = getattr(old_value, "direccion4", None)
                if opp_val == self:
                    setattr(old_value, "direccion4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direccion4"):
                opp_val = getattr(value, "direccion4", None)
                setattr(value, "direccion4", self)

    @property
    def contacto3(self):
        return self.__contacto3
    @contacto3.setter
    def contacto3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direccion__contacto3", None)
        self.__contacto3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direccion_Principal2"):
                opp_val = getattr(old_value, "direccion_Principal2", None)
                if opp_val == self:
                    setattr(old_value, "direccion_Principal2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direccion_Principal2"):
                opp_val = getattr(value, "direccion_Principal2", None)
                setattr(value, "direccion_Principal2", self)



class Contacto:

    def __init__(self, Nombre: str, Correo: str, directorio1: "Directorio" = None, direccion_Principal2: "Direccion" = None, direccion4: "Direccion" = None):
        self.Nombre = Nombre
        self.Correo = Correo
        self.directorio1 = directorio1
        self.direccion_Principal2 = direccion_Principal2
        self.direccion4 = direccion4
        
        pass
    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def Correo(self):
        return self.__Correo
    @Correo.setter
    def Correo(self, Correo: str):
        self.__Correo = Correo

    @property
    def direccion4(self):
        return self.__direccion4
    @direccion4.setter
    def direccion4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__direccion4", None)
        self.__direccion4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto5"):
                opp_val = getattr(old_value, "contacto5", None)
                if opp_val == self:
                    setattr(old_value, "contacto5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto5"):
                opp_val = getattr(value, "contacto5", None)
                setattr(value, "contacto5", self)

    @property
    def direccion_Principal2(self):
        return self.__direccion_Principal2
    @direccion_Principal2.setter
    def direccion_Principal2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__direccion_Principal2", None)
        self.__direccion_Principal2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto3"):
                opp_val = getattr(old_value, "contacto3", None)
                if opp_val == self:
                    setattr(old_value, "contacto3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto3"):
                opp_val = getattr(value, "contacto3", None)
                setattr(value, "contacto3", self)

    @property
    def directorio1(self):
        return self.__directorio1
    @directorio1.setter
    def directorio1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__directorio1", None)
        self.__directorio1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto0"):
                opp_val = getattr(old_value, "contacto0", None)
                if opp_val == self:
                    setattr(old_value, "contacto0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto0"):
                opp_val = getattr(value, "contacto0", None)
                setattr(value, "contacto0", self)



class Directorio:

    def __init__(self, Introducir: str, contacto0: "Contacto" = None):
        self.Introducir = Introducir
        self.contacto0 = contacto0
        
        pass
    @property
    def Introducir(self):
        return self.__Introducir
    @Introducir.setter
    def Introducir(self, Introducir: str):
        self.__Introducir = Introducir

    @property
    def contacto0(self):
        return self.__contacto0
    @contacto0.setter
    def contacto0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Directorio__contacto0", None)
        self.__contacto0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "directorio1"):
                opp_val = getattr(old_value, "directorio1", None)
                if opp_val == self:
                    setattr(old_value, "directorio1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "directorio1"):
                opp_val = getattr(value, "directorio1", None)
                setattr(value, "directorio1", self)

