from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class iDM_Test_Transition:

    def __init__(self, name: str, iDM_Test_Transition: "iDM_Test_StateMachine" = None, Transition: "iDM_Test_State" = None, Transition8: "iDM_Test_State" = None, outgoing: "iDM_Test_State" = None, incomming: "iDM_Test_State" = None):
        self.name = name
        self.iDM_Test_Transition = iDM_Test_Transition
        self.Transition = Transition
        self.Transition8 = Transition8
        self.outgoing = outgoing
        self.incomming = incomming
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_Transition__Transition8", None)
        self.__Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iDM_Test_Transition(self):
        return self.__iDM_Test_Transition

    @iDM_Test_Transition.setter
    def iDM_Test_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_Transition__iDM_Test_Transition", None)
        self.__iDM_Test_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iDM_Test_StateMachine2"):
                opp_val = getattr(old_value, "iDM_Test_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iDM_Test_StateMachine2"):
                opp_val = getattr(value, "iDM_Test_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "iDM_Test_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomming(self):
        return self.__incomming

    @incomming.setter
    def incomming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_Transition__incomming", None)
        self.__incomming = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_Transition__outgoing", None)
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
        old_value = getattr(self, f"_iDM_Test_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iDM_Test_State:

    def __init__(self, name: str, iDM_Test_State: "iDM_Test_StateMachine" = None, iDM_Test_State5: "iDM_Test_StateMachine" = None, to: set["iDM_Test_Transition"] = None, from: set["iDM_Test_Transition"] = None, State: "iDM_Test_Transition" = None, State11: "iDM_Test_Transition" = None):
        self.name = name
        self.iDM_Test_State = iDM_Test_State
        self.iDM_Test_State5 = iDM_Test_State5
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.State = State
        self.State11 = State11
        
    @property
    def name(self) -> str:
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
        old_value = getattr(self, f"_iDM_Test_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomming"):
                opp_val = getattr(old_value, "incomming", None)
                if opp_val == self:
                    setattr(old_value, "incomming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomming"):
                opp_val = getattr(value, "incomming", None)
                setattr(value, "incomming", self)

    @property
    def iDM_Test_State(self):
        return self.__iDM_Test_State

    @iDM_Test_State.setter
    def iDM_Test_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_State__iDM_Test_State", None)
        self.__iDM_Test_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iDM_Test_StateMachine"):
                opp_val = getattr(old_value, "iDM_Test_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iDM_Test_StateMachine"):
                opp_val = getattr(value, "iDM_Test_StateMachine", None)
                if opp_val is None:
                    setattr(value, "iDM_Test_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iDM_Test_State5(self):
        return self.__iDM_Test_State5

    @iDM_Test_State5.setter
    def iDM_Test_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_State__iDM_Test_State5", None)
        self.__iDM_Test_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iDM_Test_StateMachine4"):
                opp_val = getattr(old_value, "iDM_Test_StateMachine4", None)
                if opp_val == self:
                    setattr(old_value, "iDM_Test_StateMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iDM_Test_StateMachine4"):
                opp_val = getattr(value, "iDM_Test_StateMachine4", None)
                setattr(value, "iDM_Test_StateMachine4", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_State__to", None)
        self.__to = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_State__State", None)
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

class iDM_Test_StateMachine:

    def __init__(self, name: str, iDM_Test_StateMachine: set["iDM_Test_State"] = None, iDM_Test_StateMachine2: set["iDM_Test_Transition"] = None, iDM_Test_StateMachine4: "iDM_Test_State" = None):
        self.name = name
        self.iDM_Test_StateMachine = iDM_Test_StateMachine if iDM_Test_StateMachine is not None else set()
        self.iDM_Test_StateMachine2 = iDM_Test_StateMachine2 if iDM_Test_StateMachine2 is not None else set()
        self.iDM_Test_StateMachine4 = iDM_Test_StateMachine4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iDM_Test_StateMachine(self):
        return self.__iDM_Test_StateMachine

    @iDM_Test_StateMachine.setter
    def iDM_Test_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_StateMachine__iDM_Test_StateMachine", None)
        self.__iDM_Test_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iDM_Test_State"):
                    opp_val = getattr(item, "iDM_Test_State", None)
                    
                    if opp_val == self:
                        setattr(item, "iDM_Test_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iDM_Test_State"):
                    opp_val = getattr(item, "iDM_Test_State", None)
                    
                    setattr(item, "iDM_Test_State", self)
                    

    @property
    def iDM_Test_StateMachine2(self):
        return self.__iDM_Test_StateMachine2

    @iDM_Test_StateMachine2.setter
    def iDM_Test_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_StateMachine__iDM_Test_StateMachine2", None)
        self.__iDM_Test_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iDM_Test_Transition"):
                    opp_val = getattr(item, "iDM_Test_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "iDM_Test_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iDM_Test_Transition"):
                    opp_val = getattr(item, "iDM_Test_Transition", None)
                    
                    setattr(item, "iDM_Test_Transition", self)
                    

    @property
    def iDM_Test_StateMachine4(self):
        return self.__iDM_Test_StateMachine4

    @iDM_Test_StateMachine4.setter
    def iDM_Test_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iDM_Test_StateMachine__iDM_Test_StateMachine4", None)
        self.__iDM_Test_StateMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iDM_Test_State5"):
                opp_val = getattr(old_value, "iDM_Test_State5", None)
                if opp_val == self:
                    setattr(old_value, "iDM_Test_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iDM_Test_State5"):
                opp_val = getattr(value, "iDM_Test_State5", None)
                setattr(value, "iDM_Test_State5", self)
