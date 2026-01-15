from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class datatypes_Field:

    def __init__(self, measureUnit: str, name: str, description: str, datatypes_Field: "datatypes_CustomType" = None, datatypes_Field7: "datatypes_DataType" = None):
        self.measureUnit = measureUnit
        self.name = name
        self.description = description
        self.datatypes_Field = datatypes_Field
        self.datatypes_Field7 = datatypes_Field7
        
    @property
    def measureUnit(self) -> str:
        return self.__measureUnit

    @measureUnit.setter
    def measureUnit(self, measureUnit: str):
        self.__measureUnit = measureUnit

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatypes_Field(self):
        return self.__datatypes_Field

    @datatypes_Field.setter
    def datatypes_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_Field__datatypes_Field", None)
        self.__datatypes_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_CustomType"):
                opp_val = getattr(old_value, "datatypes_CustomType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_CustomType"):
                opp_val = getattr(value, "datatypes_CustomType", None)
                if opp_val is None:
                    setattr(value, "datatypes_CustomType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datatypes_Field7(self):
        return self.__datatypes_Field7

    @datatypes_Field7.setter
    def datatypes_Field7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_Field__datatypes_Field7", None)
        self.__datatypes_Field7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_DataType8"):
                opp_val = getattr(old_value, "datatypes_DataType8", None)
                if opp_val == self:
                    setattr(old_value, "datatypes_DataType8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_DataType8"):
                opp_val = getattr(value, "datatypes_DataType8", None)
                setattr(value, "datatypes_DataType8", self)

class ComplexType:

    pass
class datatypes_CustomType(ComplexType):

    pass
class datatypes_VectorType(ComplexType):

    pass
class datatypes_IDLReference(ComplexType):

    pass
class datatypes_DataType(ABC):

    def __init__(self, name: str, DataType: "datatypes_TypesLibrary" = None, types: "datatypes_TypesLibrary" = None, datatypes_DataType: "datatypes_VectorType" = None, datatypes_DataType8: "datatypes_Field" = None):
        self.name = name
        self.DataType = DataType
        self.types = types
        self.datatypes_DataType = datatypes_DataType
        self.datatypes_DataType8 = datatypes_DataType8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataType__DataType", None)
        self.__DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typesLibrary"):
                opp_val = getattr(old_value, "typesLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typesLibrary"):
                opp_val = getattr(value, "typesLibrary", None)
                if opp_val is None:
                    setattr(value, "typesLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datatypes_DataType8(self):
        return self.__datatypes_DataType8

    @datatypes_DataType8.setter
    def datatypes_DataType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataType__datatypes_DataType8", None)
        self.__datatypes_DataType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_Field7"):
                opp_val = getattr(old_value, "datatypes_Field7", None)
                if opp_val == self:
                    setattr(old_value, "datatypes_Field7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_Field7"):
                opp_val = getattr(value, "datatypes_Field7", None)
                setattr(value, "datatypes_Field7", self)

    @property
    def datatypes_DataType(self):
        return self.__datatypes_DataType

    @datatypes_DataType.setter
    def datatypes_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataType__datatypes_DataType", None)
        self.__datatypes_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_VectorType"):
                opp_val = getattr(old_value, "datatypes_VectorType", None)
                if opp_val == self:
                    setattr(old_value, "datatypes_VectorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_VectorType"):
                opp_val = getattr(value, "datatypes_VectorType", None)
                setattr(value, "datatypes_VectorType", self)

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_DataType__types", None)
        self.__types = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypesLibrary"):
                opp_val = getattr(old_value, "TypesLibrary", None)
                if opp_val == self:
                    setattr(old_value, "TypesLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypesLibrary"):
                opp_val = getattr(value, "TypesLibrary", None)
                setattr(value, "TypesLibrary", self)

class datatypes_TypesLibrary:

    def __init__(self, name: str, typesLibrary: set["datatypes_DataType"] = None, datatypes_TypesLibrary: "datatypes_TypesLibrary" = None, datatypes_TypesLibrary1: set["datatypes_TypesLibrary"] = None, TypesLibrary: "datatypes_DataType" = None):
        self.name = name
        self.typesLibrary = typesLibrary if typesLibrary is not None else set()
        self.datatypes_TypesLibrary = datatypes_TypesLibrary
        self.datatypes_TypesLibrary1 = datatypes_TypesLibrary1 if datatypes_TypesLibrary1 is not None else set()
        self.TypesLibrary = TypesLibrary
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def datatypes_TypesLibrary(self):
        return self.__datatypes_TypesLibrary

    @datatypes_TypesLibrary.setter
    def datatypes_TypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_TypesLibrary__datatypes_TypesLibrary", None)
        self.__datatypes_TypesLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "datatypes_TypesLibrary1"):
                opp_val = getattr(old_value, "datatypes_TypesLibrary1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "datatypes_TypesLibrary1"):
                opp_val = getattr(value, "datatypes_TypesLibrary1", None)
                if opp_val is None:
                    setattr(value, "datatypes_TypesLibrary1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def datatypes_TypesLibrary1(self):
        return self.__datatypes_TypesLibrary1

    @datatypes_TypesLibrary1.setter
    def datatypes_TypesLibrary1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_TypesLibrary__datatypes_TypesLibrary1", None)
        self.__datatypes_TypesLibrary1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "datatypes_TypesLibrary"):
                    opp_val = getattr(item, "datatypes_TypesLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "datatypes_TypesLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "datatypes_TypesLibrary"):
                    opp_val = getattr(item, "datatypes_TypesLibrary", None)
                    
                    setattr(item, "datatypes_TypesLibrary", self)
                    

    @property
    def TypesLibrary(self):
        return self.__TypesLibrary

    @TypesLibrary.setter
    def TypesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_TypesLibrary__TypesLibrary", None)
        self.__TypesLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types"):
                opp_val = getattr(old_value, "types", None)
                if opp_val == self:
                    setattr(old_value, "types", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types"):
                opp_val = getattr(value, "types", None)
                setattr(value, "types", self)

    @property
    def typesLibrary(self):
        return self.__typesLibrary

    @typesLibrary.setter
    def typesLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_datatypes_TypesLibrary__typesLibrary", None)
        self.__typesLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType"):
                    opp_val = getattr(item, "DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType"):
                    opp_val = getattr(item, "DataType", None)
                    
                    setattr(item, "DataType", self)
                    

class IDLReference:

    pass
class datatypes_RosIDLReference(IDLReference):

    def __init__(self, namespace: str, rosPackage: str):
        self.namespace = namespace
        self.rosPackage = rosPackage
        
    @property
    def rosPackage(self) -> str:
        return self.__rosPackage

    @rosPackage.setter
    def rosPackage(self, rosPackage: str):
        self.__rosPackage = rosPackage

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

class DataType:

    pass
class datatypes_ComplexType(DataType):

    def __init__(self):
        
    def getLabel(self) -> str:
        # TODO: Implement getLabel method
        pass

class datatypes_SimpleType(DataType):

    pass