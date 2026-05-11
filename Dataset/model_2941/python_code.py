from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ER_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class ER_EntityType(NamedElement):

    pass
class ER_ERModel(NamedElement):

    pass
class Reference:

    pass
class ER_StrongReference(Reference):

    pass
class ER_WeakReference(Reference):

    pass
class Feature:

    pass
class ER_Reference(Feature):

    pass
class ER_Attribute(Feature):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class ER_Feature(NamedElement):

    pass