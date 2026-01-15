from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleClass_Association:

    def __init__(self, name: str, SimpleClass_Association: "SimpleClass_Class" = None, SimpleClass_Association9: "SimpleClass_Class" = None):
        self.name = name
        self.SimpleClass_Association = SimpleClass_Association
        self.SimpleClass_Association9 = SimpleClass_Association9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "SimpleClass_Class7"):
                opp_val = getattr(old_value, "SimpleClass_Class7", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Class7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Class7"):
                opp_val = getattr(value, "SimpleClass_Class7", None)
                setattr(value, "SimpleClass_Class7", self)

    @property
    def SimpleClass_Association9(self):
        return self.__SimpleClass_Association9

    @SimpleClass_Association9.setter
    def SimpleClass_Association9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Association__SimpleClass_Association9", None)
        self.__SimpleClass_Association9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Class10"):
                opp_val = getattr(old_value, "SimpleClass_Class10", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Class10"):
                opp_val = getattr(value, "SimpleClass_Class10", None)
                setattr(value, "SimpleClass_Class10", self)

class SimpleClass_Classifier:

    def __init__(self, name: str, SimpleClass_Classifier: "SimpleClass_Attribute" = None):
        self.name = name
        self.SimpleClass_Classifier = SimpleClass_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleClass_Classifier(self):
        return self.__SimpleClass_Classifier

    @SimpleClass_Classifier.setter
    def SimpleClass_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Classifier__SimpleClass_Classifier", None)
        self.__SimpleClass_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Attribute5"):
                opp_val = getattr(old_value, "SimpleClass_Attribute5", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Attribute5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Attribute5"):
                opp_val = getattr(value, "SimpleClass_Attribute5", None)
                setattr(value, "SimpleClass_Attribute5", self)

class SimpleClass_Attribute:

    def __init__(self, name: str, is_primary: bool, SimpleClass_Attribute: "SimpleClass_Class" = None, SimpleClass_Attribute5: "SimpleClass_Classifier" = None):
        self.name = name
        self.is_primary = is_primary
        self.SimpleClass_Attribute = SimpleClass_Attribute
        self.SimpleClass_Attribute5 = SimpleClass_Attribute5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: bool):
        self.__is_primary = is_primary

    @property
    def SimpleClass_Attribute5(self):
        return self.__SimpleClass_Attribute5

    @SimpleClass_Attribute5.setter
    def SimpleClass_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Attribute__SimpleClass_Attribute5", None)
        self.__SimpleClass_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Classifier"):
                opp_val = getattr(old_value, "SimpleClass_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Classifier"):
                opp_val = getattr(value, "SimpleClass_Classifier", None)
                setattr(value, "SimpleClass_Classifier", self)

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
            if hasattr(old_value, "SimpleClass_Class3"):
                opp_val = getattr(old_value, "SimpleClass_Class3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Class3"):
                opp_val = getattr(value, "SimpleClass_Class3", None)
                if opp_val is None:
                    setattr(value, "SimpleClass_Class3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class SimpleClass_PrimitiveDataType(Classifier):

    pass
class SimpleClass_Class(Classifier):

    def __init__(self, is_persistent: bool, SimpleClass_Class: "SimpleClass_Class" = None, SimpleClass_Class0: "SimpleClass_Class" = None, SimpleClass_Class3: set["SimpleClass_Attribute"] = None, SimpleClass_Class7: "SimpleClass_Association" = None, SimpleClass_Class10: "SimpleClass_Association" = None):
        self.is_persistent = is_persistent
        self.SimpleClass_Class = SimpleClass_Class
        self.SimpleClass_Class0 = SimpleClass_Class0
        self.SimpleClass_Class3 = SimpleClass_Class3 if SimpleClass_Class3 is not None else set()
        self.SimpleClass_Class7 = SimpleClass_Class7
        self.SimpleClass_Class10 = SimpleClass_Class10
        
    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
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
            if hasattr(old_value, "SimpleClass_Class0"):
                opp_val = getattr(old_value, "SimpleClass_Class0", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Class0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Class0"):
                opp_val = getattr(value, "SimpleClass_Class0", None)
                setattr(value, "SimpleClass_Class0", self)

    @property
    def SimpleClass_Class7(self):
        return self.__SimpleClass_Class7

    @SimpleClass_Class7.setter
    def SimpleClass_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class7", None)
        self.__SimpleClass_Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Association"):
                opp_val = getattr(old_value, "SimpleClass_Association", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Association"):
                opp_val = getattr(value, "SimpleClass_Association", None)
                setattr(value, "SimpleClass_Association", self)

    @property
    def SimpleClass_Class10(self):
        return self.__SimpleClass_Class10

    @SimpleClass_Class10.setter
    def SimpleClass_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class10", None)
        self.__SimpleClass_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Association9"):
                opp_val = getattr(old_value, "SimpleClass_Association9", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Association9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Association9"):
                opp_val = getattr(value, "SimpleClass_Association9", None)
                setattr(value, "SimpleClass_Association9", self)

    @property
    def SimpleClass_Class0(self):
        return self.__SimpleClass_Class0

    @SimpleClass_Class0.setter
    def SimpleClass_Class0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class0", None)
        self.__SimpleClass_Class0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleClass_Class"):
                opp_val = getattr(old_value, "SimpleClass_Class", None)
                if opp_val == self:
                    setattr(old_value, "SimpleClass_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleClass_Class"):
                opp_val = getattr(value, "SimpleClass_Class", None)
                setattr(value, "SimpleClass_Class", self)

    @property
    def SimpleClass_Class3(self):
        return self.__SimpleClass_Class3

    @SimpleClass_Class3.setter
    def SimpleClass_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__SimpleClass_Class3", None)
        self.__SimpleClass_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleClass_Attribute"):
                    opp_val = getattr(item, "SimpleClass_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleClass_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleClass_Attribute"):
                    opp_val = getattr(item, "SimpleClass_Attribute", None)
                    
                    setattr(item, "SimpleClass_Attribute", self)
                    
