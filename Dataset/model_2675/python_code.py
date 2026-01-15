from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class D:

    pass
class compmultinher_F(D):

    pass
class K:

    pass
class F:

    pass
class compmultinher_I(K, F):

    pass
class compmultinher_A:

    pass
class B:

    pass
class compmultinher_D(B):

    pass
class compmultinher_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class compmultinher_H(Named):

    pass
class compmultinher_L(Named):

    pass
class compmultinher_E(Named):

    pass
class compmultinher_C(Named):

    pass
class compmultinher_B(Named):

    pass
class compmultinher_G(Named):

    pass
class compmultinher_K(Named):

    pass