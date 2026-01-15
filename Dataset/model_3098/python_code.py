from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UML_Association:

    def __init__(self, name: str, UML_Association: "UML_Package" = None, UML_Association11: "UML_Class" = None, UML_Association14: "UML_Class" = None):
        self.name = name
        self.UML_Association = UML_Association
        self.UML_Association11 = UML_Association11
        self.UML_Association14 = UML_Association14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UML_Association14(self):
        return self.__UML_Association14

    @UML_Association14.setter
    def UML_Association14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Association__UML_Association14", None)
        self.__UML_Association14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Class15"):
                opp_val = getattr(old_value, "UML_Class15", None)
                if opp_val == self:
                    setattr(old_value, "UML_Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Class15"):
                opp_val = getattr(value, "UML_Class15", None)
                setattr(value, "UML_Class15", self)

    @property
    def UML_Association(self):
        return self.__UML_Association

    @UML_Association.setter
    def UML_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Association__UML_Association", None)
        self.__UML_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Package2"):
                opp_val = getattr(old_value, "UML_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Package2"):
                opp_val = getattr(value, "UML_Package2", None)
                if opp_val is None:
                    setattr(value, "UML_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Association11(self):
        return self.__UML_Association11

    @UML_Association11.setter
    def UML_Association11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Association__UML_Association11", None)
        self.__UML_Association11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Class12"):
                opp_val = getattr(old_value, "UML_Class12", None)
                if opp_val == self:
                    setattr(old_value, "UML_Class12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Class12"):
                opp_val = getattr(value, "UML_Class12", None)
                setattr(value, "UML_Class12", self)

class UML_Classifier(ABC):

    def __init__(self, name: str, UML_Classifier: "UML_Package" = None, UML_Classifier9: "UML_Attribute" = None):
        self.name = name
        self.UML_Classifier = UML_Classifier
        self.UML_Classifier9 = UML_Classifier9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UML_Classifier9(self):
        return self.__UML_Classifier9

    @UML_Classifier9.setter
    def UML_Classifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Classifier__UML_Classifier9", None)
        self.__UML_Classifier9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Attribute8"):
                opp_val = getattr(old_value, "UML_Attribute8", None)
                if opp_val == self:
                    setattr(old_value, "UML_Attribute8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Attribute8"):
                opp_val = getattr(value, "UML_Attribute8", None)
                setattr(value, "UML_Attribute8", self)

    @property
    def UML_Classifier(self):
        return self.__UML_Classifier

    @UML_Classifier.setter
    def UML_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Classifier__UML_Classifier", None)
        self.__UML_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Package"):
                opp_val = getattr(old_value, "UML_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Package"):
                opp_val = getattr(value, "UML_Package", None)
                if opp_val is None:
                    setattr(value, "UML_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML_Package:

    def __init__(self, name: str, UML_Package: set["UML_Classifier"] = None, UML_Package2: set["UML_Association"] = None):
        self.name = name
        self.UML_Package = UML_Package if UML_Package is not None else set()
        self.UML_Package2 = UML_Package2 if UML_Package2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UML_Package(self):
        return self.__UML_Package

    @UML_Package.setter
    def UML_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Package__UML_Package", None)
        self.__UML_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_Classifier"):
                    opp_val = getattr(item, "UML_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_Classifier"):
                    opp_val = getattr(item, "UML_Classifier", None)
                    
                    setattr(item, "UML_Classifier", self)
                    

    @property
    def UML_Package2(self):
        return self.__UML_Package2

    @UML_Package2.setter
    def UML_Package2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Package__UML_Package2", None)
        self.__UML_Package2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_Association"):
                    opp_val = getattr(item, "UML_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_Association"):
                    opp_val = getattr(item, "UML_Association", None)
                    
                    setattr(item, "UML_Association", self)
                    

class UML_Attribute:

    def __init__(self, name: str, is_primary: bool, UML_Attribute: "UML_Class" = None, UML_Attribute8: "UML_Classifier" = None):
        self.name = name
        self.is_primary = is_primary
        self.UML_Attribute = UML_Attribute
        self.UML_Attribute8 = UML_Attribute8
        
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
    def UML_Attribute(self):
        return self.__UML_Attribute

    @UML_Attribute.setter
    def UML_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Attribute__UML_Attribute", None)
        self.__UML_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Class"):
                opp_val = getattr(old_value, "UML_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Class"):
                opp_val = getattr(value, "UML_Class", None)
                if opp_val is None:
                    setattr(value, "UML_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML_Attribute8(self):
        return self.__UML_Attribute8

    @UML_Attribute8.setter
    def UML_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Attribute__UML_Attribute8", None)
        self.__UML_Attribute8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Classifier9"):
                opp_val = getattr(old_value, "UML_Classifier9", None)
                if opp_val == self:
                    setattr(old_value, "UML_Classifier9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Classifier9"):
                opp_val = getattr(value, "UML_Classifier9", None)
                setattr(value, "UML_Classifier9", self)

class Classifier:

    pass
class UML_Class(Classifier):

    def __init__(self, is_persistent: bool, UML_Class: set["UML_Attribute"] = None, UML_Class6: "UML_Class" = None, UML_Class4: "UML_Class" = None, UML_Class12: "UML_Association" = None, UML_Class15: "UML_Association" = None):
        self.is_persistent = is_persistent
        self.UML_Class = UML_Class if UML_Class is not None else set()
        self.UML_Class6 = UML_Class6
        self.UML_Class4 = UML_Class4
        self.UML_Class12 = UML_Class12
        self.UML_Class15 = UML_Class15
        
    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
        self.__is_persistent = is_persistent

    @property
    def UML_Class(self):
        return self.__UML_Class

    @UML_Class.setter
    def UML_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Class__UML_Class", None)
        self.__UML_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML_Attribute"):
                    opp_val = getattr(item, "UML_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "UML_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML_Attribute"):
                    opp_val = getattr(item, "UML_Attribute", None)
                    
                    setattr(item, "UML_Attribute", self)
                    

    @property
    def UML_Class4(self):
        return self.__UML_Class4

    @UML_Class4.setter
    def UML_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Class__UML_Class4", None)
        self.__UML_Class4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Class6"):
                opp_val = getattr(old_value, "UML_Class6", None)
                if opp_val == self:
                    setattr(old_value, "UML_Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Class6"):
                opp_val = getattr(value, "UML_Class6", None)
                setattr(value, "UML_Class6", self)

    @property
    def UML_Class6(self):
        return self.__UML_Class6

    @UML_Class6.setter
    def UML_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Class__UML_Class6", None)
        self.__UML_Class6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Class4"):
                opp_val = getattr(old_value, "UML_Class4", None)
                if opp_val == self:
                    setattr(old_value, "UML_Class4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Class4"):
                opp_val = getattr(value, "UML_Class4", None)
                setattr(value, "UML_Class4", self)

    @property
    def UML_Class15(self):
        return self.__UML_Class15

    @UML_Class15.setter
    def UML_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Class__UML_Class15", None)
        self.__UML_Class15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association14"):
                opp_val = getattr(old_value, "UML_Association14", None)
                if opp_val == self:
                    setattr(old_value, "UML_Association14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association14"):
                opp_val = getattr(value, "UML_Association14", None)
                setattr(value, "UML_Association14", self)

    @property
    def UML_Class12(self):
        return self.__UML_Class12

    @UML_Class12.setter
    def UML_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML_Class__UML_Class12", None)
        self.__UML_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML_Association11"):
                opp_val = getattr(old_value, "UML_Association11", None)
                if opp_val == self:
                    setattr(old_value, "UML_Association11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML_Association11"):
                opp_val = getattr(value, "UML_Association11", None)
                setattr(value, "UML_Association11", self)

class UML_PrimitiveDataType(Classifier):

    pass