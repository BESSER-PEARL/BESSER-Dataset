from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lts_av_PerJoinPointScope:

    pass
class lts_av_GlobalScope:

    pass
class lts_av_EObject:

    pass
class lts_av_Advice:

    pass
class lts_av_Transition:

    def __init__(self, input: str, output: str, Transition: "lts_av_State" = None, Transition11: "lts_av_State" = None, outgoingTransition: "lts_av_State" = None, incomingTransition: "lts_av_State" = None):
        self.input = input
        self.output = output
        self.Transition = Transition
        self.Transition11 = Transition11
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_Transition__outgoingTransition", None)
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
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_Transition__incomingTransition", None)
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
        old_value = getattr(self, f"_lts_av_Transition__Transition11", None)
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
        old_value = getattr(self, f"_lts_av_Transition__Transition", None)
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

class lts_av_State:

    def __init__(self, name: str, State: "lts_av_LTS" = None, lts_av_State: "lts_av_LTS" = None, lts_av_State4: "lts_av_LTS" = None, lts_av_State7: "lts_av_LTS" = None, ownedState: "lts_av_LTS" = None, source: set["lts_av_Transition"] = None, target: set["lts_av_Transition"] = None, State13: "lts_av_Transition" = None, State15: "lts_av_Transition" = None):
        self.name = name
        self.State = State
        self.lts_av_State = lts_av_State
        self.lts_av_State4 = lts_av_State4
        self.lts_av_State7 = lts_av_State7
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State13 = State13
        self.State15 = State15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__State13", None)
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
    def lts_av_State7(self):
        return self.__lts_av_State7

    @lts_av_State7.setter
    def lts_av_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__lts_av_State7", None)
        self.__lts_av_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_av_LTS6"):
                opp_val = getattr(old_value, "lts_av_LTS6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_av_LTS6"):
                opp_val = getattr(value, "lts_av_LTS6", None)
                if opp_val is None:
                    setattr(value, "lts_av_LTS6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__target", None)
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
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__source", None)
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
    def lts_av_State(self):
        return self.__lts_av_State

    @lts_av_State.setter
    def lts_av_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__lts_av_State", None)
        self.__lts_av_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_av_LTS"):
                opp_val = getattr(old_value, "lts_av_LTS", None)
                if opp_val == self:
                    setattr(old_value, "lts_av_LTS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_av_LTS"):
                opp_val = getattr(value, "lts_av_LTS", None)
                setattr(value, "lts_av_LTS", self)

    @property
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__State15", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningLTS"):
                opp_val = getattr(old_value, "owningLTS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningLTS"):
                opp_val = getattr(value, "owningLTS", None)
                if opp_val is None:
                    setattr(value, "owningLTS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__ownedState", None)
        self.__ownedState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LTS"):
                opp_val = getattr(old_value, "LTS", None)
                if opp_val == self:
                    setattr(old_value, "LTS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LTS"):
                opp_val = getattr(value, "LTS", None)
                setattr(value, "LTS", self)

    @property
    def lts_av_State4(self):
        return self.__lts_av_State4

    @lts_av_State4.setter
    def lts_av_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_State__lts_av_State4", None)
        self.__lts_av_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_av_LTS3"):
                opp_val = getattr(old_value, "lts_av_LTS3", None)
                if opp_val == self:
                    setattr(old_value, "lts_av_LTS3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_av_LTS3"):
                opp_val = getattr(value, "lts_av_LTS3", None)
                setattr(value, "lts_av_LTS3", self)

class lts_av_LTS:

    def __init__(self, name: str, owningLTS: set["lts_av_State"] = None, lts_av_LTS: "lts_av_State" = None, lts_av_LTS3: "lts_av_State" = None, lts_av_LTS6: set["lts_av_State"] = None, LTS: "lts_av_State" = None):
        self.name = name
        self.owningLTS = owningLTS if owningLTS is not None else set()
        self.lts_av_LTS = lts_av_LTS
        self.lts_av_LTS3 = lts_av_LTS3
        self.lts_av_LTS6 = lts_av_LTS6 if lts_av_LTS6 is not None else set()
        self.LTS = LTS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LTS(self):
        return self.__LTS

    @LTS.setter
    def LTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_LTS__LTS", None)
        self.__LTS = value
        
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
    def owningLTS(self):
        return self.__owningLTS

    @owningLTS.setter
    def owningLTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_LTS__owningLTS", None)
        self.__owningLTS = value if value is not None else set()
        
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
    def lts_av_LTS6(self):
        return self.__lts_av_LTS6

    @lts_av_LTS6.setter
    def lts_av_LTS6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_LTS__lts_av_LTS6", None)
        self.__lts_av_LTS6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lts_av_State7"):
                    opp_val = getattr(item, "lts_av_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "lts_av_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lts_av_State7"):
                    opp_val = getattr(item, "lts_av_State7", None)
                    
                    setattr(item, "lts_av_State7", self)
                    

    @property
    def lts_av_LTS3(self):
        return self.__lts_av_LTS3

    @lts_av_LTS3.setter
    def lts_av_LTS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_LTS__lts_av_LTS3", None)
        self.__lts_av_LTS3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_av_State4"):
                opp_val = getattr(old_value, "lts_av_State4", None)
                if opp_val == self:
                    setattr(old_value, "lts_av_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_av_State4"):
                opp_val = getattr(value, "lts_av_State4", None)
                setattr(value, "lts_av_State4", self)

    @property
    def lts_av_LTS(self):
        return self.__lts_av_LTS

    @lts_av_LTS.setter
    def lts_av_LTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_av_LTS__lts_av_LTS", None)
        self.__lts_av_LTS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_av_State"):
                opp_val = getattr(old_value, "lts_av_State", None)
                if opp_val == self:
                    setattr(old_value, "lts_av_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_av_State"):
                opp_val = getattr(value, "lts_av_State", None)
                setattr(value, "lts_av_State", self)
