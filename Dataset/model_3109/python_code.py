from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ClassM_Model:

    pass
class ClassM_Classifier:

    def __init__(self, name: str, ClassM_Classifier: "ClassM_Attribute" = None, ClassM_Classifier4: "ClassM_Model" = None):
        self.name = name
        self.ClassM_Classifier = ClassM_Classifier
        self.ClassM_Classifier4 = ClassM_Classifier4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassM_Classifier4(self):
        return self.__ClassM_Classifier4

    @ClassM_Classifier4.setter
    def ClassM_Classifier4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Classifier__ClassM_Classifier4", None)
        self.__ClassM_Classifier4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassM_Model"):
                opp_val = getattr(old_value, "ClassM_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassM_Model"):
                opp_val = getattr(value, "ClassM_Model", None)
                if opp_val is None:
                    setattr(value, "ClassM_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassM_Classifier(self):
        return self.__ClassM_Classifier

    @ClassM_Classifier.setter
    def ClassM_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Classifier__ClassM_Classifier", None)
        self.__ClassM_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassM_Attribute"):
                opp_val = getattr(old_value, "ClassM_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "ClassM_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassM_Attribute"):
                opp_val = getattr(value, "ClassM_Attribute", None)
                setattr(value, "ClassM_Attribute", self)

class ClassM_Attribute:

    def __init__(self, name: str, is_primary: bool, Attribute: "ClassM_Class" = None, ClassM_Attribute: "ClassM_Classifier" = None, attrs: "ClassM_Class" = None):
        self.name = name
        self.is_primary = is_primary
        self.Attribute = Attribute
        self.ClassM_Attribute = ClassM_Attribute
        self.attrs = attrs
        
    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: bool):
        self.__is_primary = is_primary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassM_Attribute(self):
        return self.__ClassM_Attribute

    @ClassM_Attribute.setter
    def ClassM_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Attribute__ClassM_Attribute", None)
        self.__ClassM_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassM_Classifier"):
                opp_val = getattr(old_value, "ClassM_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "ClassM_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassM_Classifier"):
                opp_val = getattr(value, "ClassM_Classifier", None)
                setattr(value, "ClassM_Classifier", self)

    @property
    def attrs(self):
        return self.__attrs

    @attrs.setter
    def attrs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassM_Attribute__attrs", None)
        self.__attrs = value
        
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

class Classifier:

    pass
class ClassM_PrimitiveType(Classifier):

    pass
class ClassM_Class(Classifier):

    pass