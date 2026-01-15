from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class basicfsm_InitialState(State):

    pass
class basicfsm_Action(ABC):

    pass
class basicfsm_Guard(ABC):

    pass
class basicfsm_State:

    def __init__(self, name: str, basicfsm_State: "basicfsm_Machine" = None, State8: "basicfsm_Trans" = None, tgt: set["basicfsm_Trans"] = None, src: set["basicfsm_Trans"] = None, State: "basicfsm_Trans" = None):
        self.name = name
        self.basicfsm_State = basicfsm_State
        self.State8 = State8
        self.tgt = tgt if tgt is not None else set()
        self.src = src if src is not None else set()
        self.State = State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_State__State8", None)
        self.__State8 = value
        
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
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_State__tgt", None)
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
    def basicfsm_State(self):
        return self.__basicfsm_State

    @basicfsm_State.setter
    def basicfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_State__basicfsm_State", None)
        self.__basicfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfsm_Machine"):
                opp_val = getattr(old_value, "basicfsm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfsm_Machine"):
                opp_val = getattr(value, "basicfsm_Machine", None)
                if opp_val is None:
                    setattr(value, "basicfsm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_State__State", None)
        self.__State = value
        
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_State__src", None)
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
                    

class basicfsm_Machine:

    def __init__(self, name: str, basicfsm_Machine2: set["basicfsm_Trans"] = None, basicfsm_Machine: set["basicfsm_State"] = None):
        self.name = name
        self.basicfsm_Machine2 = basicfsm_Machine2 if basicfsm_Machine2 is not None else set()
        self.basicfsm_Machine = basicfsm_Machine if basicfsm_Machine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def basicfsm_Machine(self):
        return self.__basicfsm_Machine

    @basicfsm_Machine.setter
    def basicfsm_Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Machine__basicfsm_Machine", None)
        self.__basicfsm_Machine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfsm_State"):
                    opp_val = getattr(item, "basicfsm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfsm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfsm_State"):
                    opp_val = getattr(item, "basicfsm_State", None)
                    
                    setattr(item, "basicfsm_State", self)
                    

    @property
    def basicfsm_Machine2(self):
        return self.__basicfsm_Machine2

    @basicfsm_Machine2.setter
    def basicfsm_Machine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Machine__basicfsm_Machine2", None)
        self.__basicfsm_Machine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "basicfsm_Trans"):
                    opp_val = getattr(item, "basicfsm_Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "basicfsm_Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "basicfsm_Trans"):
                    opp_val = getattr(item, "basicfsm_Trans", None)
                    
                    setattr(item, "basicfsm_Trans", self)
                    

class basicfsm_Trans:

    def __init__(self, event: str, basicfsm_Trans: "basicfsm_Machine" = None, out: "basicfsm_State" = None, in: "basicfsm_State" = None, Trans: "basicfsm_State" = None, Trans5: "basicfsm_State" = None, basicfsm_Trans10: "basicfsm_Guard" = None, basicfsm_Trans12: "basicfsm_Action" = None):
        self.event = event
        self.basicfsm_Trans = basicfsm_Trans
        self.out = out
        self.in = in
        self.Trans = Trans
        self.Trans5 = Trans5
        self.basicfsm_Trans10 = basicfsm_Trans10
        self.basicfsm_Trans12 = basicfsm_Trans12
        
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
        old_value = getattr(self, f"_basicfsm_Trans__out", None)
        self.__out = value
        
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

    @property
    def basicfsm_Trans10(self):
        return self.__basicfsm_Trans10

    @basicfsm_Trans10.setter
    def basicfsm_Trans10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__basicfsm_Trans10", None)
        self.__basicfsm_Trans10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfsm_Guard"):
                opp_val = getattr(old_value, "basicfsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "basicfsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfsm_Guard"):
                opp_val = getattr(value, "basicfsm_Guard", None)
                setattr(value, "basicfsm_Guard", self)

    @property
    def basicfsm_Trans(self):
        return self.__basicfsm_Trans

    @basicfsm_Trans.setter
    def basicfsm_Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__basicfsm_Trans", None)
        self.__basicfsm_Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfsm_Machine2"):
                opp_val = getattr(old_value, "basicfsm_Machine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfsm_Machine2"):
                opp_val = getattr(value, "basicfsm_Machine2", None)
                if opp_val is None:
                    setattr(value, "basicfsm_Machine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def basicfsm_Trans12(self):
        return self.__basicfsm_Trans12

    @basicfsm_Trans12.setter
    def basicfsm_Trans12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__basicfsm_Trans12", None)
        self.__basicfsm_Trans12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicfsm_Action"):
                opp_val = getattr(old_value, "basicfsm_Action", None)
                if opp_val == self:
                    setattr(old_value, "basicfsm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicfsm_Action"):
                opp_val = getattr(value, "basicfsm_Action", None)
                setattr(value, "basicfsm_Action", self)

    @property
    def Trans5(self):
        return self.__Trans5

    @Trans5.setter
    def Trans5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__Trans5", None)
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
    def Trans(self):
        return self.__Trans

    @Trans.setter
    def Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__Trans", None)
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
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_basicfsm_Trans__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State8"):
                opp_val = getattr(old_value, "State8", None)
                if opp_val == self:
                    setattr(old_value, "State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State8"):
                opp_val = getattr(value, "State8", None)
                setattr(value, "State8", self)
