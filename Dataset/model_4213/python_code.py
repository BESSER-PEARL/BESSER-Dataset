from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MyAbstractElement:

    pass
class mydsl_MyReference(MyAbstractElement):

    pass
class mydsl_MyElement(MyAbstractElement):

    def __init__(self, name: str, mydsl_MyElement: "mydsl_MyReference" = None):
        self.name = name
        self.mydsl_MyElement = mydsl_MyElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_MyElement(self):
        return self.__mydsl_MyElement

    @mydsl_MyElement.setter
    def mydsl_MyElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_MyElement__mydsl_MyElement", None)
        self.__mydsl_MyElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_MyReference"):
                opp_val = getattr(old_value, "mydsl_MyReference", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_MyReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_MyReference"):
                opp_val = getattr(value, "mydsl_MyReference", None)
                setattr(value, "mydsl_MyReference", self)

class mydsl_MyAbstractElement(ABC):

    pass
class mydsl_MyModel:

    def __init__(self, name: str, mydsl_MyModel: set["mydsl_MyAbstractElement"] = None):
        self.name = name
        self.mydsl_MyModel = mydsl_MyModel if mydsl_MyModel is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_MyModel(self):
        return self.__mydsl_MyModel

    @mydsl_MyModel.setter
    def mydsl_MyModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_MyModel__mydsl_MyModel", None)
        self.__mydsl_MyModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_MyAbstractElement"):
                    opp_val = getattr(item, "mydsl_MyAbstractElement", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_MyAbstractElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_MyAbstractElement"):
                    opp_val = getattr(item, "mydsl_MyAbstractElement", None)
                    
                    setattr(item, "mydsl_MyAbstractElement", self)
                    
