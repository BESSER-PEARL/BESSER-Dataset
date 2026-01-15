from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FSM_Transition:

    def __init__(self, input: str, output: str, Transition: "FSM_State" = None, FSM_Transition: "FSM_State" = None, transitions: "FSM_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.FSM_Transition = FSM_Transition
        self.transitions = transitions
        
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
    def FSM_Transition(self):
        return self.__FSM_Transition

    @FSM_Transition.setter
    def FSM_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_Transition__FSM_Transition", None)
        self.__FSM_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_State8"):
                opp_val = getattr(old_value, "FSM_State8", None)
                if opp_val == self:
                    setattr(old_value, "FSM_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_State8"):
                opp_val = getattr(value, "FSM_State8", None)
                setattr(value, "FSM_State8", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_Transition__Transition", None)
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
        old_value = getattr(self, f"_FSM_Transition__transitions", None)
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

class FSM_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class FSM_StateMachine(NamedElement):

    pass
class FSM_State(NamedElement):

    def __init__(self, isFinal: bool, FSM_State: "FSM_StateMachine" = None, FSM_State5: "FSM_StateMachine" = None, source: set["FSM_Transition"] = None, FSM_State8: "FSM_Transition" = None, State: "FSM_Transition" = None):
        self.isFinal = isFinal
        self.FSM_State = FSM_State
        self.FSM_State5 = FSM_State5
        self.source = source if source is not None else set()
        self.FSM_State8 = FSM_State8
        self.State = State
        
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
        old_value = getattr(self, f"_FSM_State__State", None)
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
    def FSM_State(self):
        return self.__FSM_State

    @FSM_State.setter
    def FSM_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__FSM_State", None)
        self.__FSM_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_StateMachine2"):
                opp_val = getattr(old_value, "FSM_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "FSM_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_StateMachine2"):
                opp_val = getattr(value, "FSM_StateMachine2", None)
                setattr(value, "FSM_StateMachine2", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__source", None)
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
    def FSM_State5(self):
        return self.__FSM_State5

    @FSM_State5.setter
    def FSM_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__FSM_State5", None)
        self.__FSM_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_StateMachine4"):
                opp_val = getattr(old_value, "FSM_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_StateMachine4"):
                opp_val = getattr(value, "FSM_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "FSM_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FSM_State8(self):
        return self.__FSM_State8

    @FSM_State8.setter
    def FSM_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_State__FSM_State8", None)
        self.__FSM_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_Transition"):
                opp_val = getattr(old_value, "FSM_Transition", None)
                if opp_val == self:
                    setattr(old_value, "FSM_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_Transition"):
                opp_val = getattr(value, "FSM_Transition", None)
                setattr(value, "FSM_Transition", self)

class FSM_FSMModel(NamedElement):

    pass