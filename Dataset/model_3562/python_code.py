from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinExp:

    pass
class boolexp_Or(BinExp):

    pass
class boolexp_And(BinExp):

    pass
class Lit:

    pass
class boolexp_Fals(Lit):

    pass
class boolexp_Tru(Lit):

    pass
class Exp:

    pass
class boolexp_VarRef(Exp):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class boolexp_Not(Exp):

    pass
class boolexp_BinExp(Exp):

    pass
class boolexp_Exp(ABC):

    pass
class boolexp_Lit(Exp):

    pass