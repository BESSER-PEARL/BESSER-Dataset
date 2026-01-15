from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    public = "public"
    private = "private"
    protected = "protected"


############################################
# Definition of Classes
############################################

class Type:

    pass
class domainmodel_Entity(Type):

    pass
class domainmodel_DataType(Type):

    pass
class domainmodel_TypeRef:

    def __init__(self, multi: bool, domainmodel_TypeRef: "domainmodel_TypedElement" = None, domainmodel_TypeRef12: "domainmodel_Type" = None):
        self.multi = multi
        self.domainmodel_TypeRef = domainmodel_TypeRef
        self.domainmodel_TypeRef12 = domainmodel_TypeRef12
        
    @property
    def multi(self) -> bool:
        return self.__multi

    @multi.setter
    def multi(self, multi: bool):
        self.__multi = multi

    @property
    def domainmodel_TypeRef12(self):
        return self.__domainmodel_TypeRef12

    @domainmodel_TypeRef12.setter
    def domainmodel_TypeRef12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_TypeRef__domainmodel_TypeRef12", None)
        self.__domainmodel_TypeRef12 = value
        
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

    @property
    def domainmodel_TypeRef(self):
        return self.__domainmodel_TypeRef

    @domainmodel_TypeRef.setter
    def domainmodel_TypeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_TypeRef__domainmodel_TypeRef", None)
        self.__domainmodel_TypeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_TypedElement"):
                opp_val = getattr(old_value, "domainmodel_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_TypedElement"):
                opp_val = getattr(value, "domainmodel_TypedElement", None)
                setattr(value, "domainmodel_TypedElement", self)

class domainmodel_TypedElement:

    def __init__(self, name: str, domainmodel_TypedElement: "domainmodel_TypeRef" = None):
        self.name = name
        self.domainmodel_TypedElement = domainmodel_TypedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_TypedElement(self):
        return self.__domainmodel_TypedElement

    @domainmodel_TypedElement.setter
    def domainmodel_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_TypedElement__domainmodel_TypedElement", None)
        self.__domainmodel_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_TypeRef"):
                opp_val = getattr(old_value, "domainmodel_TypeRef", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_TypeRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_TypeRef"):
                opp_val = getattr(value, "domainmodel_TypeRef", None)
                setattr(value, "domainmodel_TypeRef", self)

class StructuralFeature:

    pass
class domainmodel_Reference(StructuralFeature):

    pass
class domainmodel_Attribute(StructuralFeature):

    pass
class Feature:

    pass
class domainmodel_Operation(Feature):

    def __init__(self, visibility: str, domainmodel_Operation: set["domainmodel_Parameter"] = None):
        self.visibility = visibility
        self.domainmodel_Operation = domainmodel_Operation if domainmodel_Operation is not None else set()
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def domainmodel_Operation(self):
        return self.__domainmodel_Operation

    @domainmodel_Operation.setter
    def domainmodel_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Operation__domainmodel_Operation", None)
        self.__domainmodel_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "domainmodel_Parameter"):
                    opp_val = getattr(item, "domainmodel_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "domainmodel_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "domainmodel_Parameter"):
                    opp_val = getattr(item, "domainmodel_Parameter", None)
                    
                    setattr(item, "domainmodel_Parameter", self)
                    

class domainmodel_StructuralFeature(Feature):

    pass
class TypedElement:

    pass
class domainmodel_Parameter(TypedElement):

    pass
class domainmodel_Feature(TypedElement):

    pass
class AbstractElement:

    pass
class domainmodel_Type(AbstractElement):

    def __init__(self, name: str, domainmodel_Type: "domainmodel_TypeRef" = None):
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
            if hasattr(old_value, "domainmodel_TypeRef12"):
                opp_val = getattr(old_value, "domainmodel_TypeRef12", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_TypeRef12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_TypeRef12"):
                opp_val = getattr(value, "domainmodel_TypeRef12", None)
                setattr(value, "domainmodel_TypeRef12", self)

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
                    

class domainmodel_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class domainmodel_AbstractElement:

    pass
class domainmodel_DomainModel:

    pass