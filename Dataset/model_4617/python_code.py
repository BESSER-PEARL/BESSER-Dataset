from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class Elements_ReferencingNode(Node):

    pass
class Element:

    pass
class Elements_StrictElement(Element):

    def __init__(self, sValue: int, sValues: int, Elements_StrictElement44: "Elements_Element" = None, Elements_StrictElement47: set["Elements_Element"] = None, Elements_StrictElement50: "Elements_Element" = None, StrictElement: "Elements_StrictElement" = None, sSingleFromManyRef: set["Elements_StrictElement"] = None, StrictElement56: "Elements_StrictElement" = None, sManyFromSingleRef: "Elements_StrictElement" = None, StrictElement59: "Elements_StrictElement" = None, sManyFromManyRef2: set["Elements_StrictElement"] = None, StrictElement62: "Elements_StrictElement" = None, sManyFromManyRef1: set["Elements_StrictElement"] = None, Elements_StrictElement: set["Elements_Element"] = None):
        self.sValue = sValue
        self.sValues = sValues
        self.Elements_StrictElement44 = Elements_StrictElement44
        self.Elements_StrictElement47 = Elements_StrictElement47 if Elements_StrictElement47 is not None else set()
        self.Elements_StrictElement50 = Elements_StrictElement50
        self.StrictElement = StrictElement
        self.sSingleFromManyRef = sSingleFromManyRef if sSingleFromManyRef is not None else set()
        self.StrictElement56 = StrictElement56
        self.sManyFromSingleRef = sManyFromSingleRef
        self.StrictElement59 = StrictElement59
        self.sManyFromManyRef2 = sManyFromManyRef2 if sManyFromManyRef2 is not None else set()
        self.StrictElement62 = StrictElement62
        self.sManyFromManyRef1 = sManyFromManyRef1 if sManyFromManyRef1 is not None else set()
        self.Elements_StrictElement = Elements_StrictElement if Elements_StrictElement is not None else set()
        
    @property
    def sValues(self) -> int:
        return self.__sValues

    @sValues.setter
    def sValues(self, sValues: int):
        self.__sValues = sValues

    @property
    def sValue(self) -> int:
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: int):
        self.__sValue = sValue

    @property
    def StrictElement59(self):
        return self.__StrictElement59

    @StrictElement59.setter
    def StrictElement59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__StrictElement59", None)
        self.__StrictElement59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sManyFromManyRef2"):
                opp_val = getattr(old_value, "sManyFromManyRef2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sManyFromManyRef2"):
                opp_val = getattr(value, "sManyFromManyRef2", None)
                if opp_val is None:
                    setattr(value, "sManyFromManyRef2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_StrictElement44(self):
        return self.__Elements_StrictElement44

    @Elements_StrictElement44.setter
    def Elements_StrictElement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__Elements_StrictElement44", None)
        self.__Elements_StrictElement44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element45"):
                opp_val = getattr(old_value, "Elements_Element45", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element45"):
                opp_val = getattr(value, "Elements_Element45", None)
                setattr(value, "Elements_Element45", self)

    @property
    def StrictElement62(self):
        return self.__StrictElement62

    @StrictElement62.setter
    def StrictElement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__StrictElement62", None)
        self.__StrictElement62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sManyFromManyRef1"):
                opp_val = getattr(old_value, "sManyFromManyRef1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sManyFromManyRef1"):
                opp_val = getattr(value, "sManyFromManyRef1", None)
                if opp_val is None:
                    setattr(value, "sManyFromManyRef1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_StrictElement50(self):
        return self.__Elements_StrictElement50

    @Elements_StrictElement50.setter
    def Elements_StrictElement50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__Elements_StrictElement50", None)
        self.__Elements_StrictElement50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element51"):
                opp_val = getattr(old_value, "Elements_Element51", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element51"):
                opp_val = getattr(value, "Elements_Element51", None)
                setattr(value, "Elements_Element51", self)

    @property
    def sManyFromManyRef2(self):
        return self.__sManyFromManyRef2

    @sManyFromManyRef2.setter
    def sManyFromManyRef2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__sManyFromManyRef2", None)
        self.__sManyFromManyRef2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StrictElement59"):
                    opp_val = getattr(item, "StrictElement59", None)
                    
                    if opp_val == self:
                        setattr(item, "StrictElement59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StrictElement59"):
                    opp_val = getattr(item, "StrictElement59", None)
                    
                    setattr(item, "StrictElement59", self)
                    

    @property
    def StrictElement56(self):
        return self.__StrictElement56

    @StrictElement56.setter
    def StrictElement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__StrictElement56", None)
        self.__StrictElement56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sManyFromSingleRef"):
                opp_val = getattr(old_value, "sManyFromSingleRef", None)
                if opp_val == self:
                    setattr(old_value, "sManyFromSingleRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sManyFromSingleRef"):
                opp_val = getattr(value, "sManyFromSingleRef", None)
                setattr(value, "sManyFromSingleRef", self)

    @property
    def sSingleFromManyRef(self):
        return self.__sSingleFromManyRef

    @sSingleFromManyRef.setter
    def sSingleFromManyRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__sSingleFromManyRef", None)
        self.__sSingleFromManyRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StrictElement"):
                    opp_val = getattr(item, "StrictElement", None)
                    
                    if opp_val == self:
                        setattr(item, "StrictElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StrictElement"):
                    opp_val = getattr(item, "StrictElement", None)
                    
                    setattr(item, "StrictElement", self)
                    

    @property
    def StrictElement(self):
        return self.__StrictElement

    @StrictElement.setter
    def StrictElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__StrictElement", None)
        self.__StrictElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sSingleFromManyRef"):
                opp_val = getattr(old_value, "sSingleFromManyRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sSingleFromManyRef"):
                opp_val = getattr(value, "sSingleFromManyRef", None)
                if opp_val is None:
                    setattr(value, "sSingleFromManyRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_StrictElement(self):
        return self.__Elements_StrictElement

    @Elements_StrictElement.setter
    def Elements_StrictElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__Elements_StrictElement", None)
        self.__Elements_StrictElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_Element42"):
                    opp_val = getattr(item, "Elements_Element42", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_Element42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_Element42"):
                    opp_val = getattr(item, "Elements_Element42", None)
                    
                    setattr(item, "Elements_Element42", self)
                    

    @property
    def sManyFromSingleRef(self):
        return self.__sManyFromSingleRef

    @sManyFromSingleRef.setter
    def sManyFromSingleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__sManyFromSingleRef", None)
        self.__sManyFromSingleRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StrictElement56"):
                opp_val = getattr(old_value, "StrictElement56", None)
                if opp_val == self:
                    setattr(old_value, "StrictElement56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StrictElement56"):
                opp_val = getattr(value, "StrictElement56", None)
                setattr(value, "StrictElement56", self)

    @property
    def Elements_StrictElement47(self):
        return self.__Elements_StrictElement47

    @Elements_StrictElement47.setter
    def Elements_StrictElement47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__Elements_StrictElement47", None)
        self.__Elements_StrictElement47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_Element48"):
                    opp_val = getattr(item, "Elements_Element48", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_Element48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_Element48"):
                    opp_val = getattr(item, "Elements_Element48", None)
                    
                    setattr(item, "Elements_Element48", self)
                    

    @property
    def sManyFromManyRef1(self):
        return self.__sManyFromManyRef1

    @sManyFromManyRef1.setter
    def sManyFromManyRef1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_StrictElement__sManyFromManyRef1", None)
        self.__sManyFromManyRef1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StrictElement62"):
                    opp_val = getattr(item, "StrictElement62", None)
                    
                    if opp_val == self:
                        setattr(item, "StrictElement62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StrictElement62"):
                    opp_val = getattr(item, "StrictElement62", None)
                    
                    setattr(item, "StrictElement62", self)
                    

class IdentifiedElement:

    pass
class Elements_Root(IdentifiedElement):

    def __init__(self, name: str, Elements_Root: set["Elements_NamedElement"] = None):
        self.name = name
        self.Elements_Root = Elements_Root if Elements_Root is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Elements_Root(self):
        return self.__Elements_Root

    @Elements_Root.setter
    def Elements_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Root__Elements_Root", None)
        self.__Elements_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_NamedElement"):
                    opp_val = getattr(item, "Elements_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_NamedElement"):
                    opp_val = getattr(item, "Elements_NamedElement", None)
                    
                    setattr(item, "Elements_NamedElement", self)
                    

class Elements_NamedElement(IdentifiedElement):

    def __init__(self, name: str, Elements_NamedElement: "Elements_Root" = None, Elements_NamedElement67: "Elements_Node" = None):
        self.name = name
        self.Elements_NamedElement = Elements_NamedElement
        self.Elements_NamedElement67 = Elements_NamedElement67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Elements_NamedElement(self):
        return self.__Elements_NamedElement

    @Elements_NamedElement.setter
    def Elements_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_NamedElement__Elements_NamedElement", None)
        self.__Elements_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Root"):
                opp_val = getattr(old_value, "Elements_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Root"):
                opp_val = getattr(value, "Elements_Root", None)
                if opp_val is None:
                    setattr(value, "Elements_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_NamedElement67(self):
        return self.__Elements_NamedElement67

    @Elements_NamedElement67.setter
    def Elements_NamedElement67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_NamedElement__Elements_NamedElement67", None)
        self.__Elements_NamedElement67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Node"):
                opp_val = getattr(old_value, "Elements_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Node"):
                opp_val = getattr(value, "Elements_Node", None)
                if opp_val is None:
                    setattr(value, "Elements_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class Elements_Edge(NamedElement):

    pass
class Elements_Node(NamedElement):

    pass
class Elements_Element(NamedElement):

    def __init__(self, value: int, values: int, Elements_Element: "Elements_Element" = None, Elements_Element1: set["Elements_Element"] = None, Elements_Element5: "Elements_Element" = None, Elements_Element3: "Elements_Element" = None, Element: "Elements_Element" = None, upFromManyContent: set["Elements_Element"] = None, Element10: "Elements_Element" = None, manyContentWithUp: "Elements_Element" = None, Element13: "Elements_Element" = None, upFromSingleContent: "Elements_Element" = None, Element16: "Elements_Element" = None, singleContentWithUp: "Elements_Element" = None, Elements_Element19: "Elements_Element" = None, Elements_Element17: set["Elements_Element"] = None, Elements_Element22: "Elements_Element" = None, Elements_Element20: "Elements_Element" = None, Element25: "Elements_Element" = None, singleFromSingleRef2: "Elements_Element" = None, Element28: "Elements_Element" = None, singleFromSingleRef1: "Elements_Element" = None, Element31: "Elements_Element" = None, singleFromManyRef: set["Elements_Element"] = None, Element34: "Elements_Element" = None, manyFromSingleRef: "Elements_Element" = None, Element37: "Elements_Element" = None, manyFromManyRef2: set["Elements_Element"] = None, Element40: "Elements_Element" = None, manyFromManyRef1: set["Elements_Element"] = None, Elements_Element48: "Elements_StrictElement" = None, Elements_Element51: "Elements_StrictElement" = None, Elements_Element42: "Elements_StrictElement" = None, Elements_Element45: "Elements_StrictElement" = None):
        self.value = value
        self.values = values
        self.Elements_Element = Elements_Element
        self.Elements_Element1 = Elements_Element1 if Elements_Element1 is not None else set()
        self.Elements_Element5 = Elements_Element5
        self.Elements_Element3 = Elements_Element3
        self.Element = Element
        self.upFromManyContent = upFromManyContent if upFromManyContent is not None else set()
        self.Element10 = Element10
        self.manyContentWithUp = manyContentWithUp
        self.Element13 = Element13
        self.upFromSingleContent = upFromSingleContent
        self.Element16 = Element16
        self.singleContentWithUp = singleContentWithUp
        self.Elements_Element19 = Elements_Element19
        self.Elements_Element17 = Elements_Element17 if Elements_Element17 is not None else set()
        self.Elements_Element22 = Elements_Element22
        self.Elements_Element20 = Elements_Element20
        self.Element25 = Element25
        self.singleFromSingleRef2 = singleFromSingleRef2
        self.Element28 = Element28
        self.singleFromSingleRef1 = singleFromSingleRef1
        self.Element31 = Element31
        self.singleFromManyRef = singleFromManyRef if singleFromManyRef is not None else set()
        self.Element34 = Element34
        self.manyFromSingleRef = manyFromSingleRef
        self.Element37 = Element37
        self.manyFromManyRef2 = manyFromManyRef2 if manyFromManyRef2 is not None else set()
        self.Element40 = Element40
        self.manyFromManyRef1 = manyFromManyRef1 if manyFromManyRef1 is not None else set()
        self.Elements_Element48 = Elements_Element48
        self.Elements_Element51 = Elements_Element51
        self.Elements_Element42 = Elements_Element42
        self.Elements_Element45 = Elements_Element45
        
    @property
    def values(self) -> int:
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def Elements_Element3(self):
        return self.__Elements_Element3

    @Elements_Element3.setter
    def Elements_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element3", None)
        self.__Elements_Element3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element5"):
                opp_val = getattr(old_value, "Elements_Element5", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element5"):
                opp_val = getattr(value, "Elements_Element5", None)
                setattr(value, "Elements_Element5", self)

    @property
    def singleFromSingleRef1(self):
        return self.__singleFromSingleRef1

    @singleFromSingleRef1.setter
    def singleFromSingleRef1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__singleFromSingleRef1", None)
        self.__singleFromSingleRef1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element28"):
                opp_val = getattr(old_value, "Element28", None)
                if opp_val == self:
                    setattr(old_value, "Element28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element28"):
                opp_val = getattr(value, "Element28", None)
                setattr(value, "Element28", self)

    @property
    def manyFromManyRef2(self):
        return self.__manyFromManyRef2

    @manyFromManyRef2.setter
    def manyFromManyRef2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__manyFromManyRef2", None)
        self.__manyFromManyRef2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element37"):
                    opp_val = getattr(item, "Element37", None)
                    
                    if opp_val == self:
                        setattr(item, "Element37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element37"):
                    opp_val = getattr(item, "Element37", None)
                    
                    setattr(item, "Element37", self)
                    

    @property
    def Element31(self):
        return self.__Element31

    @Element31.setter
    def Element31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element31", None)
        self.__Element31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "singleFromManyRef"):
                opp_val = getattr(old_value, "singleFromManyRef", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "singleFromManyRef"):
                opp_val = getattr(value, "singleFromManyRef", None)
                if opp_val is None:
                    setattr(value, "singleFromManyRef", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_Element19(self):
        return self.__Elements_Element19

    @Elements_Element19.setter
    def Elements_Element19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element19", None)
        self.__Elements_Element19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element17"):
                opp_val = getattr(old_value, "Elements_Element17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element17"):
                opp_val = getattr(value, "Elements_Element17", None)
                if opp_val is None:
                    setattr(value, "Elements_Element17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_Element17(self):
        return self.__Elements_Element17

    @Elements_Element17.setter
    def Elements_Element17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element17", None)
        self.__Elements_Element17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_Element19"):
                    opp_val = getattr(item, "Elements_Element19", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_Element19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_Element19"):
                    opp_val = getattr(item, "Elements_Element19", None)
                    
                    setattr(item, "Elements_Element19", self)
                    

    @property
    def Elements_Element1(self):
        return self.__Elements_Element1

    @Elements_Element1.setter
    def Elements_Element1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element1", None)
        self.__Elements_Element1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Elements_Element"):
                    opp_val = getattr(item, "Elements_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Elements_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Elements_Element"):
                    opp_val = getattr(item, "Elements_Element", None)
                    
                    setattr(item, "Elements_Element", self)
                    

    @property
    def Element25(self):
        return self.__Element25

    @Element25.setter
    def Element25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element25", None)
        self.__Element25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "singleFromSingleRef2"):
                opp_val = getattr(old_value, "singleFromSingleRef2", None)
                if opp_val == self:
                    setattr(old_value, "singleFromSingleRef2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "singleFromSingleRef2"):
                opp_val = getattr(value, "singleFromSingleRef2", None)
                setattr(value, "singleFromSingleRef2", self)

    @property
    def upFromSingleContent(self):
        return self.__upFromSingleContent

    @upFromSingleContent.setter
    def upFromSingleContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__upFromSingleContent", None)
        self.__upFromSingleContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element13"):
                opp_val = getattr(old_value, "Element13", None)
                if opp_val == self:
                    setattr(old_value, "Element13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element13"):
                opp_val = getattr(value, "Element13", None)
                setattr(value, "Element13", self)

    @property
    def Element34(self):
        return self.__Element34

    @Element34.setter
    def Element34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element34", None)
        self.__Element34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manyFromSingleRef"):
                opp_val = getattr(old_value, "manyFromSingleRef", None)
                if opp_val == self:
                    setattr(old_value, "manyFromSingleRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manyFromSingleRef"):
                opp_val = getattr(value, "manyFromSingleRef", None)
                setattr(value, "manyFromSingleRef", self)

    @property
    def Elements_Element51(self):
        return self.__Elements_Element51

    @Elements_Element51.setter
    def Elements_Element51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element51", None)
        self.__Elements_Element51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_StrictElement50"):
                opp_val = getattr(old_value, "Elements_StrictElement50", None)
                if opp_val == self:
                    setattr(old_value, "Elements_StrictElement50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_StrictElement50"):
                opp_val = getattr(value, "Elements_StrictElement50", None)
                setattr(value, "Elements_StrictElement50", self)

    @property
    def Element13(self):
        return self.__Element13

    @Element13.setter
    def Element13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element13", None)
        self.__Element13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upFromSingleContent"):
                opp_val = getattr(old_value, "upFromSingleContent", None)
                if opp_val == self:
                    setattr(old_value, "upFromSingleContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upFromSingleContent"):
                opp_val = getattr(value, "upFromSingleContent", None)
                setattr(value, "upFromSingleContent", self)

    @property
    def manyContentWithUp(self):
        return self.__manyContentWithUp

    @manyContentWithUp.setter
    def manyContentWithUp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__manyContentWithUp", None)
        self.__manyContentWithUp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element10"):
                opp_val = getattr(old_value, "Element10", None)
                if opp_val == self:
                    setattr(old_value, "Element10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element10"):
                opp_val = getattr(value, "Element10", None)
                setattr(value, "Element10", self)

    @property
    def manyFromSingleRef(self):
        return self.__manyFromSingleRef

    @manyFromSingleRef.setter
    def manyFromSingleRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__manyFromSingleRef", None)
        self.__manyFromSingleRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element34"):
                opp_val = getattr(old_value, "Element34", None)
                if opp_val == self:
                    setattr(old_value, "Element34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element34"):
                opp_val = getattr(value, "Element34", None)
                setattr(value, "Element34", self)

    @property
    def Element16(self):
        return self.__Element16

    @Element16.setter
    def Element16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element16", None)
        self.__Element16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "singleContentWithUp"):
                opp_val = getattr(old_value, "singleContentWithUp", None)
                if opp_val == self:
                    setattr(old_value, "singleContentWithUp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "singleContentWithUp"):
                opp_val = getattr(value, "singleContentWithUp", None)
                setattr(value, "singleContentWithUp", self)

    @property
    def manyFromManyRef1(self):
        return self.__manyFromManyRef1

    @manyFromManyRef1.setter
    def manyFromManyRef1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__manyFromManyRef1", None)
        self.__manyFromManyRef1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element40"):
                    opp_val = getattr(item, "Element40", None)
                    
                    if opp_val == self:
                        setattr(item, "Element40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element40"):
                    opp_val = getattr(item, "Element40", None)
                    
                    setattr(item, "Element40", self)
                    

    @property
    def Elements_Element20(self):
        return self.__Elements_Element20

    @Elements_Element20.setter
    def Elements_Element20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element20", None)
        self.__Elements_Element20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element22"):
                opp_val = getattr(old_value, "Elements_Element22", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element22"):
                opp_val = getattr(value, "Elements_Element22", None)
                setattr(value, "Elements_Element22", self)

    @property
    def Element10(self):
        return self.__Element10

    @Element10.setter
    def Element10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element10", None)
        self.__Element10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manyContentWithUp"):
                opp_val = getattr(old_value, "manyContentWithUp", None)
                if opp_val == self:
                    setattr(old_value, "manyContentWithUp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manyContentWithUp"):
                opp_val = getattr(value, "manyContentWithUp", None)
                setattr(value, "manyContentWithUp", self)

    @property
    def Elements_Element45(self):
        return self.__Elements_Element45

    @Elements_Element45.setter
    def Elements_Element45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element45", None)
        self.__Elements_Element45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_StrictElement44"):
                opp_val = getattr(old_value, "Elements_StrictElement44", None)
                if opp_val == self:
                    setattr(old_value, "Elements_StrictElement44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_StrictElement44"):
                opp_val = getattr(value, "Elements_StrictElement44", None)
                setattr(value, "Elements_StrictElement44", self)

    @property
    def Elements_Element48(self):
        return self.__Elements_Element48

    @Elements_Element48.setter
    def Elements_Element48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element48", None)
        self.__Elements_Element48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_StrictElement47"):
                opp_val = getattr(old_value, "Elements_StrictElement47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_StrictElement47"):
                opp_val = getattr(value, "Elements_StrictElement47", None)
                if opp_val is None:
                    setattr(value, "Elements_StrictElement47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upFromManyContent"):
                opp_val = getattr(old_value, "upFromManyContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upFromManyContent"):
                opp_val = getattr(value, "upFromManyContent", None)
                if opp_val is None:
                    setattr(value, "upFromManyContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Elements_Element5(self):
        return self.__Elements_Element5

    @Elements_Element5.setter
    def Elements_Element5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element5", None)
        self.__Elements_Element5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element3"):
                opp_val = getattr(old_value, "Elements_Element3", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element3"):
                opp_val = getattr(value, "Elements_Element3", None)
                setattr(value, "Elements_Element3", self)

    @property
    def Elements_Element(self):
        return self.__Elements_Element

    @Elements_Element.setter
    def Elements_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element", None)
        self.__Elements_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element1"):
                opp_val = getattr(old_value, "Elements_Element1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element1"):
                opp_val = getattr(value, "Elements_Element1", None)
                if opp_val is None:
                    setattr(value, "Elements_Element1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def singleContentWithUp(self):
        return self.__singleContentWithUp

    @singleContentWithUp.setter
    def singleContentWithUp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__singleContentWithUp", None)
        self.__singleContentWithUp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element16"):
                opp_val = getattr(old_value, "Element16", None)
                if opp_val == self:
                    setattr(old_value, "Element16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element16"):
                opp_val = getattr(value, "Element16", None)
                setattr(value, "Element16", self)

    @property
    def Elements_Element42(self):
        return self.__Elements_Element42

    @Elements_Element42.setter
    def Elements_Element42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element42", None)
        self.__Elements_Element42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_StrictElement"):
                opp_val = getattr(old_value, "Elements_StrictElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_StrictElement"):
                opp_val = getattr(value, "Elements_StrictElement", None)
                if opp_val is None:
                    setattr(value, "Elements_StrictElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def singleFromManyRef(self):
        return self.__singleFromManyRef

    @singleFromManyRef.setter
    def singleFromManyRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__singleFromManyRef", None)
        self.__singleFromManyRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element31"):
                    opp_val = getattr(item, "Element31", None)
                    
                    if opp_val == self:
                        setattr(item, "Element31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element31"):
                    opp_val = getattr(item, "Element31", None)
                    
                    setattr(item, "Element31", self)
                    

    @property
    def Elements_Element22(self):
        return self.__Elements_Element22

    @Elements_Element22.setter
    def Elements_Element22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Elements_Element22", None)
        self.__Elements_Element22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Elements_Element20"):
                opp_val = getattr(old_value, "Elements_Element20", None)
                if opp_val == self:
                    setattr(old_value, "Elements_Element20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Elements_Element20"):
                opp_val = getattr(value, "Elements_Element20", None)
                setattr(value, "Elements_Element20", self)

    @property
    def singleFromSingleRef2(self):
        return self.__singleFromSingleRef2

    @singleFromSingleRef2.setter
    def singleFromSingleRef2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__singleFromSingleRef2", None)
        self.__singleFromSingleRef2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element25"):
                opp_val = getattr(old_value, "Element25", None)
                if opp_val == self:
                    setattr(old_value, "Element25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element25"):
                opp_val = getattr(value, "Element25", None)
                setattr(value, "Element25", self)

    @property
    def Element28(self):
        return self.__Element28

    @Element28.setter
    def Element28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element28", None)
        self.__Element28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "singleFromSingleRef1"):
                opp_val = getattr(old_value, "singleFromSingleRef1", None)
                if opp_val == self:
                    setattr(old_value, "singleFromSingleRef1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "singleFromSingleRef1"):
                opp_val = getattr(value, "singleFromSingleRef1", None)
                setattr(value, "singleFromSingleRef1", self)

    @property
    def Element40(self):
        return self.__Element40

    @Element40.setter
    def Element40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element40", None)
        self.__Element40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manyFromManyRef1"):
                opp_val = getattr(old_value, "manyFromManyRef1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manyFromManyRef1"):
                opp_val = getattr(value, "manyFromManyRef1", None)
                if opp_val is None:
                    setattr(value, "manyFromManyRef1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def upFromManyContent(self):
        return self.__upFromManyContent

    @upFromManyContent.setter
    def upFromManyContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__upFromManyContent", None)
        self.__upFromManyContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def Element37(self):
        return self.__Element37

    @Element37.setter
    def Element37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elements_Element__Element37", None)
        self.__Element37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manyFromManyRef2"):
                opp_val = getattr(old_value, "manyFromManyRef2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manyFromManyRef2"):
                opp_val = getattr(value, "manyFromManyRef2", None)
                if opp_val is None:
                    setattr(value, "manyFromManyRef2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Elements_IdentifiedElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
