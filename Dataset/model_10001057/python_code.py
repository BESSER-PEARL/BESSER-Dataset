from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Foto:

    def __init__(self, alto: int, ancho: int, contacto10: "Contacto" = None):
        self.alto = alto
        self.ancho = ancho
        self.contacto10 = contacto10
        
        pass
    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self, alto: int):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho: int):
        self.__ancho = ancho

    @property
    def contacto10(self):
        return self.__contacto10
    @contacto10.setter
    def contacto10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Foto__contacto10", None)
        self.__contacto10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foto11"):
                opp_val = getattr(old_value, "foto11", None)
                if opp_val == self:
                    setattr(old_value, "foto11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foto11"):
                opp_val = getattr(value, "foto11", None)
                setattr(value, "foto11", self)



class Telefono:

    def __init__(self, codigo: int, prefijo: int, numero: int, contacto6: "Contacto" = None, contacto8: "Contacto" = None):
        self.codigo = codigo
        self.prefijo = prefijo
        self.numero = numero
        self.contacto6 = contacto6
        self.contacto8 = contacto8
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def prefijo(self):
        return self.__prefijo
    @prefijo.setter
    def prefijo(self, prefijo: int):
        self.__prefijo = prefijo

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def contacto6(self):
        return self.__contacto6
    @contacto6.setter
    def contacto6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Telefono__contacto6", None)
        self.__contacto6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "telefonoPrincipal7"):
                opp_val = getattr(old_value, "telefonoPrincipal7", None)
                if opp_val == self:
                    setattr(old_value, "telefonoPrincipal7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "telefonoPrincipal7"):
                opp_val = getattr(value, "telefonoPrincipal7", None)
                setattr(value, "telefonoPrincipal7", self)

    @property
    def contacto8(self):
        return self.__contacto8
    @contacto8.setter
    def contacto8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Telefono__contacto8", None)
        self.__contacto8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "telefonoAlternativo9"):
                opp_val = getattr(old_value, "telefonoAlternativo9", None)
                if opp_val == self:
                    setattr(old_value, "telefonoAlternativo9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "telefonoAlternativo9"):
                opp_val = getattr(value, "telefonoAlternativo9", None)
                setattr(value, "telefonoAlternativo9", self)



class Direccion:

    def __init__(self, nombre: str, codigo: int, ciudad: str, pais: str, contacto2: "Contacto" = None, contacto4: "Contacto" = None):
        self.nombre = nombre
        self.codigo = codigo
        self.ciudad = ciudad
        self.pais = pais
        self.contacto2 = contacto2
        self.contacto4 = contacto4
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, ciudad: str):
        self.__ciudad = ciudad

    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, pais: str):
        self.__pais = pais

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def contacto4(self):
        return self.__contacto4
    @contacto4.setter
    def contacto4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direccion__contacto4", None)
        self.__contacto4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direccionAlternativa5"):
                opp_val = getattr(old_value, "direccionAlternativa5", None)
                if opp_val == self:
                    setattr(old_value, "direccionAlternativa5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direccionAlternativa5"):
                opp_val = getattr(value, "direccionAlternativa5", None)
                setattr(value, "direccionAlternativa5", self)

    @property
    def contacto2(self):
        return self.__contacto2
    @contacto2.setter
    def contacto2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direccion__contacto2", None)
        self.__contacto2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direccionPrincipal3"):
                opp_val = getattr(old_value, "direccionPrincipal3", None)
                if opp_val == self:
                    setattr(old_value, "direccionPrincipal3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direccionPrincipal3"):
                opp_val = getattr(value, "direccionPrincipal3", None)
                setattr(value, "direccionPrincipal3", self)



class Contacto:

    def __init__(self, nombre: str, email: str, agenda1: "Agenda" = None, direccionPrincipal3: "Direccion" = None, direccionAlternativa5: "Direccion" = None, telefonoPrincipal7: "Telefono" = None, telefonoAlternativo9: "Telefono" = None, foto11: "Foto" = None):
        self.nombre = nombre
        self.email = email
        self.agenda1 = agenda1
        self.direccionPrincipal3 = direccionPrincipal3
        self.direccionAlternativa5 = direccionAlternativa5
        self.telefonoPrincipal7 = telefonoPrincipal7
        self.telefonoAlternativo9 = telefonoAlternativo9
        self.foto11 = foto11
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def direccionAlternativa5(self):
        return self.__direccionAlternativa5
    @direccionAlternativa5.setter
    def direccionAlternativa5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__direccionAlternativa5", None)
        self.__direccionAlternativa5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto4"):
                opp_val = getattr(old_value, "contacto4", None)
                if opp_val == self:
                    setattr(old_value, "contacto4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto4"):
                opp_val = getattr(value, "contacto4", None)
                setattr(value, "contacto4", self)

    @property
    def foto11(self):
        return self.__foto11
    @foto11.setter
    def foto11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__foto11", None)
        self.__foto11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto10"):
                opp_val = getattr(old_value, "contacto10", None)
                if opp_val == self:
                    setattr(old_value, "contacto10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto10"):
                opp_val = getattr(value, "contacto10", None)
                setattr(value, "contacto10", self)

    @property
    def agenda1(self):
        return self.__agenda1
    @agenda1.setter
    def agenda1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__agenda1", None)
        self.__agenda1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto0"):
                opp_val = getattr(old_value, "contacto0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto0"):
                opp_val = getattr(value, "contacto0", None)
                if opp_val is None:
                    setattr(value, "contacto0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def direccionPrincipal3(self):
        return self.__direccionPrincipal3
    @direccionPrincipal3.setter
    def direccionPrincipal3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__direccionPrincipal3", None)
        self.__direccionPrincipal3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto2"):
                opp_val = getattr(old_value, "contacto2", None)
                if opp_val == self:
                    setattr(old_value, "contacto2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto2"):
                opp_val = getattr(value, "contacto2", None)
                setattr(value, "contacto2", self)

    @property
    def telefonoAlternativo9(self):
        return self.__telefonoAlternativo9
    @telefonoAlternativo9.setter
    def telefonoAlternativo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__telefonoAlternativo9", None)
        self.__telefonoAlternativo9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto8"):
                opp_val = getattr(old_value, "contacto8", None)
                if opp_val == self:
                    setattr(old_value, "contacto8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto8"):
                opp_val = getattr(value, "contacto8", None)
                setattr(value, "contacto8", self)

    @property
    def telefonoPrincipal7(self):
        return self.__telefonoPrincipal7
    @telefonoPrincipal7.setter
    def telefonoPrincipal7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__telefonoPrincipal7", None)
        self.__telefonoPrincipal7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto6"):
                opp_val = getattr(old_value, "contacto6", None)
                if opp_val == self:
                    setattr(old_value, "contacto6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto6"):
                opp_val = getattr(value, "contacto6", None)
                setattr(value, "contacto6", self)



class Agenda:

    def __init__(self, Introduccion: str, contacto0: set["Contacto"] = None):
        self.Introduccion = Introduccion
        self.contacto0 = contacto0 if contacto0 is not None else set()
        
        pass
    @property
    def Introduccion(self):
        return self.__Introduccion
    @Introduccion.setter
    def Introduccion(self, Introduccion: str):
        self.__Introduccion = Introduccion

    @property
    def contacto0(self):
        return self.__contacto0
    @contacto0.setter
    def contacto0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agenda__contacto0", None)
        self.__contacto0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "agenda1"):
                    opp_val = getattr(item, "agenda1", None)
                    
                    if opp_val == self:
                        setattr(item, "agenda1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "agenda1"):
                    opp_val = getattr(item, "agenda1", None)
                    
                    setattr(item, "agenda1", self)
                    

