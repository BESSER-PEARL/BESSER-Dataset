from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class simpleUML_Attribute(NamedElement):

    pass
class Classifier:

    pass
class simpleUML_Association(Classifier):

    pass
class simpleUML_Class(Classifier):

    pass
class simpleUML_Package(Classifier):

    pass
class simpleUML_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleUML_DataType(Classifier):

    pass
class simpleUML_Classifier(NamedElement):

    pass