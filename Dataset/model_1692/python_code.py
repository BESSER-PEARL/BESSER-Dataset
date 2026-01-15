from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionDomain(Enum):
    time = "time"
    space = "space"
    form = "form"


############################################
# Definition of Classes
############################################

class syswbeff1065ok_System:

    def __init__(self, id: str, syswbeff1065ok_System: "syswbeff1065ok_Function" = None, syswbeff1065ok_System55: "syswbeff1065ok_Component" = None, syswbeff1065ok_System66: "syswbeff1065ok_Workbench" = None):
        self.id = id
        self.syswbeff1065ok_System = syswbeff1065ok_System
        self.syswbeff1065ok_System55 = syswbeff1065ok_System55
        self.syswbeff1065ok_System66 = syswbeff1065ok_System66
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff1065ok_System(self):
        return self.__syswbeff1065ok_System

    @syswbeff1065ok_System.setter
    def syswbeff1065ok_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_System__syswbeff1065ok_System", None)
        self.__syswbeff1065ok_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function53"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function53", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Function53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function53"):
                opp_val = getattr(value, "syswbeff1065ok_Function53", None)
                setattr(value, "syswbeff1065ok_Function53", self)

    @property
    def syswbeff1065ok_System55(self):
        return self.__syswbeff1065ok_System55

    @syswbeff1065ok_System55.setter
    def syswbeff1065ok_System55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_System__syswbeff1065ok_System55", None)
        self.__syswbeff1065ok_System55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Component56"):
                opp_val = getattr(old_value, "syswbeff1065ok_Component56", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Component56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Component56"):
                opp_val = getattr(value, "syswbeff1065ok_Component56", None)
                setattr(value, "syswbeff1065ok_Component56", self)

    @property
    def syswbeff1065ok_System66(self):
        return self.__syswbeff1065ok_System66

    @syswbeff1065ok_System66.setter
    def syswbeff1065ok_System66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_System__syswbeff1065ok_System66", None)
        self.__syswbeff1065ok_System66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Workbench65"):
                opp_val = getattr(old_value, "syswbeff1065ok_Workbench65", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Workbench65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Workbench65"):
                opp_val = getattr(value, "syswbeff1065ok_Workbench65", None)
                setattr(value, "syswbeff1065ok_Workbench65", self)

class syswbeff1065ok_Workbench:

    pass
class syswbeff1065ok_PatternCatalog:

    def __init__(self, id: str, syswbeff1065ok_PatternCatalog: set["syswbeff1065ok_Function"] = None, syswbeff1065ok_PatternCatalog72: "syswbeff1065ok_Workbench" = None):
        self.id = id
        self.syswbeff1065ok_PatternCatalog = syswbeff1065ok_PatternCatalog if syswbeff1065ok_PatternCatalog is not None else set()
        self.syswbeff1065ok_PatternCatalog72 = syswbeff1065ok_PatternCatalog72
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff1065ok_PatternCatalog72(self):
        return self.__syswbeff1065ok_PatternCatalog72

    @syswbeff1065ok_PatternCatalog72.setter
    def syswbeff1065ok_PatternCatalog72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_PatternCatalog__syswbeff1065ok_PatternCatalog72", None)
        self.__syswbeff1065ok_PatternCatalog72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Workbench71"):
                opp_val = getattr(old_value, "syswbeff1065ok_Workbench71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Workbench71"):
                opp_val = getattr(value, "syswbeff1065ok_Workbench71", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Workbench71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_PatternCatalog(self):
        return self.__syswbeff1065ok_PatternCatalog

    @syswbeff1065ok_PatternCatalog.setter
    def syswbeff1065ok_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_PatternCatalog__syswbeff1065ok_PatternCatalog", None)
        self.__syswbeff1065ok_PatternCatalog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Function58"):
                    opp_val = getattr(item, "syswbeff1065ok_Function58", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Function58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Function58"):
                    opp_val = getattr(item, "syswbeff1065ok_Function58", None)
                    
                    setattr(item, "syswbeff1065ok_Function58", self)
                    

class syswbeff1065ok_Thoughts:

    def __init__(self, id: str, syswbeff1065ok_Thoughts: set["syswbeff1065ok_Thing"] = None, syswbeff1065ok_Thoughts63: "syswbeff1065ok_Workbench" = None):
        self.id = id
        self.syswbeff1065ok_Thoughts = syswbeff1065ok_Thoughts if syswbeff1065ok_Thoughts is not None else set()
        self.syswbeff1065ok_Thoughts63 = syswbeff1065ok_Thoughts63
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff1065ok_Thoughts(self):
        return self.__syswbeff1065ok_Thoughts

    @syswbeff1065ok_Thoughts.setter
    def syswbeff1065ok_Thoughts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thoughts__syswbeff1065ok_Thoughts", None)
        self.__syswbeff1065ok_Thoughts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Thing39"):
                    opp_val = getattr(item, "syswbeff1065ok_Thing39", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Thing39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Thing39"):
                    opp_val = getattr(item, "syswbeff1065ok_Thing39", None)
                    
                    setattr(item, "syswbeff1065ok_Thing39", self)
                    

    @property
    def syswbeff1065ok_Thoughts63(self):
        return self.__syswbeff1065ok_Thoughts63

    @syswbeff1065ok_Thoughts63.setter
    def syswbeff1065ok_Thoughts63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thoughts__syswbeff1065ok_Thoughts63", None)
        self.__syswbeff1065ok_Thoughts63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Workbench62"):
                opp_val = getattr(old_value, "syswbeff1065ok_Workbench62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Workbench62"):
                opp_val = getattr(value, "syswbeff1065ok_Workbench62", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Workbench62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff1065ok_Thing:

    def __init__(self, id: int, syswbeff1065ok_Thing: "syswbeff1065ok_AssociatedTo" = None, syswbeff1065ok_Thing34: "syswbeff1065ok_AssociatedTo" = None, syswbeff1065ok_Thing39: "syswbeff1065ok_Thoughts" = None, syswbeff1065ok_Thing36: set["syswbeff1065ok_AssociatedTo"] = None, syswbeff1065ok_Thing60: "syswbeff1065ok_Workbench" = None):
        self.id = id
        self.syswbeff1065ok_Thing = syswbeff1065ok_Thing
        self.syswbeff1065ok_Thing34 = syswbeff1065ok_Thing34
        self.syswbeff1065ok_Thing39 = syswbeff1065ok_Thing39
        self.syswbeff1065ok_Thing36 = syswbeff1065ok_Thing36 if syswbeff1065ok_Thing36 is not None else set()
        self.syswbeff1065ok_Thing60 = syswbeff1065ok_Thing60
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def syswbeff1065ok_Thing39(self):
        return self.__syswbeff1065ok_Thing39

    @syswbeff1065ok_Thing39.setter
    def syswbeff1065ok_Thing39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thing__syswbeff1065ok_Thing39", None)
        self.__syswbeff1065ok_Thing39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Thoughts"):
                opp_val = getattr(old_value, "syswbeff1065ok_Thoughts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Thoughts"):
                opp_val = getattr(value, "syswbeff1065ok_Thoughts", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Thoughts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Thing34(self):
        return self.__syswbeff1065ok_Thing34

    @syswbeff1065ok_Thing34.setter
    def syswbeff1065ok_Thing34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thing__syswbeff1065ok_Thing34", None)
        self.__syswbeff1065ok_Thing34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_AssociatedTo33"):
                opp_val = getattr(old_value, "syswbeff1065ok_AssociatedTo33", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_AssociatedTo33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_AssociatedTo33"):
                opp_val = getattr(value, "syswbeff1065ok_AssociatedTo33", None)
                setattr(value, "syswbeff1065ok_AssociatedTo33", self)

    @property
    def syswbeff1065ok_Thing36(self):
        return self.__syswbeff1065ok_Thing36

    @syswbeff1065ok_Thing36.setter
    def syswbeff1065ok_Thing36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thing__syswbeff1065ok_Thing36", None)
        self.__syswbeff1065ok_Thing36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_AssociatedTo37"):
                    opp_val = getattr(item, "syswbeff1065ok_AssociatedTo37", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_AssociatedTo37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_AssociatedTo37"):
                    opp_val = getattr(item, "syswbeff1065ok_AssociatedTo37", None)
                    
                    setattr(item, "syswbeff1065ok_AssociatedTo37", self)
                    

    @property
    def syswbeff1065ok_Thing60(self):
        return self.__syswbeff1065ok_Thing60

    @syswbeff1065ok_Thing60.setter
    def syswbeff1065ok_Thing60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thing__syswbeff1065ok_Thing60", None)
        self.__syswbeff1065ok_Thing60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Workbench"):
                opp_val = getattr(old_value, "syswbeff1065ok_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Workbench"):
                opp_val = getattr(value, "syswbeff1065ok_Workbench", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Thing(self):
        return self.__syswbeff1065ok_Thing

    @syswbeff1065ok_Thing.setter
    def syswbeff1065ok_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Thing__syswbeff1065ok_Thing", None)
        self.__syswbeff1065ok_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_AssociatedTo"):
                opp_val = getattr(old_value, "syswbeff1065ok_AssociatedTo", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_AssociatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_AssociatedTo"):
                opp_val = getattr(value, "syswbeff1065ok_AssociatedTo", None)
                setattr(value, "syswbeff1065ok_AssociatedTo", self)

class syswbeff1065ok_AssociatedTo:

    def __init__(self, since: str, syswbeff1065ok_AssociatedTo: "syswbeff1065ok_Thing" = None, syswbeff1065ok_AssociatedTo33: "syswbeff1065ok_Thing" = None, syswbeff1065ok_AssociatedTo37: "syswbeff1065ok_Thing" = None):
        self.since = since
        self.syswbeff1065ok_AssociatedTo = syswbeff1065ok_AssociatedTo
        self.syswbeff1065ok_AssociatedTo33 = syswbeff1065ok_AssociatedTo33
        self.syswbeff1065ok_AssociatedTo37 = syswbeff1065ok_AssociatedTo37
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def syswbeff1065ok_AssociatedTo33(self):
        return self.__syswbeff1065ok_AssociatedTo33

    @syswbeff1065ok_AssociatedTo33.setter
    def syswbeff1065ok_AssociatedTo33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_AssociatedTo__syswbeff1065ok_AssociatedTo33", None)
        self.__syswbeff1065ok_AssociatedTo33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Thing34"):
                opp_val = getattr(old_value, "syswbeff1065ok_Thing34", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Thing34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Thing34"):
                opp_val = getattr(value, "syswbeff1065ok_Thing34", None)
                setattr(value, "syswbeff1065ok_Thing34", self)

    @property
    def syswbeff1065ok_AssociatedTo(self):
        return self.__syswbeff1065ok_AssociatedTo

    @syswbeff1065ok_AssociatedTo.setter
    def syswbeff1065ok_AssociatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_AssociatedTo__syswbeff1065ok_AssociatedTo", None)
        self.__syswbeff1065ok_AssociatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Thing"):
                opp_val = getattr(old_value, "syswbeff1065ok_Thing", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Thing"):
                opp_val = getattr(value, "syswbeff1065ok_Thing", None)
                setattr(value, "syswbeff1065ok_Thing", self)

    @property
    def syswbeff1065ok_AssociatedTo37(self):
        return self.__syswbeff1065ok_AssociatedTo37

    @syswbeff1065ok_AssociatedTo37.setter
    def syswbeff1065ok_AssociatedTo37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_AssociatedTo__syswbeff1065ok_AssociatedTo37", None)
        self.__syswbeff1065ok_AssociatedTo37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Thing36"):
                opp_val = getattr(old_value, "syswbeff1065ok_Thing36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Thing36"):
                opp_val = getattr(value, "syswbeff1065ok_Thing36", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Thing36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff1065ok_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class syswbeff1065ok_Port(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Port:

    pass
class syswbeff1065ok_Item:

    def __init__(self, name: str, syswbeff1065ok_Item: "syswbeff1065ok_Flow" = None):
        self.name = name
        self.syswbeff1065ok_Item = syswbeff1065ok_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff1065ok_Item(self):
        return self.__syswbeff1065ok_Item

    @syswbeff1065ok_Item.setter
    def syswbeff1065ok_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Item__syswbeff1065ok_Item", None)
        self.__syswbeff1065ok_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Flow27"):
                opp_val = getattr(old_value, "syswbeff1065ok_Flow27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Flow27"):
                opp_val = getattr(value, "syswbeff1065ok_Flow27", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Flow27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Sequence:

    pass
class syswbeff1065ok_Loop(Sequence):

    pass
class syswbeff1065ok_Iteration(Sequence):

    pass
class syswbeff1065ok_LoopExit(Sequence):

    pass
class syswbeff1065ok_Start(Sequence):

    pass
class syswbeff1065ok_Final(Sequence):

    pass
class syswbeff1065ok_Or(Sequence):

    pass
class syswbeff1065ok_And(Sequence):

    pass
class syswbeff1065ok_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, syswbeff1065ok_SequenceNode21: set["syswbeff1065ok_SequenceNode"] = None, syswbeff1065ok_SequenceNode: "syswbeff1065ok_SequenceNode" = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.syswbeff1065ok_SequenceNode21 = syswbeff1065ok_SequenceNode21 if syswbeff1065ok_SequenceNode21 is not None else set()
        self.syswbeff1065ok_SequenceNode = syswbeff1065ok_SequenceNode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def syswbeff1065ok_SequenceNode(self):
        return self.__syswbeff1065ok_SequenceNode

    @syswbeff1065ok_SequenceNode.setter
    def syswbeff1065ok_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_SequenceNode__syswbeff1065ok_SequenceNode", None)
        self.__syswbeff1065ok_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_SequenceNode21"):
                opp_val = getattr(old_value, "syswbeff1065ok_SequenceNode21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_SequenceNode21"):
                opp_val = getattr(value, "syswbeff1065ok_SequenceNode21", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_SequenceNode21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_SequenceNode21(self):
        return self.__syswbeff1065ok_SequenceNode21

    @syswbeff1065ok_SequenceNode21.setter
    def syswbeff1065ok_SequenceNode21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_SequenceNode__syswbeff1065ok_SequenceNode21", None)
        self.__syswbeff1065ok_SequenceNode21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_SequenceNode"):
                    opp_val = getattr(item, "syswbeff1065ok_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_SequenceNode"):
                    opp_val = getattr(item, "syswbeff1065ok_SequenceNode", None)
                    
                    setattr(item, "syswbeff1065ok_SequenceNode", self)
                    

class syswbeff1065ok_Component:

    def __init__(self, name: str, syswbeff1065ok_Component: "syswbeff1065ok_Function" = None, syswbeff1065ok_Component45: "syswbeff1065ok_Component" = None, syswbeff1065ok_Component43: set["syswbeff1065ok_Component"] = None, syswbeff1065ok_Component48: "syswbeff1065ok_Component" = None, syswbeff1065ok_Component46: set["syswbeff1065ok_Component"] = None, syswbeff1065ok_Component56: "syswbeff1065ok_System" = None, syswbeff1065ok_Component50: set["syswbeff1065ok_Function"] = None):
        self.name = name
        self.syswbeff1065ok_Component = syswbeff1065ok_Component
        self.syswbeff1065ok_Component45 = syswbeff1065ok_Component45
        self.syswbeff1065ok_Component43 = syswbeff1065ok_Component43 if syswbeff1065ok_Component43 is not None else set()
        self.syswbeff1065ok_Component48 = syswbeff1065ok_Component48
        self.syswbeff1065ok_Component46 = syswbeff1065ok_Component46 if syswbeff1065ok_Component46 is not None else set()
        self.syswbeff1065ok_Component56 = syswbeff1065ok_Component56
        self.syswbeff1065ok_Component50 = syswbeff1065ok_Component50 if syswbeff1065ok_Component50 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff1065ok_Component(self):
        return self.__syswbeff1065ok_Component

    @syswbeff1065ok_Component.setter
    def syswbeff1065ok_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component", None)
        self.__syswbeff1065ok_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function20"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function20", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Function20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function20"):
                opp_val = getattr(value, "syswbeff1065ok_Function20", None)
                setattr(value, "syswbeff1065ok_Function20", self)

    @property
    def syswbeff1065ok_Component50(self):
        return self.__syswbeff1065ok_Component50

    @syswbeff1065ok_Component50.setter
    def syswbeff1065ok_Component50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component50", None)
        self.__syswbeff1065ok_Component50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Function51"):
                    opp_val = getattr(item, "syswbeff1065ok_Function51", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Function51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Function51"):
                    opp_val = getattr(item, "syswbeff1065ok_Function51", None)
                    
                    setattr(item, "syswbeff1065ok_Function51", self)
                    

    @property
    def syswbeff1065ok_Component48(self):
        return self.__syswbeff1065ok_Component48

    @syswbeff1065ok_Component48.setter
    def syswbeff1065ok_Component48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component48", None)
        self.__syswbeff1065ok_Component48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Component46"):
                opp_val = getattr(old_value, "syswbeff1065ok_Component46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Component46"):
                opp_val = getattr(value, "syswbeff1065ok_Component46", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Component46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Component56(self):
        return self.__syswbeff1065ok_Component56

    @syswbeff1065ok_Component56.setter
    def syswbeff1065ok_Component56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component56", None)
        self.__syswbeff1065ok_Component56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_System55"):
                opp_val = getattr(old_value, "syswbeff1065ok_System55", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_System55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_System55"):
                opp_val = getattr(value, "syswbeff1065ok_System55", None)
                setattr(value, "syswbeff1065ok_System55", self)

    @property
    def syswbeff1065ok_Component45(self):
        return self.__syswbeff1065ok_Component45

    @syswbeff1065ok_Component45.setter
    def syswbeff1065ok_Component45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component45", None)
        self.__syswbeff1065ok_Component45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Component43"):
                opp_val = getattr(old_value, "syswbeff1065ok_Component43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Component43"):
                opp_val = getattr(value, "syswbeff1065ok_Component43", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Component43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Component43(self):
        return self.__syswbeff1065ok_Component43

    @syswbeff1065ok_Component43.setter
    def syswbeff1065ok_Component43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component43", None)
        self.__syswbeff1065ok_Component43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Component45"):
                    opp_val = getattr(item, "syswbeff1065ok_Component45", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Component45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Component45"):
                    opp_val = getattr(item, "syswbeff1065ok_Component45", None)
                    
                    setattr(item, "syswbeff1065ok_Component45", self)
                    

    @property
    def syswbeff1065ok_Component46(self):
        return self.__syswbeff1065ok_Component46

    @syswbeff1065ok_Component46.setter
    def syswbeff1065ok_Component46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Component__syswbeff1065ok_Component46", None)
        self.__syswbeff1065ok_Component46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Component48"):
                    opp_val = getattr(item, "syswbeff1065ok_Component48", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Component48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Component48"):
                    opp_val = getattr(item, "syswbeff1065ok_Component48", None)
                    
                    setattr(item, "syswbeff1065ok_Component48", self)
                    

class syswbeff1065ok_FunctionProperty:

    def __init__(self, description: str, syswbeff1065ok_FunctionProperty: "syswbeff1065ok_Function" = None, syswbeff1065ok_FunctionProperty42: "syswbeff1065ok_FunctionProperty" = None, syswbeff1065ok_FunctionProperty40: "syswbeff1065ok_FunctionProperty" = None, syswbeff1065ok_FunctionProperty69: "syswbeff1065ok_Workbench" = None):
        self.description = description
        self.syswbeff1065ok_FunctionProperty = syswbeff1065ok_FunctionProperty
        self.syswbeff1065ok_FunctionProperty42 = syswbeff1065ok_FunctionProperty42
        self.syswbeff1065ok_FunctionProperty40 = syswbeff1065ok_FunctionProperty40
        self.syswbeff1065ok_FunctionProperty69 = syswbeff1065ok_FunctionProperty69
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def syswbeff1065ok_FunctionProperty42(self):
        return self.__syswbeff1065ok_FunctionProperty42

    @syswbeff1065ok_FunctionProperty42.setter
    def syswbeff1065ok_FunctionProperty42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_FunctionProperty__syswbeff1065ok_FunctionProperty42", None)
        self.__syswbeff1065ok_FunctionProperty42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_FunctionProperty40"):
                opp_val = getattr(old_value, "syswbeff1065ok_FunctionProperty40", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_FunctionProperty40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_FunctionProperty40"):
                opp_val = getattr(value, "syswbeff1065ok_FunctionProperty40", None)
                setattr(value, "syswbeff1065ok_FunctionProperty40", self)

    @property
    def syswbeff1065ok_FunctionProperty69(self):
        return self.__syswbeff1065ok_FunctionProperty69

    @syswbeff1065ok_FunctionProperty69.setter
    def syswbeff1065ok_FunctionProperty69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_FunctionProperty__syswbeff1065ok_FunctionProperty69", None)
        self.__syswbeff1065ok_FunctionProperty69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Workbench68"):
                opp_val = getattr(old_value, "syswbeff1065ok_Workbench68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Workbench68"):
                opp_val = getattr(value, "syswbeff1065ok_Workbench68", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Workbench68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_FunctionProperty40(self):
        return self.__syswbeff1065ok_FunctionProperty40

    @syswbeff1065ok_FunctionProperty40.setter
    def syswbeff1065ok_FunctionProperty40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_FunctionProperty__syswbeff1065ok_FunctionProperty40", None)
        self.__syswbeff1065ok_FunctionProperty40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_FunctionProperty42"):
                opp_val = getattr(old_value, "syswbeff1065ok_FunctionProperty42", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_FunctionProperty42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_FunctionProperty42"):
                opp_val = getattr(value, "syswbeff1065ok_FunctionProperty42", None)
                setattr(value, "syswbeff1065ok_FunctionProperty42", self)

    @property
    def syswbeff1065ok_FunctionProperty(self):
        return self.__syswbeff1065ok_FunctionProperty

    @syswbeff1065ok_FunctionProperty.setter
    def syswbeff1065ok_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_FunctionProperty__syswbeff1065ok_FunctionProperty", None)
        self.__syswbeff1065ok_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function15"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function15"):
                opp_val = getattr(value, "syswbeff1065ok_Function15", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Function15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff1065ok_Token:

    pass
class syswbeff1065ok_Description:

    def __init__(self, content: str, syswbeff1065ok_Description: "syswbeff1065ok_Function" = None):
        self.content = content
        self.syswbeff1065ok_Description = syswbeff1065ok_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def syswbeff1065ok_Description(self):
        return self.__syswbeff1065ok_Description

    @syswbeff1065ok_Description.setter
    def syswbeff1065ok_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Description__syswbeff1065ok_Description", None)
        self.__syswbeff1065ok_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function11"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function11"):
                opp_val = getattr(value, "syswbeff1065ok_Function11", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff1065ok_InputPort(Port):

    pass
class syswbeff1065ok_OutputPort(Port):

    pass
class ProcessNode:

    pass
class syswbeff1065ok_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class syswbeff1065ok_Sequence(SequenceNode):

    pass
class syswbeff1065ok_Function(ProcessNode, SequenceNode):

    def __init__(self, domain: str, syswbeff1065ok_Function5: set["syswbeff1065ok_Flow"] = None, syswbeff1065ok_Function7: set["syswbeff1065ok_OutputPort"] = None, syswbeff1065ok_Function9: set["syswbeff1065ok_InputPort"] = None, syswbeff1065ok_Function11: set["syswbeff1065ok_Description"] = None, syswbeff1065ok_Function13: set["syswbeff1065ok_Token"] = None, syswbeff1065ok_Function15: set["syswbeff1065ok_FunctionProperty"] = None, syswbeff1065ok_Function18: "syswbeff1065ok_Function" = None, syswbeff1065ok_Function16: "syswbeff1065ok_Function" = None, syswbeff1065ok_Function20: "syswbeff1065ok_Component" = None, syswbeff1065ok_Function: "syswbeff1065ok_Function" = None, syswbeff1065ok_Function0: set["syswbeff1065ok_Function"] = None, syswbeff1065ok_Function3: set["syswbeff1065ok_Sequence"] = None, syswbeff1065ok_Function51: "syswbeff1065ok_Component" = None, syswbeff1065ok_Function53: "syswbeff1065ok_System" = None, syswbeff1065ok_Function58: "syswbeff1065ok_PatternCatalog" = None):
        self.domain = domain
        self.syswbeff1065ok_Function5 = syswbeff1065ok_Function5 if syswbeff1065ok_Function5 is not None else set()
        self.syswbeff1065ok_Function7 = syswbeff1065ok_Function7 if syswbeff1065ok_Function7 is not None else set()
        self.syswbeff1065ok_Function9 = syswbeff1065ok_Function9 if syswbeff1065ok_Function9 is not None else set()
        self.syswbeff1065ok_Function11 = syswbeff1065ok_Function11 if syswbeff1065ok_Function11 is not None else set()
        self.syswbeff1065ok_Function13 = syswbeff1065ok_Function13 if syswbeff1065ok_Function13 is not None else set()
        self.syswbeff1065ok_Function15 = syswbeff1065ok_Function15 if syswbeff1065ok_Function15 is not None else set()
        self.syswbeff1065ok_Function18 = syswbeff1065ok_Function18
        self.syswbeff1065ok_Function16 = syswbeff1065ok_Function16
        self.syswbeff1065ok_Function20 = syswbeff1065ok_Function20
        self.syswbeff1065ok_Function = syswbeff1065ok_Function
        self.syswbeff1065ok_Function0 = syswbeff1065ok_Function0 if syswbeff1065ok_Function0 is not None else set()
        self.syswbeff1065ok_Function3 = syswbeff1065ok_Function3 if syswbeff1065ok_Function3 is not None else set()
        self.syswbeff1065ok_Function51 = syswbeff1065ok_Function51
        self.syswbeff1065ok_Function53 = syswbeff1065ok_Function53
        self.syswbeff1065ok_Function58 = syswbeff1065ok_Function58
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def syswbeff1065ok_Function53(self):
        return self.__syswbeff1065ok_Function53

    @syswbeff1065ok_Function53.setter
    def syswbeff1065ok_Function53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function53", None)
        self.__syswbeff1065ok_Function53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_System"):
                opp_val = getattr(old_value, "syswbeff1065ok_System", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_System"):
                opp_val = getattr(value, "syswbeff1065ok_System", None)
                setattr(value, "syswbeff1065ok_System", self)

    @property
    def syswbeff1065ok_Function20(self):
        return self.__syswbeff1065ok_Function20

    @syswbeff1065ok_Function20.setter
    def syswbeff1065ok_Function20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function20", None)
        self.__syswbeff1065ok_Function20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Component"):
                opp_val = getattr(old_value, "syswbeff1065ok_Component", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Component"):
                opp_val = getattr(value, "syswbeff1065ok_Component", None)
                setattr(value, "syswbeff1065ok_Component", self)

    @property
    def syswbeff1065ok_Function13(self):
        return self.__syswbeff1065ok_Function13

    @syswbeff1065ok_Function13.setter
    def syswbeff1065ok_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function13", None)
        self.__syswbeff1065ok_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Token"):
                    opp_val = getattr(item, "syswbeff1065ok_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Token"):
                    opp_val = getattr(item, "syswbeff1065ok_Token", None)
                    
                    setattr(item, "syswbeff1065ok_Token", self)
                    

    @property
    def syswbeff1065ok_Function(self):
        return self.__syswbeff1065ok_Function

    @syswbeff1065ok_Function.setter
    def syswbeff1065ok_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function", None)
        self.__syswbeff1065ok_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function0"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function0"):
                opp_val = getattr(value, "syswbeff1065ok_Function0", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Function7(self):
        return self.__syswbeff1065ok_Function7

    @syswbeff1065ok_Function7.setter
    def syswbeff1065ok_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function7", None)
        self.__syswbeff1065ok_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_OutputPort"):
                    opp_val = getattr(item, "syswbeff1065ok_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_OutputPort"):
                    opp_val = getattr(item, "syswbeff1065ok_OutputPort", None)
                    
                    setattr(item, "syswbeff1065ok_OutputPort", self)
                    

    @property
    def syswbeff1065ok_Function16(self):
        return self.__syswbeff1065ok_Function16

    @syswbeff1065ok_Function16.setter
    def syswbeff1065ok_Function16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function16", None)
        self.__syswbeff1065ok_Function16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function18"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function18", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Function18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function18"):
                opp_val = getattr(value, "syswbeff1065ok_Function18", None)
                setattr(value, "syswbeff1065ok_Function18", self)

    @property
    def syswbeff1065ok_Function18(self):
        return self.__syswbeff1065ok_Function18

    @syswbeff1065ok_Function18.setter
    def syswbeff1065ok_Function18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function18", None)
        self.__syswbeff1065ok_Function18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Function16"):
                opp_val = getattr(old_value, "syswbeff1065ok_Function16", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff1065ok_Function16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Function16"):
                opp_val = getattr(value, "syswbeff1065ok_Function16", None)
                setattr(value, "syswbeff1065ok_Function16", self)

    @property
    def syswbeff1065ok_Function9(self):
        return self.__syswbeff1065ok_Function9

    @syswbeff1065ok_Function9.setter
    def syswbeff1065ok_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function9", None)
        self.__syswbeff1065ok_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_InputPort"):
                    opp_val = getattr(item, "syswbeff1065ok_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_InputPort"):
                    opp_val = getattr(item, "syswbeff1065ok_InputPort", None)
                    
                    setattr(item, "syswbeff1065ok_InputPort", self)
                    

    @property
    def syswbeff1065ok_Function15(self):
        return self.__syswbeff1065ok_Function15

    @syswbeff1065ok_Function15.setter
    def syswbeff1065ok_Function15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function15", None)
        self.__syswbeff1065ok_Function15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_FunctionProperty"):
                    opp_val = getattr(item, "syswbeff1065ok_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_FunctionProperty"):
                    opp_val = getattr(item, "syswbeff1065ok_FunctionProperty", None)
                    
                    setattr(item, "syswbeff1065ok_FunctionProperty", self)
                    

    @property
    def syswbeff1065ok_Function58(self):
        return self.__syswbeff1065ok_Function58

    @syswbeff1065ok_Function58.setter
    def syswbeff1065ok_Function58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function58", None)
        self.__syswbeff1065ok_Function58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_PatternCatalog"):
                opp_val = getattr(old_value, "syswbeff1065ok_PatternCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_PatternCatalog"):
                opp_val = getattr(value, "syswbeff1065ok_PatternCatalog", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_PatternCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Function5(self):
        return self.__syswbeff1065ok_Function5

    @syswbeff1065ok_Function5.setter
    def syswbeff1065ok_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function5", None)
        self.__syswbeff1065ok_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Flow"):
                    opp_val = getattr(item, "syswbeff1065ok_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Flow"):
                    opp_val = getattr(item, "syswbeff1065ok_Flow", None)
                    
                    setattr(item, "syswbeff1065ok_Flow", self)
                    

    @property
    def syswbeff1065ok_Function51(self):
        return self.__syswbeff1065ok_Function51

    @syswbeff1065ok_Function51.setter
    def syswbeff1065ok_Function51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function51", None)
        self.__syswbeff1065ok_Function51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff1065ok_Component50"):
                opp_val = getattr(old_value, "syswbeff1065ok_Component50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff1065ok_Component50"):
                opp_val = getattr(value, "syswbeff1065ok_Component50", None)
                if opp_val is None:
                    setattr(value, "syswbeff1065ok_Component50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff1065ok_Function3(self):
        return self.__syswbeff1065ok_Function3

    @syswbeff1065ok_Function3.setter
    def syswbeff1065ok_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function3", None)
        self.__syswbeff1065ok_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Sequence"):
                    opp_val = getattr(item, "syswbeff1065ok_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Sequence"):
                    opp_val = getattr(item, "syswbeff1065ok_Sequence", None)
                    
                    setattr(item, "syswbeff1065ok_Sequence", self)
                    

    @property
    def syswbeff1065ok_Function11(self):
        return self.__syswbeff1065ok_Function11

    @syswbeff1065ok_Function11.setter
    def syswbeff1065ok_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function11", None)
        self.__syswbeff1065ok_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Description"):
                    opp_val = getattr(item, "syswbeff1065ok_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Description"):
                    opp_val = getattr(item, "syswbeff1065ok_Description", None)
                    
                    setattr(item, "syswbeff1065ok_Description", self)
                    

    @property
    def syswbeff1065ok_Function0(self):
        return self.__syswbeff1065ok_Function0

    @syswbeff1065ok_Function0.setter
    def syswbeff1065ok_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff1065ok_Function__syswbeff1065ok_Function0", None)
        self.__syswbeff1065ok_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff1065ok_Function"):
                    opp_val = getattr(item, "syswbeff1065ok_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff1065ok_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff1065ok_Function"):
                    opp_val = getattr(item, "syswbeff1065ok_Function", None)
                    
                    setattr(item, "syswbeff1065ok_Function", self)
                    
