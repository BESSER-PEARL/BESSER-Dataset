from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Attribute:

    pass
class SimpleClass_NonReferencedClass:

    pass
class SimpleClass_Attribute:

    def __init__(self, name: str, is_primary: str, SimpleClass_Attribute: "Classifier" = None, 09: "Class" = None):
        self.name = name
        self.is_primary = is_primary
        self.SimpleClass_Attribute = SimpleClass_Attribute
        self.09 = 09
        
    @property
    def is_primary(self) -> str:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: str):
        self.__is_primary = is_primary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 09(self):
        return self.__09

    @09.setter
    def 09(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Attribute__09", None)
        self.__09 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#10"):
                opp_val = getattr(old_value, "#10", None)
                if opp_val == self:
                    setattr(old_value, "#10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#10"):
                opp_val = getattr(value, "#10", None)
                setattr(value, "#10", self)

    @property
    def SimpleClass_Attribute(self):
        return self.__SimpleClass_Attribute

    @SimpleClass_Attribute.setter
    def SimpleClass_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Attribute__SimpleClass_Attribute", None)
        self.__SimpleClass_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

class SimpleClass_Association:

    def __init__(self, name: str, SimpleClass_Association: "Class" = None, SimpleClass_Association5: "Class" = None):
        self.name = name
        self.SimpleClass_Association = SimpleClass_Association
        self.SimpleClass_Association5 = SimpleClass_Association5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleClass_Association5(self):
        return self.__SimpleClass_Association5

    @SimpleClass_Association5.setter
    def SimpleClass_Association5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Association__SimpleClass_Association5", None)
        self.__SimpleClass_Association5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class6"):
                opp_val = getattr(old_value, "Class6", None)
                if opp_val == self:
                    setattr(old_value, "Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class6"):
                opp_val = getattr(value, "Class6", None)
                setattr(value, "Class6", self)

    @property
    def SimpleClass_Association(self):
        return self.__SimpleClass_Association

    @SimpleClass_Association.setter
    def SimpleClass_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Association__SimpleClass_Association", None)
        self.__SimpleClass_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class3"):
                opp_val = getattr(old_value, "Class3", None)
                if opp_val == self:
                    setattr(old_value, "Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class3"):
                opp_val = getattr(value, "Class3", None)
                setattr(value, "Class3", self)

class Class:

    pass
class Classifier:

    pass
class SimpleClass_PrimitiveDataType(Classifier):

    pass
class SimpleClass_Class(Classifier):

    def __init__(self, is_persistent: str, SimpleClass_Class: "Class" = None, 0: set["Attribute"] = None, Classifier: "SimpleClass_Attribute"):
        self.is_persistent = is_persistent
        self.SimpleClass_Class = SimpleClass_Class
        self.0 = 0 if 0 is not None else set()
        
    @property
    def is_persistent(self) -> str:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: str):
        self.__is_persistent = is_persistent

    @property
    def SimpleClass_Class(self):
        return self.__SimpleClass_Class

    @SimpleClass_Class.setter
    def SimpleClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class", None)
        self.__SimpleClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class SimpleClass_Classifier:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
