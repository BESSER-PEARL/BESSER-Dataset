from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class extmetadata_Attribute(NamedElement):

    pass
class extmetadata_Class(NamedElement):

    pass
class extmetadata_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

