from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Cancelar_UseCase:

    pass


class Guardar_UseCase:

    pass


class Eliminar_Contacto_UseCase:

    pass


class Actualizar_COntacto_UseCase:

    pass


class Crear_Contacto_UseCase:

    pass


class Buscar_Contactos_UseCase:

    pass


class Usuario_Actor:

    pass





class Lista_de_COntacto:

    pass


class Crear_Contacto:

    pass


class Buscar:

    pass


class Menu_Principal:

    pass


class Libro_de_Direcciones1:

    pass


class Foto:

    def __init__(self, largo: int, ancho: int, contacto13: "Contacto" = None):
        self.largo = largo
        self.ancho = ancho
        self.contacto13 = contacto13
        
        pass
    @property
    def largo(self):
        return self.__largo
    @largo.setter
    def largo(self, largo: int):
        self.__largo = largo

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho: int):
        self.__ancho = ancho

    @property
    def contacto13(self):
        return self.__contacto13
    @contacto13.setter
    def contacto13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Foto__contacto13", None)
        self.__contacto13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foto12"):
                opp_val = getattr(old_value, "foto12", None)
                if opp_val == self:
                    setattr(old_value, "foto12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foto12"):
                opp_val = getattr(value, "foto12", None)
                setattr(value, "foto12", self)



class Tel_fono:

    def __init__(self, Codigo_area: int, prefijo: int, numero: int, contacto11: "Contacto" = None):
        self.Codigo_area = Codigo_area
        self.prefijo = prefijo
        self.numero = numero
        self.contacto11 = contacto11
        
        pass
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def prefijo(self):
        return self.__prefijo
    @prefijo.setter
    def prefijo(self, prefijo: int):
        self.__prefijo = prefijo

    @property
    def Codigo_area(self):
        return self.__Codigo_area
    @Codigo_area.setter
    def Codigo_area(self, Codigo_area: int):
        self.__Codigo_area = Codigo_area

    @property
    def contacto11(self):
        return self.__contacto11
    @contacto11.setter
    def contacto11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tel_fono__contacto11", None)
        self.__contacto11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tel_fono10"):
                opp_val = getattr(old_value, "tel_fono10", None)
                if opp_val == self:
                    setattr(old_value, "tel_fono10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tel_fono10"):
                opp_val = getattr(value, "tel_fono10", None)
                setattr(value, "tel_fono10", self)



class Direccion:

    def __init__(self, nombre: str, CodigoPostal: int, Ciudad: str, departamento: str, contacto9: "Contacto" = None):
        self.nombre = nombre
        self.CodigoPostal = CodigoPostal
        self.Ciudad = Ciudad
        self.departamento = departamento
        self.contacto9 = contacto9
        
        pass
    @property
    def CodigoPostal(self):
        return self.__CodigoPostal
    @CodigoPostal.setter
    def CodigoPostal(self, CodigoPostal: int):
        self.__CodigoPostal = CodigoPostal

    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, departamento: str):
        self.__departamento = departamento

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def Ciudad(self):
        return self.__Ciudad
    @Ciudad.setter
    def Ciudad(self, Ciudad: str):
        self.__Ciudad = Ciudad

    @property
    def contacto9(self):
        return self.__contacto9
    @contacto9.setter
    def contacto9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Direccion__contacto9", None)
        self.__contacto9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direccion8"):
                opp_val = getattr(old_value, "direccion8", None)
                if opp_val == self:
                    setattr(old_value, "direccion8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direccion8"):
                opp_val = getattr(value, "direccion8", None)
                setattr(value, "direccion8", self)



class Contacto:

    def __init__(self, nombre: str, email: str, direccion8: "Direccion" = None, tel_fono10: "Tel_fono" = None, foto12: "Foto" = None, libro_de_Direcciones15: "Libro_de_Direcciones" = None):
        self.nombre = nombre
        self.email = email
        self.direccion8 = direccion8
        self.tel_fono10 = tel_fono10
        self.foto12 = foto12
        self.libro_de_Direcciones15 = libro_de_Direcciones15
        
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
    def direccion8(self):
        return self.__direccion8
    @direccion8.setter
    def direccion8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__direccion8", None)
        self.__direccion8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto9"):
                opp_val = getattr(old_value, "contacto9", None)
                if opp_val == self:
                    setattr(old_value, "contacto9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto9"):
                opp_val = getattr(value, "contacto9", None)
                setattr(value, "contacto9", self)

    @property
    def foto12(self):
        return self.__foto12
    @foto12.setter
    def foto12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__foto12", None)
        self.__foto12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto13"):
                opp_val = getattr(old_value, "contacto13", None)
                if opp_val == self:
                    setattr(old_value, "contacto13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto13"):
                opp_val = getattr(value, "contacto13", None)
                setattr(value, "contacto13", self)

    @property
    def tel_fono10(self):
        return self.__tel_fono10
    @tel_fono10.setter
    def tel_fono10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__tel_fono10", None)
        self.__tel_fono10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto11"):
                opp_val = getattr(old_value, "contacto11", None)
                if opp_val == self:
                    setattr(old_value, "contacto11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto11"):
                opp_val = getattr(value, "contacto11", None)
                setattr(value, "contacto11", self)

    @property
    def libro_de_Direcciones15(self):
        return self.__libro_de_Direcciones15
    @libro_de_Direcciones15.setter
    def libro_de_Direcciones15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contacto__libro_de_Direcciones15", None)
        self.__libro_de_Direcciones15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacto14"):
                opp_val = getattr(old_value, "contacto14", None)
                if opp_val == self:
                    setattr(old_value, "contacto14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacto14"):
                opp_val = getattr(value, "contacto14", None)
                setattr(value, "contacto14", self)



class Libro_de_Direcciones:

    def __init__(self, Introduccion: str, contacto14: "Contacto" = None):
        self.Introduccion = Introduccion
        self.contacto14 = contacto14
        
        pass
    @property
    def Introduccion(self):
        return self.__Introduccion
    @Introduccion.setter
    def Introduccion(self, Introduccion: str):
        self.__Introduccion = Introduccion

    @property
    def contacto14(self):
        return self.__contacto14
    @contacto14.setter
    def contacto14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Libro_de_Direcciones__contacto14", None)
        self.__contacto14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libro_de_Direcciones15"):
                opp_val = getattr(old_value, "libro_de_Direcciones15", None)
                if opp_val == self:
                    setattr(old_value, "libro_de_Direcciones15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libro_de_Direcciones15"):
                opp_val = getattr(value, "libro_de_Direcciones15", None)
                setattr(value, "libro_de_Direcciones15", self)

