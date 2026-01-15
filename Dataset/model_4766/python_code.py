from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class types_EEnum:

    pass
class FunctionType:

    pass
class types_MethodType(FunctionType):

    pass
class RealType:

    pass
class types_IntegerType(RealType):

    pass
class DataType:

    pass
class types_NumberType(DataType):

    pass
class types_BooleanType(DataType):

    pass
class Type:

    pass
class types_EnumType(Type):

    pass
class types_DataType(Type):

    pass
class types_Type:

    def __init__(self, inExtentDomain: bool, types_Type: "types_CollectionType" = None, types_Type3: "types_MapType" = None, types_Type6: "types_MapType" = None, types_Type8: "types_FunctionType" = None, types_Type11: "types_FunctionType" = None, types_Type13: "types_MethodType" = None):
        self.inExtentDomain = inExtentDomain
        self.types_Type = types_Type
        self.types_Type3 = types_Type3
        self.types_Type6 = types_Type6
        self.types_Type8 = types_Type8
        self.types_Type11 = types_Type11
        self.types_Type13 = types_Type13
        
    @property
    def inExtentDomain(self) -> bool:
        return self.__inExtentDomain

    @inExtentDomain.setter
    def inExtentDomain(self, inExtentDomain: bool):
        self.__inExtentDomain = inExtentDomain

    @property
    def types_Type13(self):
        return self.__types_Type13

    @types_Type13.setter
    def types_Type13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type13", None)
        self.__types_Type13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MethodType"):
                opp_val = getattr(old_value, "types_MethodType", None)
                if opp_val == self:
                    setattr(old_value, "types_MethodType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MethodType"):
                opp_val = getattr(value, "types_MethodType", None)
                setattr(value, "types_MethodType", self)

    @property
    def types_Type8(self):
        return self.__types_Type8

    @types_Type8.setter
    def types_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type8", None)
        self.__types_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_FunctionType"):
                opp_val = getattr(old_value, "types_FunctionType", None)
                if opp_val == self:
                    setattr(old_value, "types_FunctionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_FunctionType"):
                opp_val = getattr(value, "types_FunctionType", None)
                setattr(value, "types_FunctionType", self)

    @property
    def types_Type6(self):
        return self.__types_Type6

    @types_Type6.setter
    def types_Type6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type6", None)
        self.__types_Type6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MapType5"):
                opp_val = getattr(old_value, "types_MapType5", None)
                if opp_val == self:
                    setattr(old_value, "types_MapType5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MapType5"):
                opp_val = getattr(value, "types_MapType5", None)
                setattr(value, "types_MapType5", self)

    @property
    def types_Type3(self):
        return self.__types_Type3

    @types_Type3.setter
    def types_Type3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type3", None)
        self.__types_Type3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MapType"):
                opp_val = getattr(old_value, "types_MapType", None)
                if opp_val == self:
                    setattr(old_value, "types_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MapType"):
                opp_val = getattr(value, "types_MapType", None)
                setattr(value, "types_MapType", self)

    @property
    def types_Type11(self):
        return self.__types_Type11

    @types_Type11.setter
    def types_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type11", None)
        self.__types_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_FunctionType10"):
                opp_val = getattr(old_value, "types_FunctionType10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_FunctionType10"):
                opp_val = getattr(value, "types_FunctionType10", None)
                if opp_val is None:
                    setattr(value, "types_FunctionType10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Type(self):
        return self.__types_Type

    @types_Type.setter
    def types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type", None)
        self.__types_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_CollectionType"):
                opp_val = getattr(old_value, "types_CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "types_CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_CollectionType"):
                opp_val = getattr(value, "types_CollectionType", None)
                setattr(value, "types_CollectionType", self)

class types_FunctionType(Type):

    def __init__(self, optionalParameterCount: int, types_FunctionType: "types_Type" = None, types_FunctionType10: set["types_Type"] = None):
        self.optionalParameterCount = optionalParameterCount
        self.types_FunctionType = types_FunctionType
        self.types_FunctionType10 = types_FunctionType10 if types_FunctionType10 is not None else set()
        
    @property
    def optionalParameterCount(self) -> int:
        return self.__optionalParameterCount

    @optionalParameterCount.setter
    def optionalParameterCount(self, optionalParameterCount: int):
        self.__optionalParameterCount = optionalParameterCount

    @property
    def types_FunctionType(self):
        return self.__types_FunctionType

    @types_FunctionType.setter
    def types_FunctionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_FunctionType__types_FunctionType", None)
        self.__types_FunctionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type8"):
                opp_val = getattr(old_value, "types_Type8", None)
                if opp_val == self:
                    setattr(old_value, "types_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type8"):
                opp_val = getattr(value, "types_Type8", None)
                setattr(value, "types_Type8", self)

    @property
    def types_FunctionType10(self):
        return self.__types_FunctionType10

    @types_FunctionType10.setter
    def types_FunctionType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_FunctionType__types_FunctionType10", None)
        self.__types_FunctionType10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Type11"):
                    opp_val = getattr(item, "types_Type11", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Type11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Type11"):
                    opp_val = getattr(item, "types_Type11", None)
                    
                    setattr(item, "types_Type11", self)
                    

class types_MapType(Type):

    pass
class types_CollectionType(Type):

    pass
class types_EClass:

    pass
class types_ObjectType(Type):

    pass
class types_StringType(DataType):

    pass
class NumberType:

    pass
class types_RealType(NumberType):

    pass