from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleUML_UmlModelElement:

    def __init__(self, umlName: str, umlKind: str, id: str):
        self.umlName = umlName
        self.umlKind = umlKind
        self.id = id
        
    @property
    def umlKind(self) -> str:
        return self.__umlKind

    @umlKind.setter
    def umlKind(self, umlKind: str):
        self.__umlKind = umlKind

    @property
    def umlName(self) -> str:
        return self.__umlName

    @umlName.setter
    def umlName(self, umlName: str):
        self.__umlName = umlName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class UmlClassifier:

    pass
class SimpleUML_UmlPrimitiveDataType(UmlClassifier):

    pass
class UmlModelElement:

    pass
class SimpleUML_UmlPackageElement(UmlModelElement):

    pass
class SimpleUML_UmlPackage(UmlModelElement):

    pass
class SimpleUML_UmlAttribute(UmlModelElement):

    pass
class SimpleUML_UmlClass(UmlClassifier):

    pass
class UmlPackageElement:

    pass
class SimpleUML_UmlClassifier(UmlPackageElement):

    pass
class SimpleUML_UmlAssociation(UmlPackageElement):

    pass