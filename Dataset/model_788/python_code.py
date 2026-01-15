from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FSMException:

    pass
class fsm_NoInitialStateException(FSMException):

    pass
class fsm_NoTransition(FSMException):

    pass
class fsm_NonDeterminism(FSMException):

    pass
class fsm_FSMException:

    pass
class fsm_Transition:

    def __init__(self, input: str, output: str, Transition: "fsm_State" = None, Transition15: "fsm_State" = None, outgoingTransition: "fsm_State" = None, incomingTransition: "fsm_State" = None, fsm_Transition: "fsm_FSM" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition15 = Transition15
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        self.fsm_Transition = fsm_Transition
        
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State17"):
                opp_val = getattr(old_value, "State17", None)
                if opp_val == self:
                    setattr(old_value, "State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State17"):
                opp_val = getattr(value, "State17", None)
                setattr(value, "State17", self)

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State19"):
                opp_val = getattr(old_value, "State19", None)
                if opp_val == self:
                    setattr(old_value, "State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State19"):
                opp_val = getattr(value, "State19", None)
                setattr(value, "State19", self)

    @property
    def Transition15(self):
        return self.__Transition15

    @Transition15.setter
    def Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition15", None)
        self.__Transition15 = value
        
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
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM9"):
                opp_val = getattr(old_value, "fsm_FSM9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM9"):
                opp_val = getattr(value, "fsm_FSM9", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self):
        # TODO: Implement fire method
        pass

class fsm_State:

    def __init__(self, name: str, State: "fsm_FSM" = None, fsm_State: "fsm_FSM" = None, fsm_State4: "fsm_FSM" = None, fsm_State7: "fsm_FSM" = None, source: set["fsm_Transition"] = None, target: set["fsm_Transition"] = None, State17: "fsm_Transition" = None, State19: "fsm_Transition" = None, ownedState: "fsm_FSM" = None):
        self.name = name
        self.State = State
        self.fsm_State = fsm_State
        self.fsm_State4 = fsm_State4
        self.fsm_State7 = fsm_State7
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State17 = State17
        self.State19 = State19
        self.ownedState = ownedState
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                setattr(value, "fsm_FSM", self)

    @property
    def fsm_State7(self):
        return self.__fsm_State7

    @fsm_State7.setter
    def fsm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State7", None)
        self.__fsm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM6"):
                opp_val = getattr(old_value, "fsm_FSM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM6"):
                opp_val = getattr(value, "fsm_FSM6", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State", None)
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
        old_value = getattr(self, f"_fsm_State__ownedState", None)
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
    def fsm_State4(self):
        return self.__fsm_State4

    @fsm_State4.setter
    def fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State4", None)
        self.__fsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM3"):
                opp_val = getattr(old_value, "fsm_FSM3", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM3"):
                opp_val = getattr(value, "fsm_FSM3", None)
                setattr(value, "fsm_FSM3", self)

    @property
    def State17(self):
        return self.__State17

    @State17.setter
    def State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State17", None)
        self.__State17 = value
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition15"):
                    opp_val = getattr(item, "Transition15", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition15"):
                    opp_val = getattr(item, "Transition15", None)
                    
                    setattr(item, "Transition15", self)
                    

    @property
    def State19(self):
        return self.__State19

    @State19.setter
    def State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State19", None)
        self.__State19 = value
        
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

    def step(self, c: str):
        # TODO: Implement step method
        pass

class fsm_FSM:

    def __init__(self, owningFSM: set["fsm_State"] = None, fsm_FSM: "fsm_State" = None, fsm_FSM3: "fsm_State" = None, fsm_FSM6: set["fsm_State"] = None, fsm_FSM9: set["fsm_Transition"] = None, fsm_FSM11: "fsm_FSMException" = None, FSM: "fsm_State" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.fsm_FSM = fsm_FSM
        self.fsm_FSM3 = fsm_FSM3
        self.fsm_FSM6 = fsm_FSM6 if fsm_FSM6 is not None else set()
        self.fsm_FSM9 = fsm_FSM9 if fsm_FSM9 is not None else set()
        self.fsm_FSM11 = fsm_FSM11
        self.FSM = FSM
        
    @property
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def fsm_FSM9(self):
        return self.__fsm_FSM9

    @fsm_FSM9.setter
    def fsm_FSM9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM9", None)
        self.__fsm_FSM9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Transition"):
                    opp_val = getattr(item, "fsm_Transition", None)
                    
                    setattr(item, "fsm_Transition", self)
                    

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__owningFSM", None)
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
        old_value = getattr(self, f"_fsm_FSM__FSM", None)
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
    def fsm_FSM6(self):
        return self.__fsm_FSM6

    @fsm_FSM6.setter
    def fsm_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM6", None)
        self.__fsm_FSM6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_State7"):
                    opp_val = getattr(item, "fsm_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_State7"):
                    opp_val = getattr(item, "fsm_State7", None)
                    
                    setattr(item, "fsm_State7", self)
                    

    @property
    def fsm_FSM11(self):
        return self.__fsm_FSM11

    @fsm_FSM11.setter
    def fsm_FSM11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM11", None)
        self.__fsm_FSM11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSMException"):
                opp_val = getattr(old_value, "fsm_FSMException", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSMException", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSMException"):
                opp_val = getattr(value, "fsm_FSMException", None)
                setattr(value, "fsm_FSMException", self)

    @property
    def fsm_FSM3(self):
        return self.__fsm_FSM3

    @fsm_FSM3.setter
    def fsm_FSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM3", None)
        self.__fsm_FSM3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State4"):
                opp_val = getattr(old_value, "fsm_State4", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State4"):
                opp_val = getattr(value, "fsm_State4", None)
                setattr(value, "fsm_State4", self)

    def reset(self):
        # TODO: Implement reset method
        pass

    def run(self):
        # TODO: Implement run method
        pass
