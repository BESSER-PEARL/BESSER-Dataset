from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Graphql_Schema:

    def __init__(self, name: str, Graphql_Schema: set["Graphql_Type"] = None):
        self.name = name
        self.Graphql_Schema = Graphql_Schema if Graphql_Schema is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Graphql_Schema(self):
        return self.__Graphql_Schema

    @Graphql_Schema.setter
    def Graphql_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graphql_Schema__Graphql_Schema", None)
        self.__Graphql_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graphql_Type2"):
                    opp_val = getattr(item, "Graphql_Type2", None)
                    
                    if opp_val == self:
                        setattr(item, "Graphql_Type2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graphql_Type2"):
                    opp_val = getattr(item, "Graphql_Type2", None)
                    
                    setattr(item, "Graphql_Type2", self)
                    

class Graphql_Attribute:

    def __init__(self, name: str, isArray: str, isNullable: str, typeName: str, Graphql_Attribute: "Graphql_Type" = None):
        self.name = name
        self.isArray = isArray
        self.isNullable = isNullable
        self.typeName = typeName
        self.Graphql_Attribute = Graphql_Attribute
        
    @property
    def isArray(self) -> str:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: str):
        self.__isArray = isArray

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isNullable(self) -> str:
        return self.__isNullable

    @isNullable.setter
    def isNullable(self, isNullable: str):
        self.__isNullable = isNullable

    @property
    def Graphql_Attribute(self):
        return self.__Graphql_Attribute

    @Graphql_Attribute.setter
    def Graphql_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graphql_Attribute__Graphql_Attribute", None)
        self.__Graphql_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graphql_Type"):
                opp_val = getattr(old_value, "Graphql_Type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graphql_Type"):
                opp_val = getattr(value, "Graphql_Type", None)
                if opp_val is None:
                    setattr(value, "Graphql_Type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graphql_Type(ABC):

    def __init__(self, name: str, Graphql_Type2: "Graphql_Schema" = None, Graphql_Type: set["Graphql_Attribute"] = None):
        self.name = name
        self.Graphql_Type2 = Graphql_Type2
        self.Graphql_Type = Graphql_Type if Graphql_Type is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Graphql_Type2(self):
        return self.__Graphql_Type2

    @Graphql_Type2.setter
    def Graphql_Type2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graphql_Type__Graphql_Type2", None)
        self.__Graphql_Type2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graphql_Schema"):
                opp_val = getattr(old_value, "Graphql_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graphql_Schema"):
                opp_val = getattr(value, "Graphql_Schema", None)
                if opp_val is None:
                    setattr(value, "Graphql_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Graphql_Type(self):
        return self.__Graphql_Type

    @Graphql_Type.setter
    def Graphql_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graphql_Type__Graphql_Type", None)
        self.__Graphql_Type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graphql_Attribute"):
                    opp_val = getattr(item, "Graphql_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Graphql_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graphql_Attribute"):
                    opp_val = getattr(item, "Graphql_Attribute", None)
                    
                    setattr(item, "Graphql_Attribute", self)
                    

class Graphql_EnumValue:

    def __init__(self, value: str, number: str, Graphql_EnumValue: "Graphql_Enum" = None):
        self.value = value
        self.number = number
        self.Graphql_EnumValue = Graphql_EnumValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def Graphql_EnumValue(self):
        return self.__Graphql_EnumValue

    @Graphql_EnumValue.setter
    def Graphql_EnumValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graphql_EnumValue__Graphql_EnumValue", None)
        self.__Graphql_EnumValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graphql_Enum"):
                opp_val = getattr(old_value, "Graphql_Enum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graphql_Enum"):
                opp_val = getattr(value, "Graphql_Enum", None)
                if opp_val is None:
                    setattr(value, "Graphql_Enum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ScalarType:

    pass
class Graphql_ID(ScalarType):

    pass
class Graphql_String(ScalarType):

    pass
class Graphql_Boolean(ScalarType):

    pass
class Graphql_Float(ScalarType):

    pass
class Graphql_Int(ScalarType):

    pass
class Type:

    pass
class Graphql_Enum(Type):

    pass
class Graphql_SystemType(Type):

    pass
class Graphql_ScalarType(Type):

    pass