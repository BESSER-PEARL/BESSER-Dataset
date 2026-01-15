from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rcd_ClassModel:

    def __init__(self, name: str, rcd_ClassModel14: set["rcd_Association"] = None, rcd_ClassModel: set["rcd_Classifier"] = None):
        self.name = name
        self.rcd_ClassModel14 = rcd_ClassModel14 if rcd_ClassModel14 is not None else set()
        self.rcd_ClassModel = rcd_ClassModel if rcd_ClassModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rcd_ClassModel(self):
        return self.__rcd_ClassModel

    @rcd_ClassModel.setter
    def rcd_ClassModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_ClassModel__rcd_ClassModel", None)
        self.__rcd_ClassModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rcd_Classifier12"):
                    opp_val = getattr(item, "rcd_Classifier12", None)
                    
                    if opp_val == self:
                        setattr(item, "rcd_Classifier12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rcd_Classifier12"):
                    opp_val = getattr(item, "rcd_Classifier12", None)
                    
                    setattr(item, "rcd_Classifier12", self)
                    

    @property
    def rcd_ClassModel14(self):
        return self.__rcd_ClassModel14

    @rcd_ClassModel14.setter
    def rcd_ClassModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_ClassModel__rcd_ClassModel14", None)
        self.__rcd_ClassModel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rcd_Association15"):
                    opp_val = getattr(item, "rcd_Association15", None)
                    
                    if opp_val == self:
                        setattr(item, "rcd_Association15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rcd_Association15"):
                    opp_val = getattr(item, "rcd_Association15", None)
                    
                    setattr(item, "rcd_Association15", self)
                    

class Classifier:

    pass
class rcd_PrimitiveDataType(Classifier):

    pass
class rcd_Class(Classifier):

    def __init__(self, is_persistent: bool, rcd_Class: "rcd_Association" = None, rcd_Class3: "rcd_Association" = None, rcd_Class6: set["rcd_Attribute"] = None, rcd_Class10: "rcd_Class" = None, rcd_Class8: "rcd_Class" = None):
        self.is_persistent = is_persistent
        self.rcd_Class = rcd_Class
        self.rcd_Class3 = rcd_Class3
        self.rcd_Class6 = rcd_Class6 if rcd_Class6 is not None else set()
        self.rcd_Class10 = rcd_Class10
        self.rcd_Class8 = rcd_Class8
        
    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
        self.__is_persistent = is_persistent

    @property
    def rcd_Class3(self):
        return self.__rcd_Class3

    @rcd_Class3.setter
    def rcd_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Class__rcd_Class3", None)
        self.__rcd_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Association2"):
                opp_val = getattr(old_value, "rcd_Association2", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Association2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Association2"):
                opp_val = getattr(value, "rcd_Association2", None)
                setattr(value, "rcd_Association2", self)

    @property
    def rcd_Class10(self):
        return self.__rcd_Class10

    @rcd_Class10.setter
    def rcd_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Class__rcd_Class10", None)
        self.__rcd_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Class8"):
                opp_val = getattr(old_value, "rcd_Class8", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Class8"):
                opp_val = getattr(value, "rcd_Class8", None)
                setattr(value, "rcd_Class8", self)

    @property
    def rcd_Class8(self):
        return self.__rcd_Class8

    @rcd_Class8.setter
    def rcd_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Class__rcd_Class8", None)
        self.__rcd_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Class10"):
                opp_val = getattr(old_value, "rcd_Class10", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Class10"):
                opp_val = getattr(value, "rcd_Class10", None)
                setattr(value, "rcd_Class10", self)

    @property
    def rcd_Class6(self):
        return self.__rcd_Class6

    @rcd_Class6.setter
    def rcd_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Class__rcd_Class6", None)
        self.__rcd_Class6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rcd_Attribute7"):
                    opp_val = getattr(item, "rcd_Attribute7", None)
                    
                    if opp_val == self:
                        setattr(item, "rcd_Attribute7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rcd_Attribute7"):
                    opp_val = getattr(item, "rcd_Attribute7", None)
                    
                    setattr(item, "rcd_Attribute7", self)
                    

    @property
    def rcd_Class(self):
        return self.__rcd_Class

    @rcd_Class.setter
    def rcd_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Class__rcd_Class", None)
        self.__rcd_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Association"):
                opp_val = getattr(old_value, "rcd_Association", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Association"):
                opp_val = getattr(value, "rcd_Association", None)
                setattr(value, "rcd_Association", self)

class rcd_Association:

    def __init__(self, upper: str, lower: str, name: str, rcd_Association2: "rcd_Class" = None, rcd_Association: "rcd_Class" = None, rcd_Association15: "rcd_ClassModel" = None):
        self.upper = upper
        self.lower = lower
        self.name = name
        self.rcd_Association2 = rcd_Association2
        self.rcd_Association = rcd_Association
        self.rcd_Association15 = rcd_Association15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def rcd_Association(self):
        return self.__rcd_Association

    @rcd_Association.setter
    def rcd_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Association__rcd_Association", None)
        self.__rcd_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Class"):
                opp_val = getattr(old_value, "rcd_Class", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Class"):
                opp_val = getattr(value, "rcd_Class", None)
                setattr(value, "rcd_Class", self)

    @property
    def rcd_Association2(self):
        return self.__rcd_Association2

    @rcd_Association2.setter
    def rcd_Association2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Association__rcd_Association2", None)
        self.__rcd_Association2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Class3"):
                opp_val = getattr(old_value, "rcd_Class3", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Class3"):
                opp_val = getattr(value, "rcd_Class3", None)
                setattr(value, "rcd_Class3", self)

    @property
    def rcd_Association15(self):
        return self.__rcd_Association15

    @rcd_Association15.setter
    def rcd_Association15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Association__rcd_Association15", None)
        self.__rcd_Association15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_ClassModel14"):
                opp_val = getattr(old_value, "rcd_ClassModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_ClassModel14"):
                opp_val = getattr(value, "rcd_ClassModel14", None)
                if opp_val is None:
                    setattr(value, "rcd_ClassModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rcd_Classifier(ABC):

    def __init__(self, name: str, rcd_Classifier: "rcd_Attribute" = None, rcd_Classifier12: "rcd_ClassModel" = None):
        self.name = name
        self.rcd_Classifier = rcd_Classifier
        self.rcd_Classifier12 = rcd_Classifier12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rcd_Classifier12(self):
        return self.__rcd_Classifier12

    @rcd_Classifier12.setter
    def rcd_Classifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Classifier__rcd_Classifier12", None)
        self.__rcd_Classifier12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_ClassModel"):
                opp_val = getattr(old_value, "rcd_ClassModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_ClassModel"):
                opp_val = getattr(value, "rcd_ClassModel", None)
                if opp_val is None:
                    setattr(value, "rcd_ClassModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rcd_Classifier(self):
        return self.__rcd_Classifier

    @rcd_Classifier.setter
    def rcd_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Classifier__rcd_Classifier", None)
        self.__rcd_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Attribute"):
                opp_val = getattr(old_value, "rcd_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Attribute"):
                opp_val = getattr(value, "rcd_Attribute", None)
                setattr(value, "rcd_Attribute", self)

class rcd_Attribute:

    def __init__(self, name: str, is_primary: bool, upper: str, lower: str, rcd_Attribute: "rcd_Classifier" = None, rcd_Attribute7: "rcd_Class" = None):
        self.name = name
        self.is_primary = is_primary
        self.upper = upper
        self.lower = lower
        self.rcd_Attribute = rcd_Attribute
        self.rcd_Attribute7 = rcd_Attribute7
        
    @property
    def is_primary(self) -> bool:
        return self.__is_primary

    @is_primary.setter
    def is_primary(self, is_primary: bool):
        self.__is_primary = is_primary

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def rcd_Attribute(self):
        return self.__rcd_Attribute

    @rcd_Attribute.setter
    def rcd_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Attribute__rcd_Attribute", None)
        self.__rcd_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Classifier"):
                opp_val = getattr(old_value, "rcd_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "rcd_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Classifier"):
                opp_val = getattr(value, "rcd_Classifier", None)
                setattr(value, "rcd_Classifier", self)

    @property
    def rcd_Attribute7(self):
        return self.__rcd_Attribute7

    @rcd_Attribute7.setter
    def rcd_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcd_Attribute__rcd_Attribute7", None)
        self.__rcd_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcd_Class6"):
                opp_val = getattr(old_value, "rcd_Class6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcd_Class6"):
                opp_val = getattr(value, "rcd_Class6", None)
                if opp_val is None:
                    setattr(value, "rcd_Class6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
