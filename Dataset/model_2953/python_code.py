from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Type:

    pass
class myDsl_TypeDef(Type):

    pass
class myDsl_Type:

    def __init__(self, name: str, myDsl_Type8: "myDsl_Attribute" = None, myDsl_Type: "myDsl_Model" = None):
        self.name = name
        self.myDsl_Type8 = myDsl_Type8
        self.myDsl_Type = myDsl_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Type8(self):
        return self.__myDsl_Type8

    @myDsl_Type8.setter
    def myDsl_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Type__myDsl_Type8", None)
        self.__myDsl_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Attribute7"):
                opp_val = getattr(old_value, "myDsl_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Attribute7"):
                opp_val = getattr(value, "myDsl_Attribute7", None)
                setattr(value, "myDsl_Attribute7", self)

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
            if hasattr(old_value, "myDsl_Model"):
                opp_val = getattr(old_value, "myDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Model"):
                opp_val = getattr(value, "myDsl_Model", None)
                if opp_val is None:
                    setattr(value, "myDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Model:

    pass
class myDsl_Attribute(Type):

    def __init__(self, many: bool, myDsl_Attribute: "myDsl_Interface" = None, myDsl_Attribute7: "myDsl_Type" = None):
        self.many = many
        self.myDsl_Attribute = myDsl_Attribute
        self.myDsl_Attribute7 = myDsl_Attribute7
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

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
            if hasattr(old_value, "myDsl_Interface5"):
                opp_val = getattr(old_value, "myDsl_Interface5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Interface5"):
                opp_val = getattr(value, "myDsl_Interface5", None)
                if opp_val is None:
                    setattr(value, "myDsl_Interface5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Attribute7(self):
        return self.__myDsl_Attribute7

    @myDsl_Attribute7.setter
    def myDsl_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Attribute__myDsl_Attribute7", None)
        self.__myDsl_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Type8"):
                opp_val = getattr(old_value, "myDsl_Type8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Type8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Type8"):
                opp_val = getattr(value, "myDsl_Type8", None)
                setattr(value, "myDsl_Type8", self)

class myDsl_Interface(Type):

    pass
class myDsl_JAVAID:

    def __init__(self, name: str, myDsl_JAVAID: "myDsl_TypeDef" = None):
        self.name = name
        self.myDsl_JAVAID = myDsl_JAVAID
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_JAVAID(self):
        return self.__myDsl_JAVAID

    @myDsl_JAVAID.setter
    def myDsl_JAVAID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_JAVAID__myDsl_JAVAID", None)
        self.__myDsl_JAVAID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_TypeDef"):
                opp_val = getattr(old_value, "myDsl_TypeDef", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_TypeDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_TypeDef"):
                opp_val = getattr(value, "myDsl_TypeDef", None)
                setattr(value, "myDsl_TypeDef", self)
