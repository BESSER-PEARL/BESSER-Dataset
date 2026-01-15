from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateMachine_Condition:

    def __init__(self, op: str, value: int, stateMachine_Condition: "stateMachine_Transition" = None, stateMachine_Condition25: "stateMachine_Variable" = None):
        self.op = op
        self.value = value
        self.stateMachine_Condition = stateMachine_Condition
        self.stateMachine_Condition25 = stateMachine_Condition25
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def stateMachine_Condition(self):
        return self.__stateMachine_Condition

    @stateMachine_Condition.setter
    def stateMachine_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Condition__stateMachine_Condition", None)
        self.__stateMachine_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition20"):
                opp_val = getattr(old_value, "stateMachine_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition20"):
                opp_val = getattr(value, "stateMachine_Transition20", None)
                setattr(value, "stateMachine_Transition20", self)

    @property
    def stateMachine_Condition25(self):
        return self.__stateMachine_Condition25

    @stateMachine_Condition25.setter
    def stateMachine_Condition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Condition__stateMachine_Condition25", None)
        self.__stateMachine_Condition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Variable26"):
                opp_val = getattr(old_value, "stateMachine_Variable26", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Variable26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Variable26"):
                opp_val = getattr(value, "stateMachine_Variable26", None)
                setattr(value, "stateMachine_Variable26", self)

class stateMachine_Transition:

    pass
class stateMachine_State:

    def __init__(self, name: str, stateMachine_State: "stateMachine_States" = None, stateMachine_State13: "stateMachine_States" = None, stateMachine_State15: set["stateMachine_Transition"] = None, stateMachine_State23: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_State = stateMachine_State
        self.stateMachine_State13 = stateMachine_State13
        self.stateMachine_State15 = stateMachine_State15 if stateMachine_State15 is not None else set()
        self.stateMachine_State23 = stateMachine_State23
        
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
            if hasattr(old_value, "stateMachine_States10"):
                opp_val = getattr(old_value, "stateMachine_States10", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_States10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_States10"):
                opp_val = getattr(value, "stateMachine_States10", None)
                setattr(value, "stateMachine_States10", self)

    @property
    def stateMachine_State23(self):
        return self.__stateMachine_State23

    @stateMachine_State23.setter
    def stateMachine_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State23", None)
        self.__stateMachine_State23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition22"):
                opp_val = getattr(old_value, "stateMachine_Transition22", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition22"):
                opp_val = getattr(value, "stateMachine_Transition22", None)
                setattr(value, "stateMachine_Transition22", self)

    @property
    def stateMachine_State13(self):
        return self.__stateMachine_State13

    @stateMachine_State13.setter
    def stateMachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State13", None)
        self.__stateMachine_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_States12"):
                opp_val = getattr(old_value, "stateMachine_States12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_States12"):
                opp_val = getattr(value, "stateMachine_States12", None)
                if opp_val is None:
                    setattr(value, "stateMachine_States12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_State15(self):
        return self.__stateMachine_State15

    @stateMachine_State15.setter
    def stateMachine_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State15", None)
        self.__stateMachine_State15 = value if value is not None else set()
        
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
                    

class stateMachine_Event:

    def __init__(self, name: str, stateMachine_Event: "stateMachine_Events" = None, stateMachine_Event18: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_Event = stateMachine_Event
        self.stateMachine_Event18 = stateMachine_Event18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Event(self):
        return self.__stateMachine_Event

    @stateMachine_Event.setter
    def stateMachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event", None)
        self.__stateMachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Events8"):
                opp_val = getattr(old_value, "stateMachine_Events8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Events8"):
                opp_val = getattr(value, "stateMachine_Events8", None)
                if opp_val is None:
                    setattr(value, "stateMachine_Events8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_Event18(self):
        return self.__stateMachine_Event18

    @stateMachine_Event18.setter
    def stateMachine_Event18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event18", None)
        self.__stateMachine_Event18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition17"):
                opp_val = getattr(old_value, "stateMachine_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition17"):
                opp_val = getattr(value, "stateMachine_Transition17", None)
                setattr(value, "stateMachine_Transition17", self)

class stateMachine_Variable:

    def __init__(self, name: str, stateMachine_Variable: "stateMachine_Variables" = None, stateMachine_Variable26: "stateMachine_Condition" = None):
        self.name = name
        self.stateMachine_Variable = stateMachine_Variable
        self.stateMachine_Variable26 = stateMachine_Variable26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_Variable(self):
        return self.__stateMachine_Variable

    @stateMachine_Variable.setter
    def stateMachine_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Variable__stateMachine_Variable", None)
        self.__stateMachine_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Variables6"):
                opp_val = getattr(old_value, "stateMachine_Variables6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Variables6"):
                opp_val = getattr(value, "stateMachine_Variables6", None)
                if opp_val is None:
                    setattr(value, "stateMachine_Variables6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_Variable26(self):
        return self.__stateMachine_Variable26

    @stateMachine_Variable26.setter
    def stateMachine_Variable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Variable__stateMachine_Variable26", None)
        self.__stateMachine_Variable26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Condition25"):
                opp_val = getattr(old_value, "stateMachine_Condition25", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Condition25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Condition25"):
                opp_val = getattr(value, "stateMachine_Condition25", None)
                setattr(value, "stateMachine_Condition25", self)

class stateMachine_States:

    pass
class stateMachine_Events:

    pass
class stateMachine_Variables:

    pass
class stateMachine_StateMachine:

    def __init__(self, name: str, stateMachine_StateMachine: "stateMachine_Variables" = None, stateMachine_StateMachine2: "stateMachine_Events" = None, stateMachine_StateMachine4: "stateMachine_States" = None):
        self.name = name
        self.stateMachine_StateMachine = stateMachine_StateMachine
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2
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
            if hasattr(old_value, "stateMachine_States"):
                opp_val = getattr(old_value, "stateMachine_States", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_States", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_States"):
                opp_val = getattr(value, "stateMachine_States", None)
                setattr(value, "stateMachine_States", self)

    @property
    def stateMachine_StateMachine2(self):
        return self.__stateMachine_StateMachine2

    @stateMachine_StateMachine2.setter
    def stateMachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine2", None)
        self.__stateMachine_StateMachine2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Events"):
                opp_val = getattr(old_value, "stateMachine_Events", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Events"):
                opp_val = getattr(value, "stateMachine_Events", None)
                setattr(value, "stateMachine_Events", self)

    @property
    def stateMachine_StateMachine(self):
        return self.__stateMachine_StateMachine

    @stateMachine_StateMachine.setter
    def stateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine", None)
        self.__stateMachine_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Variables"):
                opp_val = getattr(old_value, "stateMachine_Variables", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Variables"):
                opp_val = getattr(value, "stateMachine_Variables", None)
                setattr(value, "stateMachine_Variables", self)
