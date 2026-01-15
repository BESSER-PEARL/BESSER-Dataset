from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StateVertex:

    pass
class StateMachineHyperedges_InitialState(StateVertex):

    pass
class StateMachineHyperedges_FinalState(StateVertex):

    pass
class StateMachineHyperedges_SimpleState(StateVertex):

    pass
class StateMachineHyperedges_Event:

    pass
class StateMachineHyperedges_Transition:

    def __init__(self, name: str, StateMachineHyperedges_Transition: "StateMachineHyperedges_StateMachine" = None, Transition: "StateMachineHyperedges_StateVertex" = None, Transition5: "StateMachineHyperedges_StateVertex" = None, StateMachineHyperedges_Transition7: "StateMachineHyperedges_Event" = None, outgoing: set["StateMachineHyperedges_StateVertex"] = None, incoming: set["StateMachineHyperedges_StateVertex"] = None):
        self.name = name
        self.StateMachineHyperedges_Transition = StateMachineHyperedges_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.StateMachineHyperedges_Transition7 = StateMachineHyperedges_Transition7
        self.outgoing = outgoing if outgoing is not None else set()
        self.incoming = incoming if incoming is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachineHyperedges_Transition(self):
        return self.__StateMachineHyperedges_Transition

    @StateMachineHyperedges_Transition.setter
    def StateMachineHyperedges_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__StateMachineHyperedges_Transition", None)
        self.__StateMachineHyperedges_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineHyperedges_StateMachine2"):
                opp_val = getattr(old_value, "StateMachineHyperedges_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineHyperedges_StateMachine2"):
                opp_val = getattr(value, "StateMachineHyperedges_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "StateMachineHyperedges_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__Transition5", None)
        self.__Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targets"):
                opp_val = getattr(old_value, "targets", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targets"):
                opp_val = getattr(value, "targets", None)
                if opp_val is None:
                    setattr(value, "targets", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                if opp_val is None:
                    setattr(value, "sources", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__incoming", None)
        self.__incoming = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex10"):
                    opp_val = getattr(item, "StateVertex10", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex10"):
                    opp_val = getattr(item, "StateVertex10", None)
                    
                    setattr(item, "StateVertex10", self)
                    

    @property
    def StateMachineHyperedges_Transition7(self):
        return self.__StateMachineHyperedges_Transition7

    @StateMachineHyperedges_Transition7.setter
    def StateMachineHyperedges_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__StateMachineHyperedges_Transition7", None)
        self.__StateMachineHyperedges_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineHyperedges_Event"):
                opp_val = getattr(old_value, "StateMachineHyperedges_Event", None)
                if opp_val == self:
                    setattr(old_value, "StateMachineHyperedges_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineHyperedges_Event"):
                opp_val = getattr(value, "StateMachineHyperedges_Event", None)
                setattr(value, "StateMachineHyperedges_Event", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_Transition__outgoing", None)
        self.__outgoing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    setattr(item, "StateVertex", self)
                    

class StateMachineHyperedges_StateVertex(ABC):

    def __init__(self, name: str, StateMachineHyperedges_StateVertex: "StateMachineHyperedges_StateMachine" = None, sources: set["StateMachineHyperedges_Transition"] = None, targets: set["StateMachineHyperedges_Transition"] = None, StateVertex: "StateMachineHyperedges_Transition" = None, StateVertex10: "StateMachineHyperedges_Transition" = None):
        self.name = name
        self.StateMachineHyperedges_StateVertex = StateMachineHyperedges_StateVertex
        self.sources = sources if sources is not None else set()
        self.targets = targets if targets is not None else set()
        self.StateVertex = StateVertex
        self.StateVertex10 = StateVertex10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateVertex(self):
        return self.__StateVertex

    @StateVertex.setter
    def StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_StateVertex__StateVertex", None)
        self.__StateVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                if opp_val is None:
                    setattr(value, "outgoing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachineHyperedges_StateVertex(self):
        return self.__StateMachineHyperedges_StateVertex

    @StateMachineHyperedges_StateVertex.setter
    def StateMachineHyperedges_StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_StateVertex__StateMachineHyperedges_StateVertex", None)
        self.__StateMachineHyperedges_StateVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineHyperedges_StateMachine"):
                opp_val = getattr(old_value, "StateMachineHyperedges_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineHyperedges_StateMachine"):
                opp_val = getattr(value, "StateMachineHyperedges_StateMachine", None)
                if opp_val is None:
                    setattr(value, "StateMachineHyperedges_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_StateVertex__targets", None)
        self.__targets = value if value is not None else set()
        
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
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_StateVertex__sources", None)
        self.__sources = value if value is not None else set()
        
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
    def StateVertex10(self):
        return self.__StateVertex10

    @StateVertex10.setter
    def StateVertex10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachineHyperedges_StateVertex__StateVertex10", None)
        self.__StateVertex10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                if opp_val is None:
                    setattr(value, "incoming", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachineHyperedges_StateMachine:

    pass