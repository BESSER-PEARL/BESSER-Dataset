from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StateVertex:

    pass
class StateMachineUnnamed_FinalState(StateVertex):

    pass
class StateMachineUnnamed_SimpleState(StateVertex):

    pass
class StateMachineUnnamed_InitialState(StateVertex):

    pass
class StateMachineUnnamed_Event:

    pass
class StateMachineUnnamed_StateMachine:

    pass
class StateMachineUnnamed_Transition:

    def __init__(self, name: str, StateMachineUnnamed_Transition: "StateMachineUnnamed_StateMachine" = None, Transition: "StateMachineUnnamed_StateVertex" = None, Transition5: "StateMachineUnnamed_StateVertex" = None, outgoing: "StateMachineUnnamed_StateVertex" = None, incoming: "StateMachineUnnamed_StateVertex" = None, StateMachineUnnamed_Transition13: "StateMachineUnnamed_Event" = None):
        self.name = name
        self.StateMachineUnnamed_Transition = StateMachineUnnamed_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.outgoing = outgoing
        self.incoming = incoming
        self.StateMachineUnnamed_Transition13 = StateMachineUnnamed_Transition13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateVertex11"):
                opp_val = getattr(old_value, "StateVertex11", None)
                if opp_val == self:
                    setattr(old_value, "StateVertex11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateVertex11"):
                opp_val = getattr(value, "StateVertex11", None)
                setattr(value, "StateVertex11", self)

    @property
    def StateMachineUnnamed_Transition(self):
        return self.__StateMachineUnnamed_Transition

    @StateMachineUnnamed_Transition.setter
    def StateMachineUnnamed_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__StateMachineUnnamed_Transition", None)
        self.__StateMachineUnnamed_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineUnnamed_StateMachine2"):
                opp_val = getattr(old_value, "StateMachineUnnamed_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineUnnamed_StateMachine2"):
                opp_val = getattr(value, "StateMachineUnnamed_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "StateMachineUnnamed_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachineUnnamed_Transition13(self):
        return self.__StateMachineUnnamed_Transition13

    @StateMachineUnnamed_Transition13.setter
    def StateMachineUnnamed_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__StateMachineUnnamed_Transition13", None)
        self.__StateMachineUnnamed_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineUnnamed_Event"):
                opp_val = getattr(old_value, "StateMachineUnnamed_Event", None)
                if opp_val == self:
                    setattr(old_value, "StateMachineUnnamed_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineUnnamed_Event"):
                opp_val = getattr(value, "StateMachineUnnamed_Event", None)
                setattr(value, "StateMachineUnnamed_Event", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateVertex"):
                opp_val = getattr(old_value, "StateVertex", None)
                if opp_val == self:
                    setattr(old_value, "StateVertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateVertex"):
                opp_val = getattr(value, "StateVertex", None)
                setattr(value, "StateVertex", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__Transition", None)
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
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_Transition__Transition5", None)
        self.__Transition5 = value
        
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

class StateMachineUnnamed_StateVertex(ABC):

    def __init__(self, name: str, StateMachineUnnamed_StateVertex: "StateMachineUnnamed_StateMachine" = None, source: set["StateMachineUnnamed_Transition"] = None, target: set["StateMachineUnnamed_Transition"] = None, StateMachineUnnamed_StateVertex8: "StateMachineUnnamed_StateVertex" = None, StateMachineUnnamed_StateVertex6: set["StateMachineUnnamed_StateVertex"] = None, StateVertex: "StateMachineUnnamed_Transition" = None, StateVertex11: "StateMachineUnnamed_Transition" = None):
        self.name = name
        self.StateMachineUnnamed_StateVertex = StateMachineUnnamed_StateVertex
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.StateMachineUnnamed_StateVertex8 = StateMachineUnnamed_StateVertex8
        self.StateMachineUnnamed_StateVertex6 = StateMachineUnnamed_StateVertex6 if StateMachineUnnamed_StateVertex6 is not None else set()
        self.StateVertex = StateVertex
        self.StateVertex11 = StateVertex11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateVertex11(self):
        return self.__StateVertex11

    @StateVertex11.setter
    def StateVertex11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__StateVertex11", None)
        self.__StateVertex11 = value
        
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
    def StateMachineUnnamed_StateVertex6(self):
        return self.__StateMachineUnnamed_StateVertex6

    @StateMachineUnnamed_StateVertex6.setter
    def StateMachineUnnamed_StateVertex6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__StateMachineUnnamed_StateVertex6", None)
        self.__StateMachineUnnamed_StateVertex6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachineUnnamed_StateVertex8"):
                    opp_val = getattr(item, "StateMachineUnnamed_StateVertex8", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachineUnnamed_StateVertex8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachineUnnamed_StateVertex8"):
                    opp_val = getattr(item, "StateMachineUnnamed_StateVertex8", None)
                    
                    setattr(item, "StateMachineUnnamed_StateVertex8", self)
                    

    @property
    def StateVertex(self):
        return self.__StateVertex

    @StateVertex.setter
    def StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__StateVertex", None)
        self.__StateVertex = value
        
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
    def StateMachineUnnamed_StateVertex8(self):
        return self.__StateMachineUnnamed_StateVertex8

    @StateMachineUnnamed_StateVertex8.setter
    def StateMachineUnnamed_StateVertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__StateMachineUnnamed_StateVertex8", None)
        self.__StateMachineUnnamed_StateVertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineUnnamed_StateVertex6"):
                opp_val = getattr(old_value, "StateMachineUnnamed_StateVertex6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineUnnamed_StateVertex6"):
                opp_val = getattr(value, "StateMachineUnnamed_StateVertex6", None)
                if opp_val is None:
                    setattr(value, "StateMachineUnnamed_StateVertex6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__source", None)
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
    def StateMachineUnnamed_StateVertex(self):
        return self.__StateMachineUnnamed_StateVertex

    @StateMachineUnnamed_StateVertex.setter
    def StateMachineUnnamed_StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineUnnamed_StateVertex__StateMachineUnnamed_StateVertex", None)
        self.__StateMachineUnnamed_StateVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineUnnamed_StateMachine"):
                opp_val = getattr(old_value, "StateMachineUnnamed_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineUnnamed_StateMachine"):
                opp_val = getattr(value, "StateMachineUnnamed_StateMachine", None)
                if opp_val is None:
                    setattr(value, "StateMachineUnnamed_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
