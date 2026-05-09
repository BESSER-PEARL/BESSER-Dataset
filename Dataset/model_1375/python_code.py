from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Pseudostate:

    pass
class finitestatemachines_Join2(Pseudostate):

    pass
class finitestatemachines_Fork(Pseudostate):

    pass
class Transition2:

    pass
class finitestatemachines_TimedTransition(Transition2):

    def __init__(self, duration: int):
        self.duration = duration
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration


class NamedElement:

    pass
class finitestatemachines_State2(NamedElement):

    def __init__(self, initialTime2: int, finalTime: int, State28: "finitestatemachines_Transition2" = None, State210: "finitestatemachines_Transition2" = None, State2: "finitestatemachines_StateMachine" = None, source: set["finitestatemachines_Transition2"] = None, target: set["finitestatemachines_Transition2"] = None, states2: "finitestatemachines_StateMachine" = None):
        self.initialTime2 = initialTime2
        self.finalTime = finalTime
        self.State28 = State28
        self.State210 = State210
        self.State2 = State2
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.states2 = states2
        
        pass
    @property
    def initialTime2(self):
        return self.__initialTime2

    @initialTime2.setter
    def initialTime2(self, initialTime2: int):
        self.__initialTime2 = initialTime2


    @property
    def finalTime(self):
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime


    @property
    def State2(self):
        return self.__State2

    @State2.setter
    def State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__State2", None)
        self.__State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine2"):
                opp_val = getattr(old_value, "stateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine2"):
                opp_val = getattr(value, "stateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State28(self):
        return self.__State28

    @State28.setter
    def State28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__State28", None)
        self.__State28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition23"):
                    opp_val = getattr(item, "Transition23", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition23"):
                    opp_val = getattr(item, "Transition23", None)
                    
                    setattr(item, "Transition23", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition25"):
                    opp_val = getattr(item, "Transition25", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition25"):
                    opp_val = getattr(item, "Transition25", None)
                    
                    setattr(item, "Transition25", self)
                    

    @property
    def State210(self):
        return self.__State210

    @State210.setter
    def State210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__State210", None)
        self.__State210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def states2(self):
        return self.__states2

    @states2.setter
    def states2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__states2", None)
        self.__states2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

class finitestatemachines_Transition2(NamedElement):

    def __init__(self, initialTime: int, finalTime2: int, incoming: "finitestatemachines_State2" = None, outgoing: "finitestatemachines_State2" = None, finitestatemachines_Transition2: "finitestatemachines_Trigger2" = None, transitions2: "finitestatemachines_StateMachine" = None, Transition2: "finitestatemachines_StateMachine" = None, Transition23: "finitestatemachines_State2" = None, Transition25: "finitestatemachines_State2" = None):
        self.initialTime = initialTime
        self.finalTime2 = finalTime2
        self.incoming = incoming
        self.outgoing = outgoing
        self.finitestatemachines_Transition2 = finitestatemachines_Transition2
        self.transitions2 = transitions2
        self.Transition2 = Transition2
        self.Transition23 = Transition23
        self.Transition25 = Transition25
        
        pass
    @property
    def initialTime(self):
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime


    @property
    def finalTime2(self):
        return self.__finalTime2

    @finalTime2.setter
    def finalTime2(self, finalTime2: int):
        self.__finalTime2 = finalTime2


    @property
    def Transition25(self):
        return self.__Transition25

    @Transition25.setter
    def Transition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__Transition25", None)
        self.__Transition25 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State210"):
                opp_val = getattr(old_value, "State210", None)
                if opp_val == self:
                    setattr(old_value, "State210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State210"):
                opp_val = getattr(value, "State210", None)
                setattr(value, "State210", self)

    @property
    def Transition23(self):
        return self.__Transition23

    @Transition23.setter
    def Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__Transition23", None)
        self.__Transition23 = value
        
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
    def transitions2(self):
        return self.__transitions2

    @transitions2.setter
    def transitions2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__transitions2", None)
        self.__transitions2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine13"):
                opp_val = getattr(old_value, "StateMachine13", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine13"):
                opp_val = getattr(value, "StateMachine13", None)
                setattr(value, "StateMachine13", self)

    @property
    def finitestatemachines_Transition2(self):
        return self.__finitestatemachines_Transition2

    @finitestatemachines_Transition2.setter
    def finitestatemachines_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__finitestatemachines_Transition2", None)
        self.__finitestatemachines_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finitestatemachines_Trigger2"):
                opp_val = getattr(old_value, "finitestatemachines_Trigger2", None)
                if opp_val == self:
                    setattr(old_value, "finitestatemachines_Trigger2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finitestatemachines_Trigger2"):
                opp_val = getattr(value, "finitestatemachines_Trigger2", None)
                setattr(value, "finitestatemachines_Trigger2", self)

    @property
    def Transition2(self):
        return self.__Transition2

    @Transition2.setter
    def Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__Transition2", None)
        self.__Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine"):
                opp_val = getattr(old_value, "stateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine"):
                opp_val = getattr(value, "stateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State28"):
                opp_val = getattr(old_value, "State28", None)
                if opp_val == self:
                    setattr(old_value, "State28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State28"):
                opp_val = getattr(value, "State28", None)
                setattr(value, "State28", self)

class finitestatemachines_StateMachine(NamedElement):

    pass
class finitestatemachines_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class finitestatemachines_Trigger2:

    def __init__(self, expression: str, finitestatemachines_Trigger2: "finitestatemachines_Transition2" = None):
        self.expression = expression
        self.finitestatemachines_Trigger2 = finitestatemachines_Trigger2
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def finitestatemachines_Trigger2(self):
        return self.__finitestatemachines_Trigger2

    @finitestatemachines_Trigger2.setter
    def finitestatemachines_Trigger2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Trigger2__finitestatemachines_Trigger2", None)
        self.__finitestatemachines_Trigger2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finitestatemachines_Transition2"):
                opp_val = getattr(old_value, "finitestatemachines_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "finitestatemachines_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finitestatemachines_Transition2"):
                opp_val = getattr(value, "finitestatemachines_Transition2", None)
                setattr(value, "finitestatemachines_Transition2", self)

class State2:

    pass
class finitestatemachines_Pseudostate(State2):

    pass
class finitestatemachines_InitialState(State2):

    pass
class finitestatemachines_FinalState(State2):

    pass