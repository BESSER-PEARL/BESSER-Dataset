from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FSMException:

    pass
class fsmkerm_NoInitialStateException(FSMException):

    pass
class fsmkerm_NoTransition(FSMException):

    pass
class fsmkerm_NonDeterminism(FSMException):

    pass
class fsmkerm_FSMException:

    pass
class fsmkerm_Transition:

    def __init__(self, input: str, output: str, fsmkerm_Transition: "fsmkerm_FSM" = None, Transition: "fsmkerm_State" = None, Transition15: "fsmkerm_State" = None, outgoingTransition: "fsmkerm_State" = None, incomingTransition: "fsmkerm_State" = None):
        self.input = input
        self.output = output
        self.fsmkerm_Transition = fsmkerm_Transition
        self.Transition = Transition
        self.Transition15 = Transition15
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
        old_value = getattr(self, f"_fsmkerm_Transition__Transition", None)
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
    def fsmkerm_Transition(self):
        return self.__fsmkerm_Transition

    @fsmkerm_Transition.setter
    def fsmkerm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_Transition__fsmkerm_Transition", None)
        self.__fsmkerm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_FSM9"):
                opp_val = getattr(old_value, "fsmkerm_FSM9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_FSM9"):
                opp_val = getattr(value, "fsmkerm_FSM9", None)
                if opp_val is None:
                    setattr(value, "fsmkerm_FSM9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_Transition__outgoingTransition", None)
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
        old_value = getattr(self, f"_fsmkerm_Transition__incomingTransition", None)
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
        old_value = getattr(self, f"_fsmkerm_Transition__Transition15", None)
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

    def fire(self):
        # TODO: Implement fire method
        pass

class fsmkerm_State:

    def __init__(self, name: str, State: "fsmkerm_FSM" = None, fsmkerm_State: "fsmkerm_FSM" = None, fsmkerm_State4: "fsmkerm_FSM" = None, fsmkerm_State7: "fsmkerm_FSM" = None, source: set["fsmkerm_Transition"] = None, target: set["fsmkerm_Transition"] = None, State17: "fsmkerm_Transition" = None, State19: "fsmkerm_Transition" = None, ownedState: "fsmkerm_FSM" = None):
        self.name = name
        self.State = State
        self.fsmkerm_State = fsmkerm_State
        self.fsmkerm_State4 = fsmkerm_State4
        self.fsmkerm_State7 = fsmkerm_State7
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
    def State17(self):
        return self.__State17

    @State17.setter
    def State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__State17", None)
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__source", None)
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__target", None)
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
        old_value = getattr(self, f"_fsmkerm_State__State19", None)
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

    @property
    def fsmkerm_State4(self):
        return self.__fsmkerm_State4

    @fsmkerm_State4.setter
    def fsmkerm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__fsmkerm_State4", None)
        self.__fsmkerm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_FSM3"):
                opp_val = getattr(old_value, "fsmkerm_FSM3", None)
                if opp_val == self:
                    setattr(old_value, "fsmkerm_FSM3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_FSM3"):
                opp_val = getattr(value, "fsmkerm_FSM3", None)
                setattr(value, "fsmkerm_FSM3", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__State", None)
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
    def fsmkerm_State7(self):
        return self.__fsmkerm_State7

    @fsmkerm_State7.setter
    def fsmkerm_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__fsmkerm_State7", None)
        self.__fsmkerm_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_FSM6"):
                opp_val = getattr(old_value, "fsmkerm_FSM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_FSM6"):
                opp_val = getattr(value, "fsmkerm_FSM6", None)
                if opp_val is None:
                    setattr(value, "fsmkerm_FSM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__ownedState", None)
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
    def fsmkerm_State(self):
        return self.__fsmkerm_State

    @fsmkerm_State.setter
    def fsmkerm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_State__fsmkerm_State", None)
        self.__fsmkerm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_FSM"):
                opp_val = getattr(old_value, "fsmkerm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsmkerm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_FSM"):
                opp_val = getattr(value, "fsmkerm_FSM", None)
                setattr(value, "fsmkerm_FSM", self)

    def step(self, c: str):
        # TODO: Implement step method
        pass

class fsmkerm_FSM:

    def __init__(self, owningFSM: set["fsmkerm_State"] = None, fsmkerm_FSM: "fsmkerm_State" = None, fsmkerm_FSM3: "fsmkerm_State" = None, fsmkerm_FSM6: set["fsmkerm_State"] = None, fsmkerm_FSM9: set["fsmkerm_Transition"] = None, fsmkerm_FSM11: "fsmkerm_FSMException" = None, FSM: "fsmkerm_State" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.fsmkerm_FSM = fsmkerm_FSM
        self.fsmkerm_FSM3 = fsmkerm_FSM3
        self.fsmkerm_FSM6 = fsmkerm_FSM6 if fsmkerm_FSM6 is not None else set()
        self.fsmkerm_FSM9 = fsmkerm_FSM9 if fsmkerm_FSM9 is not None else set()
        self.fsmkerm_FSM11 = fsmkerm_FSM11
        self.FSM = FSM
        
    @property
    def fsmkerm_FSM(self):
        return self.__fsmkerm_FSM

    @fsmkerm_FSM.setter
    def fsmkerm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__fsmkerm_FSM", None)
        self.__fsmkerm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_State"):
                opp_val = getattr(old_value, "fsmkerm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsmkerm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_State"):
                opp_val = getattr(value, "fsmkerm_State", None)
                setattr(value, "fsmkerm_State", self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__owningFSM", None)
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
        old_value = getattr(self, f"_fsmkerm_FSM__FSM", None)
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
    def fsmkerm_FSM11(self):
        return self.__fsmkerm_FSM11

    @fsmkerm_FSM11.setter
    def fsmkerm_FSM11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__fsmkerm_FSM11", None)
        self.__fsmkerm_FSM11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_FSMException"):
                opp_val = getattr(old_value, "fsmkerm_FSMException", None)
                if opp_val == self:
                    setattr(old_value, "fsmkerm_FSMException", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_FSMException"):
                opp_val = getattr(value, "fsmkerm_FSMException", None)
                setattr(value, "fsmkerm_FSMException", self)

    @property
    def fsmkerm_FSM6(self):
        return self.__fsmkerm_FSM6

    @fsmkerm_FSM6.setter
    def fsmkerm_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__fsmkerm_FSM6", None)
        self.__fsmkerm_FSM6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmkerm_State7"):
                    opp_val = getattr(item, "fsmkerm_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmkerm_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmkerm_State7"):
                    opp_val = getattr(item, "fsmkerm_State7", None)
                    
                    setattr(item, "fsmkerm_State7", self)
                    

    @property
    def fsmkerm_FSM3(self):
        return self.__fsmkerm_FSM3

    @fsmkerm_FSM3.setter
    def fsmkerm_FSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__fsmkerm_FSM3", None)
        self.__fsmkerm_FSM3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmkerm_State4"):
                opp_val = getattr(old_value, "fsmkerm_State4", None)
                if opp_val == self:
                    setattr(old_value, "fsmkerm_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmkerm_State4"):
                opp_val = getattr(value, "fsmkerm_State4", None)
                setattr(value, "fsmkerm_State4", self)

    @property
    def fsmkerm_FSM9(self):
        return self.__fsmkerm_FSM9

    @fsmkerm_FSM9.setter
    def fsmkerm_FSM9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmkerm_FSM__fsmkerm_FSM9", None)
        self.__fsmkerm_FSM9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsmkerm_Transition"):
                    opp_val = getattr(item, "fsmkerm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fsmkerm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsmkerm_Transition"):
                    opp_val = getattr(item, "fsmkerm_Transition", None)
                    
                    setattr(item, "fsmkerm_Transition", self)
                    

    def run(self):
        # TODO: Implement run method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass
