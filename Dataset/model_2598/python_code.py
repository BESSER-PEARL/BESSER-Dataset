from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ClassInMainPackage:

    pass
class MainPackage_Subpackage_InheritingClass(ClassInMainPackage):

    pass
class MainPackage_Subpackage_ClassInSubpackage:

    pass
class MainPackage_EObject:

    pass
class MainPackage_Model:

    pass
class MainPackage_ClassInMainPackage:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
