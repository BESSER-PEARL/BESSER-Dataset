from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleumltordbms_UmlToRdbmsModelElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simpleumltordbms_Package:

    pass
class simpleumltordbms_Column:

    pass
class simpleumltordbms_ToColumn(ABC):

    pass
class simpleumltordbms_PrimitiveDataType:

    pass
class simpleumltordbms_Schema:

    pass
class simpleumltordbms_FromAttributeOwner(ABC):

    pass
class simpleumltordbms_Attribute:

    pass
class FromAttributeOwner:

    pass
class PrimitiveToName:

    pass
class simpleumltordbms_IntegerToNumber(PrimitiveToName):

    pass
class simpleumltordbms_StringToVarchar(PrimitiveToName):

    pass
class simpleumltordbms_BooleanToBoolean(PrimitiveToName):

    pass
class simpleumltordbms_ForeignKey:

    pass
class simpleumltordbms_Association:

    pass
class UmlToRdbmsModelElement:

    pass
class simpleumltordbms_FromAttribute(UmlToRdbmsModelElement):

    def __init__(self, kind: str, simpleumltordbms_FromAttribute: "simpleumltordbms_Attribute" = None, FromAttribute: "simpleumltordbms_FromAttributeOwner" = None, simpleumltordbms_FromAttribute17: set["simpleumltordbms_AttributeToColumn"] = None, fromAttributes: "simpleumltordbms_FromAttributeOwner" = None):
        self.kind = kind
        self.simpleumltordbms_FromAttribute = simpleumltordbms_FromAttribute
        self.FromAttribute = FromAttribute
        self.simpleumltordbms_FromAttribute17 = simpleumltordbms_FromAttribute17 if simpleumltordbms_FromAttribute17 is not None else set()
        self.fromAttributes = fromAttributes
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def simpleumltordbms_FromAttribute17(self):
        return self.__simpleumltordbms_FromAttribute17

    @simpleumltordbms_FromAttribute17.setter
    def simpleumltordbms_FromAttribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_FromAttribute__simpleumltordbms_FromAttribute17", None)
        self.__simpleumltordbms_FromAttribute17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleumltordbms_AttributeToColumn18"):
                    opp_val = getattr(item, "simpleumltordbms_AttributeToColumn18", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleumltordbms_AttributeToColumn18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleumltordbms_AttributeToColumn18"):
                    opp_val = getattr(item, "simpleumltordbms_AttributeToColumn18", None)
                    
                    setattr(item, "simpleumltordbms_AttributeToColumn18", self)
                    

    @property
    def FromAttribute(self):
        return self.__FromAttribute

    @FromAttribute.setter
    def FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_FromAttribute__FromAttribute", None)
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
    def simpleumltordbms_FromAttribute(self):
        return self.__simpleumltordbms_FromAttribute

    @simpleumltordbms_FromAttribute.setter
    def simpleumltordbms_FromAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_FromAttribute__simpleumltordbms_FromAttribute", None)
        self.__simpleumltordbms_FromAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleumltordbms_Attribute"):
                opp_val = getattr(old_value, "simpleumltordbms_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "simpleumltordbms_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleumltordbms_Attribute"):
                opp_val = getattr(value, "simpleumltordbms_Attribute", None)
                setattr(value, "simpleumltordbms_Attribute", self)

    @property
    def fromAttributes(self):
        return self.__fromAttributes

    @fromAttributes.setter
    def fromAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_FromAttribute__fromAttributes", None)
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

class simpleumltordbms_PackageToSchema(UmlToRdbmsModelElement):

    pass
class simpleumltordbms_Class:

    pass
class simpleumltordbms_Table:

    pass
class simpleumltordbms_Key:

    pass
class simpleumltordbms_PrimitiveToName(UmlToRdbmsModelElement):

    def __init__(self, typeName: str, simpleumltordbms_PrimitiveToName: "simpleumltordbms_AttributeToColumn" = None, PrimitiveToName: "simpleumltordbms_PackageToSchema" = None, primitivesToNames: "simpleumltordbms_PackageToSchema" = None, simpleumltordbms_PrimitiveToName33: "simpleumltordbms_PrimitiveDataType" = None):
        self.typeName = typeName
        self.simpleumltordbms_PrimitiveToName = simpleumltordbms_PrimitiveToName
        self.PrimitiveToName = PrimitiveToName
        self.primitivesToNames = primitivesToNames
        self.simpleumltordbms_PrimitiveToName33 = simpleumltordbms_PrimitiveToName33
        
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
        old_value = getattr(self, f"_simpleumltordbms_PrimitiveToName__primitivesToNames", None)
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
    def PrimitiveToName(self):
        return self.__PrimitiveToName

    @PrimitiveToName.setter
    def PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_PrimitiveToName__PrimitiveToName", None)
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
    def simpleumltordbms_PrimitiveToName(self):
        return self.__simpleumltordbms_PrimitiveToName

    @simpleumltordbms_PrimitiveToName.setter
    def simpleumltordbms_PrimitiveToName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_PrimitiveToName__simpleumltordbms_PrimitiveToName", None)
        self.__simpleumltordbms_PrimitiveToName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleumltordbms_AttributeToColumn"):
                opp_val = getattr(old_value, "simpleumltordbms_AttributeToColumn", None)
                if opp_val == self:
                    setattr(old_value, "simpleumltordbms_AttributeToColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleumltordbms_AttributeToColumn"):
                opp_val = getattr(value, "simpleumltordbms_AttributeToColumn", None)
                setattr(value, "simpleumltordbms_AttributeToColumn", self)

    @property
    def simpleumltordbms_PrimitiveToName33(self):
        return self.__simpleumltordbms_PrimitiveToName33

    @simpleumltordbms_PrimitiveToName33.setter
    def simpleumltordbms_PrimitiveToName33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleumltordbms_PrimitiveToName__simpleumltordbms_PrimitiveToName33", None)
        self.__simpleumltordbms_PrimitiveToName33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleumltordbms_PrimitiveDataType"):
                opp_val = getattr(old_value, "simpleumltordbms_PrimitiveDataType", None)
                if opp_val == self:
                    setattr(old_value, "simpleumltordbms_PrimitiveDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleumltordbms_PrimitiveDataType"):
                opp_val = getattr(value, "simpleumltordbms_PrimitiveDataType", None)
                setattr(value, "simpleumltordbms_PrimitiveDataType", self)

class ToColumn:

    pass
class simpleumltordbms_AssociationToForeignKey(ToColumn, UmlToRdbmsModelElement):

    pass
class simpleumltordbms_ClassToTable(FromAttributeOwner, ToColumn, UmlToRdbmsModelElement):

    pass
class FromAttribute:

    pass
class simpleumltordbms_NonLeafAttribute(FromAttributeOwner, FromAttribute):

    pass
class simpleumltordbms_AttributeToColumn(FromAttribute, ToColumn):

    pass