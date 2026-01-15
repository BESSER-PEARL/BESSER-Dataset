from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractFunction:

    pass
class syswbeff106prepa_Workbench:

    pass
class syswbeff106prepa_Pattern(AbstractFunction):

    pass
class syswbeff106prepa_Port(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Port:

    pass
class syswbeff106prepa_AbstractFunction(ABC):

    def __init__(self, name: str, syswbeff106prepa_AbstractFunction: "syswbeff106prepa_AbstractFunction" = None, syswbeff106prepa_AbstractFunction0: "syswbeff106prepa_AbstractFunction" = None, syswbeff106prepa_AbstractFunction3: set["syswbeff106prepa_InputPort"] = None, syswbeff106prepa_AbstractFunction5: set["syswbeff106prepa_OutputPort"] = None, syswbeff106prepa_AbstractFunction7: set["syswbeff106prepa_Flow"] = None):
        self.name = name
        self.syswbeff106prepa_AbstractFunction = syswbeff106prepa_AbstractFunction
        self.syswbeff106prepa_AbstractFunction0 = syswbeff106prepa_AbstractFunction0
        self.syswbeff106prepa_AbstractFunction3 = syswbeff106prepa_AbstractFunction3 if syswbeff106prepa_AbstractFunction3 is not None else set()
        self.syswbeff106prepa_AbstractFunction5 = syswbeff106prepa_AbstractFunction5 if syswbeff106prepa_AbstractFunction5 is not None else set()
        self.syswbeff106prepa_AbstractFunction7 = syswbeff106prepa_AbstractFunction7 if syswbeff106prepa_AbstractFunction7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def syswbeff106prepa_AbstractFunction0(self):
        return self.__syswbeff106prepa_AbstractFunction0

    @syswbeff106prepa_AbstractFunction0.setter
    def syswbeff106prepa_AbstractFunction0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_AbstractFunction__syswbeff106prepa_AbstractFunction0", None)
        self.__syswbeff106prepa_AbstractFunction0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106prepa_AbstractFunction"):
                opp_val = getattr(old_value, "syswbeff106prepa_AbstractFunction", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106prepa_AbstractFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106prepa_AbstractFunction"):
                opp_val = getattr(value, "syswbeff106prepa_AbstractFunction", None)
                setattr(value, "syswbeff106prepa_AbstractFunction", self)

    @property
    def syswbeff106prepa_AbstractFunction(self):
        return self.__syswbeff106prepa_AbstractFunction

    @syswbeff106prepa_AbstractFunction.setter
    def syswbeff106prepa_AbstractFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_AbstractFunction__syswbeff106prepa_AbstractFunction", None)
        self.__syswbeff106prepa_AbstractFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106prepa_AbstractFunction0"):
                opp_val = getattr(old_value, "syswbeff106prepa_AbstractFunction0", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106prepa_AbstractFunction0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106prepa_AbstractFunction0"):
                opp_val = getattr(value, "syswbeff106prepa_AbstractFunction0", None)
                setattr(value, "syswbeff106prepa_AbstractFunction0", self)

    @property
    def syswbeff106prepa_AbstractFunction7(self):
        return self.__syswbeff106prepa_AbstractFunction7

    @syswbeff106prepa_AbstractFunction7.setter
    def syswbeff106prepa_AbstractFunction7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_AbstractFunction__syswbeff106prepa_AbstractFunction7", None)
        self.__syswbeff106prepa_AbstractFunction7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106prepa_Flow"):
                    opp_val = getattr(item, "syswbeff106prepa_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106prepa_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106prepa_Flow"):
                    opp_val = getattr(item, "syswbeff106prepa_Flow", None)
                    
                    setattr(item, "syswbeff106prepa_Flow", self)
                    

    @property
    def syswbeff106prepa_AbstractFunction5(self):
        return self.__syswbeff106prepa_AbstractFunction5

    @syswbeff106prepa_AbstractFunction5.setter
    def syswbeff106prepa_AbstractFunction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_AbstractFunction__syswbeff106prepa_AbstractFunction5", None)
        self.__syswbeff106prepa_AbstractFunction5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106prepa_OutputPort"):
                    opp_val = getattr(item, "syswbeff106prepa_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106prepa_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106prepa_OutputPort"):
                    opp_val = getattr(item, "syswbeff106prepa_OutputPort", None)
                    
                    setattr(item, "syswbeff106prepa_OutputPort", self)
                    

    @property
    def syswbeff106prepa_AbstractFunction3(self):
        return self.__syswbeff106prepa_AbstractFunction3

    @syswbeff106prepa_AbstractFunction3.setter
    def syswbeff106prepa_AbstractFunction3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_AbstractFunction__syswbeff106prepa_AbstractFunction3", None)
        self.__syswbeff106prepa_AbstractFunction3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106prepa_InputPort"):
                    opp_val = getattr(item, "syswbeff106prepa_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106prepa_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106prepa_InputPort"):
                    opp_val = getattr(item, "syswbeff106prepa_InputPort", None)
                    
                    setattr(item, "syswbeff106prepa_InputPort", self)
                    

class syswbeff106prepa_PatternCatalog:

    def __init__(self, id: str, syswbeff106prepa_PatternCatalog: set["syswbeff106prepa_Pattern"] = None, syswbeff106prepa_PatternCatalog14: "syswbeff106prepa_Workbench" = None):
        self.id = id
        self.syswbeff106prepa_PatternCatalog = syswbeff106prepa_PatternCatalog if syswbeff106prepa_PatternCatalog is not None else set()
        self.syswbeff106prepa_PatternCatalog14 = syswbeff106prepa_PatternCatalog14
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff106prepa_PatternCatalog14(self):
        return self.__syswbeff106prepa_PatternCatalog14

    @syswbeff106prepa_PatternCatalog14.setter
    def syswbeff106prepa_PatternCatalog14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_PatternCatalog__syswbeff106prepa_PatternCatalog14", None)
        self.__syswbeff106prepa_PatternCatalog14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106prepa_Workbench13"):
                opp_val = getattr(old_value, "syswbeff106prepa_Workbench13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106prepa_Workbench13"):
                opp_val = getattr(value, "syswbeff106prepa_Workbench13", None)
                if opp_val is None:
                    setattr(value, "syswbeff106prepa_Workbench13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def syswbeff106prepa_PatternCatalog(self):
        return self.__syswbeff106prepa_PatternCatalog

    @syswbeff106prepa_PatternCatalog.setter
    def syswbeff106prepa_PatternCatalog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_PatternCatalog__syswbeff106prepa_PatternCatalog", None)
        self.__syswbeff106prepa_PatternCatalog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syswbeff106prepa_Pattern"):
                    opp_val = getattr(item, "syswbeff106prepa_Pattern", None)
                    
                    if opp_val == self:
                        setattr(item, "syswbeff106prepa_Pattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syswbeff106prepa_Pattern"):
                    opp_val = getattr(item, "syswbeff106prepa_Pattern", None)
                    
                    setattr(item, "syswbeff106prepa_Pattern", self)
                    

class syswbeff106prepa_Function(AbstractFunction):

    pass
class syswbeff106prepa_System:

    def __init__(self, id: str, syswbeff106prepa_System: "syswbeff106prepa_Function" = None, syswbeff106prepa_System11: "syswbeff106prepa_Workbench" = None):
        self.id = id
        self.syswbeff106prepa_System = syswbeff106prepa_System
        self.syswbeff106prepa_System11 = syswbeff106prepa_System11
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def syswbeff106prepa_System11(self):
        return self.__syswbeff106prepa_System11

    @syswbeff106prepa_System11.setter
    def syswbeff106prepa_System11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_System__syswbeff106prepa_System11", None)
        self.__syswbeff106prepa_System11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106prepa_Workbench"):
                opp_val = getattr(old_value, "syswbeff106prepa_Workbench", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106prepa_Workbench", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106prepa_Workbench"):
                opp_val = getattr(value, "syswbeff106prepa_Workbench", None)
                setattr(value, "syswbeff106prepa_Workbench", self)

    @property
    def syswbeff106prepa_System(self):
        return self.__syswbeff106prepa_System

    @syswbeff106prepa_System.setter
    def syswbeff106prepa_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_syswbeff106prepa_System__syswbeff106prepa_System", None)
        self.__syswbeff106prepa_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syswbeff106prepa_Function"):
                opp_val = getattr(old_value, "syswbeff106prepa_Function", None)
                if opp_val == self:
                    setattr(old_value, "syswbeff106prepa_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syswbeff106prepa_Function"):
                opp_val = getattr(value, "syswbeff106prepa_Function", None)
                setattr(value, "syswbeff106prepa_Function", self)

class syswbeff106prepa_Flow:

    pass
class syswbeff106prepa_OutputPort(Port):

    pass
class syswbeff106prepa_InputPort(Port):

    pass