from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Attribute:

    pass
class Class:

    pass
class Classifier:

    pass
class SimpleClass_Class(Classifier):

    def __init__(self, is_persistent: str, SimpleClass_Class: "Class" = None, class_: set["Attribute"] = None, Classifier: "SimpleClass_Attribute" = None):
        self.is_persistent = is_persistent
        self.SimpleClass_Class = SimpleClass_Class
        self.class_ = class_ if class_ is not None else set()
        
        pass
    @property
    def is_persistent(self):
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: str):
        self.__is_persistent = is_persistent


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

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

class SimpleClass_Classifier:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class SimpleClass_Attribute:

    def __init__(self, name: str, is_primary: str, SimpleClass_Attribute: "Classifier" = None, attrs: "Class" = None):
        self.name = name
        self.is_primary = is_primary
        self.SimpleClass_Attribute = SimpleClass_Attribute
        self.attrs = attrs
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def is_primary(self):
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: str):
        self.__is_primary = is_primary


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

    @property
    def attrs(self):
        return self.__attrs

    @attrs.setter
    def attrs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleClass_Attribute__attrs", None)
        self.__attrs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class9"):
                opp_val = getattr(old_value, "Class9", None)
                if opp_val == self:
                    setattr(old_value, "Class9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class9"):
                opp_val = getattr(value, "Class9", None)
                setattr(value, "Class9", self)

class SimpleClass_Association:

    def __init__(self, name: str, SimpleClass_Association: "Class" = None, SimpleClass_Association5: "Class" = None):
        self.name = name
        self.SimpleClass_Association = SimpleClass_Association
        self.SimpleClass_Association5 = SimpleClass_Association5
        
        pass
    @property
    def name(self):
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

class SimpleClass_PrimitiveDataType(Classifier):

    pass