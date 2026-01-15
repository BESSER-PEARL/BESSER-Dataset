from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classdiagram_Attribute:

    def __init__(self, name: str, is_primary: bool, classdiagram_Attribute: "classdiagram_Class" = None, classdiagram_Attribute8: "classdiagram_Classifier" = None):
        self.name = name
        self.is_primary = is_primary
        self.classdiagram_Attribute = classdiagram_Attribute
        self.classdiagram_Attribute8 = classdiagram_Attribute8
        
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
    def classdiagram_Attribute(self):
        return self.__classdiagram_Attribute

    @classdiagram_Attribute.setter
    def classdiagram_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute", None)
        self.__classdiagram_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class"):
                opp_val = getattr(old_value, "classdiagram_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class"):
                opp_val = getattr(value, "classdiagram_Class", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Attribute8(self):
        return self.__classdiagram_Attribute8

    @classdiagram_Attribute8.setter
    def classdiagram_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Attribute__classdiagram_Attribute8", None)
        self.__classdiagram_Attribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Classifier9"):
                opp_val = getattr(old_value, "classdiagram_Classifier9", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Classifier9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Classifier9"):
                opp_val = getattr(value, "classdiagram_Classifier9", None)
                setattr(value, "classdiagram_Classifier9", self)

class Classifier:

    pass
class classdiagram_Class(Classifier):

    def __init__(self, is_persistent: bool, classdiagram_Class: set["classdiagram_Attribute"] = None, classdiagram_Class6: "classdiagram_Class" = None, classdiagram_Class4: "classdiagram_Class" = None, classdiagram_Class12: "classdiagram_Association" = None, classdiagram_Class15: "classdiagram_Association" = None):
        self.is_persistent = is_persistent
        self.classdiagram_Class = classdiagram_Class if classdiagram_Class is not None else set()
        self.classdiagram_Class6 = classdiagram_Class6
        self.classdiagram_Class4 = classdiagram_Class4
        self.classdiagram_Class12 = classdiagram_Class12
        self.classdiagram_Class15 = classdiagram_Class15
        
    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
        self.__is_persistent = is_persistent

    @property
    def classdiagram_Class(self):
        return self.__classdiagram_Class

    @classdiagram_Class.setter
    def classdiagram_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class", None)
        self.__classdiagram_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Attribute"):
                    opp_val = getattr(item, "classdiagram_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Attribute"):
                    opp_val = getattr(item, "classdiagram_Attribute", None)
                    
                    setattr(item, "classdiagram_Attribute", self)
                    

    @property
    def classdiagram_Class15(self):
        return self.__classdiagram_Class15

    @classdiagram_Class15.setter
    def classdiagram_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class15", None)
        self.__classdiagram_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Association14"):
                opp_val = getattr(old_value, "classdiagram_Association14", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Association14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Association14"):
                opp_val = getattr(value, "classdiagram_Association14", None)
                setattr(value, "classdiagram_Association14", self)

    @property
    def classdiagram_Class6(self):
        return self.__classdiagram_Class6

    @classdiagram_Class6.setter
    def classdiagram_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class6", None)
        self.__classdiagram_Class6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class4"):
                opp_val = getattr(old_value, "classdiagram_Class4", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class4"):
                opp_val = getattr(value, "classdiagram_Class4", None)
                setattr(value, "classdiagram_Class4", self)

    @property
    def classdiagram_Class4(self):
        return self.__classdiagram_Class4

    @classdiagram_Class4.setter
    def classdiagram_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class4", None)
        self.__classdiagram_Class4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class6"):
                opp_val = getattr(old_value, "classdiagram_Class6", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class6"):
                opp_val = getattr(value, "classdiagram_Class6", None)
                setattr(value, "classdiagram_Class6", self)

    @property
    def classdiagram_Class12(self):
        return self.__classdiagram_Class12

    @classdiagram_Class12.setter
    def classdiagram_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Class__classdiagram_Class12", None)
        self.__classdiagram_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Association11"):
                opp_val = getattr(old_value, "classdiagram_Association11", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Association11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Association11"):
                opp_val = getattr(value, "classdiagram_Association11", None)
                setattr(value, "classdiagram_Association11", self)

class classdiagram_PrimitiveDataType(Classifier):

    pass
class classdiagram_Association:

    def __init__(self, name: str, classdiagram_Association: "classdiagram_Package" = None, classdiagram_Association11: "classdiagram_Class" = None, classdiagram_Association14: "classdiagram_Class" = None):
        self.name = name
        self.classdiagram_Association = classdiagram_Association
        self.classdiagram_Association11 = classdiagram_Association11
        self.classdiagram_Association14 = classdiagram_Association14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Association(self):
        return self.__classdiagram_Association

    @classdiagram_Association.setter
    def classdiagram_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association", None)
        self.__classdiagram_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Package2"):
                opp_val = getattr(old_value, "classdiagram_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Package2"):
                opp_val = getattr(value, "classdiagram_Package2", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Association14(self):
        return self.__classdiagram_Association14

    @classdiagram_Association14.setter
    def classdiagram_Association14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association14", None)
        self.__classdiagram_Association14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class15"):
                opp_val = getattr(old_value, "classdiagram_Class15", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class15"):
                opp_val = getattr(value, "classdiagram_Class15", None)
                setattr(value, "classdiagram_Class15", self)

    @property
    def classdiagram_Association11(self):
        return self.__classdiagram_Association11

    @classdiagram_Association11.setter
    def classdiagram_Association11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Association__classdiagram_Association11", None)
        self.__classdiagram_Association11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Class12"):
                opp_val = getattr(old_value, "classdiagram_Class12", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Class12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Class12"):
                opp_val = getattr(value, "classdiagram_Class12", None)
                setattr(value, "classdiagram_Class12", self)

class classdiagram_Classifier(ABC):

    def __init__(self, name: str, classdiagram_Classifier: "classdiagram_Package" = None, classdiagram_Classifier9: "classdiagram_Attribute" = None):
        self.name = name
        self.classdiagram_Classifier = classdiagram_Classifier
        self.classdiagram_Classifier9 = classdiagram_Classifier9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Classifier(self):
        return self.__classdiagram_Classifier

    @classdiagram_Classifier.setter
    def classdiagram_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Classifier__classdiagram_Classifier", None)
        self.__classdiagram_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Package"):
                opp_val = getattr(old_value, "classdiagram_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Package"):
                opp_val = getattr(value, "classdiagram_Package", None)
                if opp_val is None:
                    setattr(value, "classdiagram_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classdiagram_Classifier9(self):
        return self.__classdiagram_Classifier9

    @classdiagram_Classifier9.setter
    def classdiagram_Classifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Classifier__classdiagram_Classifier9", None)
        self.__classdiagram_Classifier9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classdiagram_Attribute8"):
                opp_val = getattr(old_value, "classdiagram_Attribute8", None)
                if opp_val == self:
                    setattr(old_value, "classdiagram_Attribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classdiagram_Attribute8"):
                opp_val = getattr(value, "classdiagram_Attribute8", None)
                setattr(value, "classdiagram_Attribute8", self)

class classdiagram_Package:

    def __init__(self, name: str, classdiagram_Package: set["classdiagram_Classifier"] = None, classdiagram_Package2: set["classdiagram_Association"] = None):
        self.name = name
        self.classdiagram_Package = classdiagram_Package if classdiagram_Package is not None else set()
        self.classdiagram_Package2 = classdiagram_Package2 if classdiagram_Package2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classdiagram_Package2(self):
        return self.__classdiagram_Package2

    @classdiagram_Package2.setter
    def classdiagram_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Package__classdiagram_Package2", None)
        self.__classdiagram_Package2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Association"):
                    opp_val = getattr(item, "classdiagram_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Association"):
                    opp_val = getattr(item, "classdiagram_Association", None)
                    
                    setattr(item, "classdiagram_Association", self)
                    

    @property
    def classdiagram_Package(self):
        return self.__classdiagram_Package

    @classdiagram_Package.setter
    def classdiagram_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classdiagram_Package__classdiagram_Package", None)
        self.__classdiagram_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classdiagram_Classifier"):
                    opp_val = getattr(item, "classdiagram_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "classdiagram_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classdiagram_Classifier"):
                    opp_val = getattr(item, "classdiagram_Classifier", None)
                    
                    setattr(item, "classdiagram_Classifier", self)
                    
