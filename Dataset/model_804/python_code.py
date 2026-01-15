from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class kfsm_Transition:

    def __init__(self, input: str, output: str, outgoingTransition: "kfsm_State" = None, incomingTransition: "kfsm_State" = None, Transition: "kfsm_State" = None, Transition8: "kfsm_State" = None):
        self.input = input
        self.output = output
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        self.Transition = Transition
        self.Transition8 = Transition8
        
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_Transition__outgoingTransition", None)
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
        old_value = getattr(self, f"_kfsm_Transition__Transition", None)
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
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_Transition__incomingTransition", None)
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
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_Transition__Transition8", None)
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

class kfsm_State:

    def __init__(self, name: str, kfsm_State10: "kfsm_Action" = None, State12: "kfsm_Transition" = None, State14: "kfsm_Transition" = None, State: "kfsm_FSM" = None, kfsm_State: "kfsm_FSM" = None, kfsm_State4: "kfsm_FSM" = None, ownedState: "kfsm_FSM" = None, source: set["kfsm_Transition"] = None, target: set["kfsm_Transition"] = None):
        self.name = name
        self.kfsm_State10 = kfsm_State10
        self.State12 = State12
        self.State14 = State14
        self.State = State
        self.kfsm_State = kfsm_State
        self.kfsm_State4 = kfsm_State4
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__source", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__State", None)
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
    def kfsm_State10(self):
        return self.__kfsm_State10

    @kfsm_State10.setter
    def kfsm_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__kfsm_State10", None)
        self.__kfsm_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kfsm_Action"):
                opp_val = getattr(old_value, "kfsm_Action", None)
                if opp_val == self:
                    setattr(old_value, "kfsm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kfsm_Action"):
                opp_val = getattr(value, "kfsm_Action", None)
                setattr(value, "kfsm_Action", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__target", None)
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
    def State12(self):
        return self.__State12

    @State12.setter
    def State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__State12", None)
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
        old_value = getattr(self, f"_kfsm_State__State14", None)
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
    def kfsm_State(self):
        return self.__kfsm_State

    @kfsm_State.setter
    def kfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__kfsm_State", None)
        self.__kfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kfsm_FSM"):
                opp_val = getattr(old_value, "kfsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "kfsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kfsm_FSM"):
                opp_val = getattr(value, "kfsm_FSM", None)
                setattr(value, "kfsm_FSM", self)

    @property
    def kfsm_State4(self):
        return self.__kfsm_State4

    @kfsm_State4.setter
    def kfsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__kfsm_State4", None)
        self.__kfsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kfsm_FSM3"):
                opp_val = getattr(old_value, "kfsm_FSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kfsm_FSM3"):
                opp_val = getattr(value, "kfsm_FSM3", None)
                if opp_val is None:
                    setattr(value, "kfsm_FSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_State__ownedState", None)
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

class kfsm_FSM:

    pass
class kfsm_Action:

    def __init__(self, id: str, kfsm_Action: "kfsm_State" = None):
        self.id = id
        self.kfsm_Action = kfsm_Action
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kfsm_Action(self):
        return self.__kfsm_Action

    @kfsm_Action.setter
    def kfsm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kfsm_Action__kfsm_Action", None)
        self.__kfsm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kfsm_State10"):
                opp_val = getattr(old_value, "kfsm_State10", None)
                if opp_val == self:
                    setattr(old_value, "kfsm_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kfsm_State10"):
                opp_val = getattr(value, "kfsm_State10", None)
                setattr(value, "kfsm_State10", self)
