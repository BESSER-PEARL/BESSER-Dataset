from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class family_Family(NamedElement):

    def __init__(self, children: str, mother: str, father: str):
        self.children = children
        self.mother = mother
        self.father = father
        
    @property
    def children(self) -> str:
        return self.__children

    @children.setter
    def children(self, children: str):
        self.__children = children

    @property
    def mother(self) -> str:
        return self.__mother

    @mother.setter
    def mother(self, mother: str):
        self.__mother = mother

    @property
    def father(self) -> str:
        return self.__father

    @father.setter
    def father(self, father: str):
        self.__father = father

class family_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
