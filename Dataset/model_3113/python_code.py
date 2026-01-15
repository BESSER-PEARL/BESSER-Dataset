from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class simpleClass_PrimitiveDataType(Classifier):

    pass
class simpleClass_Attribute:

    def __init__(self, name: str, id: bool, simpleClass_Attribute: "simpleClass_Class" = None, simpleClass_Attribute14: "simpleClass_Classifier" = None):
        self.name = name
        self.id = id
        self.simpleClass_Attribute = simpleClass_Attribute
        self.simpleClass_Attribute14 = simpleClass_Attribute14
        
    @property
    def id(self) -> bool:
        return self.__id

    @id.setter
    def id(self, id: bool):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleClass_Attribute14(self):
        return self.__simpleClass_Attribute14

    @simpleClass_Attribute14.setter
    def simpleClass_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Attribute__simpleClass_Attribute14", None)
        self.__simpleClass_Attribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Classifier15"):
                opp_val = getattr(old_value, "simpleClass_Classifier15", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Classifier15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Classifier15"):
                opp_val = getattr(value, "simpleClass_Classifier15", None)
                setattr(value, "simpleClass_Classifier15", self)

    @property
    def simpleClass_Attribute(self):
        return self.__simpleClass_Attribute

    @simpleClass_Attribute.setter
    def simpleClass_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Attribute__simpleClass_Attribute", None)
        self.__simpleClass_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class12"):
                opp_val = getattr(old_value, "simpleClass_Class12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class12"):
                opp_val = getattr(value, "simpleClass_Class12", None)
                if opp_val is None:
                    setattr(value, "simpleClass_Class12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleClass_Classifier(ABC):

    def __init__(self, name: str, simpleClass_Classifier: "simpleClass_ClassModel" = None, simpleClass_Classifier15: "simpleClass_Attribute" = None):
        self.name = name
        self.simpleClass_Classifier = simpleClass_Classifier
        self.simpleClass_Classifier15 = simpleClass_Classifier15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleClass_Classifier(self):
        return self.__simpleClass_Classifier

    @simpleClass_Classifier.setter
    def simpleClass_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Classifier__simpleClass_Classifier", None)
        self.__simpleClass_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_ClassModel"):
                opp_val = getattr(old_value, "simpleClass_ClassModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_ClassModel"):
                opp_val = getattr(value, "simpleClass_ClassModel", None)
                if opp_val is None:
                    setattr(value, "simpleClass_ClassModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleClass_Classifier15(self):
        return self.__simpleClass_Classifier15

    @simpleClass_Classifier15.setter
    def simpleClass_Classifier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Classifier__simpleClass_Classifier15", None)
        self.__simpleClass_Classifier15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Attribute14"):
                opp_val = getattr(old_value, "simpleClass_Attribute14", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Attribute14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Attribute14"):
                opp_val = getattr(value, "simpleClass_Attribute14", None)
                setattr(value, "simpleClass_Attribute14", self)

class simpleClass_Class(Classifier):

    def __init__(self, persistent: bool, simpleClass_Class: "simpleClass_Association" = None, simpleClass_Class7: "simpleClass_Association" = None, simpleClass_Class10: "simpleClass_Class" = None, simpleClass_Class8: "simpleClass_Class" = None, simpleClass_Class12: set["simpleClass_Attribute"] = None):
        self.persistent = persistent
        self.simpleClass_Class = simpleClass_Class
        self.simpleClass_Class7 = simpleClass_Class7
        self.simpleClass_Class10 = simpleClass_Class10
        self.simpleClass_Class8 = simpleClass_Class8
        self.simpleClass_Class12 = simpleClass_Class12 if simpleClass_Class12 is not None else set()
        
    @property
    def persistent(self) -> bool:
        return self.__persistent

    @persistent.setter
    def persistent(self, persistent: bool):
        self.__persistent = persistent

    @property
    def simpleClass_Class(self):
        return self.__simpleClass_Class

    @simpleClass_Class.setter
    def simpleClass_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class", None)
        self.__simpleClass_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Association4"):
                opp_val = getattr(old_value, "simpleClass_Association4", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Association4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Association4"):
                opp_val = getattr(value, "simpleClass_Association4", None)
                setattr(value, "simpleClass_Association4", self)

    @property
    def simpleClass_Class7(self):
        return self.__simpleClass_Class7

    @simpleClass_Class7.setter
    def simpleClass_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class7", None)
        self.__simpleClass_Class7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Association6"):
                opp_val = getattr(old_value, "simpleClass_Association6", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Association6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Association6"):
                opp_val = getattr(value, "simpleClass_Association6", None)
                setattr(value, "simpleClass_Association6", self)

    @property
    def simpleClass_Class12(self):
        return self.__simpleClass_Class12

    @simpleClass_Class12.setter
    def simpleClass_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class12", None)
        self.__simpleClass_Class12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleClass_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleClass_Attribute"):
                    opp_val = getattr(item, "simpleClass_Attribute", None)
                    
                    setattr(item, "simpleClass_Attribute", self)
                    

    @property
    def simpleClass_Class10(self):
        return self.__simpleClass_Class10

    @simpleClass_Class10.setter
    def simpleClass_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class10", None)
        self.__simpleClass_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class8"):
                opp_val = getattr(old_value, "simpleClass_Class8", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Class8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class8"):
                opp_val = getattr(value, "simpleClass_Class8", None)
                setattr(value, "simpleClass_Class8", self)

    @property
    def simpleClass_Class8(self):
        return self.__simpleClass_Class8

    @simpleClass_Class8.setter
    def simpleClass_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Class__simpleClass_Class8", None)
        self.__simpleClass_Class8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class10"):
                opp_val = getattr(old_value, "simpleClass_Class10", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class10"):
                opp_val = getattr(value, "simpleClass_Class10", None)
                setattr(value, "simpleClass_Class10", self)

class simpleClass_Association:

    def __init__(self, name: str, simpleClass_Association: "simpleClass_ClassModel" = None, simpleClass_Association4: "simpleClass_Class" = None, simpleClass_Association6: "simpleClass_Class" = None):
        self.name = name
        self.simpleClass_Association = simpleClass_Association
        self.simpleClass_Association4 = simpleClass_Association4
        self.simpleClass_Association6 = simpleClass_Association6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleClass_Association6(self):
        return self.__simpleClass_Association6

    @simpleClass_Association6.setter
    def simpleClass_Association6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Association__simpleClass_Association6", None)
        self.__simpleClass_Association6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class7"):
                opp_val = getattr(old_value, "simpleClass_Class7", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Class7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class7"):
                opp_val = getattr(value, "simpleClass_Class7", None)
                setattr(value, "simpleClass_Class7", self)

    @property
    def simpleClass_Association4(self):
        return self.__simpleClass_Association4

    @simpleClass_Association4.setter
    def simpleClass_Association4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Association__simpleClass_Association4", None)
        self.__simpleClass_Association4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_Class"):
                opp_val = getattr(old_value, "simpleClass_Class", None)
                if opp_val == self:
                    setattr(old_value, "simpleClass_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_Class"):
                opp_val = getattr(value, "simpleClass_Class", None)
                setattr(value, "simpleClass_Class", self)

    @property
    def simpleClass_Association(self):
        return self.__simpleClass_Association

    @simpleClass_Association.setter
    def simpleClass_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleClass_Association__simpleClass_Association", None)
        self.__simpleClass_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleClass_ClassModel2"):
                opp_val = getattr(old_value, "simpleClass_ClassModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleClass_ClassModel2"):
                opp_val = getattr(value, "simpleClass_ClassModel2", None)
                if opp_val is None:
                    setattr(value, "simpleClass_ClassModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleClass_ClassModel:

    pass