from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, input: str, output: str, transitions: "fsm_State" = None, fsm_Transition: "fsm_State" = None, Transition: "fsm_State" = None):
        self.input = input
        self.output = output
        self.transitions = transitions
        self.fsm_Transition = fsm_Transition
        self.Transition = Transition
        
    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__transitions", None)
        self.__transitions = value
        
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
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State6"):
                opp_val = getattr(old_value, "fsm_State6", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State6"):
                opp_val = getattr(value, "fsm_State6", None)
                setattr(value, "fsm_State6", self)

class NamedElement:

    pass
class fsm_State(NamedElement):

    def __init__(self, isFinal: bool, fsm_State: "fsm_StateMachine" = None, fsm_State3: "fsm_StateMachine" = None, State: "fsm_Transition" = None, fsm_State6: "fsm_Transition" = None, source: set["fsm_Transition"] = None):
        self.isFinal = isFinal
        self.fsm_State = fsm_State
        self.fsm_State3 = fsm_State3
        self.State = State
        self.fsm_State6 = fsm_State6
        self.source = source if source is not None else set()
        
    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State", None)
        self.__State = value
        
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
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine"):
                opp_val = getattr(old_value, "fsm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine"):
                opp_val = getattr(value, "fsm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State3(self):
        return self.__fsm_State3

    @fsm_State3.setter
    def fsm_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State3", None)
        self.__fsm_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine2"):
                opp_val = getattr(old_value, "fsm_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "fsm_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine2"):
                opp_val = getattr(value, "fsm_StateMachine2", None)
                setattr(value, "fsm_StateMachine2", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__source", None)
        self.__source = value if value is not None else set()
        
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
    def fsm_State6(self):
        return self.__fsm_State6

    @fsm_State6.setter
    def fsm_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State6", None)
        self.__fsm_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

class fsm_FSMModel(NamedElement):

    pass
class fsm_StateMachine(NamedElement):

    pass
class fsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
