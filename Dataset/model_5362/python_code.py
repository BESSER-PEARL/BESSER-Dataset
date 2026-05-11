from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BaseType:

    pass
class base_nested_SubA(BaseType):

    pass
class base_BaseType:

    def __init__(self, stuff: str):
        self.stuff = stuff
        
        pass
    @property
    def stuff(self):
        return self.__stuff

    @stuff.setter
    def stuff(self, stuff: str):
        self.__stuff = stuff

