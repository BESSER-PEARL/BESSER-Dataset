from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StateMachine_Event:

    pass
class StateMachine_Transition:

    def __init__(self, name: str, incoming: "StateMachine_StateVertex" = None, StateMachine_Transition: "StateMachine_StateMachine" = None, Transition: "StateMachine_StateVertex" = None, Transition5: "StateMachine_StateVertex" = None, StateMachine_Transition7: "StateMachine_Event" = None, outgoing: "StateMachine_StateVertex" = None):
        self.name = name
        self.incoming = incoming
        self.StateMachine_Transition = StateMachine_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.StateMachine_Transition7 = StateMachine_Transition7
        self.outgoing = outgoing
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine_Transition(self):
        return self.__StateMachine_Transition

    @StateMachine_Transition.setter
    def StateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition", None)
        self.__StateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine2"):
                opp_val = getattr(old_value, "StateMachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine2"):
                opp_val = getattr(value, "StateMachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "StateMachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateVertex10"):
                opp_val = getattr(old_value, "StateVertex10", None)
                if opp_val == self:
                    setattr(old_value, "StateVertex10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateVertex10"):
                opp_val = getattr(value, "StateVertex10", None)
                setattr(value, "StateVertex10", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__outgoing", None)
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
    def StateMachine_Transition7(self):
        return self.__StateMachine_Transition7

    @StateMachine_Transition7.setter
    def StateMachine_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition7", None)
        self.__StateMachine_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Event"):
                opp_val = getattr(old_value, "StateMachine_Event", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Event"):
                opp_val = getattr(value, "StateMachine_Event", None)
                setattr(value, "StateMachine_Event", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition5", None)
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

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition", None)
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

class StateMachine_StateVertex:

    def __init__(self, name: str, StateVertex10: "StateMachine_Transition" = None, StateMachine_StateVertex: "StateMachine_StateMachine" = None, source: set["StateMachine_Transition"] = None, target: set["StateMachine_Transition"] = None, StateVertex: "StateMachine_Transition" = None):
        self.name = name
        self.StateVertex10 = StateVertex10
        self.StateMachine_StateVertex = StateMachine_StateVertex
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.StateVertex = StateVertex
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateVertex10(self):
        return self.__StateVertex10

    @StateVertex10.setter
    def StateVertex10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateVertex__StateVertex10", None)
        self.__StateVertex10 = value
        
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
    def StateVertex(self):
        return self.__StateVertex

    @StateVertex.setter
    def StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateVertex__StateVertex", None)
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
    def StateMachine_StateVertex(self):
        return self.__StateMachine_StateVertex

    @StateMachine_StateVertex.setter
    def StateMachine_StateVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateVertex__StateMachine_StateVertex", None)
        self.__StateMachine_StateVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine"):
                opp_val = getattr(old_value, "StateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine"):
                opp_val = getattr(value, "StateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "StateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateVertex__target", None)
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
        old_value = getattr(self, f"_StateMachine_StateVertex__source", None)
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
                    

class StateMachine_StateMachine:

    pass
class StateVertex:

    pass
class StateMachine_SimpleState(StateVertex):

    pass
class StateMachine_FinalState(StateVertex):

    pass
class StateMachine_InitialState(StateVertex):

    pass