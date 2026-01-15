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

class Feature:

    pass
class domainmodel_StructuralFeature(Feature):

    pass
class domainmodel_TypeRef:

    def __init__(self, multi: bool, domainmodel_TypeRef14: "domainmodel_Parameter" = None, domainmodel_TypeRef16: "domainmodel_Type" = None, domainmodel_TypeRef: "domainmodel_Feature" = None):
        self.multi = multi
        self.domainmodel_TypeRef14 = domainmodel_TypeRef14
        self.domainmodel_TypeRef16 = domainmodel_TypeRef16
        self.domainmodel_TypeRef = domainmodel_TypeRef
        
    @property
    def multi(self) -> bool:
        return self.__multi

    @multi.setter
    def multi(self, multi: bool):
        self.__multi = multi

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
            if hasattr(old_value, "domainmodel_Feature8"):
                opp_val = getattr(old_value, "domainmodel_Feature8", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Feature8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Feature8"):
                opp_val = getattr(value, "domainmodel_Feature8", None)
                setattr(value, "domainmodel_Feature8", self)

    @property
    def domainmodel_TypeRef16(self):
        return self.__domainmodel_TypeRef16

    @domainmodel_TypeRef16.setter
    def domainmodel_TypeRef16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_TypeRef__domainmodel_TypeRef16", None)
        self.__domainmodel_TypeRef16 = value
        
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
    def domainmodel_TypeRef14(self):
        return self.__domainmodel_TypeRef14

    @domainmodel_TypeRef14.setter
    def domainmodel_TypeRef14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_TypeRef__domainmodel_TypeRef14", None)
        self.__domainmodel_TypeRef14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Parameter13"):
                opp_val = getattr(old_value, "domainmodel_Parameter13", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Parameter13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Parameter13"):
                opp_val = getattr(value, "domainmodel_Parameter13", None)
                setattr(value, "domainmodel_Parameter13", self)

class domainmodel_Feature:

    def __init__(self, name: str, domainmodel_Feature: "domainmodel_Entity" = None, domainmodel_Feature8: "domainmodel_TypeRef" = None):
        self.name = name
        self.domainmodel_Feature = domainmodel_Feature
        self.domainmodel_Feature8 = domainmodel_Feature8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Feature8(self):
        return self.__domainmodel_Feature8

    @domainmodel_Feature8.setter
    def domainmodel_Feature8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature8", None)
        self.__domainmodel_Feature8 = value
        
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

    @property
    def domainmodel_Feature(self):
        return self.__domainmodel_Feature

    @domainmodel_Feature.setter
    def domainmodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature", None)
        self.__domainmodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity6"):
                opp_val = getattr(old_value, "domainmodel_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity6"):
                opp_val = getattr(value, "domainmodel_Entity6", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_Parameter:

    def __init__(self, name: str, domainmodel_Parameter: "domainmodel_Operation" = None, domainmodel_Parameter13: "domainmodel_TypeRef" = None):
        self.name = name
        self.domainmodel_Parameter = domainmodel_Parameter
        self.domainmodel_Parameter13 = domainmodel_Parameter13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def domainmodel_Parameter(self):
        return self.__domainmodel_Parameter

    @domainmodel_Parameter.setter
    def domainmodel_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Parameter__domainmodel_Parameter", None)
        self.__domainmodel_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Operation"):
                opp_val = getattr(old_value, "domainmodel_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Operation"):
                opp_val = getattr(value, "domainmodel_Operation", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_Parameter13(self):
        return self.__domainmodel_Parameter13

    @domainmodel_Parameter13.setter
    def domainmodel_Parameter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Parameter__domainmodel_Parameter13", None)
        self.__domainmodel_Parameter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_TypeRef14"):
                opp_val = getattr(old_value, "domainmodel_TypeRef14", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_TypeRef14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_TypeRef14"):
                opp_val = getattr(value, "domainmodel_TypeRef14", None)
                setattr(value, "domainmodel_TypeRef14", self)

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
                    

class StructuralFeature:

    pass
class domainmodel_Reference(StructuralFeature):

    pass
class domainmodel_Attribute(StructuralFeature):

    pass
class domainmodel_AbstractElement:

    pass
class domainmodel_DomainModel:

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
            if hasattr(old_value, "domainmodel_TypeRef16"):
                opp_val = getattr(old_value, "domainmodel_TypeRef16", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_TypeRef16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_TypeRef16"):
                opp_val = getattr(value, "domainmodel_TypeRef16", None)
                setattr(value, "domainmodel_TypeRef16", self)

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
