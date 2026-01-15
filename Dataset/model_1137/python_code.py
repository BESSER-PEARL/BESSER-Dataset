from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class esm_EObject:

    pass
class State:

    pass
class esm_EndState(State):

    pass
class esm_Transition:

    def __init__(self, action: str, esm_Transition: "esm_Machine" = None, Transition: "esm_State" = None, Transition5: "esm_State" = None, esm_Transition7: "esm_EObject" = None, outgoing: "esm_State" = None, incoming: "esm_State" = None):
        self.action = action
        self.esm_Transition = esm_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.esm_Transition7 = esm_Transition7
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_Transition__Transition5", None)
        self.__Transition5 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_Transition__outgoing", None)
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
        old_value = getattr(self, f"_esm_Transition__Transition", None)
        self.__Transition = value
        
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
    def esm_Transition7(self):
        return self.__esm_Transition7

    @esm_Transition7.setter
    def esm_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_Transition__esm_Transition7", None)
        self.__esm_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_EObject"):
                opp_val = getattr(old_value, "esm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "esm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_EObject"):
                opp_val = getattr(value, "esm_EObject", None)
                setattr(value, "esm_EObject", self)

    @property
    def esm_Transition(self):
        return self.__esm_Transition

    @esm_Transition.setter
    def esm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_Transition__esm_Transition", None)
        self.__esm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_Machine2"):
                opp_val = getattr(old_value, "esm_Machine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_Machine2"):
                opp_val = getattr(value, "esm_Machine2", None)
                if opp_val is None:
                    setattr(value, "esm_Machine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State10"):
                opp_val = getattr(old_value, "State10", None)
                if opp_val == self:
                    setattr(old_value, "State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State10"):
                opp_val = getattr(value, "State10", None)
                setattr(value, "State10", self)

class esm_State:

    def __init__(self, name: str, esm_State: "esm_Machine" = None, target: set["esm_Transition"] = None, source: set["esm_Transition"] = None, State: "esm_Transition" = None, State10: "esm_Transition" = None):
        self.name = name
        self.esm_State = esm_State
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.State = State
        self.State10 = State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State10(self):
        return self.__State10

    @State10.setter
    def State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_State__State10", None)
        self.__State10 = value
        
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
    def esm_State(self):
        return self.__esm_State

    @esm_State.setter
    def esm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_State__esm_State", None)
        self.__esm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "esm_Machine"):
                opp_val = getattr(old_value, "esm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "esm_Machine"):
                opp_val = getattr(value, "esm_Machine", None)
                if opp_val is None:
                    setattr(value, "esm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_State__source", None)
        self.__source = value if value is not None else set()
        
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
        old_value = getattr(self, f"_esm_State__State", None)
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

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_esm_State__target", None)
        self.__target = value if value is not None else set()
        
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
                    

class esm_Machine:

    pass