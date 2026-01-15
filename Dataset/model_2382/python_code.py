from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml2rdbms_UmlToRdbmsModelElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class uml2rdbms_Package:

    pass
class uml2rdbms_Column:

    pass
class uml2rdbms_ToColumn(ABC):

    pass
class uml2rdbms_PrimitiveDataType:

    pass
class uml2rdbms_FromAttributeOwner(ABC):

    pass
class uml2rdbms_Schema:

    pass
class uml2rdbms_Table:

    pass
class uml2rdbms_Attribute:

    pass
class uml2rdbms_Class:

    pass
class uml2rdbms_ForeignKey:

    pass
class uml2rdbms_Key:

    pass
class FromAttributeOwner:

    pass
class PrimitiveToName:

    pass
class uml2rdbms_IntegerToNumber(PrimitiveToName):

    pass
class uml2rdbms_StringToVarchar(PrimitiveToName):

    pass
class uml2rdbms_BooleanToBoolean(PrimitiveToName):

    pass
class uml2rdbms_Association:

    pass
class UmlToRdbmsModelElement:

    pass
class uml2rdbms_PackageToSchema(UmlToRdbmsModelElement):

    pass
class uml2rdbms_FromAttribute(UmlToRdbmsModelElement):

    def __init__(self, kind: str, uml2rdbms_FromAttribute: "uml2rdbms_Attribute" = None, FromAttribute: "uml2rdbms_FromAttributeOwner" = None, uml2rdbms_FromAttribute17: set["uml2rdbms_AttributeToColumn"] = None, fromAttributes: "uml2rdbms_FromAttributeOwner" = None):
        self.kind = kind
        self.uml2rdbms_FromAttribute = uml2rdbms_FromAttribute
        self.FromAttribute = FromAttribute
        self.uml2rdbms_FromAttribute17 = uml2rdbms_FromAttribute17 if uml2rdbms_FromAttribute17 is not None else set()
        self.fromAttributes = fromAttributes
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def FromAttribute(self):
        return self.__FromAttribute

    @FromAttribute.setter
    def FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__FromAttribute", None)
        self.__FromAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner21"):
                opp_val = getattr(old_value, "owner21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner21"):
                opp_val = getattr(value, "owner21", None)
                if opp_val is None:
                    setattr(value, "owner21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2rdbms_FromAttribute17(self):
        return self.__uml2rdbms_FromAttribute17

    @uml2rdbms_FromAttribute17.setter
    def uml2rdbms_FromAttribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__uml2rdbms_FromAttribute17", None)
        self.__uml2rdbms_FromAttribute17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uml2rdbms_AttributeToColumn18"):
                    opp_val = getattr(item, "uml2rdbms_AttributeToColumn18", None)
                    
                    if opp_val == self:
                        setattr(item, "uml2rdbms_AttributeToColumn18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uml2rdbms_AttributeToColumn18"):
                    opp_val = getattr(item, "uml2rdbms_AttributeToColumn18", None)
                    
                    setattr(item, "uml2rdbms_AttributeToColumn18", self)
                    

    @property
    def fromAttributes(self):
        return self.__fromAttributes

    @fromAttributes.setter
    def fromAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__fromAttributes", None)
        self.__fromAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FromAttributeOwner"):
                opp_val = getattr(old_value, "FromAttributeOwner", None)
                if opp_val == self:
                    setattr(old_value, "FromAttributeOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FromAttributeOwner"):
                opp_val = getattr(value, "FromAttributeOwner", None)
                setattr(value, "FromAttributeOwner", self)

    @property
    def uml2rdbms_FromAttribute(self):
        return self.__uml2rdbms_FromAttribute

    @uml2rdbms_FromAttribute.setter
    def uml2rdbms_FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_FromAttribute__uml2rdbms_FromAttribute", None)
        self.__uml2rdbms_FromAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_Attribute"):
                opp_val = getattr(old_value, "uml2rdbms_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_Attribute"):
                opp_val = getattr(value, "uml2rdbms_Attribute", None)
                setattr(value, "uml2rdbms_Attribute", self)

class uml2rdbms_PrimitiveToName(UmlToRdbmsModelElement):

    def __init__(self, typeName: str, uml2rdbms_PrimitiveToName: "uml2rdbms_AttributeToColumn" = None, PrimitiveToName: "uml2rdbms_PackageToSchema" = None, primitivesToNames: "uml2rdbms_PackageToSchema" = None, uml2rdbms_PrimitiveToName33: "uml2rdbms_PrimitiveDataType" = None):
        self.typeName = typeName
        self.uml2rdbms_PrimitiveToName = uml2rdbms_PrimitiveToName
        self.PrimitiveToName = PrimitiveToName
        self.primitivesToNames = primitivesToNames
        self.uml2rdbms_PrimitiveToName33 = uml2rdbms_PrimitiveToName33
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def primitivesToNames(self):
        return self.__primitivesToNames

    @primitivesToNames.setter
    def primitivesToNames(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__primitivesToNames", None)
        self.__primitivesToNames = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageToSchema31"):
                opp_val = getattr(old_value, "PackageToSchema31", None)
                if opp_val == self:
                    setattr(old_value, "PackageToSchema31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageToSchema31"):
                opp_val = getattr(value, "PackageToSchema31", None)
                setattr(value, "PackageToSchema31", self)

    @property
    def uml2rdbms_PrimitiveToName33(self):
        return self.__uml2rdbms_PrimitiveToName33

    @uml2rdbms_PrimitiveToName33.setter
    def uml2rdbms_PrimitiveToName33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__uml2rdbms_PrimitiveToName33", None)
        self.__uml2rdbms_PrimitiveToName33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_PrimitiveDataType"):
                opp_val = getattr(old_value, "uml2rdbms_PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_PrimitiveDataType"):
                opp_val = getattr(value, "uml2rdbms_PrimitiveDataType", None)
                setattr(value, "uml2rdbms_PrimitiveDataType", self)

    @property
    def PrimitiveToName(self):
        return self.__PrimitiveToName

    @PrimitiveToName.setter
    def PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__PrimitiveToName", None)
        self.__PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner26"):
                opp_val = getattr(old_value, "owner26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner26"):
                opp_val = getattr(value, "owner26", None)
                if opp_val is None:
                    setattr(value, "owner26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uml2rdbms_PrimitiveToName(self):
        return self.__uml2rdbms_PrimitiveToName

    @uml2rdbms_PrimitiveToName.setter
    def uml2rdbms_PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml2rdbms_PrimitiveToName__uml2rdbms_PrimitiveToName", None)
        self.__uml2rdbms_PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml2rdbms_AttributeToColumn"):
                opp_val = getattr(old_value, "uml2rdbms_AttributeToColumn", None)
                if opp_val == self:
                    setattr(old_value, "uml2rdbms_AttributeToColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml2rdbms_AttributeToColumn"):
                opp_val = getattr(value, "uml2rdbms_AttributeToColumn", None)
                setattr(value, "uml2rdbms_AttributeToColumn", self)

class ToColumn:

    pass
class uml2rdbms_ClassToTable(UmlToRdbmsModelElement, FromAttributeOwner, ToColumn):

    pass
class uml2rdbms_AssociationToForeignKey(UmlToRdbmsModelElement, ToColumn):

    pass
class FromAttribute:

    pass
class uml2rdbms_NonLeafAttribute(FromAttribute, FromAttributeOwner):

    pass
class uml2rdbms_AttributeToColumn(FromAttribute, ToColumn):

    pass