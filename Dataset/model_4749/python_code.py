from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TreeElementType(Enum):
    empty = "empty"
    yes = "yes"
    no = "no"
    trusted = "trusted"
    dont_know = "dont_know"
    inadmissible = "inadmissible"


############################################
# Definition of Classes
############################################

class ed2_Model:

    pass
class ed2_ED2:

    def __init__(self, name: str, ed2_ED2: set["ed2_TreeElement"] = None, ed2_ED215: "ed2_Model" = None):
        self.name = name
        self.ed2_ED2 = ed2_ED2 if ed2_ED2 is not None else set()
        self.ed2_ED215 = ed2_ED215
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ed2_ED2(self):
        return self.__ed2_ED2

    @ed2_ED2.setter
    def ed2_ED2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_ED2__ed2_ED2", None)
        self.__ed2_ED2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ed2_TreeElement"):
                    opp_val = getattr(item, "ed2_TreeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ed2_TreeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ed2_TreeElement"):
                    opp_val = getattr(item, "ed2_TreeElement", None)
                    
                    setattr(item, "ed2_TreeElement", self)
                    

    @property
    def ed2_ED215(self):
        return self.__ed2_ED215

    @ed2_ED215.setter
    def ed2_ED215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_ED2__ed2_ED215", None)
        self.__ed2_ED215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_Model"):
                opp_val = getattr(old_value, "ed2_Model", None)
                if opp_val == self:
                    setattr(old_value, "ed2_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_Model"):
                opp_val = getattr(value, "ed2_Model", None)
                setattr(value, "ed2_Model", self)

class TreeElement:

    pass
class ed2_Leaf(TreeElement):

    pass
class ed2_Node(TreeElement):

    pass
class ed2_TreeElement(ABC):

    def __init__(self, index: str, name: str, type: str, ed2_TreeElement: "ed2_ED2" = None):
        self.index = index
        self.name = name
        self.type = type
        self.ed2_TreeElement = ed2_TreeElement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def ed2_TreeElement(self):
        return self.__ed2_TreeElement

    @ed2_TreeElement.setter
    def ed2_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeElement__ed2_TreeElement", None)
        self.__ed2_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_ED2"):
                opp_val = getattr(old_value, "ed2_ED2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_ED2"):
                opp_val = getattr(value, "ed2_ED2", None)
                if opp_val is None:
                    setattr(value, "ed2_ED2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ed2_TreeParent:

    def __init__(self, index: str, name: str, type: str, ed2_TreeParent: "ed2_EDD" = None, ed2_TreeParent8: set["ed2_TreeObject"] = None, ed2_TreeParent12: "ed2_TreeParent" = None, ed2_TreeParent10: set["ed2_TreeParent"] = None):
        self.index = index
        self.name = name
        self.type = type
        self.ed2_TreeParent = ed2_TreeParent
        self.ed2_TreeParent8 = ed2_TreeParent8 if ed2_TreeParent8 is not None else set()
        self.ed2_TreeParent12 = ed2_TreeParent12
        self.ed2_TreeParent10 = ed2_TreeParent10 if ed2_TreeParent10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def ed2_TreeParent10(self):
        return self.__ed2_TreeParent10

    @ed2_TreeParent10.setter
    def ed2_TreeParent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeParent__ed2_TreeParent10", None)
        self.__ed2_TreeParent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ed2_TreeParent12"):
                    opp_val = getattr(item, "ed2_TreeParent12", None)
                    
                    if opp_val == self:
                        setattr(item, "ed2_TreeParent12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ed2_TreeParent12"):
                    opp_val = getattr(item, "ed2_TreeParent12", None)
                    
                    setattr(item, "ed2_TreeParent12", self)
                    

    @property
    def ed2_TreeParent(self):
        return self.__ed2_TreeParent

    @ed2_TreeParent.setter
    def ed2_TreeParent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeParent__ed2_TreeParent", None)
        self.__ed2_TreeParent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_EDD2"):
                opp_val = getattr(old_value, "ed2_EDD2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_EDD2"):
                opp_val = getattr(value, "ed2_EDD2", None)
                if opp_val is None:
                    setattr(value, "ed2_EDD2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ed2_TreeParent12(self):
        return self.__ed2_TreeParent12

    @ed2_TreeParent12.setter
    def ed2_TreeParent12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeParent__ed2_TreeParent12", None)
        self.__ed2_TreeParent12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_TreeParent10"):
                opp_val = getattr(old_value, "ed2_TreeParent10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_TreeParent10"):
                opp_val = getattr(value, "ed2_TreeParent10", None)
                if opp_val is None:
                    setattr(value, "ed2_TreeParent10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ed2_TreeParent8(self):
        return self.__ed2_TreeParent8

    @ed2_TreeParent8.setter
    def ed2_TreeParent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeParent__ed2_TreeParent8", None)
        self.__ed2_TreeParent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ed2_TreeObject9"):
                    opp_val = getattr(item, "ed2_TreeObject9", None)
                    
                    if opp_val == self:
                        setattr(item, "ed2_TreeObject9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ed2_TreeObject9"):
                    opp_val = getattr(item, "ed2_TreeObject9", None)
                    
                    setattr(item, "ed2_TreeObject9", self)
                    

class ed2_TreeObject:

    def __init__(self, type: str, index: str, name: str, ed2_TreeObject: "ed2_EDD" = None, ed2_TreeObject9: "ed2_TreeParent" = None):
        self.type = type
        self.index = index
        self.name = name
        self.ed2_TreeObject = ed2_TreeObject
        self.ed2_TreeObject9 = ed2_TreeObject9
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ed2_TreeObject9(self):
        return self.__ed2_TreeObject9

    @ed2_TreeObject9.setter
    def ed2_TreeObject9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeObject__ed2_TreeObject9", None)
        self.__ed2_TreeObject9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_TreeParent8"):
                opp_val = getattr(old_value, "ed2_TreeParent8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_TreeParent8"):
                opp_val = getattr(value, "ed2_TreeParent8", None)
                if opp_val is None:
                    setattr(value, "ed2_TreeParent8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ed2_TreeObject(self):
        return self.__ed2_TreeObject

    @ed2_TreeObject.setter
    def ed2_TreeObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_TreeObject__ed2_TreeObject", None)
        self.__ed2_TreeObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ed2_EDD"):
                opp_val = getattr(old_value, "ed2_EDD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ed2_EDD"):
                opp_val = getattr(value, "ed2_EDD", None)
                if opp_val is None:
                    setattr(value, "ed2_EDD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ed2_EDD:

    def __init__(self, name: str, ed2_EDD: set["ed2_TreeObject"] = None, ed2_EDD2: set["ed2_TreeParent"] = None):
        self.name = name
        self.ed2_EDD = ed2_EDD if ed2_EDD is not None else set()
        self.ed2_EDD2 = ed2_EDD2 if ed2_EDD2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ed2_EDD(self):
        return self.__ed2_EDD

    @ed2_EDD.setter
    def ed2_EDD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_EDD__ed2_EDD", None)
        self.__ed2_EDD = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ed2_TreeObject"):
                    opp_val = getattr(item, "ed2_TreeObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ed2_TreeObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ed2_TreeObject"):
                    opp_val = getattr(item, "ed2_TreeObject", None)
                    
                    setattr(item, "ed2_TreeObject", self)
                    

    @property
    def ed2_EDD2(self):
        return self.__ed2_EDD2

    @ed2_EDD2.setter
    def ed2_EDD2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ed2_EDD__ed2_EDD2", None)
        self.__ed2_EDD2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ed2_TreeParent"):
                    opp_val = getattr(item, "ed2_TreeParent", None)
                    
                    if opp_val == self:
                        setattr(item, "ed2_TreeParent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ed2_TreeParent"):
                    opp_val = getattr(item, "ed2_TreeParent", None)
                    
                    setattr(item, "ed2_TreeParent", self)
                    
