from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MTpre__Person:

    pass
class ramRoot_MTpre__Woman(MTpre__Person):

    pass
class ramRoot_MTpre__Man(MTpre__Person):

    pass
class MTpre__Element:

    pass
class ramRoot_MTpre__Classroom(MTpre__Element):

    def __init__(self, id: str, ramRoot_MTpre__Classroom: "ramRoot_MTpre__Person" = None, ramRoot_MTpre__Classroom13: set["ramRoot_MTpre__Person"] = None):
        self.id = id
        self.ramRoot_MTpre__Classroom = ramRoot_MTpre__Classroom
        self.ramRoot_MTpre__Classroom13 = ramRoot_MTpre__Classroom13 if ramRoot_MTpre__Classroom13 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ramRoot_MTpre__Classroom(self):
        return self.__ramRoot_MTpre__Classroom

    @ramRoot_MTpre__Classroom.setter
    def ramRoot_MTpre__Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Classroom__ramRoot_MTpre__Classroom", None)
        self.__ramRoot_MTpre__Classroom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Person"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Person", None)
                if opp_val == self:
                    setattr(old_value, "ramRoot_MTpre__Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Person"):
                opp_val = getattr(value, "ramRoot_MTpre__Person", None)
                setattr(value, "ramRoot_MTpre__Person", self)

    @property
    def ramRoot_MTpre__Classroom13(self):
        return self.__ramRoot_MTpre__Classroom13

    @ramRoot_MTpre__Classroom13.setter
    def ramRoot_MTpre__Classroom13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Classroom__ramRoot_MTpre__Classroom13", None)
        self.__ramRoot_MTpre__Classroom13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpre__Person14"):
                    opp_val = getattr(item, "ramRoot_MTpre__Person14", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpre__Person14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpre__Person14"):
                    opp_val = getattr(item, "ramRoot_MTpre__Person14", None)
                    
                    setattr(item, "ramRoot_MTpre__Person14", self)
                    

class ramRoot_MTpre__Person(MTpre__Element):

    def __init__(self, name: str, ramRoot_MTpre__Person: "ramRoot_MTpre__Classroom" = None, ramRoot_MTpre__Person11: "ramRoot_MTpre__Person" = None, ramRoot_MTpre__Person9: set["ramRoot_MTpre__Person"] = None, ramRoot_MTpre__Person14: "ramRoot_MTpre__Classroom" = None):
        self.name = name
        self.ramRoot_MTpre__Person = ramRoot_MTpre__Person
        self.ramRoot_MTpre__Person11 = ramRoot_MTpre__Person11
        self.ramRoot_MTpre__Person9 = ramRoot_MTpre__Person9 if ramRoot_MTpre__Person9 is not None else set()
        self.ramRoot_MTpre__Person14 = ramRoot_MTpre__Person14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ramRoot_MTpre__Person11(self):
        return self.__ramRoot_MTpre__Person11

    @ramRoot_MTpre__Person11.setter
    def ramRoot_MTpre__Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Person__ramRoot_MTpre__Person11", None)
        self.__ramRoot_MTpre__Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Person9"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Person9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Person9"):
                opp_val = getattr(value, "ramRoot_MTpre__Person9", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Person9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpre__Person9(self):
        return self.__ramRoot_MTpre__Person9

    @ramRoot_MTpre__Person9.setter
    def ramRoot_MTpre__Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Person__ramRoot_MTpre__Person9", None)
        self.__ramRoot_MTpre__Person9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpre__Person11"):
                    opp_val = getattr(item, "ramRoot_MTpre__Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpre__Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpre__Person11"):
                    opp_val = getattr(item, "ramRoot_MTpre__Person11", None)
                    
                    setattr(item, "ramRoot_MTpre__Person11", self)
                    

    @property
    def ramRoot_MTpre__Person14(self):
        return self.__ramRoot_MTpre__Person14

    @ramRoot_MTpre__Person14.setter
    def ramRoot_MTpre__Person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Person__ramRoot_MTpre__Person14", None)
        self.__ramRoot_MTpre__Person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Classroom13"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Classroom13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Classroom13"):
                opp_val = getattr(value, "ramRoot_MTpre__Classroom13", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpre__Classroom13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpre__Person(self):
        return self.__ramRoot_MTpre__Person

    @ramRoot_MTpre__Person.setter
    def ramRoot_MTpre__Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpre__Person__ramRoot_MTpre__Person", None)
        self.__ramRoot_MTpre__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpre__Classroom"):
                opp_val = getattr(old_value, "ramRoot_MTpre__Classroom", None)
                if opp_val == self:
                    setattr(old_value, "ramRoot_MTpre__Classroom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpre__Classroom"):
                opp_val = getattr(value, "ramRoot_MTpre__Classroom", None)
                setattr(value, "ramRoot_MTpre__Classroom", self)

class MTpos__Person:

    pass
class ramRoot_MTpos__Woman(MTpos__Person):

    pass
class ramRoot_MTpos__Man(MTpos__Person):

    pass
class MTpos__Element:

    pass
class ramRoot_MTpos__Classroom(MTpos__Element):

    def __init__(self, id: str, ramRoot_MTpos__Classroom: "ramRoot_MTpos__Person" = None, ramRoot_MTpos__Classroom6: set["ramRoot_MTpos__Person"] = None):
        self.id = id
        self.ramRoot_MTpos__Classroom = ramRoot_MTpos__Classroom
        self.ramRoot_MTpos__Classroom6 = ramRoot_MTpos__Classroom6 if ramRoot_MTpos__Classroom6 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ramRoot_MTpos__Classroom6(self):
        return self.__ramRoot_MTpos__Classroom6

    @ramRoot_MTpos__Classroom6.setter
    def ramRoot_MTpos__Classroom6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Classroom__ramRoot_MTpos__Classroom6", None)
        self.__ramRoot_MTpos__Classroom6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpos__Person7"):
                    opp_val = getattr(item, "ramRoot_MTpos__Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpos__Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpos__Person7"):
                    opp_val = getattr(item, "ramRoot_MTpos__Person7", None)
                    
                    setattr(item, "ramRoot_MTpos__Person7", self)
                    

    @property
    def ramRoot_MTpos__Classroom(self):
        return self.__ramRoot_MTpos__Classroom

    @ramRoot_MTpos__Classroom.setter
    def ramRoot_MTpos__Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Classroom__ramRoot_MTpos__Classroom", None)
        self.__ramRoot_MTpos__Classroom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Person"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Person", None)
                if opp_val == self:
                    setattr(old_value, "ramRoot_MTpos__Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Person"):
                opp_val = getattr(value, "ramRoot_MTpos__Person", None)
                setattr(value, "ramRoot_MTpos__Person", self)

class ramRoot_MTpos__Person(MTpos__Element):

    def __init__(self, name: str, ramRoot_MTpos__Person: "ramRoot_MTpos__Classroom" = None, ramRoot_MTpos__Person4: "ramRoot_MTpos__Person" = None, ramRoot_MTpos__Person2: set["ramRoot_MTpos__Person"] = None, ramRoot_MTpos__Person7: "ramRoot_MTpos__Classroom" = None):
        self.name = name
        self.ramRoot_MTpos__Person = ramRoot_MTpos__Person
        self.ramRoot_MTpos__Person4 = ramRoot_MTpos__Person4
        self.ramRoot_MTpos__Person2 = ramRoot_MTpos__Person2 if ramRoot_MTpos__Person2 is not None else set()
        self.ramRoot_MTpos__Person7 = ramRoot_MTpos__Person7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ramRoot_MTpos__Person(self):
        return self.__ramRoot_MTpos__Person

    @ramRoot_MTpos__Person.setter
    def ramRoot_MTpos__Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Person__ramRoot_MTpos__Person", None)
        self.__ramRoot_MTpos__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Classroom"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Classroom", None)
                if opp_val == self:
                    setattr(old_value, "ramRoot_MTpos__Classroom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Classroom"):
                opp_val = getattr(value, "ramRoot_MTpos__Classroom", None)
                setattr(value, "ramRoot_MTpos__Classroom", self)

    @property
    def ramRoot_MTpos__Person2(self):
        return self.__ramRoot_MTpos__Person2

    @ramRoot_MTpos__Person2.setter
    def ramRoot_MTpos__Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Person__ramRoot_MTpos__Person2", None)
        self.__ramRoot_MTpos__Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ramRoot_MTpos__Person4"):
                    opp_val = getattr(item, "ramRoot_MTpos__Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "ramRoot_MTpos__Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ramRoot_MTpos__Person4"):
                    opp_val = getattr(item, "ramRoot_MTpos__Person4", None)
                    
                    setattr(item, "ramRoot_MTpos__Person4", self)
                    

    @property
    def ramRoot_MTpos__Person7(self):
        return self.__ramRoot_MTpos__Person7

    @ramRoot_MTpos__Person7.setter
    def ramRoot_MTpos__Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Person__ramRoot_MTpos__Person7", None)
        self.__ramRoot_MTpos__Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Classroom6"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Classroom6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Classroom6"):
                opp_val = getattr(value, "ramRoot_MTpos__Classroom6", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Classroom6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ramRoot_MTpos__Person4(self):
        return self.__ramRoot_MTpos__Person4

    @ramRoot_MTpos__Person4.setter
    def ramRoot_MTpos__Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MTpos__Person__ramRoot_MTpos__Person4", None)
        self.__ramRoot_MTpos__Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_MTpos__Person2"):
                opp_val = getattr(old_value, "ramRoot_MTpos__Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_MTpos__Person2"):
                opp_val = getattr(value, "ramRoot_MTpos__Person2", None)
                if opp_val is None:
                    setattr(value, "ramRoot_MTpos__Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MT__Element:

    pass
class ramRoot_GenericNode(MT__Element):

    pass
class ramRoot_MTpre__Element(MT__Element):

    def __init__(self, MT__matchSubtype: bool):
        self.MT__matchSubtype = MT__matchSubtype
        
    @property
    def MT__matchSubtype(self) -> bool:
        return self.__MT__matchSubtype

    @MT__matchSubtype.setter
    def MT__matchSubtype(self, MT__matchSubtype: bool):
        self.__MT__matchSubtype = MT__matchSubtype

class ramRoot_MTpos__Element(MT__Element):

    pass
class ramRoot_MT__Element(ABC):

    def __init__(self, MT__isProcessed: bool, MT__label: str, ramRoot_MT__Element: "ramRoot_GenericNode" = None):
        self.MT__isProcessed = MT__isProcessed
        self.MT__label = MT__label
        self.ramRoot_MT__Element = ramRoot_MT__Element
        
    @property
    def MT__isProcessed(self) -> bool:
        return self.__MT__isProcessed

    @MT__isProcessed.setter
    def MT__isProcessed(self, MT__isProcessed: bool):
        self.__MT__isProcessed = MT__isProcessed

    @property
    def MT__label(self) -> str:
        return self.__MT__label

    @MT__label.setter
    def MT__label(self, MT__label: str):
        self.__MT__label = MT__label

    @property
    def ramRoot_MT__Element(self):
        return self.__ramRoot_MT__Element

    @ramRoot_MT__Element.setter
    def ramRoot_MT__Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ramRoot_MT__Element__ramRoot_MT__Element", None)
        self.__ramRoot_MT__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ramRoot_GenericNode"):
                opp_val = getattr(old_value, "ramRoot_GenericNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ramRoot_GenericNode"):
                opp_val = getattr(value, "ramRoot_GenericNode", None)
                if opp_val is None:
                    setattr(value, "ramRoot_GenericNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
