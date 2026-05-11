from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Lit:

    pass
class boolexp_Fals(Lit):

    pass
class boolexp_Tru(Lit):

    pass
class BinaryExp:

    pass
class boolexp_Or(BinaryExp):

    pass
class boolexp_And(BinaryExp):

    pass
class Exp:

    pass
class boolexp_Lit(Exp):

    pass
class boolexp_BinaryExp(Exp):

    pass
class boolexp_Exp(ABC):

    pass