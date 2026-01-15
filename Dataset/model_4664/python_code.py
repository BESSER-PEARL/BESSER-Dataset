from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Exp:

    pass
class boolexp_BinExp(Exp):

    pass
class boolexp_Exp(ABC):

    pass
class BinExp:

    pass
class boolexp_Or(BinExp):

    pass
class boolexp_And(BinExp):

    pass
class boolexp_Not(Exp):

    pass
class Lit:

    pass
class boolexp_Fals(Lit):

    pass
class boolexp_Tru(Lit):

    pass
class boolexp_Lit(Exp):

    pass