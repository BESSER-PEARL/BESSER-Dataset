from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UML2_Property:

    def __init__(self, isDerived: bool, isDerivedUnion: bool):
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass