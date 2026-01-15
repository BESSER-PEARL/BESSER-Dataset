from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ecore_ENamedElement(ABC):

    pass
class FSM:

    pass
class ecore_EClass(FSM):

    pass
class ecore_Transition:

    def __init__(self, input: str, output: str, Transition: "ecore_State" = None, Transition8: "ecore_State" = None, outgoingTransition: "ecore_State" = None, incomingTransition: "ecore_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition8 = Transition8
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__Transition8", None)
        self.__Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State14"):
                opp_val = getattr(old_value, "State14", None)
                if opp_val == self:
                    setattr(old_value, "State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State14"):
                opp_val = getattr(value, "State14", None)
                setattr(value, "State14", self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State12"):
                opp_val = getattr(old_value, "State12", None)
                if opp_val == self:
                    setattr(old_value, "State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State12"):
                opp_val = getattr(value, "State12", None)
                setattr(value, "State12", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_Transition__Transition", None)
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

class ecore_State:

    def __init__(self, name: str, State: "ecore_FSM" = None, ecore_State: "ecore_FSM" = None, ecore_State4: "ecore_FSM" = None, ownedState: "ecore_FSM" = None, source: set["ecore_Transition"] = None, target: set["ecore_Transition"] = None, State12: "ecore_Transition" = None, State14: "ecore_Transition" = None, ecore_State10: set["ecore_EClass"] = None):
        self.name = name
        self.State = State
        self.ecore_State = ecore_State
        self.ecore_State4 = ecore_State4
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State12 = State12
        self.State14 = State14
        self.ecore_State10 = ecore_State10 if ecore_State10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecore_State4(self):
        return self.__ecore_State4

    @ecore_State4.setter
    def ecore_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State4", None)
        self.__ecore_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_FSM3"):
                opp_val = getattr(old_value, "ecore_FSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_FSM3"):
                opp_val = getattr(value, "ecore_FSM3", None)
                if opp_val is None:
                    setattr(value, "ecore_FSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ecore_State(self):
        return self.__ecore_State

    @ecore_State.setter
    def ecore_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State", None)
        self.__ecore_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecore_FSM"):
                opp_val = getattr(old_value, "ecore_FSM", None)
                if opp_val == self:
                    setattr(old_value, "ecore_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecore_FSM"):
                opp_val = getattr(value, "ecore_FSM", None)
                setattr(value, "ecore_FSM", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__source", None)
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
    def ecore_State10(self):
        return self.__ecore_State10

    @ecore_State10.setter
    def ecore_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ecore_State10", None)
        self.__ecore_State10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ecore_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecore_EClass"):
                    opp_val = getattr(item, "ecore_EClass", None)
                    
                    setattr(item, "ecore_EClass", self)
                    

    @property
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State12", None)
        self.__State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransition"):
                opp_val = getattr(old_value, "outgoingTransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransition"):
                opp_val = getattr(value, "outgoingTransition", None)
                setattr(value, "outgoingTransition", self)

    @property
    def State14(self):
        return self.__State14

    @State14.setter
    def State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State14", None)
        self.__State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransition"):
                opp_val = getattr(old_value, "incomingTransition", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransition"):
                opp_val = getattr(value, "incomingTransition", None)
                setattr(value, "incomingTransition", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecore_State__ownedState", None)
        self.__ownedState = value
        
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

class ecore_FSM:

    pass