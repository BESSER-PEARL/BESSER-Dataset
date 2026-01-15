from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class compositefsm_Transition:

    def __init__(self, input: str, output: str, Transition: "compositefsm_State" = None, Transition8: "compositefsm_State" = None, outgoingTransition: "compositefsm_State" = None, incomingTransition: "compositefsm_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition8 = Transition8
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
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
        old_value = getattr(self, f"_compositefsm_Transition__Transition", None)
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State16"):
                opp_val = getattr(old_value, "State16", None)
                if opp_val == self:
                    setattr(old_value, "State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State16"):
                opp_val = getattr(value, "State16", None)
                setattr(value, "State16", self)

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_Transition__Transition8", None)
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
        old_value = getattr(self, f"_compositefsm_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State18"):
                opp_val = getattr(old_value, "State18", None)
                if opp_val == self:
                    setattr(old_value, "State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State18"):
                opp_val = getattr(value, "State18", None)
                setattr(value, "State18", self)

class compositefsm_State:

    def __init__(self, name: str, State: "compositefsm_FSM" = None, compositefsm_State: "compositefsm_FSM" = None, compositefsm_State4: "compositefsm_FSM" = None, ownedState: "compositefsm_FSM" = None, source: set["compositefsm_Transition"] = None, target: set["compositefsm_Transition"] = None, State11: "compositefsm_State" = None, superState: set["compositefsm_State"] = None, State14: "compositefsm_State" = None, subStates: "compositefsm_State" = None, State16: "compositefsm_Transition" = None, State18: "compositefsm_Transition" = None):
        self.name = name
        self.State = State
        self.compositefsm_State = compositefsm_State
        self.compositefsm_State4 = compositefsm_State4
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State11 = State11
        self.superState = superState if superState is not None else set()
        self.State14 = State14
        self.subStates = subStates
        self.State16 = State16
        self.State18 = State18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__State", None)
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__target", None)
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
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__ownedState", None)
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

    @property
    def subStates(self):
        return self.__subStates

    @subStates.setter
    def subStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__subStates", None)
        self.__subStates = value
        
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
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superState"):
                opp_val = getattr(old_value, "superState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superState"):
                opp_val = getattr(value, "superState", None)
                if opp_val is None:
                    setattr(value, "superState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State18(self):
        return self.__State18

    @State18.setter
    def State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__State18", None)
        self.__State18 = value
        
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
    def State16(self):
        return self.__State16

    @State16.setter
    def State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__State16", None)
        self.__State16 = value
        
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
    def superState(self):
        return self.__superState

    @superState.setter
    def superState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__superState", None)
        self.__superState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State11"):
                    opp_val = getattr(item, "State11", None)
                    
                    if opp_val == self:
                        setattr(item, "State11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State11"):
                    opp_val = getattr(item, "State11", None)
                    
                    setattr(item, "State11", self)
                    

    @property
    def compositefsm_State(self):
        return self.__compositefsm_State

    @compositefsm_State.setter
    def compositefsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__compositefsm_State", None)
        self.__compositefsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compositefsm_FSM"):
                opp_val = getattr(old_value, "compositefsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "compositefsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compositefsm_FSM"):
                opp_val = getattr(value, "compositefsm_FSM", None)
                setattr(value, "compositefsm_FSM", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__source", None)
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
    def State14(self):
        return self.__State14

    @State14.setter
    def State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__State14", None)
        self.__State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subStates"):
                opp_val = getattr(old_value, "subStates", None)
                if opp_val == self:
                    setattr(old_value, "subStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subStates"):
                opp_val = getattr(value, "subStates", None)
                setattr(value, "subStates", self)

    @property
    def compositefsm_State4(self):
        return self.__compositefsm_State4

    @compositefsm_State4.setter
    def compositefsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compositefsm_State__compositefsm_State4", None)
        self.__compositefsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compositefsm_FSM3"):
                opp_val = getattr(old_value, "compositefsm_FSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compositefsm_FSM3"):
                opp_val = getattr(value, "compositefsm_FSM3", None)
                if opp_val is None:
                    setattr(value, "compositefsm_FSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class compositefsm_FSM:

    pass