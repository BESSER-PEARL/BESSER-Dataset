from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lts_Transition:

    def __init__(self, label: str, incoming: "lts_State" = None, outgoing: "lts_State" = None, Transition: "lts_State" = None, Transition12: "lts_State" = None, lts_Transition: "lts_LTS" = None):
        self.label = label
        self.incoming = incoming
        self.outgoing = outgoing
        self.Transition = Transition
        self.Transition12 = Transition12
        self.lts_Transition = lts_Transition
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def Transition12(self):
        return self.__Transition12

    @Transition12.setter
    def Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_Transition__Transition12", None)
        self.__Transition12 = value
        
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
        old_value = getattr(self, f"_lts_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def lts_Transition(self):
        return self.__lts_Transition

    @lts_Transition.setter
    def lts_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_Transition__lts_Transition", None)
        self.__lts_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_LTS"):
                opp_val = getattr(old_value, "lts_LTS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_LTS"):
                opp_val = getattr(value, "lts_LTS", None)
                if opp_val is None:
                    setattr(value, "lts_LTS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_Transition__incoming", None)
        self.__incoming = value
        
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
        old_value = getattr(self, f"_lts_Transition__Transition", None)
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

class lts_LTS:

    def __init__(self, name: str, lts_LTS4: set["lts_IntermediateState"] = None, lts_LTS6: "lts_FinalState" = None, lts_LTS: set["lts_Transition"] = None, lts_LTS2: "lts_InitialState" = None):
        self.name = name
        self.lts_LTS4 = lts_LTS4 if lts_LTS4 is not None else set()
        self.lts_LTS6 = lts_LTS6
        self.lts_LTS = lts_LTS if lts_LTS is not None else set()
        self.lts_LTS2 = lts_LTS2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lts_LTS6(self):
        return self.__lts_LTS6

    @lts_LTS6.setter
    def lts_LTS6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_LTS__lts_LTS6", None)
        self.__lts_LTS6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_FinalState"):
                opp_val = getattr(old_value, "lts_FinalState", None)
                if opp_val == self:
                    setattr(old_value, "lts_FinalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_FinalState"):
                opp_val = getattr(value, "lts_FinalState", None)
                setattr(value, "lts_FinalState", self)

    @property
    def lts_LTS2(self):
        return self.__lts_LTS2

    @lts_LTS2.setter
    def lts_LTS2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_LTS__lts_LTS2", None)
        self.__lts_LTS2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lts_InitialState"):
                opp_val = getattr(old_value, "lts_InitialState", None)
                if opp_val == self:
                    setattr(old_value, "lts_InitialState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lts_InitialState"):
                opp_val = getattr(value, "lts_InitialState", None)
                setattr(value, "lts_InitialState", self)

    @property
    def lts_LTS4(self):
        return self.__lts_LTS4

    @lts_LTS4.setter
    def lts_LTS4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_LTS__lts_LTS4", None)
        self.__lts_LTS4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lts_IntermediateState"):
                    opp_val = getattr(item, "lts_IntermediateState", None)
                    
                    if opp_val == self:
                        setattr(item, "lts_IntermediateState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lts_IntermediateState"):
                    opp_val = getattr(item, "lts_IntermediateState", None)
                    
                    setattr(item, "lts_IntermediateState", self)
                    

    @property
    def lts_LTS(self):
        return self.__lts_LTS

    @lts_LTS.setter
    def lts_LTS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_LTS__lts_LTS", None)
        self.__lts_LTS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lts_Transition"):
                    opp_val = getattr(item, "lts_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "lts_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lts_Transition"):
                    opp_val = getattr(item, "lts_Transition", None)
                    
                    setattr(item, "lts_Transition", self)
                    

class State:

    pass
class lts_InitialState(State):

    pass
class lts_State:

    def __init__(self, Id: str, State: "lts_Transition" = None, State9: "lts_Transition" = None, target: set["lts_Transition"] = None, source: set["lts_Transition"] = None):
        self.Id = Id
        self.State = State
        self.State9 = State9
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_State__target", None)
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
                    

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_State__State9", None)
        self.__State9 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lts_State__State", None)
        self.__State = value
        
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
        old_value = getattr(self, f"_lts_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition12"):
                    opp_val = getattr(item, "Transition12", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition12"):
                    opp_val = getattr(item, "Transition12", None)
                    
                    setattr(item, "Transition12", self)
                    

class lts_FinalState(State):

    pass
class lts_IntermediateState(State):

    pass