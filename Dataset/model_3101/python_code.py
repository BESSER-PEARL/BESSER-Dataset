from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class simpleUML_MM_Attribute:

    def __init__(self, name: str, is_primary: bool, simpleUML_MM_Attribute7: "simpleUML_MM_Class" = None, simpleUML_MM_Attribute: "simpleUML_MM_Classifier" = None):
        self.name = name
        self.is_primary = is_primary
        self.simpleUML_MM_Attribute7 = simpleUML_MM_Attribute7
        self.simpleUML_MM_Attribute = simpleUML_MM_Attribute
        
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
    def simpleUML_MM_Attribute(self):
        return self.__simpleUML_MM_Attribute

    @simpleUML_MM_Attribute.setter
    def simpleUML_MM_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Attribute__simpleUML_MM_Attribute", None)
        self.__simpleUML_MM_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Classifier"):
                opp_val = getattr(old_value, "simpleUML_MM_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Classifier"):
                opp_val = getattr(value, "simpleUML_MM_Classifier", None)
                setattr(value, "simpleUML_MM_Classifier", self)

    @property
    def simpleUML_MM_Attribute7(self):
        return self.__simpleUML_MM_Attribute7

    @simpleUML_MM_Attribute7.setter
    def simpleUML_MM_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Attribute__simpleUML_MM_Attribute7", None)
        self.__simpleUML_MM_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Class6"):
                opp_val = getattr(old_value, "simpleUML_MM_Class6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Class6"):
                opp_val = getattr(value, "simpleUML_MM_Class6", None)
                if opp_val is None:
                    setattr(value, "simpleUML_MM_Class6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleUML_MM_Class(Classifier):

    def __init__(self, is_persistent: bool, simpleUML_MM_Class6: set["simpleUML_MM_Attribute"] = None, simpleUML_MM_Class10: "simpleUML_MM_Class" = None, simpleUML_MM_Class8: "simpleUML_MM_Class" = None, simpleUML_MM_Class: "simpleUML_MM_Association" = None, simpleUML_MM_Class3: "simpleUML_MM_Association" = None):
        self.is_persistent = is_persistent
        self.simpleUML_MM_Class6 = simpleUML_MM_Class6 if simpleUML_MM_Class6 is not None else set()
        self.simpleUML_MM_Class10 = simpleUML_MM_Class10
        self.simpleUML_MM_Class8 = simpleUML_MM_Class8
        self.simpleUML_MM_Class = simpleUML_MM_Class
        self.simpleUML_MM_Class3 = simpleUML_MM_Class3
        
    @property
    def is_persistent(self) -> bool:
        return self.__is_persistent

    @is_persistent.setter
    def is_persistent(self, is_persistent: bool):
        self.__is_persistent = is_persistent

    @property
    def simpleUML_MM_Class(self):
        return self.__simpleUML_MM_Class

    @simpleUML_MM_Class.setter
    def simpleUML_MM_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Class__simpleUML_MM_Class", None)
        self.__simpleUML_MM_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Association"):
                opp_val = getattr(old_value, "simpleUML_MM_Association", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Association"):
                opp_val = getattr(value, "simpleUML_MM_Association", None)
                setattr(value, "simpleUML_MM_Association", self)

    @property
    def simpleUML_MM_Class10(self):
        return self.__simpleUML_MM_Class10

    @simpleUML_MM_Class10.setter
    def simpleUML_MM_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Class__simpleUML_MM_Class10", None)
        self.__simpleUML_MM_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Class8"):
                opp_val = getattr(old_value, "simpleUML_MM_Class8", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Class8"):
                opp_val = getattr(value, "simpleUML_MM_Class8", None)
                setattr(value, "simpleUML_MM_Class8", self)

    @property
    def simpleUML_MM_Class3(self):
        return self.__simpleUML_MM_Class3

    @simpleUML_MM_Class3.setter
    def simpleUML_MM_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Class__simpleUML_MM_Class3", None)
        self.__simpleUML_MM_Class3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Association2"):
                opp_val = getattr(old_value, "simpleUML_MM_Association2", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Association2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Association2"):
                opp_val = getattr(value, "simpleUML_MM_Association2", None)
                setattr(value, "simpleUML_MM_Association2", self)

    @property
    def simpleUML_MM_Class6(self):
        return self.__simpleUML_MM_Class6

    @simpleUML_MM_Class6.setter
    def simpleUML_MM_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Class__simpleUML_MM_Class6", None)
        self.__simpleUML_MM_Class6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleUML_MM_Attribute7"):
                    opp_val = getattr(item, "simpleUML_MM_Attribute7", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleUML_MM_Attribute7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleUML_MM_Attribute7"):
                    opp_val = getattr(item, "simpleUML_MM_Attribute7", None)
                    
                    setattr(item, "simpleUML_MM_Attribute7", self)
                    

    @property
    def simpleUML_MM_Class8(self):
        return self.__simpleUML_MM_Class8

    @simpleUML_MM_Class8.setter
    def simpleUML_MM_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Class__simpleUML_MM_Class8", None)
        self.__simpleUML_MM_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Class10"):
                opp_val = getattr(old_value, "simpleUML_MM_Class10", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Class10"):
                opp_val = getattr(value, "simpleUML_MM_Class10", None)
                setattr(value, "simpleUML_MM_Class10", self)

class simpleUML_MM_Association:

    def __init__(self, name: str, simpleUML_MM_Association: "simpleUML_MM_Class" = None, simpleUML_MM_Association2: "simpleUML_MM_Class" = None, simpleUML_MM_Association15: "simpleUML_MM_ClassModel" = None):
        self.name = name
        self.simpleUML_MM_Association = simpleUML_MM_Association
        self.simpleUML_MM_Association2 = simpleUML_MM_Association2
        self.simpleUML_MM_Association15 = simpleUML_MM_Association15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleUML_MM_Association(self):
        return self.__simpleUML_MM_Association

    @simpleUML_MM_Association.setter
    def simpleUML_MM_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Association__simpleUML_MM_Association", None)
        self.__simpleUML_MM_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Class"):
                opp_val = getattr(old_value, "simpleUML_MM_Class", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Class"):
                opp_val = getattr(value, "simpleUML_MM_Class", None)
                setattr(value, "simpleUML_MM_Class", self)

    @property
    def simpleUML_MM_Association2(self):
        return self.__simpleUML_MM_Association2

    @simpleUML_MM_Association2.setter
    def simpleUML_MM_Association2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Association__simpleUML_MM_Association2", None)
        self.__simpleUML_MM_Association2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Class3"):
                opp_val = getattr(old_value, "simpleUML_MM_Class3", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Class3"):
                opp_val = getattr(value, "simpleUML_MM_Class3", None)
                setattr(value, "simpleUML_MM_Class3", self)

    @property
    def simpleUML_MM_Association15(self):
        return self.__simpleUML_MM_Association15

    @simpleUML_MM_Association15.setter
    def simpleUML_MM_Association15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Association__simpleUML_MM_Association15", None)
        self.__simpleUML_MM_Association15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_ClassModel14"):
                opp_val = getattr(old_value, "simpleUML_MM_ClassModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_ClassModel14"):
                opp_val = getattr(value, "simpleUML_MM_ClassModel14", None)
                if opp_val is None:
                    setattr(value, "simpleUML_MM_ClassModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleUML_MM_Classifier(ABC):

    def __init__(self, name: str, simpleUML_MM_Classifier12: "simpleUML_MM_ClassModel" = None, simpleUML_MM_Classifier: "simpleUML_MM_Attribute" = None):
        self.name = name
        self.simpleUML_MM_Classifier12 = simpleUML_MM_Classifier12
        self.simpleUML_MM_Classifier = simpleUML_MM_Classifier
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleUML_MM_Classifier12(self):
        return self.__simpleUML_MM_Classifier12

    @simpleUML_MM_Classifier12.setter
    def simpleUML_MM_Classifier12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Classifier__simpleUML_MM_Classifier12", None)
        self.__simpleUML_MM_Classifier12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_ClassModel"):
                opp_val = getattr(old_value, "simpleUML_MM_ClassModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_ClassModel"):
                opp_val = getattr(value, "simpleUML_MM_ClassModel", None)
                if opp_val is None:
                    setattr(value, "simpleUML_MM_ClassModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleUML_MM_Classifier(self):
        return self.__simpleUML_MM_Classifier

    @simpleUML_MM_Classifier.setter
    def simpleUML_MM_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleUML_MM_Classifier__simpleUML_MM_Classifier", None)
        self.__simpleUML_MM_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleUML_MM_Attribute"):
                opp_val = getattr(old_value, "simpleUML_MM_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "simpleUML_MM_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleUML_MM_Attribute"):
                opp_val = getattr(value, "simpleUML_MM_Attribute", None)
                setattr(value, "simpleUML_MM_Attribute", self)

class simpleUML_MM_ClassModel:

    pass
class simpleUML_MM_PrimitiveDataType(Classifier):

    pass