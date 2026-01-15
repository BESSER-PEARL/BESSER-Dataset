from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Transition:

    pass
class StateMachinesProv_ProtocolTransition(Transition):

    pass
class StateMachinesProv_ProtocolConformance:

    pass
class StateMachine:

    pass
class StateMachinesProv_ProtocolStateMachine(StateMachine):

    pass
class StateMachinesProv_TimeEvent:

    pass
class State:

    pass
class StateMachinesProv_FinalState(State):

    pass
class Vertex:

    pass
class StateMachinesProv_ConnectionPointReference(Vertex):

    pass
class StateMachinesProv_Transition:

    pass
class StateMachinesProv_Vertex(ABC):

    pass
class StateMachinesProv_State(Vertex):

    def __init__(self, isComposite: bool, isOrthogonal: bool, isSimple: bool, isSubmachineState: bool, StateMachinesProv_State: "StateMachinesProv_StateMachine" = None, StateMachinesProv_State17: "StateMachinesProv_Region" = None, StateMachinesProv_State54: set["StateMachinesProv_ConnectionPointReference"] = None, StateMachinesProv_State57: set["StateMachinesProv_Pseudostate"] = None, StateMachinesProv_State44: "StateMachinesProv_Pseudostate" = None, StateMachinesProv_State52: "StateMachinesProv_ConnectionPointReference" = None, StateMachinesProv_State60: "StateMachinesProv_StateMachine" = None, StateMachinesProv_State63: set["StateMachinesProv_Region"] = None, StateMachinesProv_State67: "StateMachinesProv_State" = None, StateMachinesProv_State65: "StateMachinesProv_State" = None):
        self.isComposite = isComposite
        self.isOrthogonal = isOrthogonal
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.StateMachinesProv_State = StateMachinesProv_State
        self.StateMachinesProv_State17 = StateMachinesProv_State17
        self.StateMachinesProv_State54 = StateMachinesProv_State54 if StateMachinesProv_State54 is not None else set()
        self.StateMachinesProv_State57 = StateMachinesProv_State57 if StateMachinesProv_State57 is not None else set()
        self.StateMachinesProv_State44 = StateMachinesProv_State44
        self.StateMachinesProv_State52 = StateMachinesProv_State52
        self.StateMachinesProv_State60 = StateMachinesProv_State60
        self.StateMachinesProv_State63 = StateMachinesProv_State63 if StateMachinesProv_State63 is not None else set()
        self.StateMachinesProv_State67 = StateMachinesProv_State67
        self.StateMachinesProv_State65 = StateMachinesProv_State65
        
    @property
    def isOrthogonal(self) -> bool:
        return self.__isOrthogonal

    @isOrthogonal.setter
    def isOrthogonal(self, isOrthogonal: bool):
        self.__isOrthogonal = isOrthogonal

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isSubmachineState(self) -> bool:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: bool):
        self.__isSubmachineState = isSubmachineState

    @property
    def isSimple(self) -> bool:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple

    @property
    def StateMachinesProv_State52(self):
        return self.__StateMachinesProv_State52

    @StateMachinesProv_State52.setter
    def StateMachinesProv_State52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State52", None)
        self.__StateMachinesProv_State52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_ConnectionPointReference51"):
                opp_val = getattr(old_value, "StateMachinesProv_ConnectionPointReference51", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_ConnectionPointReference51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_ConnectionPointReference51"):
                opp_val = getattr(value, "StateMachinesProv_ConnectionPointReference51", None)
                setattr(value, "StateMachinesProv_ConnectionPointReference51", self)

    @property
    def StateMachinesProv_State(self):
        return self.__StateMachinesProv_State

    @StateMachinesProv_State.setter
    def StateMachinesProv_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State", None)
        self.__StateMachinesProv_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_StateMachine4"):
                opp_val = getattr(old_value, "StateMachinesProv_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_StateMachine4"):
                opp_val = getattr(value, "StateMachinesProv_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "StateMachinesProv_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachinesProv_State54(self):
        return self.__StateMachinesProv_State54

    @StateMachinesProv_State54.setter
    def StateMachinesProv_State54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State54", None)
        self.__StateMachinesProv_State54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachinesProv_ConnectionPointReference55"):
                    opp_val = getattr(item, "StateMachinesProv_ConnectionPointReference55", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachinesProv_ConnectionPointReference55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachinesProv_ConnectionPointReference55"):
                    opp_val = getattr(item, "StateMachinesProv_ConnectionPointReference55", None)
                    
                    setattr(item, "StateMachinesProv_ConnectionPointReference55", self)
                    

    @property
    def StateMachinesProv_State17(self):
        return self.__StateMachinesProv_State17

    @StateMachinesProv_State17.setter
    def StateMachinesProv_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State17", None)
        self.__StateMachinesProv_State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_Region16"):
                opp_val = getattr(old_value, "StateMachinesProv_Region16", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_Region16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_Region16"):
                opp_val = getattr(value, "StateMachinesProv_Region16", None)
                setattr(value, "StateMachinesProv_Region16", self)

    @property
    def StateMachinesProv_State60(self):
        return self.__StateMachinesProv_State60

    @StateMachinesProv_State60.setter
    def StateMachinesProv_State60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State60", None)
        self.__StateMachinesProv_State60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_StateMachine61"):
                opp_val = getattr(old_value, "StateMachinesProv_StateMachine61", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_StateMachine61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_StateMachine61"):
                opp_val = getattr(value, "StateMachinesProv_StateMachine61", None)
                setattr(value, "StateMachinesProv_StateMachine61", self)

    @property
    def StateMachinesProv_State44(self):
        return self.__StateMachinesProv_State44

    @StateMachinesProv_State44.setter
    def StateMachinesProv_State44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State44", None)
        self.__StateMachinesProv_State44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_Pseudostate43"):
                opp_val = getattr(old_value, "StateMachinesProv_Pseudostate43", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_Pseudostate43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_Pseudostate43"):
                opp_val = getattr(value, "StateMachinesProv_Pseudostate43", None)
                setattr(value, "StateMachinesProv_Pseudostate43", self)

    @property
    def StateMachinesProv_State65(self):
        return self.__StateMachinesProv_State65

    @StateMachinesProv_State65.setter
    def StateMachinesProv_State65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State65", None)
        self.__StateMachinesProv_State65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_State67"):
                opp_val = getattr(old_value, "StateMachinesProv_State67", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_State67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_State67"):
                opp_val = getattr(value, "StateMachinesProv_State67", None)
                setattr(value, "StateMachinesProv_State67", self)

    @property
    def StateMachinesProv_State67(self):
        return self.__StateMachinesProv_State67

    @StateMachinesProv_State67.setter
    def StateMachinesProv_State67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State67", None)
        self.__StateMachinesProv_State67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesProv_State65"):
                opp_val = getattr(old_value, "StateMachinesProv_State65", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesProv_State65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesProv_State65"):
                opp_val = getattr(value, "StateMachinesProv_State65", None)
                setattr(value, "StateMachinesProv_State65", self)

    @property
    def StateMachinesProv_State57(self):
        return self.__StateMachinesProv_State57

    @StateMachinesProv_State57.setter
    def StateMachinesProv_State57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State57", None)
        self.__StateMachinesProv_State57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachinesProv_Pseudostate58"):
                    opp_val = getattr(item, "StateMachinesProv_Pseudostate58", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachinesProv_Pseudostate58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachinesProv_Pseudostate58"):
                    opp_val = getattr(item, "StateMachinesProv_Pseudostate58", None)
                    
                    setattr(item, "StateMachinesProv_Pseudostate58", self)
                    

    @property
    def StateMachinesProv_State63(self):
        return self.__StateMachinesProv_State63

    @StateMachinesProv_State63.setter
    def StateMachinesProv_State63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesProv_State__StateMachinesProv_State63", None)
        self.__StateMachinesProv_State63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachinesProv_Region64"):
                    opp_val = getattr(item, "StateMachinesProv_Region64", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachinesProv_Region64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachinesProv_Region64"):
                    opp_val = getattr(item, "StateMachinesProv_Region64", None)
                    
                    setattr(item, "StateMachinesProv_Region64", self)
                    

class StateMachinesProv_Pseudostate(Vertex):

    pass
class StateMachinesProv_Region:

    pass
class StateMachinesProv_StateMachine:

    pass