from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Role:

    def __init__(self, many: bool, name: str, myDsl_Role11: "myDsl_Entity" = None, myDsl_Role16: "myDsl_Type" = None, myDsl_Role: "myDsl_Association" = None):
        self.many = many
        self.name = name
        self.myDsl_Role11 = myDsl_Role11
        self.myDsl_Role16 = myDsl_Role16
        self.myDsl_Role = myDsl_Role
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def myDsl_Role(self):
        return self.__myDsl_Role

    @myDsl_Role.setter
    def myDsl_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Role__myDsl_Role", None)
        self.__myDsl_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Association3"):
                opp_val = getattr(old_value, "myDsl_Association3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Association3"):
                opp_val = getattr(value, "myDsl_Association3", None)
                if opp_val is None:
                    setattr(value, "myDsl_Association3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Role16(self):
        return self.__myDsl_Role16

    @myDsl_Role16.setter
    def myDsl_Role16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Role__myDsl_Role16", None)
        self.__myDsl_Role16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type17"):
                opp_val = getattr(old_value, "myDsl_Type17", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type17"):
                opp_val = getattr(value, "myDsl_Type17", None)
                setattr(value, "myDsl_Type17", self)

    @property
    def myDsl_Role11(self):
        return self.__myDsl_Role11

    @myDsl_Role11.setter
    def myDsl_Role11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Role__myDsl_Role11", None)
        self.__myDsl_Role11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity10"):
                opp_val = getattr(old_value, "myDsl_Entity10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity10"):
                opp_val = getattr(value, "myDsl_Entity10", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Attribute:

    def __init__(self, many: bool, name: str, myDsl_Attribute8: "myDsl_Entity" = None, myDsl_Attribute13: "myDsl_Type" = None, myDsl_Attribute: "myDsl_Association" = None):
        self.many = many
        self.name = name
        self.myDsl_Attribute8 = myDsl_Attribute8
        self.myDsl_Attribute13 = myDsl_Attribute13
        self.myDsl_Attribute = myDsl_Attribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def myDsl_Attribute13(self):
        return self.__myDsl_Attribute13

    @myDsl_Attribute13.setter
    def myDsl_Attribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute13", None)
        self.__myDsl_Attribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type14"):
                opp_val = getattr(old_value, "myDsl_Type14", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type14"):
                opp_val = getattr(value, "myDsl_Type14", None)
                setattr(value, "myDsl_Type14", self)

    @property
    def myDsl_Attribute(self):
        return self.__myDsl_Attribute

    @myDsl_Attribute.setter
    def myDsl_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute", None)
        self.__myDsl_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Association"):
                opp_val = getattr(old_value, "myDsl_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Association"):
                opp_val = getattr(value, "myDsl_Association", None)
                if opp_val is None:
                    setattr(value, "myDsl_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute8(self):
        return self.__myDsl_Attribute8

    @myDsl_Attribute8.setter
    def myDsl_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute8", None)
        self.__myDsl_Attribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entity7"):
                opp_val = getattr(old_value, "myDsl_Entity7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entity7"):
                opp_val = getattr(value, "myDsl_Entity7", None)
                if opp_val is None:
                    setattr(value, "myDsl_Entity7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class myDsl_Association(Type):

    pass
class myDsl_Entity(Type):

    pass
class myDsl_DataType(Type):

    pass
class myDsl_Type:

    def __init__(self, name: str, myDsl_Type14: "myDsl_Attribute" = None, myDsl_Type17: "myDsl_Role" = None, myDsl_Type: "myDsl_Domainmodel" = None):
        self.name = name
        self.myDsl_Type14 = myDsl_Type14
        self.myDsl_Type17 = myDsl_Type17
        self.myDsl_Type = myDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type(self):
        return self.__myDsl_Type

    @myDsl_Type.setter
    def myDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type", None)
        self.__myDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Domainmodel"):
                opp_val = getattr(old_value, "myDsl_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Domainmodel"):
                opp_val = getattr(value, "myDsl_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "myDsl_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Type14(self):
        return self.__myDsl_Type14

    @myDsl_Type14.setter
    def myDsl_Type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type14", None)
        self.__myDsl_Type14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Attribute13"):
                opp_val = getattr(old_value, "myDsl_Attribute13", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Attribute13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Attribute13"):
                opp_val = getattr(value, "myDsl_Attribute13", None)
                setattr(value, "myDsl_Attribute13", self)

    @property
    def myDsl_Type17(self):
        return self.__myDsl_Type17

    @myDsl_Type17.setter
    def myDsl_Type17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type17", None)
        self.__myDsl_Type17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Role16"):
                opp_val = getattr(old_value, "myDsl_Role16", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Role16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Role16"):
                opp_val = getattr(value, "myDsl_Role16", None)
                setattr(value, "myDsl_Role16", self)

class myDsl_Domainmodel:

    pass