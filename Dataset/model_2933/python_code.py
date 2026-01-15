from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
    PROTECTED = "PROTECTED"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class domainmodel_Modifier(Feature):

    def __init__(self, many: bool, name: str, static: bool, final: str, visibility: str, domainmodel_Modifier: "domainmodel_Type" = None):
        self.many = many
        self.name = name
        self.static = static
        self.final = final
        self.visibility = visibility
        self.domainmodel_Modifier = domainmodel_Modifier
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def domainmodel_Modifier(self):
        return self.__domainmodel_Modifier

    @domainmodel_Modifier.setter
    def domainmodel_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Modifier__domainmodel_Modifier", None)
        self.__domainmodel_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type"):
                opp_val = getattr(old_value, "domainmodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type"):
                opp_val = getattr(value, "domainmodel_Type", None)
                setattr(value, "domainmodel_Type", self)

class domainmodel_AbstractElement:

    pass
class domainmodel_Domainmodel:

    pass
class domainmodel_Feature:

    pass
class Type:

    pass
class domainmodel_Entity(Type):

    pass
class domainmodel_DataType(Type):

    pass
class AbstractElement:

    pass
class domainmodel_Type(AbstractElement):

    def __init__(self, name: str, domainmodel_Type: "domainmodel_Modifier" = None):
        self.name = name
        self.domainmodel_Type = domainmodel_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Type(self):
        return self.__domainmodel_Type

    @domainmodel_Type.setter
    def domainmodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Type__domainmodel_Type", None)
        self.__domainmodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Modifier"):
                opp_val = getattr(old_value, "domainmodel_Modifier", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Modifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Modifier"):
                opp_val = getattr(value, "domainmodel_Modifier", None)
                setattr(value, "domainmodel_Modifier", self)

class domainmodel_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainmodel_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, domainmodel_PackageDeclaration: set["domainmodel_AbstractElement"] = None):
        self.name = name
        self.domainmodel_PackageDeclaration = domainmodel_PackageDeclaration if domainmodel_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_PackageDeclaration(self):
        return self.__domainmodel_PackageDeclaration

    @domainmodel_PackageDeclaration.setter
    def domainmodel_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_PackageDeclaration__domainmodel_PackageDeclaration", None)
        self.__domainmodel_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_AbstractElement2"):
                    opp_val = getattr(item, "domainmodel_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_AbstractElement2"):
                    opp_val = getattr(item, "domainmodel_AbstractElement2", None)
                    
                    setattr(item, "domainmodel_AbstractElement2", self)
                    
