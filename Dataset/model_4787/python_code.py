from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OpenDDSLib:

    pass
class types_DataLib(OpenDDSLib):

    pass
class UnsignedInt:

    pass
class types_UShort(UnsignedInt):

    pass
class types_ULongLong(UnsignedInt):

    pass
class types_ULong(UnsignedInt):

    pass
class SignedInt:

    pass
class types_Long(SignedInt):

    pass
class types_Key:

    pass
class FloatingPoint:

    pass
class types_Float(FloatingPoint):

    pass
class types_Double(FloatingPoint):

    pass
class Type:

    pass
class types_Struct(Type):

    def __init__(self, name: str, isDcpsDataType: bool, types_Struct: set["types_Field"] = None, types_Struct14: set["types_Key"] = None):
        self.name = name
        self.isDcpsDataType = isDcpsDataType
        self.types_Struct = types_Struct if types_Struct is not None else set()
        self.types_Struct14 = types_Struct14 if types_Struct14 is not None else set()
        
    @property
    def isDcpsDataType(self) -> bool:
        return self.__isDcpsDataType

    @isDcpsDataType.setter
    def isDcpsDataType(self, isDcpsDataType: bool):
        self.__isDcpsDataType = isDcpsDataType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Struct14(self):
        return self.__types_Struct14

    @types_Struct14.setter
    def types_Struct14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Struct__types_Struct14", None)
        self.__types_Struct14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Key15"):
                    opp_val = getattr(item, "types_Key15", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Key15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Key15"):
                    opp_val = getattr(item, "types_Key15", None)
                    
                    setattr(item, "types_Key15", self)
                    

    @property
    def types_Struct(self):
        return self.__types_Struct

    @types_Struct.setter
    def types_Struct(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Struct__types_Struct", None)
        self.__types_Struct = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Field12"):
                    opp_val = getattr(item, "types_Field12", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Field12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Field12"):
                    opp_val = getattr(item, "types_Field12", None)
                    
                    setattr(item, "types_Field12", self)
                    

class types_Union(Type):

    def __init__(self, name: str, types_Union: set["types_Branch"] = None, types_Union21: "types_Type" = None, types_Union24: "types_Field" = None):
        self.name = name
        self.types_Union = types_Union if types_Union is not None else set()
        self.types_Union21 = types_Union21
        self.types_Union24 = types_Union24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Union(self):
        return self.__types_Union

    @types_Union.setter
    def types_Union(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Union__types_Union", None)
        self.__types_Union = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Branch19"):
                    opp_val = getattr(item, "types_Branch19", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Branch19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Branch19"):
                    opp_val = getattr(item, "types_Branch19", None)
                    
                    setattr(item, "types_Branch19", self)
                    

    @property
    def types_Union21(self):
        return self.__types_Union21

    @types_Union21.setter
    def types_Union21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Union__types_Union21", None)
        self.__types_Union21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type22"):
                opp_val = getattr(old_value, "types_Type22", None)
                if opp_val == self:
                    setattr(old_value, "types_Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type22"):
                opp_val = getattr(value, "types_Type22", None)
                setattr(value, "types_Type22", self)

    @property
    def types_Union24(self):
        return self.__types_Union24

    @types_Union24.setter
    def types_Union24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Union__types_Union24", None)
        self.__types_Union24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Field25"):
                opp_val = getattr(old_value, "types_Field25", None)
                if opp_val == self:
                    setattr(old_value, "types_Field25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Field25"):
                opp_val = getattr(value, "types_Field25", None)
                setattr(value, "types_Field25", self)

class types_Typedef(Type):

    def __init__(self, name: str, types_Typedef: "types_Type" = None):
        self.name = name
        self.types_Typedef = types_Typedef
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Typedef(self):
        return self.__types_Typedef

    @types_Typedef.setter
    def types_Typedef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Typedef__types_Typedef", None)
        self.__types_Typedef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type17"):
                opp_val = getattr(old_value, "types_Type17", None)
                if opp_val == self:
                    setattr(old_value, "types_Type17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type17"):
                opp_val = getattr(value, "types_Type17", None)
                setattr(value, "types_Type17", self)

class types_Collection(Type):

    def __init__(self, length: str):
        self.length = length
        
    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

class types_Case:

    def __init__(self, literal: str, types_Case: "types_Branch" = None):
        self.literal = literal
        self.types_Case = types_Case
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def types_Case(self):
        return self.__types_Case

    @types_Case.setter
    def types_Case(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Case__types_Case", None)
        self.__types_Case = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Branch3"):
                opp_val = getattr(old_value, "types_Branch3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Branch3"):
                opp_val = getattr(value, "types_Branch3", None)
                if opp_val is None:
                    setattr(value, "types_Branch3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Field:

    def __init__(self, name: str, types_Field: "types_Branch" = None, types_Field5: "types_Type" = None, types_Field8: "types_Key" = None, types_Field12: "types_Struct" = None, types_Field25: "types_Union" = None):
        self.name = name
        self.types_Field = types_Field
        self.types_Field5 = types_Field5
        self.types_Field8 = types_Field8
        self.types_Field12 = types_Field12
        self.types_Field25 = types_Field25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Field25(self):
        return self.__types_Field25

    @types_Field25.setter
    def types_Field25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Field__types_Field25", None)
        self.__types_Field25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Union24"):
                opp_val = getattr(old_value, "types_Union24", None)
                if opp_val == self:
                    setattr(old_value, "types_Union24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Union24"):
                opp_val = getattr(value, "types_Union24", None)
                setattr(value, "types_Union24", self)

    @property
    def types_Field(self):
        return self.__types_Field

    @types_Field.setter
    def types_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Field__types_Field", None)
        self.__types_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Branch"):
                opp_val = getattr(old_value, "types_Branch", None)
                if opp_val == self:
                    setattr(old_value, "types_Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Branch"):
                opp_val = getattr(value, "types_Branch", None)
                setattr(value, "types_Branch", self)

    @property
    def types_Field12(self):
        return self.__types_Field12

    @types_Field12.setter
    def types_Field12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Field__types_Field12", None)
        self.__types_Field12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Struct"):
                opp_val = getattr(old_value, "types_Struct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Struct"):
                opp_val = getattr(value, "types_Struct", None)
                if opp_val is None:
                    setattr(value, "types_Struct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Field8(self):
        return self.__types_Field8

    @types_Field8.setter
    def types_Field8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Field__types_Field8", None)
        self.__types_Field8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Key"):
                opp_val = getattr(old_value, "types_Key", None)
                if opp_val == self:
                    setattr(old_value, "types_Key", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Key"):
                opp_val = getattr(value, "types_Key", None)
                setattr(value, "types_Key", self)

    @property
    def types_Field5(self):
        return self.__types_Field5

    @types_Field5.setter
    def types_Field5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Field__types_Field5", None)
        self.__types_Field5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type6"):
                opp_val = getattr(old_value, "types_Type6", None)
                if opp_val == self:
                    setattr(old_value, "types_Type6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type6"):
                opp_val = getattr(value, "types_Type6", None)
                setattr(value, "types_Type6", self)

class types_Branch:

    pass
class Simple:

    pass
class types_Enum(Simple):

    def __init__(self, name: str, literals: str):
        self.name = name
        self.literals = literals
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def literals(self) -> str:
        return self.__literals

    @literals.setter
    def literals(self, literals: str):
        self.__literals = literals

class types_FloatingPoint(Simple):

    pass
class types_Char(Simple):

    pass
class types_Int(Simple):

    pass
class types_WChar(Simple):

    pass
class types_Boolean(Simple):

    pass
class types_Simple(Type):

    pass
class Int:

    pass
class types_UnsignedInt(Int):

    pass
class types_SignedInt(Int):

    pass
class types_Short(SignedInt):

    pass
class types_Octet(Simple):

    pass
class types_LongLong(SignedInt):

    pass
class types_LongDouble(FloatingPoint):

    pass
class types_Type(ABC):

    pass
class Collection:

    pass
class types_Sequence(Collection):

    pass
class types_WString(Collection):

    pass
class types_String(Collection):

    pass
class types_Array(Collection):

    pass