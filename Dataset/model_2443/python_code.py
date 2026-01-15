from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Named:

    pass
class relationalmm_Column(Named):

    pass
class relationalmm_Type(Named):

    pass
class relationalmm_Table(Named):

    pass
class relationalmm_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
