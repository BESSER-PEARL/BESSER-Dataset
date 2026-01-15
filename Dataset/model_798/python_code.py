from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsmSample_State:

    def __init__(self, name: str, source: set["fsmSample_Transition"] = None, target: set["fsmSample_Transition"] = None, State13: "fsmSample_Transition" = None, State15: "fsmSample_Transition" = None, State: "fsmSample_FSM" = None, fsmSample_State: "fsmSample_FSM" = None, fsmSample_State4: "fsmSample_FSM" = None, fsmSample_State7: "fsmSample_FSM" = None, ownedState: "fsmSample_FSM" = None):
        self.name = name
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State13 = State13
        self.State15 = State15
        self.State = State
        self.fsmSample_State = fsmSample_State
        self.fsmSample_State4 = fsmSample_State4
        self.fsmSample_State7 = fsmSample_State7
        self.ownedState = ownedState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmSample_State7(self):
        return self.__fsmSample_State7

    @fsmSample_State7.setter
    def fsmSample_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State7", None)
        self.__fsmSample_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM6"):
                opp_val = getattr(old_value, "fsmSample_FSM6", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_FSM6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM6"):
                opp_val = getattr(value, "fsmSample_FSM6", None)
                setattr(value, "fsmSample_FSM6", self)

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__State13", None)
        self.__State13 = value
        
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
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__ownedState", None)
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
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__State15", None)
        self.__State15 = value
        
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
    def fsmSample_State4(self):
        return self.__fsmSample_State4

    @fsmSample_State4.setter
    def fsmSample_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State4", None)
        self.__fsmSample_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM3"):
                opp_val = getattr(old_value, "fsmSample_FSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM3"):
                opp_val = getattr(value, "fsmSample_FSM3", None)
                if opp_val is None:
                    setattr(value, "fsmSample_FSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__source", None)
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
        old_value = getattr(self, f"_fsmSample_State__State", None)
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
    def fsmSample_State(self):
        return self.__fsmSample_State

    @fsmSample_State.setter
    def fsmSample_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__fsmSample_State", None)
        self.__fsmSample_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_FSM"):
                opp_val = getattr(old_value, "fsmSample_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_FSM"):
                opp_val = getattr(value, "fsmSample_FSM", None)
                setattr(value, "fsmSample_FSM", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    setattr(item, "Transition11", self)
                    

class fsmSample_Action:

    def __init__(self, name: str, fsmSample_Action: "fsmSample_Transition" = None):
        self.name = name
        self.fsmSample_Action = fsmSample_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsmSample_Action(self):
        return self.__fsmSample_Action

    @fsmSample_Action.setter
    def fsmSample_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Action__fsmSample_Action", None)
        self.__fsmSample_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Transition"):
                opp_val = getattr(old_value, "fsmSample_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Transition"):
                opp_val = getattr(value, "fsmSample_Transition", None)
                setattr(value, "fsmSample_Transition", self)

    def run(self, sync: bool) -> str:
        # TODO: Implement run method
        pass

class fsmSample_Transition:

    def __init__(self, input: str, output: str, Transition: "fsmSample_State" = None, Transition11: "fsmSample_State" = None, outgoingTransition: "fsmSample_State" = None, incomingTransition: "fsmSample_State" = None, fsmSample_Transition: "fsmSample_Action" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition11 = Transition11
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        self.fsmSample_Transition = fsmSample_Transition
        
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
        old_value = getattr(self, f"_fsmSample_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State13"):
                opp_val = getattr(old_value, "State13", None)
                if opp_val == self:
                    setattr(old_value, "State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State13"):
                opp_val = getattr(value, "State13", None)
                setattr(value, "State13", self)

    @property
    def fsmSample_Transition(self):
        return self.__fsmSample_Transition

    @fsmSample_Transition.setter
    def fsmSample_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__fsmSample_Transition", None)
        self.__fsmSample_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_Action"):
                opp_val = getattr(old_value, "fsmSample_Action", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_Action"):
                opp_val = getattr(value, "fsmSample_Action", None)
                setattr(value, "fsmSample_Action", self)

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State15"):
                opp_val = getattr(old_value, "State15", None)
                if opp_val == self:
                    setattr(old_value, "State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State15"):
                opp_val = getattr(value, "State15", None)
                setattr(value, "State15", self)

    @property
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__Transition11", None)
        self.__Transition11 = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_Transition__Transition", None)
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

class fsmSample_FSM:

    def __init__(self, name: str, owningFSM: set["fsmSample_State"] = None, fsmSample_FSM: "fsmSample_State" = None, fsmSample_FSM3: set["fsmSample_State"] = None, fsmSample_FSM6: "fsmSample_State" = None, FSM: "fsmSample_State" = None):
        self.name = name
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.fsmSample_FSM = fsmSample_FSM
        self.fsmSample_FSM3 = fsmSample_FSM3 if fsmSample_FSM3 is not None else set()
        self.fsmSample_FSM6 = fsmSample_FSM6
        self.FSM = FSM
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedState"):
                opp_val = getattr(old_value, "ownedState", None)
                if opp_val == self:
                    setattr(old_value, "ownedState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedState"):
                opp_val = getattr(value, "ownedState", None)
                setattr(value, "ownedState", self)

    @property
    def fsmSample_FSM(self):
        return self.__fsmSample_FSM

    @fsmSample_FSM.setter
    def fsmSample_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM", None)
        self.__fsmSample_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State"):
                opp_val = getattr(old_value, "fsmSample_State", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State"):
                opp_val = getattr(value, "fsmSample_State", None)
                setattr(value, "fsmSample_State", self)

    @property
    def fsmSample_FSM3(self):
        return self.__fsmSample_FSM3

    @fsmSample_FSM3.setter
    def fsmSample_FSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM3", None)
        self.__fsmSample_FSM3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmSample_State4"):
                    opp_val = getattr(item, "fsmSample_State4", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmSample_State4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmSample_State4"):
                    opp_val = getattr(item, "fsmSample_State4", None)
                    
                    setattr(item, "fsmSample_State4", self)
                    

    @property
    def fsmSample_FSM6(self):
        return self.__fsmSample_FSM6

    @fsmSample_FSM6.setter
    def fsmSample_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmSample_FSM__fsmSample_FSM6", None)
        self.__fsmSample_FSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmSample_State7"):
                opp_val = getattr(old_value, "fsmSample_State7", None)
                if opp_val == self:
                    setattr(old_value, "fsmSample_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmSample_State7"):
                opp_val = getattr(value, "fsmSample_State7", None)
                setattr(value, "fsmSample_State7", self)
