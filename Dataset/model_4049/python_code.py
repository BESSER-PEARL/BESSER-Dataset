from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class necsis14_classdiagram__QColumn(NamedElement):

    pass
class necsis14_classdiagram_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class necsis14_classdiagram__QTable(NamedElement):

    pass
class necsis14_classdiagram_Association(NamedElement):

    def __init__(self, lowerBound: int, upperBound: int, necsis14_classdiagram_Association11: "necsis14_classdiagram_Class" = None, necsis14_classdiagram_Association14: "necsis14_classdiagram_Class" = None, necsis14_classdiagram_Association: "necsis14_classdiagram_ClassDiagram" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.necsis14_classdiagram_Association11 = necsis14_classdiagram_Association11
        self.necsis14_classdiagram_Association14 = necsis14_classdiagram_Association14
        self.necsis14_classdiagram_Association = necsis14_classdiagram_Association
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def necsis14_classdiagram_Association(self):
        return self.__necsis14_classdiagram_Association

    @necsis14_classdiagram_Association.setter
    def necsis14_classdiagram_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_necsis14_classdiagram_Association__necsis14_classdiagram_Association", None)
        self.__necsis14_classdiagram_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "necsis14_classdiagram_ClassDiagram2"):
                opp_val = getattr(old_value, "necsis14_classdiagram_ClassDiagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "necsis14_classdiagram_ClassDiagram2"):
                opp_val = getattr(value, "necsis14_classdiagram_ClassDiagram2", None)
                if opp_val is None:
                    setattr(value, "necsis14_classdiagram_ClassDiagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def necsis14_classdiagram_Association14(self):
        return self.__necsis14_classdiagram_Association14

    @necsis14_classdiagram_Association14.setter
    def necsis14_classdiagram_Association14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_necsis14_classdiagram_Association__necsis14_classdiagram_Association14", None)
        self.__necsis14_classdiagram_Association14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "necsis14_classdiagram_Class15"):
                opp_val = getattr(old_value, "necsis14_classdiagram_Class15", None)
                if opp_val == self:
                    setattr(old_value, "necsis14_classdiagram_Class15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "necsis14_classdiagram_Class15"):
                opp_val = getattr(value, "necsis14_classdiagram_Class15", None)
                setattr(value, "necsis14_classdiagram_Class15", self)

    @property
    def necsis14_classdiagram_Association11(self):
        return self.__necsis14_classdiagram_Association11

    @necsis14_classdiagram_Association11.setter
    def necsis14_classdiagram_Association11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_necsis14_classdiagram_Association__necsis14_classdiagram_Association11", None)
        self.__necsis14_classdiagram_Association11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "necsis14_classdiagram_Class12"):
                opp_val = getattr(old_value, "necsis14_classdiagram_Class12", None)
                if opp_val == self:
                    setattr(old_value, "necsis14_classdiagram_Class12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "necsis14_classdiagram_Class12"):
                opp_val = getattr(value, "necsis14_classdiagram_Class12", None)
                setattr(value, "necsis14_classdiagram_Class12", self)

class necsis14_classdiagram_Class(NamedElement):

    pass
class necsis14_classdiagram_ClassDiagram:

    pass
class necsis14_classdiagram_Attribute(NamedElement):

    pass