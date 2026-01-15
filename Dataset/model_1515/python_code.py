from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class mydsl_Initial(State):

    pass
class mydsl_Final(State):

    pass
class mydsl_Transition:

    def __init__(self, name: str, trigger: str, mydsl_Transition8: set["mydsl_State"] = None, mydsl_Transition: "mydsl_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.mydsl_Transition8 = mydsl_Transition8 if mydsl_Transition8 is not None else set()
        self.mydsl_Transition = mydsl_Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def mydsl_Transition(self):
        return self.__mydsl_Transition

    @mydsl_Transition.setter
    def mydsl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Transition__mydsl_Transition", None)
        self.__mydsl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_FSM2"):
                opp_val = getattr(old_value, "mydsl_FSM2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_FSM2"):
                opp_val = getattr(value, "mydsl_FSM2", None)
                if opp_val is None:
                    setattr(value, "mydsl_FSM2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mydsl_Transition8(self):
        return self.__mydsl_Transition8

    @mydsl_Transition8.setter
    def mydsl_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Transition__mydsl_Transition8", None)
        self.__mydsl_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_State9"):
                    opp_val = getattr(item, "mydsl_State9", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_State9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_State9"):
                    opp_val = getattr(item, "mydsl_State9", None)
                    
                    setattr(item, "mydsl_State9", self)
                    

class mydsl_State:

    def __init__(self, name: str, mydsl_State9: "mydsl_Transition" = None, mydsl_State: "mydsl_FSM" = None):
        self.name = name
        self.mydsl_State9 = mydsl_State9
        self.mydsl_State = mydsl_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_State(self):
        return self.__mydsl_State

    @mydsl_State.setter
    def mydsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_State__mydsl_State", None)
        self.__mydsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_FSM"):
                opp_val = getattr(old_value, "mydsl_FSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_FSM"):
                opp_val = getattr(value, "mydsl_FSM", None)
                if opp_val is None:
                    setattr(value, "mydsl_FSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mydsl_State9(self):
        return self.__mydsl_State9

    @mydsl_State9.setter
    def mydsl_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_State__mydsl_State9", None)
        self.__mydsl_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Transition8"):
                opp_val = getattr(old_value, "mydsl_Transition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Transition8"):
                opp_val = getattr(value, "mydsl_Transition8", None)
                if opp_val is None:
                    setattr(value, "mydsl_Transition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mydsl_FSM:

    def __init__(self, name: str, mydsl_FSM: set["mydsl_State"] = None, mydsl_FSM2: set["mydsl_Transition"] = None, mydsl_FSM4: "mydsl_Final" = None, mydsl_FSM6: "mydsl_Initial" = None):
        self.name = name
        self.mydsl_FSM = mydsl_FSM if mydsl_FSM is not None else set()
        self.mydsl_FSM2 = mydsl_FSM2 if mydsl_FSM2 is not None else set()
        self.mydsl_FSM4 = mydsl_FSM4
        self.mydsl_FSM6 = mydsl_FSM6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_FSM6(self):
        return self.__mydsl_FSM6

    @mydsl_FSM6.setter
    def mydsl_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_FSM__mydsl_FSM6", None)
        self.__mydsl_FSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Initial"):
                opp_val = getattr(old_value, "mydsl_Initial", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Initial", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Initial"):
                opp_val = getattr(value, "mydsl_Initial", None)
                setattr(value, "mydsl_Initial", self)

    @property
    def mydsl_FSM(self):
        return self.__mydsl_FSM

    @mydsl_FSM.setter
    def mydsl_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_FSM__mydsl_FSM", None)
        self.__mydsl_FSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_State"):
                    opp_val = getattr(item, "mydsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_State"):
                    opp_val = getattr(item, "mydsl_State", None)
                    
                    setattr(item, "mydsl_State", self)
                    

    @property
    def mydsl_FSM4(self):
        return self.__mydsl_FSM4

    @mydsl_FSM4.setter
    def mydsl_FSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_FSM__mydsl_FSM4", None)
        self.__mydsl_FSM4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Final"):
                opp_val = getattr(old_value, "mydsl_Final", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Final", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Final"):
                opp_val = getattr(value, "mydsl_Final", None)
                setattr(value, "mydsl_Final", self)

    @property
    def mydsl_FSM2(self):
        return self.__mydsl_FSM2

    @mydsl_FSM2.setter
    def mydsl_FSM2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_FSM__mydsl_FSM2", None)
        self.__mydsl_FSM2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mydsl_Transition"):
                    opp_val = getattr(item, "mydsl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "mydsl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mydsl_Transition"):
                    opp_val = getattr(item, "mydsl_Transition", None)
                    
                    setattr(item, "mydsl_Transition", self)
                    
