from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Lit:

    pass
class boolExpEnv_Tru(Lit):

    pass
class Exp:

    pass
class boolExpEnv_Lit(Exp):

    pass
class boolExpEnv_BinExp(Exp):

    pass
class boolExpEnv_VarRef(Exp):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class BinExp:

    pass
class boolExpEnv_Or(BinExp):

    pass
class boolExpEnv_And(BinExp):

    pass
class boolExpEnv_Not(Exp):

    pass
class boolExpEnv_Fals(Lit):

    pass
class boolExpEnv_Exp(ABC):

    pass