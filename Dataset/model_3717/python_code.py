from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_StructuralFeature:

    def __init__(self, isReadOnly: bool):
        self.isReadOnly = isReadOnly
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    def __init__(self, isDerivedUnion: bool):
        self.isDerivedUnion = isDerivedUnion
        
    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

class UML2_Port(Property):

    pass