from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor_Actor:

    pass





class Eliminar_Contacto_external:

    pass


class Actualizar__contacto_external:

    pass


class Crear_Contacto_external:

    pass


class Actor_external:

    pass


class Buscar_Contactos_external:

    pass


class Libro_de__Direcciones_Component:

    pass


class TELEFONO:

    def __init__(self, CODIGO_DE__AREA: str, PREFIJO: int, NUMBER: int, cONTACTO3: "CONTACTO" = None):
        self.CODIGO_DE__AREA = CODIGO_DE__AREA
        self.PREFIJO = PREFIJO
        self.NUMBER = NUMBER
        self.cONTACTO3 = cONTACTO3
        
        pass
    @property
    def NUMBER(self):
        return self.__NUMBER
    @NUMBER.setter
    def NUMBER(self, NUMBER: int):
        self.__NUMBER = NUMBER

    @property
    def PREFIJO(self):
        return self.__PREFIJO
    @PREFIJO.setter
    def PREFIJO(self, PREFIJO: int):
        self.__PREFIJO = PREFIJO

    @property
    def CODIGO_DE__AREA(self):
        return self.__CODIGO_DE__AREA
    @CODIGO_DE__AREA.setter
    def CODIGO_DE__AREA(self, CODIGO_DE__AREA: str):
        self.__CODIGO_DE__AREA = CODIGO_DE__AREA

    @property
    def cONTACTO3(self):
        return self.__cONTACTO3
    @cONTACTO3.setter
    def cONTACTO3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TELEFONO__cONTACTO3", None)
        self.__cONTACTO3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tELEFONO2"):
                opp_val = getattr(old_value, "tELEFONO2", None)
                if opp_val == self:
                    setattr(old_value, "tELEFONO2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tELEFONO2"):
                opp_val = getattr(value, "tELEFONO2", None)
                setattr(value, "tELEFONO2", self)



class DIRECCION:

    def __init__(self, NOMBRE: str, CODIGO_POSTAL: str, CIUDAD: str, ESTADO: str, cONTACTO7: "CONTACTO" = None):
        self.NOMBRE = NOMBRE
        self.CODIGO_POSTAL = CODIGO_POSTAL
        self.CIUDAD = CIUDAD
        self.ESTADO = ESTADO
        self.cONTACTO7 = cONTACTO7
        
        pass
    @property
    def CODIGO_POSTAL(self):
        return self.__CODIGO_POSTAL
    @CODIGO_POSTAL.setter
    def CODIGO_POSTAL(self, CODIGO_POSTAL: str):
        self.__CODIGO_POSTAL = CODIGO_POSTAL

    @property
    def NOMBRE(self):
        return self.__NOMBRE
    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: str):
        self.__NOMBRE = NOMBRE

    @property
    def CIUDAD(self):
        return self.__CIUDAD
    @CIUDAD.setter
    def CIUDAD(self, CIUDAD: str):
        self.__CIUDAD = CIUDAD

    @property
    def ESTADO(self):
        return self.__ESTADO
    @ESTADO.setter
    def ESTADO(self, ESTADO: str):
        self.__ESTADO = ESTADO

    @property
    def cONTACTO7(self):
        return self.__cONTACTO7
    @cONTACTO7.setter
    def cONTACTO7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DIRECCION__cONTACTO7", None)
        self.__cONTACTO7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dIRECCION6"):
                opp_val = getattr(old_value, "dIRECCION6", None)
                if opp_val == self:
                    setattr(old_value, "dIRECCION6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dIRECCION6"):
                opp_val = getattr(value, "dIRECCION6", None)
                setattr(value, "dIRECCION6", self)



class CONTACTO:

    def __init__(self, NOMBRE: str, CORREO: str, LIBRO_DE__DIRECCIONES1: "LIBRO_DE__DIRECCIONES" = None, tELEFONO2: "TELEFONO" = None, fOTO4: "FOTO" = None, dIRECCION6: "DIRECCION" = None):
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        self.LIBRO_DE__DIRECCIONES1 = LIBRO_DE__DIRECCIONES1
        self.tELEFONO2 = tELEFONO2
        self.fOTO4 = fOTO4
        self.dIRECCION6 = dIRECCION6
        
        pass
    @property
    def CORREO(self):
        return self.__CORREO
    @CORREO.setter
    def CORREO(self, CORREO: str):
        self.__CORREO = CORREO

    @property
    def NOMBRE(self):
        return self.__NOMBRE
    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: str):
        self.__NOMBRE = NOMBRE

    @property
    def LIBRO_DE__DIRECCIONES1(self):
        return self.__LIBRO_DE__DIRECCIONES1
    @LIBRO_DE__DIRECCIONES1.setter
    def LIBRO_DE__DIRECCIONES1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CONTACTO__LIBRO_DE__DIRECCIONES1", None)
        self.__LIBRO_DE__DIRECCIONES1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cONTACTO0"):
                opp_val = getattr(old_value, "cONTACTO0", None)
                if opp_val == self:
                    setattr(old_value, "cONTACTO0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cONTACTO0"):
                opp_val = getattr(value, "cONTACTO0", None)
                setattr(value, "cONTACTO0", self)

    @property
    def fOTO4(self):
        return self.__fOTO4
    @fOTO4.setter
    def fOTO4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CONTACTO__fOTO4", None)
        self.__fOTO4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cONTACTO5"):
                opp_val = getattr(old_value, "cONTACTO5", None)
                if opp_val == self:
                    setattr(old_value, "cONTACTO5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cONTACTO5"):
                opp_val = getattr(value, "cONTACTO5", None)
                setattr(value, "cONTACTO5", self)

    @property
    def tELEFONO2(self):
        return self.__tELEFONO2
    @tELEFONO2.setter
    def tELEFONO2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CONTACTO__tELEFONO2", None)
        self.__tELEFONO2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cONTACTO3"):
                opp_val = getattr(old_value, "cONTACTO3", None)
                if opp_val == self:
                    setattr(old_value, "cONTACTO3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cONTACTO3"):
                opp_val = getattr(value, "cONTACTO3", None)
                setattr(value, "cONTACTO3", self)

    @property
    def dIRECCION6(self):
        return self.__dIRECCION6
    @dIRECCION6.setter
    def dIRECCION6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CONTACTO__dIRECCION6", None)
        self.__dIRECCION6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cONTACTO7"):
                opp_val = getattr(old_value, "cONTACTO7", None)
                if opp_val == self:
                    setattr(old_value, "cONTACTO7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cONTACTO7"):
                opp_val = getattr(value, "cONTACTO7", None)
                setattr(value, "cONTACTO7", self)



class LIBRO_DE__DIRECCIONES:

    def __init__(self, INTRODUCCION: str, cONTACTO0: "CONTACTO" = None):
        self.INTRODUCCION = INTRODUCCION
        self.cONTACTO0 = cONTACTO0
        
        pass
    @property
    def INTRODUCCION(self):
        return self.__INTRODUCCION
    @INTRODUCCION.setter
    def INTRODUCCION(self, INTRODUCCION: str):
        self.__INTRODUCCION = INTRODUCCION

    @property
    def cONTACTO0(self):
        return self.__cONTACTO0
    @cONTACTO0.setter
    def cONTACTO0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LIBRO_DE__DIRECCIONES__cONTACTO0", None)
        self.__cONTACTO0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LIBRO_DE__DIRECCIONES1"):
                opp_val = getattr(old_value, "LIBRO_DE__DIRECCIONES1", None)
                if opp_val == self:
                    setattr(old_value, "LIBRO_DE__DIRECCIONES1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LIBRO_DE__DIRECCIONES1"):
                opp_val = getattr(value, "LIBRO_DE__DIRECCIONES1", None)
                setattr(value, "LIBRO_DE__DIRECCIONES1", self)



class FOTO:

    def __init__(self, ANCHO: int, ALTURA: int, cONTACTO5: "CONTACTO" = None):
        self.ANCHO = ANCHO
        self.ALTURA = ALTURA
        self.cONTACTO5 = cONTACTO5
        
        pass
    @property
    def ANCHO(self):
        return self.__ANCHO
    @ANCHO.setter
    def ANCHO(self, ANCHO: int):
        self.__ANCHO = ANCHO

    @property
    def ALTURA(self):
        return self.__ALTURA
    @ALTURA.setter
    def ALTURA(self, ALTURA: int):
        self.__ALTURA = ALTURA

    @property
    def cONTACTO5(self):
        return self.__cONTACTO5
    @cONTACTO5.setter
    def cONTACTO5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FOTO__cONTACTO5", None)
        self.__cONTACTO5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fOTO4"):
                opp_val = getattr(old_value, "fOTO4", None)
                if opp_val == self:
                    setattr(old_value, "fOTO4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fOTO4"):
                opp_val = getattr(value, "fOTO4", None)
                setattr(value, "fOTO4", self)

