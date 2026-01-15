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

class syswbeff106_Workbench:

    def __init__(self, aprop: str, syswbeff106_Workbench: set["syswbeff106_Thing"] = None, syswbeff106_Workbench62: set["syswbeff106_Thoughts"] = None, syswbeff106_Workbench65: "syswbeff106_System" = None, syswbeff106_Workbench68: set["syswbeff106_FunctionProperty"] = None, syswbeff106_Workbench71: set["syswbeff106_PatternCatalog"] = None):
        self.aprop = aprop
        self.syswbeff106_Workbench = syswbeff106_Workbench if syswbeff106_Workbench is not None else set()
        self.syswbeff106_Workbench62 = syswbeff106_Workbench62 if syswbeff106_Workbench62 is not None else set()
        self.syswbeff106_Workbench65 = syswbeff106_Workbench65
        self.syswbeff106_Workbench68 = syswbeff106_Workbench68 if syswbeff106_Workbench68 is not None else set()
        self.syswbeff106_Workbench71 = syswbeff106_Workbench71 if syswbeff106_Workbench71 is not None else set()
        
    @property
    def aprop(self) -> str:
        return self.__aprop

    @aprop.setter
    def aprop(self, aprop: str):
        self.__aprop = aprop

    @property
    def syswbeff106_Workbench(self):
        return self.__syswbeff106_Workbench

    @syswbeff106_Workbench.setter
    def syswbeff106_Workbench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Workbench__syswbeff106_Workbench", None)
        self.__syswbeff106_Workbench = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Thing60"):
                    opp_val = getattr(item, "syswbeff106_Thing60", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Thing60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Thing60"):
                    opp_val = getattr(item, "syswbeff106_Thing60", None)
                    
                    setattr(item, "syswbeff106_Thing60", self)
                    

    @property
    def syswbeff106_Workbench71(self):
        return self.__syswbeff106_Workbench71

    @syswbeff106_Workbench71.setter
    def syswbeff106_Workbench71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Workbench__syswbeff106_Workbench71", None)
        self.__syswbeff106_Workbench71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_PatternCatalog72"):
                    opp_val = getattr(item, "syswbeff106_PatternCatalog72", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_PatternCatalog72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_PatternCatalog72"):
                    opp_val = getattr(item, "syswbeff106_PatternCatalog72", None)
                    
                    setattr(item, "syswbeff106_PatternCatalog72", self)
                    

    @property
    def syswbeff106_Workbench62(self):
        return self.__syswbeff106_Workbench62

    @syswbeff106_Workbench62.setter
    def syswbeff106_Workbench62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Workbench__syswbeff106_Workbench62", None)
        self.__syswbeff106_Workbench62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Thoughts63"):
                    opp_val = getattr(item, "syswbeff106_Thoughts63", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Thoughts63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Thoughts63"):
                    opp_val = getattr(item, "syswbeff106_Thoughts63", None)
                    
                    setattr(item, "syswbeff106_Thoughts63", self)
                    

    @property
    def syswbeff106_Workbench65(self):
        return self.__syswbeff106_Workbench65

    @syswbeff106_Workbench65.setter
    def syswbeff106_Workbench65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Workbench__syswbeff106_Workbench65", None)
        self.__syswbeff106_Workbench65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_System66"):
                opp_val = getattr(old_value, "syswbeff106_System66", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_System66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_System66"):
                opp_val = getattr(value, "syswbeff106_System66", None)
                setattr(value, "syswbeff106_System66", self)

    @property
    def syswbeff106_Workbench68(self):
        return self.__syswbeff106_Workbench68

    @syswbeff106_Workbench68.setter
    def syswbeff106_Workbench68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Workbench__syswbeff106_Workbench68", None)
        self.__syswbeff106_Workbench68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_FunctionProperty69"):
                    opp_val = getattr(item, "syswbeff106_FunctionProperty69", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_FunctionProperty69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_FunctionProperty69"):
                    opp_val = getattr(item, "syswbeff106_FunctionProperty69", None)
                    
                    setattr(item, "syswbeff106_FunctionProperty69", self)
                    

class syswbeff106_PatternCatalog:

    def __init__(self, id: str, syswbeff106_PatternCatalog: set["syswbeff106_Function"] = None, syswbeff106_PatternCatalog72: "syswbeff106_Workbench" = None):
        self.id = id
        self.syswbeff106_PatternCatalog = syswbeff106_PatternCatalog if syswbeff106_PatternCatalog is not None else set()
        self.syswbeff106_PatternCatalog72 = syswbeff106_PatternCatalog72
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff106_PatternCatalog(self):
        return self.__syswbeff106_PatternCatalog

    @syswbeff106_PatternCatalog.setter
    def syswbeff106_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_PatternCatalog__syswbeff106_PatternCatalog", None)
        self.__syswbeff106_PatternCatalog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Function58"):
                    opp_val = getattr(item, "syswbeff106_Function58", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Function58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Function58"):
                    opp_val = getattr(item, "syswbeff106_Function58", None)
                    
                    setattr(item, "syswbeff106_Function58", self)
                    

    @property
    def syswbeff106_PatternCatalog72(self):
        return self.__syswbeff106_PatternCatalog72

    @syswbeff106_PatternCatalog72.setter
    def syswbeff106_PatternCatalog72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_PatternCatalog__syswbeff106_PatternCatalog72", None)
        self.__syswbeff106_PatternCatalog72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Workbench71"):
                opp_val = getattr(old_value, "syswbeff106_Workbench71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Workbench71"):
                opp_val = getattr(value, "syswbeff106_Workbench71", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Workbench71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff106_Thoughts:

    pass
class syswbeff106_System:

    pass
class syswbeff106_Thing:

    def __init__(self, id: int, syswbeff106_Thing34: "syswbeff106_RelatedTo" = None, syswbeff106_Thing36: set["syswbeff106_RelatedTo"] = None, syswbeff106_Thing: "syswbeff106_RelatedTo" = None, syswbeff106_Thing39: "syswbeff106_Thoughts" = None, syswbeff106_Thing60: "syswbeff106_Workbench" = None):
        self.id = id
        self.syswbeff106_Thing34 = syswbeff106_Thing34
        self.syswbeff106_Thing36 = syswbeff106_Thing36 if syswbeff106_Thing36 is not None else set()
        self.syswbeff106_Thing = syswbeff106_Thing
        self.syswbeff106_Thing39 = syswbeff106_Thing39
        self.syswbeff106_Thing60 = syswbeff106_Thing60
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def syswbeff106_Thing34(self):
        return self.__syswbeff106_Thing34

    @syswbeff106_Thing34.setter
    def syswbeff106_Thing34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Thing__syswbeff106_Thing34", None)
        self.__syswbeff106_Thing34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_RelatedTo33"):
                opp_val = getattr(old_value, "syswbeff106_RelatedTo33", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_RelatedTo33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_RelatedTo33"):
                opp_val = getattr(value, "syswbeff106_RelatedTo33", None)
                setattr(value, "syswbeff106_RelatedTo33", self)

    @property
    def syswbeff106_Thing36(self):
        return self.__syswbeff106_Thing36

    @syswbeff106_Thing36.setter
    def syswbeff106_Thing36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Thing__syswbeff106_Thing36", None)
        self.__syswbeff106_Thing36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_RelatedTo37"):
                    opp_val = getattr(item, "syswbeff106_RelatedTo37", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_RelatedTo37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_RelatedTo37"):
                    opp_val = getattr(item, "syswbeff106_RelatedTo37", None)
                    
                    setattr(item, "syswbeff106_RelatedTo37", self)
                    

    @property
    def syswbeff106_Thing39(self):
        return self.__syswbeff106_Thing39

    @syswbeff106_Thing39.setter
    def syswbeff106_Thing39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Thing__syswbeff106_Thing39", None)
        self.__syswbeff106_Thing39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Thoughts"):
                opp_val = getattr(old_value, "syswbeff106_Thoughts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Thoughts"):
                opp_val = getattr(value, "syswbeff106_Thoughts", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Thoughts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_Thing(self):
        return self.__syswbeff106_Thing

    @syswbeff106_Thing.setter
    def syswbeff106_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Thing__syswbeff106_Thing", None)
        self.__syswbeff106_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_RelatedTo"):
                opp_val = getattr(old_value, "syswbeff106_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_RelatedTo"):
                opp_val = getattr(value, "syswbeff106_RelatedTo", None)
                setattr(value, "syswbeff106_RelatedTo", self)

    @property
    def syswbeff106_Thing60(self):
        return self.__syswbeff106_Thing60

    @syswbeff106_Thing60.setter
    def syswbeff106_Thing60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Thing__syswbeff106_Thing60", None)
        self.__syswbeff106_Thing60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Workbench"):
                opp_val = getattr(old_value, "syswbeff106_Workbench", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Workbench"):
                opp_val = getattr(value, "syswbeff106_Workbench", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Workbench", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff106_RelatedTo:

    def __init__(self, since: str, syswbeff106_RelatedTo33: "syswbeff106_Thing" = None, syswbeff106_RelatedTo37: "syswbeff106_Thing" = None, syswbeff106_RelatedTo: "syswbeff106_Thing" = None):
        self.since = since
        self.syswbeff106_RelatedTo33 = syswbeff106_RelatedTo33
        self.syswbeff106_RelatedTo37 = syswbeff106_RelatedTo37
        self.syswbeff106_RelatedTo = syswbeff106_RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def syswbeff106_RelatedTo33(self):
        return self.__syswbeff106_RelatedTo33

    @syswbeff106_RelatedTo33.setter
    def syswbeff106_RelatedTo33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_RelatedTo__syswbeff106_RelatedTo33", None)
        self.__syswbeff106_RelatedTo33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Thing34"):
                opp_val = getattr(old_value, "syswbeff106_Thing34", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Thing34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Thing34"):
                opp_val = getattr(value, "syswbeff106_Thing34", None)
                setattr(value, "syswbeff106_Thing34", self)

    @property
    def syswbeff106_RelatedTo37(self):
        return self.__syswbeff106_RelatedTo37

    @syswbeff106_RelatedTo37.setter
    def syswbeff106_RelatedTo37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_RelatedTo__syswbeff106_RelatedTo37", None)
        self.__syswbeff106_RelatedTo37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Thing36"):
                opp_val = getattr(old_value, "syswbeff106_Thing36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Thing36"):
                opp_val = getattr(value, "syswbeff106_Thing36", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Thing36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_RelatedTo(self):
        return self.__syswbeff106_RelatedTo

    @syswbeff106_RelatedTo.setter
    def syswbeff106_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_RelatedTo__syswbeff106_RelatedTo", None)
        self.__syswbeff106_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Thing"):
                opp_val = getattr(old_value, "syswbeff106_Thing", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Thing"):
                opp_val = getattr(value, "syswbeff106_Thing", None)
                setattr(value, "syswbeff106_Thing", self)

class syswbeff106_Item:

    def __init__(self, name: str, syswbeff106_Item: "syswbeff106_Flow" = None):
        self.name = name
        self.syswbeff106_Item = syswbeff106_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff106_Item(self):
        return self.__syswbeff106_Item

    @syswbeff106_Item.setter
    def syswbeff106_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Item__syswbeff106_Item", None)
        self.__syswbeff106_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Flow27"):
                opp_val = getattr(old_value, "syswbeff106_Flow27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Flow27"):
                opp_val = getattr(value, "syswbeff106_Flow27", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Flow27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff106_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class syswbeff106_Port(ABC):

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
class Sequence:

    pass
class syswbeff106_Or(Sequence):

    pass
class syswbeff106_Iteration(Sequence):

    pass
class syswbeff106_Loop(Sequence):

    pass
class syswbeff106_Final(Sequence):

    pass
class syswbeff106_LoopExit(Sequence):

    pass
class syswbeff106_And(Sequence):

    pass
class syswbeff106_Start(Sequence):

    pass
class syswbeff106_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, syswbeff106_SequenceNode: "syswbeff106_SequenceNode" = None, syswbeff106_SequenceNode21: set["syswbeff106_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.syswbeff106_SequenceNode = syswbeff106_SequenceNode
        self.syswbeff106_SequenceNode21 = syswbeff106_SequenceNode21 if syswbeff106_SequenceNode21 is not None else set()
        
    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff106_SequenceNode(self):
        return self.__syswbeff106_SequenceNode

    @syswbeff106_SequenceNode.setter
    def syswbeff106_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_SequenceNode__syswbeff106_SequenceNode", None)
        self.__syswbeff106_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_SequenceNode21"):
                opp_val = getattr(old_value, "syswbeff106_SequenceNode21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_SequenceNode21"):
                opp_val = getattr(value, "syswbeff106_SequenceNode21", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_SequenceNode21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_SequenceNode21(self):
        return self.__syswbeff106_SequenceNode21

    @syswbeff106_SequenceNode21.setter
    def syswbeff106_SequenceNode21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_SequenceNode__syswbeff106_SequenceNode21", None)
        self.__syswbeff106_SequenceNode21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_SequenceNode"):
                    opp_val = getattr(item, "syswbeff106_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_SequenceNode"):
                    opp_val = getattr(item, "syswbeff106_SequenceNode", None)
                    
                    setattr(item, "syswbeff106_SequenceNode", self)
                    

class syswbeff106_Component:

    def __init__(self, name: str, syswbeff106_Component: "syswbeff106_Function" = None, syswbeff106_Component50: set["syswbeff106_Function"] = None, syswbeff106_Component45: "syswbeff106_Component" = None, syswbeff106_Component43: set["syswbeff106_Component"] = None, syswbeff106_Component48: "syswbeff106_Component" = None, syswbeff106_Component46: set["syswbeff106_Component"] = None, syswbeff106_Component56: "syswbeff106_System" = None):
        self.name = name
        self.syswbeff106_Component = syswbeff106_Component
        self.syswbeff106_Component50 = syswbeff106_Component50 if syswbeff106_Component50 is not None else set()
        self.syswbeff106_Component45 = syswbeff106_Component45
        self.syswbeff106_Component43 = syswbeff106_Component43 if syswbeff106_Component43 is not None else set()
        self.syswbeff106_Component48 = syswbeff106_Component48
        self.syswbeff106_Component46 = syswbeff106_Component46 if syswbeff106_Component46 is not None else set()
        self.syswbeff106_Component56 = syswbeff106_Component56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff106_Component48(self):
        return self.__syswbeff106_Component48

    @syswbeff106_Component48.setter
    def syswbeff106_Component48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component48", None)
        self.__syswbeff106_Component48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Component46"):
                opp_val = getattr(old_value, "syswbeff106_Component46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Component46"):
                opp_val = getattr(value, "syswbeff106_Component46", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Component46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_Component45(self):
        return self.__syswbeff106_Component45

    @syswbeff106_Component45.setter
    def syswbeff106_Component45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component45", None)
        self.__syswbeff106_Component45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Component43"):
                opp_val = getattr(old_value, "syswbeff106_Component43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Component43"):
                opp_val = getattr(value, "syswbeff106_Component43", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Component43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_Component43(self):
        return self.__syswbeff106_Component43

    @syswbeff106_Component43.setter
    def syswbeff106_Component43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component43", None)
        self.__syswbeff106_Component43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Component45"):
                    opp_val = getattr(item, "syswbeff106_Component45", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Component45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Component45"):
                    opp_val = getattr(item, "syswbeff106_Component45", None)
                    
                    setattr(item, "syswbeff106_Component45", self)
                    

    @property
    def syswbeff106_Component(self):
        return self.__syswbeff106_Component

    @syswbeff106_Component.setter
    def syswbeff106_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component", None)
        self.__syswbeff106_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function20"):
                opp_val = getattr(old_value, "syswbeff106_Function20", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Function20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function20"):
                opp_val = getattr(value, "syswbeff106_Function20", None)
                setattr(value, "syswbeff106_Function20", self)

    @property
    def syswbeff106_Component46(self):
        return self.__syswbeff106_Component46

    @syswbeff106_Component46.setter
    def syswbeff106_Component46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component46", None)
        self.__syswbeff106_Component46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Component48"):
                    opp_val = getattr(item, "syswbeff106_Component48", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Component48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Component48"):
                    opp_val = getattr(item, "syswbeff106_Component48", None)
                    
                    setattr(item, "syswbeff106_Component48", self)
                    

    @property
    def syswbeff106_Component50(self):
        return self.__syswbeff106_Component50

    @syswbeff106_Component50.setter
    def syswbeff106_Component50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component50", None)
        self.__syswbeff106_Component50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Function51"):
                    opp_val = getattr(item, "syswbeff106_Function51", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Function51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Function51"):
                    opp_val = getattr(item, "syswbeff106_Function51", None)
                    
                    setattr(item, "syswbeff106_Function51", self)
                    

    @property
    def syswbeff106_Component56(self):
        return self.__syswbeff106_Component56

    @syswbeff106_Component56.setter
    def syswbeff106_Component56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Component__syswbeff106_Component56", None)
        self.__syswbeff106_Component56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_System55"):
                opp_val = getattr(old_value, "syswbeff106_System55", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_System55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_System55"):
                opp_val = getattr(value, "syswbeff106_System55", None)
                setattr(value, "syswbeff106_System55", self)

class syswbeff106_FunctionProperty:

    def __init__(self, description: str, syswbeff106_FunctionProperty: "syswbeff106_Function" = None, syswbeff106_FunctionProperty42: "syswbeff106_FunctionProperty" = None, syswbeff106_FunctionProperty40: "syswbeff106_FunctionProperty" = None, syswbeff106_FunctionProperty69: "syswbeff106_Workbench" = None):
        self.description = description
        self.syswbeff106_FunctionProperty = syswbeff106_FunctionProperty
        self.syswbeff106_FunctionProperty42 = syswbeff106_FunctionProperty42
        self.syswbeff106_FunctionProperty40 = syswbeff106_FunctionProperty40
        self.syswbeff106_FunctionProperty69 = syswbeff106_FunctionProperty69
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def syswbeff106_FunctionProperty69(self):
        return self.__syswbeff106_FunctionProperty69

    @syswbeff106_FunctionProperty69.setter
    def syswbeff106_FunctionProperty69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_FunctionProperty__syswbeff106_FunctionProperty69", None)
        self.__syswbeff106_FunctionProperty69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Workbench68"):
                opp_val = getattr(old_value, "syswbeff106_Workbench68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Workbench68"):
                opp_val = getattr(value, "syswbeff106_Workbench68", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Workbench68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_FunctionProperty42(self):
        return self.__syswbeff106_FunctionProperty42

    @syswbeff106_FunctionProperty42.setter
    def syswbeff106_FunctionProperty42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_FunctionProperty__syswbeff106_FunctionProperty42", None)
        self.__syswbeff106_FunctionProperty42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_FunctionProperty40"):
                opp_val = getattr(old_value, "syswbeff106_FunctionProperty40", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_FunctionProperty40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_FunctionProperty40"):
                opp_val = getattr(value, "syswbeff106_FunctionProperty40", None)
                setattr(value, "syswbeff106_FunctionProperty40", self)

    @property
    def syswbeff106_FunctionProperty40(self):
        return self.__syswbeff106_FunctionProperty40

    @syswbeff106_FunctionProperty40.setter
    def syswbeff106_FunctionProperty40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_FunctionProperty__syswbeff106_FunctionProperty40", None)
        self.__syswbeff106_FunctionProperty40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_FunctionProperty42"):
                opp_val = getattr(old_value, "syswbeff106_FunctionProperty42", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_FunctionProperty42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_FunctionProperty42"):
                opp_val = getattr(value, "syswbeff106_FunctionProperty42", None)
                setattr(value, "syswbeff106_FunctionProperty42", self)

    @property
    def syswbeff106_FunctionProperty(self):
        return self.__syswbeff106_FunctionProperty

    @syswbeff106_FunctionProperty.setter
    def syswbeff106_FunctionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_FunctionProperty__syswbeff106_FunctionProperty", None)
        self.__syswbeff106_FunctionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function15"):
                opp_val = getattr(old_value, "syswbeff106_Function15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function15"):
                opp_val = getattr(value, "syswbeff106_Function15", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Function15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff106_Token:

    pass
class syswbeff106_OutputPort(Port):

    pass
class syswbeff106_Description:

    def __init__(self, content: str, syswbeff106_Description: "syswbeff106_Function" = None):
        self.content = content
        self.syswbeff106_Description = syswbeff106_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def syswbeff106_Description(self):
        return self.__syswbeff106_Description

    @syswbeff106_Description.setter
    def syswbeff106_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Description__syswbeff106_Description", None)
        self.__syswbeff106_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function11"):
                opp_val = getattr(old_value, "syswbeff106_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function11"):
                opp_val = getattr(value, "syswbeff106_Function11", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class syswbeff106_InputPort(Port):

    pass
class ProcessNode:

    pass
class syswbeff106_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class syswbeff106_Sequence(SequenceNode):

    pass
class syswbeff106_Function(SequenceNode, ProcessNode):

    def __init__(self, domain: str, syswbeff106_Function9: set["syswbeff106_InputPort"] = None, syswbeff106_Function11: set["syswbeff106_Description"] = None, syswbeff106_Function: "syswbeff106_Function" = None, syswbeff106_Function0: set["syswbeff106_Function"] = None, syswbeff106_Function3: set["syswbeff106_Sequence"] = None, syswbeff106_Function5: set["syswbeff106_Flow"] = None, syswbeff106_Function7: set["syswbeff106_OutputPort"] = None, syswbeff106_Function13: set["syswbeff106_Token"] = None, syswbeff106_Function15: set["syswbeff106_FunctionProperty"] = None, syswbeff106_Function18: "syswbeff106_Function" = None, syswbeff106_Function16: "syswbeff106_Function" = None, syswbeff106_Function20: "syswbeff106_Component" = None, syswbeff106_Function51: "syswbeff106_Component" = None, syswbeff106_Function53: "syswbeff106_System" = None, syswbeff106_Function58: "syswbeff106_PatternCatalog" = None):
        self.domain = domain
        self.syswbeff106_Function9 = syswbeff106_Function9 if syswbeff106_Function9 is not None else set()
        self.syswbeff106_Function11 = syswbeff106_Function11 if syswbeff106_Function11 is not None else set()
        self.syswbeff106_Function = syswbeff106_Function
        self.syswbeff106_Function0 = syswbeff106_Function0 if syswbeff106_Function0 is not None else set()
        self.syswbeff106_Function3 = syswbeff106_Function3 if syswbeff106_Function3 is not None else set()
        self.syswbeff106_Function5 = syswbeff106_Function5 if syswbeff106_Function5 is not None else set()
        self.syswbeff106_Function7 = syswbeff106_Function7 if syswbeff106_Function7 is not None else set()
        self.syswbeff106_Function13 = syswbeff106_Function13 if syswbeff106_Function13 is not None else set()
        self.syswbeff106_Function15 = syswbeff106_Function15 if syswbeff106_Function15 is not None else set()
        self.syswbeff106_Function18 = syswbeff106_Function18
        self.syswbeff106_Function16 = syswbeff106_Function16
        self.syswbeff106_Function20 = syswbeff106_Function20
        self.syswbeff106_Function51 = syswbeff106_Function51
        self.syswbeff106_Function53 = syswbeff106_Function53
        self.syswbeff106_Function58 = syswbeff106_Function58
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def syswbeff106_Function18(self):
        return self.__syswbeff106_Function18

    @syswbeff106_Function18.setter
    def syswbeff106_Function18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function18", None)
        self.__syswbeff106_Function18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function16"):
                opp_val = getattr(old_value, "syswbeff106_Function16", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Function16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function16"):
                opp_val = getattr(value, "syswbeff106_Function16", None)
                setattr(value, "syswbeff106_Function16", self)

    @property
    def syswbeff106_Function5(self):
        return self.__syswbeff106_Function5

    @syswbeff106_Function5.setter
    def syswbeff106_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function5", None)
        self.__syswbeff106_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Flow"):
                    opp_val = getattr(item, "syswbeff106_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Flow"):
                    opp_val = getattr(item, "syswbeff106_Flow", None)
                    
                    setattr(item, "syswbeff106_Flow", self)
                    

    @property
    def syswbeff106_Function20(self):
        return self.__syswbeff106_Function20

    @syswbeff106_Function20.setter
    def syswbeff106_Function20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function20", None)
        self.__syswbeff106_Function20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Component"):
                opp_val = getattr(old_value, "syswbeff106_Component", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Component", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Component"):
                opp_val = getattr(value, "syswbeff106_Component", None)
                setattr(value, "syswbeff106_Component", self)

    @property
    def syswbeff106_Function0(self):
        return self.__syswbeff106_Function0

    @syswbeff106_Function0.setter
    def syswbeff106_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function0", None)
        self.__syswbeff106_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Function"):
                    opp_val = getattr(item, "syswbeff106_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Function"):
                    opp_val = getattr(item, "syswbeff106_Function", None)
                    
                    setattr(item, "syswbeff106_Function", self)
                    

    @property
    def syswbeff106_Function13(self):
        return self.__syswbeff106_Function13

    @syswbeff106_Function13.setter
    def syswbeff106_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function13", None)
        self.__syswbeff106_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Token"):
                    opp_val = getattr(item, "syswbeff106_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Token"):
                    opp_val = getattr(item, "syswbeff106_Token", None)
                    
                    setattr(item, "syswbeff106_Token", self)
                    

    @property
    def syswbeff106_Function7(self):
        return self.__syswbeff106_Function7

    @syswbeff106_Function7.setter
    def syswbeff106_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function7", None)
        self.__syswbeff106_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_OutputPort"):
                    opp_val = getattr(item, "syswbeff106_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_OutputPort"):
                    opp_val = getattr(item, "syswbeff106_OutputPort", None)
                    
                    setattr(item, "syswbeff106_OutputPort", self)
                    

    @property
    def syswbeff106_Function16(self):
        return self.__syswbeff106_Function16

    @syswbeff106_Function16.setter
    def syswbeff106_Function16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function16", None)
        self.__syswbeff106_Function16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function18"):
                opp_val = getattr(old_value, "syswbeff106_Function18", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_Function18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function18"):
                opp_val = getattr(value, "syswbeff106_Function18", None)
                setattr(value, "syswbeff106_Function18", self)

    @property
    def syswbeff106_Function11(self):
        return self.__syswbeff106_Function11

    @syswbeff106_Function11.setter
    def syswbeff106_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function11", None)
        self.__syswbeff106_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Description"):
                    opp_val = getattr(item, "syswbeff106_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Description"):
                    opp_val = getattr(item, "syswbeff106_Description", None)
                    
                    setattr(item, "syswbeff106_Description", self)
                    

    @property
    def syswbeff106_Function3(self):
        return self.__syswbeff106_Function3

    @syswbeff106_Function3.setter
    def syswbeff106_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function3", None)
        self.__syswbeff106_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_Sequence"):
                    opp_val = getattr(item, "syswbeff106_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_Sequence"):
                    opp_val = getattr(item, "syswbeff106_Sequence", None)
                    
                    setattr(item, "syswbeff106_Sequence", self)
                    

    @property
    def syswbeff106_Function(self):
        return self.__syswbeff106_Function

    @syswbeff106_Function.setter
    def syswbeff106_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function", None)
        self.__syswbeff106_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Function0"):
                opp_val = getattr(old_value, "syswbeff106_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Function0"):
                opp_val = getattr(value, "syswbeff106_Function0", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_Function51(self):
        return self.__syswbeff106_Function51

    @syswbeff106_Function51.setter
    def syswbeff106_Function51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function51", None)
        self.__syswbeff106_Function51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_Component50"):
                opp_val = getattr(old_value, "syswbeff106_Component50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_Component50"):
                opp_val = getattr(value, "syswbeff106_Component50", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_Component50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106_Function9(self):
        return self.__syswbeff106_Function9

    @syswbeff106_Function9.setter
    def syswbeff106_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function9", None)
        self.__syswbeff106_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_InputPort"):
                    opp_val = getattr(item, "syswbeff106_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_InputPort"):
                    opp_val = getattr(item, "syswbeff106_InputPort", None)
                    
                    setattr(item, "syswbeff106_InputPort", self)
                    

    @property
    def syswbeff106_Function53(self):
        return self.__syswbeff106_Function53

    @syswbeff106_Function53.setter
    def syswbeff106_Function53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function53", None)
        self.__syswbeff106_Function53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_System"):
                opp_val = getattr(old_value, "syswbeff106_System", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106_System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_System"):
                opp_val = getattr(value, "syswbeff106_System", None)
                setattr(value, "syswbeff106_System", self)

    @property
    def syswbeff106_Function15(self):
        return self.__syswbeff106_Function15

    @syswbeff106_Function15.setter
    def syswbeff106_Function15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function15", None)
        self.__syswbeff106_Function15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106_FunctionProperty"):
                    opp_val = getattr(item, "syswbeff106_FunctionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106_FunctionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106_FunctionProperty"):
                    opp_val = getattr(item, "syswbeff106_FunctionProperty", None)
                    
                    setattr(item, "syswbeff106_FunctionProperty", self)
                    

    @property
    def syswbeff106_Function58(self):
        return self.__syswbeff106_Function58

    @syswbeff106_Function58.setter
    def syswbeff106_Function58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106_Function__syswbeff106_Function58", None)
        self.__syswbeff106_Function58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106_PatternCatalog"):
                opp_val = getattr(old_value, "syswbeff106_PatternCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106_PatternCatalog"):
                opp_val = getattr(value, "syswbeff106_PatternCatalog", None)
                if opp_val is None:
                    setattr(value, "syswbeff106_PatternCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
