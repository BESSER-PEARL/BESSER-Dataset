from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class smalluml_Package:

    pass
class smalluml_Cardinality:

    def __init__(self, lowerBound: int, upperBound: int, smalluml_Cardinality: "smalluml_Relation" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.smalluml_Cardinality = smalluml_Cardinality
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def smalluml_Cardinality(self):
        return self.__smalluml_Cardinality

    @smalluml_Cardinality.setter
    def smalluml_Cardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinality__smalluml_Cardinality", None)
        self.__smalluml_Cardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Relation"):
                opp_val = getattr(old_value, "smalluml_Relation", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Relation"):
                opp_val = getattr(value, "smalluml_Relation", None)
                setattr(value, "smalluml_Relation", self)

class smalluml_EnumerationElement:

    def __init__(self, value: str, smalluml_EnumerationElement: "smalluml_Enumeration" = None):
        self.value = value
        self.smalluml_EnumerationElement = smalluml_EnumerationElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def smalluml_EnumerationElement(self):
        return self.__smalluml_EnumerationElement

    @smalluml_EnumerationElement.setter
    def smalluml_EnumerationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_EnumerationElement__smalluml_EnumerationElement", None)
        self.__smalluml_EnumerationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Enumeration"):
                opp_val = getattr(old_value, "smalluml_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Enumeration"):
                opp_val = getattr(value, "smalluml_Enumeration", None)
                if opp_val is None:
                    setattr(value, "smalluml_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class smalluml_ConcreteType(Type):

    pass
class smalluml_Enumeration(Type):

    pass
class smalluml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class smalluml_Attribute(NamedElement):

    pass
class smalluml_Class(NamedElement):

    def __init__(self, isAbstract: bool, smalluml_Class: set["smalluml_Attribute"] = None, smalluml_Class3: set["smalluml_Method"] = None, smalluml_Class6: "smalluml_Class" = None, smalluml_Class4: set["smalluml_Class"] = None, smalluml_Class18: "smalluml_Relation" = None, smalluml_Class21: "smalluml_Relation" = None, smalluml_Class23: "smalluml_Package" = None):
        self.isAbstract = isAbstract
        self.smalluml_Class = smalluml_Class if smalluml_Class is not None else set()
        self.smalluml_Class3 = smalluml_Class3 if smalluml_Class3 is not None else set()
        self.smalluml_Class6 = smalluml_Class6
        self.smalluml_Class4 = smalluml_Class4 if smalluml_Class4 is not None else set()
        self.smalluml_Class18 = smalluml_Class18
        self.smalluml_Class21 = smalluml_Class21
        self.smalluml_Class23 = smalluml_Class23
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def smalluml_Class21(self):
        return self.__smalluml_Class21

    @smalluml_Class21.setter
    def smalluml_Class21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class21", None)
        self.__smalluml_Class21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Relation20"):
                opp_val = getattr(old_value, "smalluml_Relation20", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Relation20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Relation20"):
                opp_val = getattr(value, "smalluml_Relation20", None)
                setattr(value, "smalluml_Relation20", self)

    @property
    def smalluml_Class4(self):
        return self.__smalluml_Class4

    @smalluml_Class4.setter
    def smalluml_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class4", None)
        self.__smalluml_Class4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Class6"):
                    opp_val = getattr(item, "smalluml_Class6", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Class6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Class6"):
                    opp_val = getattr(item, "smalluml_Class6", None)
                    
                    setattr(item, "smalluml_Class6", self)
                    

    @property
    def smalluml_Class23(self):
        return self.__smalluml_Class23

    @smalluml_Class23.setter
    def smalluml_Class23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class23", None)
        self.__smalluml_Class23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Package"):
                opp_val = getattr(old_value, "smalluml_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Package"):
                opp_val = getattr(value, "smalluml_Package", None)
                if opp_val is None:
                    setattr(value, "smalluml_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Class6(self):
        return self.__smalluml_Class6

    @smalluml_Class6.setter
    def smalluml_Class6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class6", None)
        self.__smalluml_Class6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class4"):
                opp_val = getattr(old_value, "smalluml_Class4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class4"):
                opp_val = getattr(value, "smalluml_Class4", None)
                if opp_val is None:
                    setattr(value, "smalluml_Class4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Class18(self):
        return self.__smalluml_Class18

    @smalluml_Class18.setter
    def smalluml_Class18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class18", None)
        self.__smalluml_Class18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Relation17"):
                opp_val = getattr(old_value, "smalluml_Relation17", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Relation17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Relation17"):
                opp_val = getattr(value, "smalluml_Relation17", None)
                setattr(value, "smalluml_Relation17", self)

    @property
    def smalluml_Class3(self):
        return self.__smalluml_Class3

    @smalluml_Class3.setter
    def smalluml_Class3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class3", None)
        self.__smalluml_Class3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Method"):
                    opp_val = getattr(item, "smalluml_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Method"):
                    opp_val = getattr(item, "smalluml_Method", None)
                    
                    setattr(item, "smalluml_Method", self)
                    

    @property
    def smalluml_Class(self):
        return self.__smalluml_Class

    @smalluml_Class.setter
    def smalluml_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Class__smalluml_Class", None)
        self.__smalluml_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    setattr(item, "smalluml_Attribute", self)
                    

class smalluml_Relation(NamedElement):

    pass
class smalluml_Method(NamedElement):

    pass
class smalluml_Type(NamedElement):

    pass