from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class ClassMM_Attribute:

    def __init__(self, name: str, is_primary: str, ClassMM_Attribute: "ClassMM_Classifier" = None, ClassMM_Attribute7: "ClassMM_Class" = None):
        self.name = name
        self.is_primary = is_primary
        self.ClassMM_Attribute = ClassMM_Attribute
        self.ClassMM_Attribute7 = ClassMM_Attribute7
        
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
    def ClassMM_Attribute(self):
        return self.__ClassMM_Attribute

    @ClassMM_Attribute.setter
    def ClassMM_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Attribute__ClassMM_Attribute", None)
        self.__ClassMM_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Classifier"):
                opp_val = getattr(old_value, "ClassMM_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Classifier"):
                opp_val = getattr(value, "ClassMM_Classifier", None)
                setattr(value, "ClassMM_Classifier", self)

    @property
    def ClassMM_Attribute7(self):
        return self.__ClassMM_Attribute7

    @ClassMM_Attribute7.setter
    def ClassMM_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Attribute__ClassMM_Attribute7", None)
        self.__ClassMM_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Class6"):
                opp_val = getattr(old_value, "ClassMM_Class6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Class6"):
                opp_val = getattr(value, "ClassMM_Class6", None)
                if opp_val is None:
                    setattr(value, "ClassMM_Class6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassMM_Class(Classifier):

    def __init__(self, is_persistent: str, ClassMM_Class: "ClassMM_Association" = None, ClassMM_Class3: "ClassMM_Association" = None, ClassMM_Class6: set["ClassMM_Attribute"] = None, ClassMM_Class10: "ClassMM_Class" = None, ClassMM_Class8: "ClassMM_Class" = None):
        self.is_persistent = is_persistent
        self.ClassMM_Class = ClassMM_Class
        self.ClassMM_Class3 = ClassMM_Class3
        self.ClassMM_Class6 = ClassMM_Class6 if ClassMM_Class6 is not None else set()
        self.ClassMM_Class10 = ClassMM_Class10
        self.ClassMM_Class8 = ClassMM_Class8
        
    @property
    def is_persistent(self) -> str:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: str):
        self.__is_persistent = is_persistent

    @property
    def ClassMM_Class6(self):
        return self.__ClassMM_Class6

    @ClassMM_Class6.setter
    def ClassMM_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Class__ClassMM_Class6", None)
        self.__ClassMM_Class6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ClassMM_Attribute7"):
                    opp_val = getattr(item, "ClassMM_Attribute7", None)
                    
                    if opp_val == self:
                        setattr(item, "ClassMM_Attribute7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ClassMM_Attribute7"):
                    opp_val = getattr(item, "ClassMM_Attribute7", None)
                    
                    setattr(item, "ClassMM_Attribute7", self)
                    

    @property
    def ClassMM_Class(self):
        return self.__ClassMM_Class

    @ClassMM_Class.setter
    def ClassMM_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Class__ClassMM_Class", None)
        self.__ClassMM_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Association"):
                opp_val = getattr(old_value, "ClassMM_Association", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Association"):
                opp_val = getattr(value, "ClassMM_Association", None)
                setattr(value, "ClassMM_Association", self)

    @property
    def ClassMM_Class10(self):
        return self.__ClassMM_Class10

    @ClassMM_Class10.setter
    def ClassMM_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Class__ClassMM_Class10", None)
        self.__ClassMM_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Class8"):
                opp_val = getattr(old_value, "ClassMM_Class8", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Class8"):
                opp_val = getattr(value, "ClassMM_Class8", None)
                setattr(value, "ClassMM_Class8", self)

    @property
    def ClassMM_Class3(self):
        return self.__ClassMM_Class3

    @ClassMM_Class3.setter
    def ClassMM_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Class__ClassMM_Class3", None)
        self.__ClassMM_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Association2"):
                opp_val = getattr(old_value, "ClassMM_Association2", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Association2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Association2"):
                opp_val = getattr(value, "ClassMM_Association2", None)
                setattr(value, "ClassMM_Association2", self)

    @property
    def ClassMM_Class8(self):
        return self.__ClassMM_Class8

    @ClassMM_Class8.setter
    def ClassMM_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Class__ClassMM_Class8", None)
        self.__ClassMM_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Class10"):
                opp_val = getattr(old_value, "ClassMM_Class10", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Class10"):
                opp_val = getattr(value, "ClassMM_Class10", None)
                setattr(value, "ClassMM_Class10", self)

class ClassMM_Association:

    def __init__(self, name: str, ClassMM_Association15: "ClassMM_ClassModel" = None, ClassMM_Association: "ClassMM_Class" = None, ClassMM_Association2: "ClassMM_Class" = None):
        self.name = name
        self.ClassMM_Association15 = ClassMM_Association15
        self.ClassMM_Association = ClassMM_Association
        self.ClassMM_Association2 = ClassMM_Association2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassMM_Association2(self):
        return self.__ClassMM_Association2

    @ClassMM_Association2.setter
    def ClassMM_Association2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Association__ClassMM_Association2", None)
        self.__ClassMM_Association2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Class3"):
                opp_val = getattr(old_value, "ClassMM_Class3", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Class3"):
                opp_val = getattr(value, "ClassMM_Class3", None)
                setattr(value, "ClassMM_Class3", self)

    @property
    def ClassMM_Association15(self):
        return self.__ClassMM_Association15

    @ClassMM_Association15.setter
    def ClassMM_Association15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Association__ClassMM_Association15", None)
        self.__ClassMM_Association15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_ClassModel14"):
                opp_val = getattr(old_value, "ClassMM_ClassModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_ClassModel14"):
                opp_val = getattr(value, "ClassMM_ClassModel14", None)
                if opp_val is None:
                    setattr(value, "ClassMM_ClassModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassMM_Association(self):
        return self.__ClassMM_Association

    @ClassMM_Association.setter
    def ClassMM_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Association__ClassMM_Association", None)
        self.__ClassMM_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Class"):
                opp_val = getattr(old_value, "ClassMM_Class", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Class"):
                opp_val = getattr(value, "ClassMM_Class", None)
                setattr(value, "ClassMM_Class", self)

class ClassMM_ClassModel:

    pass
class ClassMM_PrimitiveDataType(Classifier):

    pass
class ClassMM_Classifier(ABC):

    def __init__(self, name: str, ClassMM_Classifier12: "ClassMM_ClassModel" = None, ClassMM_Classifier: "ClassMM_Attribute" = None):
        self.name = name
        self.ClassMM_Classifier12 = ClassMM_Classifier12
        self.ClassMM_Classifier = ClassMM_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ClassMM_Classifier12(self):
        return self.__ClassMM_Classifier12

    @ClassMM_Classifier12.setter
    def ClassMM_Classifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Classifier__ClassMM_Classifier12", None)
        self.__ClassMM_Classifier12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_ClassModel"):
                opp_val = getattr(old_value, "ClassMM_ClassModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_ClassModel"):
                opp_val = getattr(value, "ClassMM_ClassModel", None)
                if opp_val is None:
                    setattr(value, "ClassMM_ClassModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ClassMM_Classifier(self):
        return self.__ClassMM_Classifier

    @ClassMM_Classifier.setter
    def ClassMM_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ClassMM_Classifier__ClassMM_Classifier", None)
        self.__ClassMM_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassMM_Attribute"):
                opp_val = getattr(old_value, "ClassMM_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "ClassMM_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassMM_Attribute"):
                opp_val = getattr(value, "ClassMM_Attribute", None)
                setattr(value, "ClassMM_Attribute", self)
