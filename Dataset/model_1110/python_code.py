from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateMachine_Transition:

    def __init__(self, name: str, action: str, trigger: str, stateMachine_Transition: "stateMachine_StateMachine" = None, Transition: "stateMachine_State" = None, Transition8: "stateMachine_State" = None, Outgoing: "stateMachine_State" = None, incoming: "stateMachine_State" = None):
        self.name = name
        self.action = action
        self.trigger = trigger
        self.stateMachine_Transition = stateMachine_Transition
        self.Transition = Transition
        self.Transition8 = Transition8
        self.Outgoing = Outgoing
        self.incoming = incoming
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Transition__incoming", None)
        self.__incoming = value
        
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
    def stateMachine_Transition(self):
        return self.__stateMachine_Transition

    @stateMachine_Transition.setter
    def stateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Transition__stateMachine_Transition", None)
        self.__stateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine2"):
                opp_val = getattr(old_value, "stateMachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine2"):
                opp_val = getattr(value, "stateMachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Transition__Transition", None)
        self.__Transition = value
        
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
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Transition__Transition8", None)
        self.__Transition8 = value
        
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
    def Outgoing(self):
        return self.__Outgoing

    @Outgoing.setter
    def Outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Transition__Outgoing", None)
        self.__Outgoing = value
        
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

class stateMachine_State:

    def __init__(self, name: str, status: bool, State11: "stateMachine_Transition" = None, stateMachine_State: "stateMachine_StateMachine" = None, stateMachine_State5: "stateMachine_StateMachine" = None, from: set["stateMachine_Transition"] = None, target: set["stateMachine_Transition"] = None, State: "stateMachine_Transition" = None):
        self.name = name
        self.status = status
        self.State11 = State11
        self.stateMachine_State = stateMachine_State
        self.stateMachine_State5 = stateMachine_State5
        self.from = from if from is not None else set()
        self.target = target if target is not None else set()
        self.State = State
        
    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_State(self):
        return self.__stateMachine_State

    @stateMachine_State.setter
    def stateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State", None)
        self.__stateMachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine"):
                opp_val = getattr(old_value, "stateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine"):
                opp_val = getattr(value, "stateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_State5(self):
        return self.__stateMachine_State5

    @stateMachine_State5.setter
    def stateMachine_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State5", None)
        self.__stateMachine_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_StateMachine4"):
                opp_val = getattr(old_value, "stateMachine_StateMachine4", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_StateMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine4"):
                opp_val = getattr(value, "stateMachine_StateMachine4", None)
                setattr(value, "stateMachine_StateMachine4", self)

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State11", None)
        self.__State11 = value
        
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
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__from", None)
        self.__from = value if value is not None else set()
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__target", None)
        self.__target = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Outgoing"):
                opp_val = getattr(old_value, "Outgoing", None)
                if opp_val == self:
                    setattr(old_value, "Outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Outgoing"):
                opp_val = getattr(value, "Outgoing", None)
                setattr(value, "Outgoing", self)

class stateMachine_StateMachine:

    def __init__(self, name: str, stateMachine_StateMachine: set["stateMachine_State"] = None, stateMachine_StateMachine2: set["stateMachine_Transition"] = None, stateMachine_StateMachine4: "stateMachine_State" = None):
        self.name = name
        self.stateMachine_StateMachine = stateMachine_StateMachine if stateMachine_StateMachine is not None else set()
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2 if stateMachine_StateMachine2 is not None else set()
        self.stateMachine_StateMachine4 = stateMachine_StateMachine4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_StateMachine4(self):
        return self.__stateMachine_StateMachine4

    @stateMachine_StateMachine4.setter
    def stateMachine_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine4", None)
        self.__stateMachine_StateMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_State5"):
                opp_val = getattr(old_value, "stateMachine_State5", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_State5"):
                opp_val = getattr(value, "stateMachine_State5", None)
                setattr(value, "stateMachine_State5", self)

    @property
    def stateMachine_StateMachine(self):
        return self.__stateMachine_StateMachine

    @stateMachine_StateMachine.setter
    def stateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine", None)
        self.__stateMachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_State"):
                    opp_val = getattr(item, "stateMachine_State", None)
                    
                    setattr(item, "stateMachine_State", self)
                    

    @property
    def stateMachine_StateMachine2(self):
        return self.__stateMachine_StateMachine2

    @stateMachine_StateMachine2.setter
    def stateMachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine2", None)
        self.__stateMachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateMachine_Transition"):
                    opp_val = getattr(item, "stateMachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Transition"):
                    opp_val = getattr(item, "stateMachine_Transition", None)
                    
                    setattr(item, "stateMachine_Transition", self)
                    
