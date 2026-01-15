from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Named:

    pass
class entityDsl_Attribute(Named):

    pass
class entityDsl_Entity(Named):

    pass
class entityDsl_Module(Named):

    pass
class AbstractType:

    pass
class entityDsl_StringType(AbstractType):

    pass
class entityDsl_EntityReference(AbstractType):

    pass
class entityDsl_IntType(AbstractType):

    pass
class entityDsl_BooleanType(AbstractType):

    pass
class entityDsl_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class entityDsl_AbstractType:

    pass