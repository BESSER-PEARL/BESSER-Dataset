from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_RuntimeConcept2:

    def __init__(self, bar: str, fsm_RuntimeConcept2: set["fsm_RuntimeConcept1"] = None):
        self.bar = bar
        self.fsm_RuntimeConcept2 = fsm_RuntimeConcept2 if fsm_RuntimeConcept2 is not None else set()
        
        pass
    @property
    def bar(self):
        return self.__bar

    @bar.setter
    def bar(self, bar: str):
        self.__bar = bar


    @property
    def fsm_RuntimeConcept2(self):
        return self.__fsm_RuntimeConcept2

    @fsm_RuntimeConcept2.setter
    def fsm_RuntimeConcept2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept2__fsm_RuntimeConcept2", None)
        self.__fsm_RuntimeConcept2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_RuntimeConcept1"):
                    opp_val = getattr(item, "fsm_RuntimeConcept1", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_RuntimeConcept1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_RuntimeConcept1"):
                    opp_val = getattr(item, "fsm_RuntimeConcept1", None)
                    
                    setattr(item, "fsm_RuntimeConcept1", self)
                    

class fsm_Transition:

    def __init__(self, input: str, output: str, Transition: "fsm_State" = None, Transition9: "fsm_State" = None, outgoingTransition: "fsm_State" = None, incomingTransition: "fsm_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition9 = Transition9
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output


    @property
    def Transition9(self):
        return self.__Transition9

    @Transition9.setter
    def Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition9", None)
        self.__Transition9 = value
        
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

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
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
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

class fsm_RuntimeConcept1:

    def __init__(self, foo: int, fsm_RuntimeConcept1: "fsm_RuntimeConcept2" = None, fsm_RuntimeConcept115: "fsm_State" = None):
        self.foo = foo
        self.fsm_RuntimeConcept1 = fsm_RuntimeConcept1
        self.fsm_RuntimeConcept115 = fsm_RuntimeConcept115
        
        pass
    @property
    def foo(self):
        return self.__foo

    @foo.setter
    def foo(self, foo: int):
        self.__foo = foo


    @property
    def fsm_RuntimeConcept1(self):
        return self.__fsm_RuntimeConcept1

    @fsm_RuntimeConcept1.setter
    def fsm_RuntimeConcept1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept1__fsm_RuntimeConcept1", None)
        self.__fsm_RuntimeConcept1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_RuntimeConcept2"):
                opp_val = getattr(old_value, "fsm_RuntimeConcept2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_RuntimeConcept2"):
                opp_val = getattr(value, "fsm_RuntimeConcept2", None)
                if opp_val is None:
                    setattr(value, "fsm_RuntimeConcept2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_RuntimeConcept115(self):
        return self.__fsm_RuntimeConcept115

    @fsm_RuntimeConcept115.setter
    def fsm_RuntimeConcept115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept1__fsm_RuntimeConcept115", None)
        self.__fsm_RuntimeConcept115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State16"):
                opp_val = getattr(old_value, "fsm_State16", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State16"):
                opp_val = getattr(value, "fsm_State16", None)
                setattr(value, "fsm_State16", self)

class fsm_State:

    def __init__(self, name: str, State: "fsm_FSM" = None, fsm_State: "fsm_FSM" = None, fsm_State4: "fsm_FSM" = None, ownedState: "fsm_FSM" = None, source: set["fsm_Transition"] = None, target: set["fsm_Transition"] = None, State11: "fsm_Transition" = None, State13: "fsm_Transition" = None, fsm_State16: "fsm_RuntimeConcept1" = None):
        self.name = name
        self.State = State
        self.fsm_State = fsm_State
        self.fsm_State4 = fsm_State4
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State11 = State11
        self.State13 = State13
        self.fsm_State16 = fsm_State16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State11", None)
        self.__State11 = value
        
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
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State13", None)
        self.__State13 = value
        
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
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    setattr(item, "Transition9", self)
                    

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
    def fsm_State16(self):
        return self.__fsm_State16

    @fsm_State16.setter
    def fsm_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State16", None)
        self.__fsm_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_RuntimeConcept115"):
                opp_val = getattr(old_value, "fsm_RuntimeConcept115", None)
                if opp_val == self:
                    setattr(old_value, "fsm_RuntimeConcept115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_RuntimeConcept115"):
                opp_val = getattr(value, "fsm_RuntimeConcept115", None)
                setattr(value, "fsm_RuntimeConcept115", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM3"):
                opp_val = getattr(value, "fsm_FSM3", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class fsm_FSM:

    pass