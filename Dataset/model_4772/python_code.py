from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeReference:

    pass
class types_ArrayType(TypeReference):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class types_TypeReference:

    pass
class types_Property:

    def __init__(self, name: str, types_Property12: "types_ServiceType" = None, types_Property20: "types_Operation" = None, types_Property: "types_ClassType" = None, types_Property5: "types_TypeReference" = None):
        self.name = name
        self.types_Property12 = types_Property12
        self.types_Property20 = types_Property20
        self.types_Property = types_Property
        self.types_Property5 = types_Property5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Property5(self):
        return self.__types_Property5

    @types_Property5.setter
    def types_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property5", None)
        self.__types_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference"):
                opp_val = getattr(old_value, "types_TypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference"):
                opp_val = getattr(value, "types_TypeReference", None)
                setattr(value, "types_TypeReference", self)

    @property
    def types_Property12(self):
        return self.__types_Property12

    @types_Property12.setter
    def types_Property12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property12", None)
        self.__types_Property12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ServiceType"):
                opp_val = getattr(old_value, "types_ServiceType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ServiceType"):
                opp_val = getattr(value, "types_ServiceType", None)
                if opp_val is None:
                    setattr(value, "types_ServiceType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Property20(self):
        return self.__types_Property20

    @types_Property20.setter
    def types_Property20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property20", None)
        self.__types_Property20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Operation19"):
                opp_val = getattr(old_value, "types_Operation19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Operation19"):
                opp_val = getattr(value, "types_Operation19", None)
                if opp_val is None:
                    setattr(value, "types_Operation19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Property(self):
        return self.__types_Property

    @types_Property.setter
    def types_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property", None)
        self.__types_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ClassType3"):
                opp_val = getattr(old_value, "types_ClassType3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ClassType3"):
                opp_val = getattr(value, "types_ClassType3", None)
                if opp_val is None:
                    setattr(value, "types_ClassType3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_EObject:

    pass
class types_Operation:

    def __init__(self, name: str, types_Operation: "types_ServiceType" = None, types_Operation16: "types_TypeReference" = None, types_Operation19: set["types_Property"] = None, types_Operation22: "types_EObject" = None):
        self.name = name
        self.types_Operation = types_Operation
        self.types_Operation16 = types_Operation16
        self.types_Operation19 = types_Operation19 if types_Operation19 is not None else set()
        self.types_Operation22 = types_Operation22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Operation16(self):
        return self.__types_Operation16

    @types_Operation16.setter
    def types_Operation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__types_Operation16", None)
        self.__types_Operation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference17"):
                opp_val = getattr(old_value, "types_TypeReference17", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference17"):
                opp_val = getattr(value, "types_TypeReference17", None)
                setattr(value, "types_TypeReference17", self)

    @property
    def types_Operation(self):
        return self.__types_Operation

    @types_Operation.setter
    def types_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__types_Operation", None)
        self.__types_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ServiceType14"):
                opp_val = getattr(old_value, "types_ServiceType14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ServiceType14"):
                opp_val = getattr(value, "types_ServiceType14", None)
                if opp_val is None:
                    setattr(value, "types_ServiceType14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Operation19(self):
        return self.__types_Operation19

    @types_Operation19.setter
    def types_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__types_Operation19", None)
        self.__types_Operation19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Property20"):
                    opp_val = getattr(item, "types_Property20", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Property20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Property20"):
                    opp_val = getattr(item, "types_Property20", None)
                    
                    setattr(item, "types_Property20", self)
                    

    @property
    def types_Operation22(self):
        return self.__types_Operation22

    @types_Operation22.setter
    def types_Operation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Operation__types_Operation22", None)
        self.__types_Operation22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EObject"):
                opp_val = getattr(old_value, "types_EObject", None)
                if opp_val == self:
                    setattr(old_value, "types_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EObject"):
                opp_val = getattr(value, "types_EObject", None)
                setattr(value, "types_EObject", self)

class UserType:

    pass
class types_ServiceType(UserType):

    pass
class types_ClassType(UserType):

    pass
class Type:

    pass
class types_UserType(Type):

    pass
class types_PrimitiveType(Type):

    pass
class types_Type:

    def __init__(self, name: str, types_Type: "types_TypeReference" = None):
        self.name = name
        self.types_Type = types_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "types_TypeReference7"):
                opp_val = getattr(old_value, "types_TypeReference7", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference7"):
                opp_val = getattr(value, "types_TypeReference7", None)
                setattr(value, "types_TypeReference7", self)
