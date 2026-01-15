from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class InternalDSLType(Enum):
    NestedFunctions = "NestedFunctions"
class DataTypes(Enum):
    String = "String"
    Integer = "Integer"
    Boolean = "Boolean"
    Long = "Long"
    Double = "Double"


############################################
# Definition of Classes
############################################

class titan_Entity:

    def __init__(self, name: str, titan_Entity7: set["titan_Feature"] = None, titan_Entity9: "titan_Reference" = None, titan_Entity: "titan_Package" = None, titan_Entity5: "titan_Entity" = None, titan_Entity3: "titan_Entity" = None):
        self.name = name
        self.titan_Entity7 = titan_Entity7 if titan_Entity7 is not None else set()
        self.titan_Entity9 = titan_Entity9
        self.titan_Entity = titan_Entity
        self.titan_Entity5 = titan_Entity5
        self.titan_Entity3 = titan_Entity3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def titan_Entity(self):
        return self.__titan_Entity

    @titan_Entity.setter
    def titan_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Entity__titan_Entity", None)
        self.__titan_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Package2"):
                opp_val = getattr(old_value, "titan_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Package2"):
                opp_val = getattr(value, "titan_Package2", None)
                if opp_val is None:
                    setattr(value, "titan_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def titan_Entity3(self):
        return self.__titan_Entity3

    @titan_Entity3.setter
    def titan_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Entity__titan_Entity3", None)
        self.__titan_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Entity5"):
                opp_val = getattr(old_value, "titan_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "titan_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Entity5"):
                opp_val = getattr(value, "titan_Entity5", None)
                setattr(value, "titan_Entity5", self)

    @property
    def titan_Entity9(self):
        return self.__titan_Entity9

    @titan_Entity9.setter
    def titan_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Entity__titan_Entity9", None)
        self.__titan_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Reference"):
                opp_val = getattr(old_value, "titan_Reference", None)
                if opp_val == self:
                    setattr(old_value, "titan_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Reference"):
                opp_val = getattr(value, "titan_Reference", None)
                setattr(value, "titan_Reference", self)

    @property
    def titan_Entity7(self):
        return self.__titan_Entity7

    @titan_Entity7.setter
    def titan_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Entity__titan_Entity7", None)
        self.__titan_Entity7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "titan_Feature"):
                    opp_val = getattr(item, "titan_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "titan_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "titan_Feature"):
                    opp_val = getattr(item, "titan_Feature", None)
                    
                    setattr(item, "titan_Feature", self)
                    

    @property
    def titan_Entity5(self):
        return self.__titan_Entity5

    @titan_Entity5.setter
    def titan_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Entity__titan_Entity5", None)
        self.__titan_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Entity3"):
                opp_val = getattr(old_value, "titan_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "titan_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Entity3"):
                opp_val = getattr(value, "titan_Entity3", None)
                setattr(value, "titan_Entity3", self)

class DataType:

    pass
class titan_SingleDataType(DataType):

    pass
class titan_MultiDataType(DataType):

    def __init__(self, unique: bool, titan_MultiDataType: "titan_DataType" = None):
        self.unique = unique
        self.titan_MultiDataType = titan_MultiDataType
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def titan_MultiDataType(self):
        return self.__titan_MultiDataType

    @titan_MultiDataType.setter
    def titan_MultiDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_MultiDataType__titan_MultiDataType", None)
        self.__titan_MultiDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_DataType"):
                opp_val = getattr(old_value, "titan_DataType", None)
                if opp_val == self:
                    setattr(old_value, "titan_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_DataType"):
                opp_val = getattr(value, "titan_DataType", None)
                setattr(value, "titan_DataType", self)

class Reference:

    pass
class titan_SingleReference(Reference):

    pass
class titan_MultiReference(Reference):

    pass
class Feature:

    pass
class titan_DataType(Feature):

    def __init__(self, type: str, titan_DataType: "titan_MultiDataType" = None):
        self.type = type
        self.titan_DataType = titan_DataType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def titan_DataType(self):
        return self.__titan_DataType

    @titan_DataType.setter
    def titan_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_DataType__titan_DataType", None)
        self.__titan_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_MultiDataType"):
                opp_val = getattr(old_value, "titan_MultiDataType", None)
                if opp_val == self:
                    setattr(old_value, "titan_MultiDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_MultiDataType"):
                opp_val = getattr(value, "titan_MultiDataType", None)
                setattr(value, "titan_MultiDataType", self)

class titan_Reference(Feature):

    def __init__(self, unique: bool, titan_Reference: "titan_Entity" = None, titan_Reference11: "titan_MultiReference" = None):
        self.unique = unique
        self.titan_Reference = titan_Reference
        self.titan_Reference11 = titan_Reference11
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def titan_Reference(self):
        return self.__titan_Reference

    @titan_Reference.setter
    def titan_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Reference__titan_Reference", None)
        self.__titan_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Entity9"):
                opp_val = getattr(old_value, "titan_Entity9", None)
                if opp_val == self:
                    setattr(old_value, "titan_Entity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Entity9"):
                opp_val = getattr(value, "titan_Entity9", None)
                setattr(value, "titan_Entity9", self)

    @property
    def titan_Reference11(self):
        return self.__titan_Reference11

    @titan_Reference11.setter
    def titan_Reference11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Reference__titan_Reference11", None)
        self.__titan_Reference11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_MultiReference"):
                opp_val = getattr(old_value, "titan_MultiReference", None)
                if opp_val == self:
                    setattr(old_value, "titan_MultiReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_MultiReference"):
                opp_val = getattr(value, "titan_MultiReference", None)
                setattr(value, "titan_MultiReference", self)

class titan_Feature:

    def __init__(self, name: str, titan_Feature: "titan_Entity" = None):
        self.name = name
        self.titan_Feature = titan_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def titan_Feature(self):
        return self.__titan_Feature

    @titan_Feature.setter
    def titan_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Feature__titan_Feature", None)
        self.__titan_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Entity7"):
                opp_val = getattr(old_value, "titan_Entity7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Entity7"):
                opp_val = getattr(value, "titan_Entity7", None)
                if opp_val is None:
                    setattr(value, "titan_Entity7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class titan_Package:

    def __init__(self, name: str, titan_Package: "titan_Module" = None, titan_Package2: set["titan_Entity"] = None):
        self.name = name
        self.titan_Package = titan_Package
        self.titan_Package2 = titan_Package2 if titan_Package2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def titan_Package(self):
        return self.__titan_Package

    @titan_Package.setter
    def titan_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Package__titan_Package", None)
        self.__titan_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "titan_Module"):
                opp_val = getattr(old_value, "titan_Module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "titan_Module"):
                opp_val = getattr(value, "titan_Module", None)
                if opp_val is None:
                    setattr(value, "titan_Module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def titan_Package2(self):
        return self.__titan_Package2

    @titan_Package2.setter
    def titan_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Package__titan_Package2", None)
        self.__titan_Package2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "titan_Entity"):
                    opp_val = getattr(item, "titan_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "titan_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "titan_Entity"):
                    opp_val = getattr(item, "titan_Entity", None)
                    
                    setattr(item, "titan_Entity", self)
                    

class titan_Module:

    def __init__(self, name: str, type: str, titan_Module: set["titan_Package"] = None):
        self.name = name
        self.type = type
        self.titan_Module = titan_Module if titan_Module is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def titan_Module(self):
        return self.__titan_Module

    @titan_Module.setter
    def titan_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_titan_Module__titan_Module", None)
        self.__titan_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "titan_Package"):
                    opp_val = getattr(item, "titan_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "titan_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "titan_Package"):
                    opp_val = getattr(item, "titan_Package", None)
                    
                    setattr(item, "titan_Package", self)
                    
