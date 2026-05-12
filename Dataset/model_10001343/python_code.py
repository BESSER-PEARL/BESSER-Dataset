from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor7_Actor:

    pass


class Actor6_Actor:

    pass


class Actor5_Actor:

    pass


class Actor4_Actor:

    pass


class Actor3_Actor:

    pass


class Actor2_Actor:

    pass


class Actor_Actor:

    pass





class Component3_Component:

    pass


class Component2_Component:

    pass


class Component_Component:

    pass


class Funcionario:

    def __init__(self, cracha: int):
        self.cracha = cracha
        
        pass
    @property
    def cracha(self):
        return self.__cracha
    @cracha.setter
    def cracha(self, cracha: int):
        self.__cracha = cracha



class Pessoa:

    def __init__(self, id: int, Nome: str, idade: int):
        self.id = id
        self.Nome = Nome
        self.idade = idade
        
        pass
    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

