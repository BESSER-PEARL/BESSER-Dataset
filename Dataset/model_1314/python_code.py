from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class stateMachine_Transition:

    pass
class stateMachine_State:

    def __init__(self, name: str, stateMachine_State12: "stateMachine_Transition" = None, stateMachine_State: "stateMachine_StateMachine" = None, stateMachine_State6: set["stateMachine_Transition"] = None):
        self.name = name
        self.stateMachine_State12 = stateMachine_State12
        self.stateMachine_State = stateMachine_State
        self.stateMachine_State6 = stateMachine_State6 if stateMachine_State6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateMachine_State6(self):
        return self.__stateMachine_State6

    @stateMachine_State6.setter
    def stateMachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State6", None)
        self.__stateMachine_State6 = value if value is not None else set()
        
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
                    

    @property
    def stateMachine_State12(self):
        return self.__stateMachine_State12

    @stateMachine_State12.setter
    def stateMachine_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_State__stateMachine_State12", None)
        self.__stateMachine_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition11"):
                opp_val = getattr(old_value, "stateMachine_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition11"):
                opp_val = getattr(value, "stateMachine_Transition11", None)
                setattr(value, "stateMachine_Transition11", self)

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
            if hasattr(old_value, "stateMachine_StateMachine4"):
                opp_val = getattr(old_value, "stateMachine_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_StateMachine4"):
                opp_val = getattr(value, "stateMachine_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "stateMachine_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class stateMachine_Event:

    def __init__(self, name: str, stateMachine_Event14: "stateMachine_Condition" = None, stateMachine_Event: "stateMachine_StateMachine" = None, stateMachine_Event9: "stateMachine_Transition" = None):
        self.name = name
        self.stateMachine_Event14 = stateMachine_Event14
        self.stateMachine_Event = stateMachine_Event
        self.stateMachine_Event9 = stateMachine_Event9
        
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
    def stateMachine_Event14(self):
        return self.__stateMachine_Event14

    @stateMachine_Event14.setter
    def stateMachine_Event14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event14", None)
        self.__stateMachine_Event14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Condition"):
                opp_val = getattr(old_value, "stateMachine_Condition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Condition"):
                opp_val = getattr(value, "stateMachine_Condition", None)
                if opp_val is None:
                    setattr(value, "stateMachine_Condition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateMachine_Event9(self):
        return self.__stateMachine_Event9

    @stateMachine_Event9.setter
    def stateMachine_Event9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_Event__stateMachine_Event9", None)
        self.__stateMachine_Event9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine_Transition8"):
                opp_val = getattr(old_value, "stateMachine_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Transition8"):
                opp_val = getattr(value, "stateMachine_Transition8", None)
                setattr(value, "stateMachine_Transition8", self)

class stateMachine_Condition:

    pass
class stateMachine_StateMachine:

    def __init__(self, name: str, stateMachine_StateMachine: "stateMachine_Model" = None, stateMachine_StateMachine2: set["stateMachine_Event"] = None, stateMachine_StateMachine4: set["stateMachine_State"] = None):
        self.name = name
        self.stateMachine_StateMachine = stateMachine_StateMachine
        self.stateMachine_StateMachine2 = stateMachine_StateMachine2 if stateMachine_StateMachine2 is not None else set()
        self.stateMachine_StateMachine4 = stateMachine_StateMachine4 if stateMachine_StateMachine4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "stateMachine_Model"):
                opp_val = getattr(old_value, "stateMachine_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine_Model"):
                opp_val = getattr(value, "stateMachine_Model", None)
                if opp_val is None:
                    setattr(value, "stateMachine_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "stateMachine_Event"):
                    opp_val = getattr(item, "stateMachine_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "stateMachine_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateMachine_Event"):
                    opp_val = getattr(item, "stateMachine_Event", None)
                    
                    setattr(item, "stateMachine_Event", self)
                    

    @property
    def stateMachine_StateMachine4(self):
        return self.__stateMachine_StateMachine4

    @stateMachine_StateMachine4.setter
    def stateMachine_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateMachine_StateMachine__stateMachine_StateMachine4", None)
        self.__stateMachine_StateMachine4 = value if value is not None else set()
        
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
                    

class stateMachine_Model:

    pass