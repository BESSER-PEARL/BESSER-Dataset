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
        
        pass
    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children: str):
        self.__children = children


    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, father: str):
        self.__father = father


    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, mother: str):
        self.__mother = mother


class family_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

