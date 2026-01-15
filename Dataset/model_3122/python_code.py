from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ModifierType(Enum):
    abstract = "abstract"
    final = "final"
    static = "static"
    public = "public"
    private = "private"
    protected = "protected"


############################################
# Definition of Classes
############################################

class class_diagramm_RefPackage(ABC):

    pass
class class_diagramm_RefMethod(ABC):

    pass
class RefAssociation:

    pass
class class_diagramm_Association(RefAssociation):

    def __init__(self, minCardinality: int, maxCardinality: int, name: str, isAggregation: bool, class_diagramm_Association: "class_diagramm_RefClass" = None, class_diagramm_Association28: "class_diagramm_RefClass" = None):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        self.name = name
        self.isAggregation = isAggregation
        self.class_diagramm_Association = class_diagramm_Association
        self.class_diagramm_Association28 = class_diagramm_Association28
        
    @property
    def minCardinality(self) -> int:
        return self.__minCardinality

    @minCardinality.setter
    def minCardinality(self, minCardinality: int):
        self.__minCardinality = minCardinality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def maxCardinality(self) -> int:
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality

    @property
    def isAggregation(self) -> bool:
        return self.__isAggregation

    @isAggregation.setter
    def isAggregation(self, isAggregation: bool):
        self.__isAggregation = isAggregation

    @property
    def class_diagramm_Association28(self):
        return self.__class_diagramm_Association28

    @class_diagramm_Association28.setter
    def class_diagramm_Association28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Association__class_diagramm_Association28", None)
        self.__class_diagramm_Association28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass29"):
                opp_val = getattr(old_value, "class_diagramm_RefClass29", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass29"):
                opp_val = getattr(value, "class_diagramm_RefClass29", None)
                setattr(value, "class_diagramm_RefClass29", self)

    @property
    def class_diagramm_Association(self):
        return self.__class_diagramm_Association

    @class_diagramm_Association.setter
    def class_diagramm_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Association__class_diagramm_Association", None)
        self.__class_diagramm_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass26"):
                opp_val = getattr(old_value, "class_diagramm_RefClass26", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass26"):
                opp_val = getattr(value, "class_diagramm_RefClass26", None)
                setattr(value, "class_diagramm_RefClass26", self)

class RefParameter:

    pass
class class_diagramm_Parameter(RefParameter):

    def __init__(self, name: str, class_diagramm_Parameter: "class_diagramm_RefClass" = None, class_diagramm_Parameter17: "class_diagramm_RefDataType" = None):
        self.name = name
        self.class_diagramm_Parameter = class_diagramm_Parameter
        self.class_diagramm_Parameter17 = class_diagramm_Parameter17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class_diagramm_Parameter17(self):
        return self.__class_diagramm_Parameter17

    @class_diagramm_Parameter17.setter
    def class_diagramm_Parameter17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Parameter__class_diagramm_Parameter17", None)
        self.__class_diagramm_Parameter17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefDataType18"):
                opp_val = getattr(old_value, "class_diagramm_RefDataType18", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefDataType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefDataType18"):
                opp_val = getattr(value, "class_diagramm_RefDataType18", None)
                setattr(value, "class_diagramm_RefDataType18", self)

    @property
    def class_diagramm_Parameter(self):
        return self.__class_diagramm_Parameter

    @class_diagramm_Parameter.setter
    def class_diagramm_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Parameter__class_diagramm_Parameter", None)
        self.__class_diagramm_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass15"):
                opp_val = getattr(old_value, "class_diagramm_RefClass15", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass15"):
                opp_val = getattr(value, "class_diagramm_RefClass15", None)
                setattr(value, "class_diagramm_RefClass15", self)

class class_diagramm_RefAttribute(ABC):

    pass
class RefClass:

    pass
class class_diagramm_Class(RefClass):

    def __init__(self, modifier: str, name: str, class_diagramm_Class: "class_diagramm_RefClass" = None, class_diagramm_Class22: set["class_diagramm_RefAttribute"] = None, class_diagramm_Class24: set["class_diagramm_RefMethod"] = None):
        self.modifier = modifier
        self.name = name
        self.class_diagramm_Class = class_diagramm_Class
        self.class_diagramm_Class22 = class_diagramm_Class22 if class_diagramm_Class22 is not None else set()
        self.class_diagramm_Class24 = class_diagramm_Class24 if class_diagramm_Class24 is not None else set()
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class_diagramm_Class(self):
        return self.__class_diagramm_Class

    @class_diagramm_Class.setter
    def class_diagramm_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Class__class_diagramm_Class", None)
        self.__class_diagramm_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass20"):
                opp_val = getattr(old_value, "class_diagramm_RefClass20", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass20"):
                opp_val = getattr(value, "class_diagramm_RefClass20", None)
                setattr(value, "class_diagramm_RefClass20", self)

    @property
    def class_diagramm_Class24(self):
        return self.__class_diagramm_Class24

    @class_diagramm_Class24.setter
    def class_diagramm_Class24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Class__class_diagramm_Class24", None)
        self.__class_diagramm_Class24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_diagramm_RefMethod"):
                    opp_val = getattr(item, "class_diagramm_RefMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "class_diagramm_RefMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_diagramm_RefMethod"):
                    opp_val = getattr(item, "class_diagramm_RefMethod", None)
                    
                    setattr(item, "class_diagramm_RefMethod", self)
                    

    @property
    def class_diagramm_Class22(self):
        return self.__class_diagramm_Class22

    @class_diagramm_Class22.setter
    def class_diagramm_Class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Class__class_diagramm_Class22", None)
        self.__class_diagramm_Class22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_diagramm_RefAttribute"):
                    opp_val = getattr(item, "class_diagramm_RefAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "class_diagramm_RefAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_diagramm_RefAttribute"):
                    opp_val = getattr(item, "class_diagramm_RefAttribute", None)
                    
                    setattr(item, "class_diagramm_RefAttribute", self)
                    

class class_diagramm_RefParameter(ABC):

    pass
class RefAttribute:

    pass
class class_diagramm_Attribute(RefAttribute):

    def __init__(self, name: str, modifier: str, class_diagramm_Attribute: "class_diagramm_RefClass" = None, class_diagramm_Attribute12: "class_diagramm_RefDataType" = None):
        self.name = name
        self.modifier = modifier
        self.class_diagramm_Attribute = class_diagramm_Attribute
        self.class_diagramm_Attribute12 = class_diagramm_Attribute12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def class_diagramm_Attribute(self):
        return self.__class_diagramm_Attribute

    @class_diagramm_Attribute.setter
    def class_diagramm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Attribute__class_diagramm_Attribute", None)
        self.__class_diagramm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass10"):
                opp_val = getattr(old_value, "class_diagramm_RefClass10", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass10"):
                opp_val = getattr(value, "class_diagramm_RefClass10", None)
                setattr(value, "class_diagramm_RefClass10", self)

    @property
    def class_diagramm_Attribute12(self):
        return self.__class_diagramm_Attribute12

    @class_diagramm_Attribute12.setter
    def class_diagramm_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Attribute__class_diagramm_Attribute12", None)
        self.__class_diagramm_Attribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefDataType13"):
                opp_val = getattr(old_value, "class_diagramm_RefDataType13", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefDataType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefDataType13"):
                opp_val = getattr(value, "class_diagramm_RefDataType13", None)
                setattr(value, "class_diagramm_RefDataType13", self)

class class_diagramm_RefDataType(ABC):

    pass
class class_diagramm_RefAssociation(ABC):

    pass
class RefPackage:

    pass
class class_diagramm_Package(RefPackage):

    def __init__(self, name: str, class_diagramm_Package2: set["class_diagramm_RefClass"] = None, class_diagramm_Package: set["class_diagramm_RefAssociation"] = None):
        self.name = name
        self.class_diagramm_Package2 = class_diagramm_Package2 if class_diagramm_Package2 is not None else set()
        self.class_diagramm_Package = class_diagramm_Package if class_diagramm_Package is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class_diagramm_Package2(self):
        return self.__class_diagramm_Package2

    @class_diagramm_Package2.setter
    def class_diagramm_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Package__class_diagramm_Package2", None)
        self.__class_diagramm_Package2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_diagramm_RefClass"):
                    opp_val = getattr(item, "class_diagramm_RefClass", None)
                    
                    if opp_val == self:
                        setattr(item, "class_diagramm_RefClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_diagramm_RefClass"):
                    opp_val = getattr(item, "class_diagramm_RefClass", None)
                    
                    setattr(item, "class_diagramm_RefClass", self)
                    

    @property
    def class_diagramm_Package(self):
        return self.__class_diagramm_Package

    @class_diagramm_Package.setter
    def class_diagramm_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Package__class_diagramm_Package", None)
        self.__class_diagramm_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_diagramm_RefAssociation"):
                    opp_val = getattr(item, "class_diagramm_RefAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "class_diagramm_RefAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_diagramm_RefAssociation"):
                    opp_val = getattr(item, "class_diagramm_RefAssociation", None)
                    
                    setattr(item, "class_diagramm_RefAssociation", self)
                    

class RefMethod:

    pass
class class_diagramm_Method(RefMethod):

    def __init__(self, name: str, modifier: str, class_diagramm_Method8: "class_diagramm_RefDataType" = None, class_diagramm_Method: "class_diagramm_RefClass" = None, class_diagramm_Method6: set["class_diagramm_RefParameter"] = None):
        self.name = name
        self.modifier = modifier
        self.class_diagramm_Method8 = class_diagramm_Method8
        self.class_diagramm_Method = class_diagramm_Method
        self.class_diagramm_Method6 = class_diagramm_Method6 if class_diagramm_Method6 is not None else set()
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class_diagramm_Method(self):
        return self.__class_diagramm_Method

    @class_diagramm_Method.setter
    def class_diagramm_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Method__class_diagramm_Method", None)
        self.__class_diagramm_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefClass4"):
                opp_val = getattr(old_value, "class_diagramm_RefClass4", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefClass4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefClass4"):
                opp_val = getattr(value, "class_diagramm_RefClass4", None)
                setattr(value, "class_diagramm_RefClass4", self)

    @property
    def class_diagramm_Method6(self):
        return self.__class_diagramm_Method6

    @class_diagramm_Method6.setter
    def class_diagramm_Method6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Method__class_diagramm_Method6", None)
        self.__class_diagramm_Method6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "class_diagramm_RefParameter"):
                    opp_val = getattr(item, "class_diagramm_RefParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "class_diagramm_RefParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "class_diagramm_RefParameter"):
                    opp_val = getattr(item, "class_diagramm_RefParameter", None)
                    
                    setattr(item, "class_diagramm_RefParameter", self)
                    

    @property
    def class_diagramm_Method8(self):
        return self.__class_diagramm_Method8

    @class_diagramm_Method8.setter
    def class_diagramm_Method8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_class_diagramm_Method__class_diagramm_Method8", None)
        self.__class_diagramm_Method8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class_diagramm_RefDataType"):
                opp_val = getattr(old_value, "class_diagramm_RefDataType", None)
                if opp_val == self:
                    setattr(old_value, "class_diagramm_RefDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class_diagramm_RefDataType"):
                opp_val = getattr(value, "class_diagramm_RefDataType", None)
                setattr(value, "class_diagramm_RefDataType", self)

class RefDataType:

    pass
class class_diagramm_DataType(RefDataType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class class_diagramm_RefClass(ABC):

    pass