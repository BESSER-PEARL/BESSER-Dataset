from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BooleanExpression:

    pass
class gfsm_BooleanBinaryExpression(BooleanExpression):

    pass
class BooleanBinaryExpression:

    pass
class gfsm_BooleanAnd(BooleanBinaryExpression):

    pass
class gfsm_BooleanOr(BooleanBinaryExpression):

    pass
class BooleanCompareExpression:

    pass
class gfsm_BooleanGreaterThan(BooleanCompareExpression):

    pass
class gfsm_BooleanEqual(BooleanCompareExpression):

    pass
class gfsm_BooleanCompareExpression(BooleanExpression):

    pass
class IntBinaryExpression:

    pass
class gfsm_IntMult(IntBinaryExpression):

    pass
class gfsm_IntAdd(IntBinaryExpression):

    pass
class gfsm_IntExpression(ABC):

    pass
class IntOperation:

    pass
class gfsm_IntBlock(IntOperation):

    pass
class gfsm_IntVarAssign(IntOperation):

    def __init__(self, name: str, gfsm_IntVarAssign: "gfsm_IntExpression" = None, gfsm_IntVarAssign32: "gfsm_IntBlock" = None):
        self.name = name
        self.gfsm_IntVarAssign = gfsm_IntVarAssign
        self.gfsm_IntVarAssign32 = gfsm_IntVarAssign32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gfsm_IntVarAssign(self):
        return self.__gfsm_IntVarAssign

    @gfsm_IntVarAssign.setter
    def gfsm_IntVarAssign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_IntVarAssign__gfsm_IntVarAssign", None)
        self.__gfsm_IntVarAssign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_IntExpression30"):
                opp_val = getattr(old_value, "gfsm_IntExpression30", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_IntExpression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_IntExpression30"):
                opp_val = getattr(value, "gfsm_IntExpression30", None)
                setattr(value, "gfsm_IntExpression30", self)

    @property
    def gfsm_IntVarAssign32(self):
        return self.__gfsm_IntVarAssign32

    @gfsm_IntVarAssign32.setter
    def gfsm_IntVarAssign32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_IntVarAssign__gfsm_IntVarAssign32", None)
        self.__gfsm_IntVarAssign32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_IntBlock"):
                opp_val = getattr(old_value, "gfsm_IntBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_IntBlock"):
                opp_val = getattr(value, "gfsm_IntBlock", None)
                if opp_val is None:
                    setattr(value, "gfsm_IntBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class State:

    pass
class gfsm_InitialState(State):

    pass
class gfsm_FinalState(State):

    pass
class IntExpression:

    pass
class gfsm_IntVarRef(IntExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gfsm_IntNeg(IntExpression):

    pass
class gfsm_ConstExpr(IntExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class gfsm_IntBinaryExpression(IntExpression):

    pass
class gfsm_State:

    def __init__(self, name: str, gfsm_State: "gfsm_IntOperation" = None, gfsm_State7: "gfsm_IntOperation" = None, states: "gfsm_FSM" = None, State: "gfsm_Transition" = None, State4: "gfsm_Transition" = None, gfsm_State22: "gfsm_FSM" = None, from: set["gfsm_Transition"] = None, to: set["gfsm_Transition"] = None, State15: "gfsm_FSM" = None):
        self.name = name
        self.gfsm_State = gfsm_State
        self.gfsm_State7 = gfsm_State7
        self.states = states
        self.State = State
        self.State4 = State4
        self.gfsm_State22 = gfsm_State22
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.State15 = State15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def gfsm_State(self):
        return self.__gfsm_State

    @gfsm_State.setter
    def gfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__gfsm_State", None)
        self.__gfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_IntOperation"):
                opp_val = getattr(old_value, "gfsm_IntOperation", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_IntOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_IntOperation"):
                opp_val = getattr(value, "gfsm_IntOperation", None)
                setattr(value, "gfsm_IntOperation", self)

    @property
    def gfsm_State22(self):
        return self.__gfsm_State22

    @gfsm_State22.setter
    def gfsm_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__gfsm_State22", None)
        self.__gfsm_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_FSM21"):
                opp_val = getattr(old_value, "gfsm_FSM21", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_FSM21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_FSM21"):
                opp_val = getattr(value, "gfsm_FSM21", None)
                setattr(value, "gfsm_FSM21", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    setattr(item, "Transition13", self)
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingtransitions"):
                opp_val = getattr(old_value, "outgoingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingtransitions"):
                opp_val = getattr(value, "outgoingtransitions", None)
                setattr(value, "outgoingtransitions", self)

    @property
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State15", None)
        self.__State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm"):
                opp_val = getattr(old_value, "fsm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm"):
                opp_val = getattr(value, "fsm", None)
                if opp_val is None:
                    setattr(value, "fsm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM10"):
                opp_val = getattr(old_value, "FSM10", None)
                if opp_val == self:
                    setattr(old_value, "FSM10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM10"):
                opp_val = getattr(value, "FSM10", None)
                setattr(value, "FSM10", self)

    @property
    def State4(self):
        return self.__State4

    @State4.setter
    def State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__State4", None)
        self.__State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incommingtransitions"):
                opp_val = getattr(old_value, "incommingtransitions", None)
                if opp_val == self:
                    setattr(old_value, "incommingtransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incommingtransitions"):
                opp_val = getattr(value, "incommingtransitions", None)
                setattr(value, "incommingtransitions", self)

    @property
    def gfsm_State7(self):
        return self.__gfsm_State7

    @gfsm_State7.setter
    def gfsm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_State__gfsm_State7", None)
        self.__gfsm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_IntOperation8"):
                opp_val = getattr(old_value, "gfsm_IntOperation8", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_IntOperation8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_IntOperation8"):
                opp_val = getattr(value, "gfsm_IntOperation8", None)
                setattr(value, "gfsm_IntOperation8", self)

class gfsm_FSM:

    def __init__(self, name: str, FSM10: "gfsm_State" = None, FSM: "gfsm_Transition" = None, gfsm_FSM: "gfsm_InitialState" = None, gfsm_FSM21: "gfsm_State" = None, fsm: set["gfsm_State"] = None, fsm17: set["gfsm_Transition"] = None):
        self.name = name
        self.FSM10 = FSM10
        self.FSM = FSM
        self.gfsm_FSM = gfsm_FSM
        self.gfsm_FSM21 = gfsm_FSM21
        self.fsm = fsm if fsm is not None else set()
        self.fsm17 = fsm17 if fsm17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FSM10(self):
        return self.__FSM10

    @FSM10.setter
    def FSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__FSM10", None)
        self.__FSM10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def gfsm_FSM21(self):
        return self.__gfsm_FSM21

    @gfsm_FSM21.setter
    def gfsm_FSM21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__gfsm_FSM21", None)
        self.__gfsm_FSM21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_State22"):
                opp_val = getattr(old_value, "gfsm_State22", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_State22"):
                opp_val = getattr(value, "gfsm_State22", None)
                setattr(value, "gfsm_State22", self)

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__fsm", None)
        self.__fsm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State15"):
                    opp_val = getattr(item, "State15", None)
                    
                    if opp_val == self:
                        setattr(item, "State15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State15"):
                    opp_val = getattr(item, "State15", None)
                    
                    setattr(item, "State15", self)
                    

    @property
    def fsm17(self):
        return self.__fsm17

    @fsm17.setter
    def fsm17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__fsm17", None)
        self.__fsm17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    setattr(item, "Transition18", self)
                    

    @property
    def gfsm_FSM(self):
        return self.__gfsm_FSM

    @gfsm_FSM.setter
    def gfsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_FSM__gfsm_FSM", None)
        self.__gfsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_InitialState"):
                opp_val = getattr(old_value, "gfsm_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_InitialState"):
                opp_val = getattr(value, "gfsm_InitialState", None)
                setattr(value, "gfsm_InitialState", self)

class gfsm_BooleanExpression(ABC):

    pass
class gfsm_Transition:

    def __init__(self, event: str, gfsm_Transition: "gfsm_BooleanExpression" = None, transitions: "gfsm_FSM" = None, outgoingtransitions: "gfsm_State" = None, incommingtransitions: "gfsm_State" = None, Transition: "gfsm_State" = None, Transition13: "gfsm_State" = None, Transition18: "gfsm_FSM" = None):
        self.event = event
        self.gfsm_Transition = gfsm_Transition
        self.transitions = transitions
        self.outgoingtransitions = outgoingtransitions
        self.incommingtransitions = incommingtransitions
        self.Transition = Transition
        self.Transition13 = Transition13
        self.Transition18 = Transition18
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def incommingtransitions(self):
        return self.__incommingtransitions

    @incommingtransitions.setter
    def incommingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__incommingtransitions", None)
        self.__incommingtransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State4"):
                opp_val = getattr(old_value, "State4", None)
                if opp_val == self:
                    setattr(old_value, "State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State4"):
                opp_val = getattr(value, "State4", None)
                setattr(value, "State4", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

    @property
    def outgoingtransitions(self):
        return self.__outgoingtransitions

    @outgoingtransitions.setter
    def outgoingtransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__outgoingtransitions", None)
        self.__outgoingtransitions = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition13", None)
        self.__Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition18(self):
        return self.__Transition18

    @Transition18.setter
    def Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__Transition18", None)
        self.__Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm17"):
                opp_val = getattr(old_value, "fsm17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm17"):
                opp_val = getattr(value, "fsm17", None)
                if opp_val is None:
                    setattr(value, "fsm17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gfsm_Transition(self):
        return self.__gfsm_Transition

    @gfsm_Transition.setter
    def gfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gfsm_Transition__gfsm_Transition", None)
        self.__gfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gfsm_BooleanExpression"):
                opp_val = getattr(old_value, "gfsm_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "gfsm_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gfsm_BooleanExpression"):
                opp_val = getattr(value, "gfsm_BooleanExpression", None)
                setattr(value, "gfsm_BooleanExpression", self)

class gfsm_IntOperation(ABC):

    pass