from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SimplStateMachineDC_StateMachine:

    pass
class PseudoState:

    pass
class SimplStateMachineDC_InitialState(PseudoState):

    pass
class State:

    pass
class SimplStateMachineDC_PseudoState(State):

    pass
class SimplStateMachineDC_CompositeState(State):

    pass
class SimplStateMachineDC_State:

    def __init__(self, name: str, isActive: bool, Ord: str, Inh: str, OrdIf: str, InhIf: str, SimplStateMachineDC_State: "SimplStateMachineDC_StateMachine" = None, states: "SimplStateMachineDC_CompositeState" = None, State: "SimplStateMachineDC_CompositeState" = None, SimplStateMachineDC_State7: "SimplStateMachineDC_PseudoState" = None, SimplStateMachineDC_State10: "SimplStateMachineDC_Transition" = None, SimplStateMachineDC_State13: "SimplStateMachineDC_Transition" = None):
        self.name = name
        self.isActive = isActive
        self.Ord = Ord
        self.Inh = Inh
        self.OrdIf = OrdIf
        self.InhIf = InhIf
        self.SimplStateMachineDC_State = SimplStateMachineDC_State
        self.states = states
        self.State = State
        self.SimplStateMachineDC_State7 = SimplStateMachineDC_State7
        self.SimplStateMachineDC_State10 = SimplStateMachineDC_State10
        self.SimplStateMachineDC_State13 = SimplStateMachineDC_State13
        
    @property
    def Inh(self) -> str:
        return self.__Inh

    @Inh.setter
    def Inh(self, Inh: str):
        self.__Inh = Inh

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def OrdIf(self) -> str:
        return self.__OrdIf

    @OrdIf.setter
    def OrdIf(self, OrdIf: str):
        self.__OrdIf = OrdIf

    @property
    def InhIf(self) -> str:
        return self.__InhIf

    @InhIf.setter
    def InhIf(self, InhIf: str):
        self.__InhIf = InhIf

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Ord(self) -> str:
        return self.__Ord

    @Ord.setter
    def Ord(self, Ord: str):
        self.__Ord = Ord

    @property
    def SimplStateMachineDC_State10(self):
        return self.__SimplStateMachineDC_State10

    @SimplStateMachineDC_State10.setter
    def SimplStateMachineDC_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__SimplStateMachineDC_State10", None)
        self.__SimplStateMachineDC_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_Transition9"):
                opp_val = getattr(old_value, "SimplStateMachineDC_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachineDC_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_Transition9"):
                opp_val = getattr(value, "SimplStateMachineDC_Transition9", None)
                setattr(value, "SimplStateMachineDC_Transition9", self)

    @property
    def SimplStateMachineDC_State(self):
        return self.__SimplStateMachineDC_State

    @SimplStateMachineDC_State.setter
    def SimplStateMachineDC_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__SimplStateMachineDC_State", None)
        self.__SimplStateMachineDC_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_StateMachine2"):
                opp_val = getattr(old_value, "SimplStateMachineDC_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_StateMachine2"):
                opp_val = getattr(value, "SimplStateMachineDC_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "SimplStateMachineDC_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimplStateMachineDC_State13(self):
        return self.__SimplStateMachineDC_State13

    @SimplStateMachineDC_State13.setter
    def SimplStateMachineDC_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__SimplStateMachineDC_State13", None)
        self.__SimplStateMachineDC_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_Transition12"):
                opp_val = getattr(old_value, "SimplStateMachineDC_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachineDC_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_Transition12"):
                opp_val = getattr(value, "SimplStateMachineDC_Transition12", None)
                setattr(value, "SimplStateMachineDC_Transition12", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeState"):
                opp_val = getattr(old_value, "CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeState"):
                opp_val = getattr(value, "CompositeState", None)
                setattr(value, "CompositeState", self)

    @property
    def SimplStateMachineDC_State7(self):
        return self.__SimplStateMachineDC_State7

    @SimplStateMachineDC_State7.setter
    def SimplStateMachineDC_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_State__SimplStateMachineDC_State7", None)
        self.__SimplStateMachineDC_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_PseudoState"):
                opp_val = getattr(old_value, "SimplStateMachineDC_PseudoState", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachineDC_PseudoState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_PseudoState"):
                opp_val = getattr(value, "SimplStateMachineDC_PseudoState", None)
                setattr(value, "SimplStateMachineDC_PseudoState", self)

class SimplStateMachineDC_Transition:

    def __init__(self, event: str, SimplStateMachineDC_Transition: "SimplStateMachineDC_StateMachine" = None, SimplStateMachineDC_Transition9: "SimplStateMachineDC_State" = None, SimplStateMachineDC_Transition12: "SimplStateMachineDC_State" = None):
        self.event = event
        self.SimplStateMachineDC_Transition = SimplStateMachineDC_Transition
        self.SimplStateMachineDC_Transition9 = SimplStateMachineDC_Transition9
        self.SimplStateMachineDC_Transition12 = SimplStateMachineDC_Transition12
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def SimplStateMachineDC_Transition9(self):
        return self.__SimplStateMachineDC_Transition9

    @SimplStateMachineDC_Transition9.setter
    def SimplStateMachineDC_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_Transition__SimplStateMachineDC_Transition9", None)
        self.__SimplStateMachineDC_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_State10"):
                opp_val = getattr(old_value, "SimplStateMachineDC_State10", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachineDC_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_State10"):
                opp_val = getattr(value, "SimplStateMachineDC_State10", None)
                setattr(value, "SimplStateMachineDC_State10", self)

    @property
    def SimplStateMachineDC_Transition12(self):
        return self.__SimplStateMachineDC_Transition12

    @SimplStateMachineDC_Transition12.setter
    def SimplStateMachineDC_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_Transition__SimplStateMachineDC_Transition12", None)
        self.__SimplStateMachineDC_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_State13"):
                opp_val = getattr(old_value, "SimplStateMachineDC_State13", None)
                if opp_val == self:
                    setattr(old_value, "SimplStateMachineDC_State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_State13"):
                opp_val = getattr(value, "SimplStateMachineDC_State13", None)
                setattr(value, "SimplStateMachineDC_State13", self)

    @property
    def SimplStateMachineDC_Transition(self):
        return self.__SimplStateMachineDC_Transition

    @SimplStateMachineDC_Transition.setter
    def SimplStateMachineDC_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimplStateMachineDC_Transition__SimplStateMachineDC_Transition", None)
        self.__SimplStateMachineDC_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimplStateMachineDC_StateMachine"):
                opp_val = getattr(old_value, "SimplStateMachineDC_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimplStateMachineDC_StateMachine"):
                opp_val = getattr(value, "SimplStateMachineDC_StateMachine", None)
                if opp_val is None:
                    setattr(value, "SimplStateMachineDC_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
