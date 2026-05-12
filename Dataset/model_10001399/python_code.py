from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Usuario_Actor:

    pass


class Actualizar_Coredata_UseCase:

    pass


class Ver_detalles_de_contacto_UseCase:

    pass


class Salir_de_la_aplicacion_UseCase:

    pass


class Editar_Contacto_UseCase:

    pass


class Eliminar_Contacto_UseCase:

    pass


class Buscar_Contactos_UseCase:

    pass


class Agregar_Contactos_UseCase:

    pass





class Ver_Contactos_external:

    pass


class Contacto:

    def __init__(self, Nombre: str, Apellido: str, Email: str, Telefono: int, Foto: str, user: str, id: int, Groups: str):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Email = Email
        self.Telefono = Telefono
        self.Foto = Foto
        self.user = user
        self.id = id
        self.Groups = Groups
        
        pass
    @property
    def Foto(self):
        return self.__Foto
    @Foto.setter
    def Foto(self, Foto: str):
        self.__Foto = Foto

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def Telefono(self):
        return self.__Telefono
    @Telefono.setter
    def Telefono(self, Telefono: int):
        self.__Telefono = Telefono

    @property
    def Groups(self):
        return self.__Groups
    @Groups.setter
    def Groups(self, Groups: str):
        self.__Groups = Groups

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Apellido(self):
        return self.__Apellido
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self.__Apellido = Apellido



class AGENDA_TELEFONICA_Component:

    pass
