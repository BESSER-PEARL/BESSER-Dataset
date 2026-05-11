from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleUML_NamedElement:

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
class simpleUML_Classifier(NamedElement):

    pass
class simpleUML_Attribute(NamedElement):

    pass
class Classifier:

    pass
class simpleUML_Association(Classifier):

    pass
class simpleUML_DataType(Classifier):

    pass
class simpleUML_Package(Classifier):

    pass
class simpleUML_Class(Classifier):

    pass