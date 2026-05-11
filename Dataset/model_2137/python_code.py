from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class transitiongraph_Transition:

    def __init__(self, label: str, probability: float, transitiongraph_Transition: "transitiongraph_TransitionGraph" = None, Transition: "transitiongraph_State" = None, Transition5: "transitiongraph_State" = None, outgoing: "transitiongraph_State" = None, incoming: "transitiongraph_State" = None):
        self.label = label
        self.probability = probability
        self.transitiongraph_Transition = transitiongraph_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.outgoing = outgoing
        self.incoming = incoming
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def probability(self):
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability


    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State8"):
                opp_val = getattr(old_value, "State8", None)
                if opp_val == self:
                    setattr(old_value, "State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State8"):
                opp_val = getattr(value, "State8", None)
                setattr(value, "State8", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_Transition__Transition", None)
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
    def transitiongraph_Transition(self):
        return self.__transitiongraph_Transition

    @transitiongraph_Transition.setter
    def transitiongraph_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_Transition__transitiongraph_Transition", None)
        self.__transitiongraph_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitiongraph_TransitionGraph2"):
                opp_val = getattr(old_value, "transitiongraph_TransitionGraph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitiongraph_TransitionGraph2"):
                opp_val = getattr(value, "transitiongraph_TransitionGraph2", None)
                if opp_val is None:
                    setattr(value, "transitiongraph_TransitionGraph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_Transition__Transition5", None)
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

class transitiongraph_State:

    def __init__(self, id: int, isFinal: bool, isInitial: bool, transitiongraph_State: "transitiongraph_TransitionGraph" = None, source: set["transitiongraph_Transition"] = None, target: set["transitiongraph_Transition"] = None, State: "transitiongraph_Transition" = None, State8: "transitiongraph_Transition" = None):
        self.id = id
        self.isFinal = isFinal
        self.isInitial = isInitial
        self.transitiongraph_State = transitiongraph_State
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State = State
        self.State8 = State8
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial


    @property
    def isFinal(self):
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal


    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_State__State8", None)
        self.__State8 = value
        
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
        old_value = getattr(self, f"_transitiongraph_State__source", None)
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
    def transitiongraph_State(self):
        return self.__transitiongraph_State

    @transitiongraph_State.setter
    def transitiongraph_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_State__transitiongraph_State", None)
        self.__transitiongraph_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitiongraph_TransitionGraph"):
                opp_val = getattr(old_value, "transitiongraph_TransitionGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitiongraph_TransitionGraph"):
                opp_val = getattr(value, "transitiongraph_TransitionGraph", None)
                if opp_val is None:
                    setattr(value, "transitiongraph_TransitionGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_State__target", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transitiongraph_State__State", None)
        self.__State = value
        
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

class transitiongraph_TransitionGraph:

    pass