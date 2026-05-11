from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_StructuralFeature:

    def __init__(self, isReadOnly: bool):
        self.isReadOnly = isReadOnly
        
        pass
    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    def __init__(self, isDerivedUnion: bool):
        self.isDerivedUnion = isDerivedUnion
        
        pass
    @property
    def isDerivedUnion(self):
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

