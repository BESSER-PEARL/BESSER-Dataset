from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class simpleuml_Classifier(ABC):

    pass
class Classifier:

    pass
class simpleuml_Class(Classifier):

    def __init__(self, name: str, simpleuml_Class: set["simpleuml_Classifier"] = None):
        self.name = name
        self.simpleuml_Class = simpleuml_Class if simpleuml_Class is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simpleuml_Class(self):
        return self.__simpleuml_Class

    @simpleuml_Class.setter
    def simpleuml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleuml_Class__simpleuml_Class", None)
        self.__simpleuml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simpleuml_Classifier"):
                    opp_val = getattr(item, "simpleuml_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "simpleuml_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simpleuml_Classifier"):
                    opp_val = getattr(item, "simpleuml_Classifier", None)
                    
                    setattr(item, "simpleuml_Classifier", self)
                    
