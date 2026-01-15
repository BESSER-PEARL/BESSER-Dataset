from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class basicFsmEnv_Guard(ABC):

    pass
class basicFsmEnv_VarDecl:

    def __init__(self, name: str, value: str, basicFsmEnv_VarDecl: "basicFsmEnv_State" = None):
        self.name = name
        self.value = value
        self.basicFsmEnv_VarDecl = basicFsmEnv_VarDecl
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def basicFsmEnv_VarDecl(self):
        return self.__basicFsmEnv_VarDecl

    @basicFsmEnv_VarDecl.setter
    def basicFsmEnv_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_VarDecl__basicFsmEnv_VarDecl", None)
        self.__basicFsmEnv_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFsmEnv_State7"):
                opp_val = getattr(old_value, "basicFsmEnv_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFsmEnv_State7"):
                opp_val = getattr(value, "basicFsmEnv_State7", None)
                if opp_val is None:
                    setattr(value, "basicFsmEnv_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class basicFsmEnv_InitialState(State):

    pass
class basicFsmEnv_Action(ABC):

    pass
class basicFsmEnv_Machine:

    def __init__(self, name: str, basicFsmEnv_Machine: set["basicFsmEnv_State"] = None, basicFsmEnv_Machine2: set["basicFsmEnv_Trans"] = None):
        self.name = name
        self.basicFsmEnv_Machine = basicFsmEnv_Machine if basicFsmEnv_Machine is not None else set()
        self.basicFsmEnv_Machine2 = basicFsmEnv_Machine2 if basicFsmEnv_Machine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basicFsmEnv_Machine2(self):
        return self.__basicFsmEnv_Machine2

    @basicFsmEnv_Machine2.setter
    def basicFsmEnv_Machine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Machine__basicFsmEnv_Machine2", None)
        self.__basicFsmEnv_Machine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicFsmEnv_Trans"):
                    opp_val = getattr(item, "basicFsmEnv_Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "basicFsmEnv_Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicFsmEnv_Trans"):
                    opp_val = getattr(item, "basicFsmEnv_Trans", None)
                    
                    setattr(item, "basicFsmEnv_Trans", self)
                    

    @property
    def basicFsmEnv_Machine(self):
        return self.__basicFsmEnv_Machine

    @basicFsmEnv_Machine.setter
    def basicFsmEnv_Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Machine__basicFsmEnv_Machine", None)
        self.__basicFsmEnv_Machine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicFsmEnv_State"):
                    opp_val = getattr(item, "basicFsmEnv_State", None)
                    
                    if opp_val == self:
                        setattr(item, "basicFsmEnv_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicFsmEnv_State"):
                    opp_val = getattr(item, "basicFsmEnv_State", None)
                    
                    setattr(item, "basicFsmEnv_State", self)
                    

class basicFsmEnv_Trans:

    def __init__(self, event: str, basicFsmEnv_Trans: "basicFsmEnv_Machine" = None, basicFsmEnv_Trans14: "basicFsmEnv_Action" = None, Trans: "basicFsmEnv_State" = None, Trans5: "basicFsmEnv_State" = None, in: "basicFsmEnv_State" = None, out: "basicFsmEnv_State" = None, basicFsmEnv_Trans12: "basicFsmEnv_Guard" = None):
        self.event = event
        self.basicFsmEnv_Trans = basicFsmEnv_Trans
        self.basicFsmEnv_Trans14 = basicFsmEnv_Trans14
        self.Trans = Trans
        self.Trans5 = Trans5
        self.in = in
        self.out = out
        self.basicFsmEnv_Trans12 = basicFsmEnv_Trans12
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__out", None)
        self.__out = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State10"):
                opp_val = getattr(old_value, "State10", None)
                if opp_val == self:
                    setattr(old_value, "State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State10"):
                opp_val = getattr(value, "State10", None)
                setattr(value, "State10", self)

    @property
    def basicFsmEnv_Trans14(self):
        return self.__basicFsmEnv_Trans14

    @basicFsmEnv_Trans14.setter
    def basicFsmEnv_Trans14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__basicFsmEnv_Trans14", None)
        self.__basicFsmEnv_Trans14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFsmEnv_Action"):
                opp_val = getattr(old_value, "basicFsmEnv_Action", None)
                if opp_val == self:
                    setattr(old_value, "basicFsmEnv_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFsmEnv_Action"):
                opp_val = getattr(value, "basicFsmEnv_Action", None)
                setattr(value, "basicFsmEnv_Action", self)

    @property
    def basicFsmEnv_Trans12(self):
        return self.__basicFsmEnv_Trans12

    @basicFsmEnv_Trans12.setter
    def basicFsmEnv_Trans12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__basicFsmEnv_Trans12", None)
        self.__basicFsmEnv_Trans12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFsmEnv_Guard"):
                opp_val = getattr(old_value, "basicFsmEnv_Guard", None)
                if opp_val == self:
                    setattr(old_value, "basicFsmEnv_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFsmEnv_Guard"):
                opp_val = getattr(value, "basicFsmEnv_Guard", None)
                setattr(value, "basicFsmEnv_Guard", self)

    @property
    def Trans(self):
        return self.__Trans

    @Trans.setter
    def Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__Trans", None)
        self.__Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgt"):
                opp_val = getattr(old_value, "tgt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgt"):
                opp_val = getattr(value, "tgt", None)
                if opp_val is None:
                    setattr(value, "tgt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicFsmEnv_Trans(self):
        return self.__basicFsmEnv_Trans

    @basicFsmEnv_Trans.setter
    def basicFsmEnv_Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__basicFsmEnv_Trans", None)
        self.__basicFsmEnv_Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFsmEnv_Machine2"):
                opp_val = getattr(old_value, "basicFsmEnv_Machine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFsmEnv_Machine2"):
                opp_val = getattr(value, "basicFsmEnv_Machine2", None)
                if opp_val is None:
                    setattr(value, "basicFsmEnv_Machine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Trans5(self):
        return self.__Trans5

    @Trans5.setter
    def Trans5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__Trans5", None)
        self.__Trans5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_Trans__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

class basicFsmEnv_State:

    def __init__(self, name: str, basicFsmEnv_State: "basicFsmEnv_Machine" = None, tgt: set["basicFsmEnv_Trans"] = None, src: set["basicFsmEnv_Trans"] = None, basicFsmEnv_State7: set["basicFsmEnv_VarDecl"] = None, State: "basicFsmEnv_Trans" = None, State10: "basicFsmEnv_Trans" = None):
        self.name = name
        self.basicFsmEnv_State = basicFsmEnv_State
        self.tgt = tgt if tgt is not None else set()
        self.src = src if src is not None else set()
        self.basicFsmEnv_State7 = basicFsmEnv_State7 if basicFsmEnv_State7 is not None else set()
        self.State = State
        self.State10 = State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__tgt", None)
        self.__tgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trans"):
                    opp_val = getattr(item, "Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trans"):
                    opp_val = getattr(item, "Trans", None)
                    
                    setattr(item, "Trans", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trans5"):
                    opp_val = getattr(item, "Trans5", None)
                    
                    if opp_val == self:
                        setattr(item, "Trans5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trans5"):
                    opp_val = getattr(item, "Trans5", None)
                    
                    setattr(item, "Trans5", self)
                    

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__State10", None)
        self.__State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

    @property
    def basicFsmEnv_State(self):
        return self.__basicFsmEnv_State

    @basicFsmEnv_State.setter
    def basicFsmEnv_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__basicFsmEnv_State", None)
        self.__basicFsmEnv_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFsmEnv_Machine"):
                opp_val = getattr(old_value, "basicFsmEnv_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFsmEnv_Machine"):
                opp_val = getattr(value, "basicFsmEnv_Machine", None)
                if opp_val is None:
                    setattr(value, "basicFsmEnv_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicFsmEnv_State7(self):
        return self.__basicFsmEnv_State7

    @basicFsmEnv_State7.setter
    def basicFsmEnv_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicFsmEnv_State__basicFsmEnv_State7", None)
        self.__basicFsmEnv_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicFsmEnv_VarDecl"):
                    opp_val = getattr(item, "basicFsmEnv_VarDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "basicFsmEnv_VarDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicFsmEnv_VarDecl"):
                    opp_val = getattr(item, "basicFsmEnv_VarDecl", None)
                    
                    setattr(item, "basicFsmEnv_VarDecl", self)
                    
