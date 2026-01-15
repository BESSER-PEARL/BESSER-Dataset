from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class minifsm_FinalState(State):

    pass
class minifsm_Transition:

    def __init__(self, event: str, minifsm_Transition: "minifsm_Machine" = None, 4: "minifsm_State" = None, 9: "minifsm_State" = None, 12: "minifsm_State" = None, 7: "minifsm_State" = None):
        self.event = event
        self.minifsm_Transition = minifsm_Transition
        self.4 = 4
        self.9 = 9
        self.12 = 12
        self.7 = 7
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def minifsm_Transition(self):
        return self.__minifsm_Transition

    @minifsm_Transition.setter
    def minifsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__minifsm_Transition", None)
        self.__minifsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Machine2"):
                opp_val = getattr(old_value, "minifsm_Machine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Machine2"):
                opp_val = getattr(value, "minifsm_Machine2", None)
                if opp_val is None:
                    setattr(value, "minifsm_Machine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_Transition__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minifsm_State:

    def __init__(self, name: str, minifsm_State: "minifsm_Machine" = None, : set["minifsm_Transition"] = None, 10: "minifsm_Transition" = None, 13: "minifsm_Transition" = None, 6: set["minifsm_Transition"] = None):
        self.name = name
        self.minifsm_State = minifsm_State
        self. =  if  is not None else set()
        self.10 = 10
        self.13 = 13
        self.6 = 6 if 6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def minifsm_State(self):
        return self.__minifsm_State

    @minifsm_State.setter
    def minifsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__minifsm_State", None)
        self.__minifsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minifsm_Machine"):
                opp_val = getattr(old_value, "minifsm_Machine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minifsm_Machine"):
                opp_val = getattr(value, "minifsm_Machine", None)
                if opp_val is None:
                    setattr(value, "minifsm_Machine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minifsm_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "12"):
                opp_val = getattr(old_value, "12", None)
                if opp_val == self:
                    setattr(old_value, "12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "12"):
                opp_val = getattr(value, "12", None)
                setattr(value, "12", self)

class minifsm_Machine:

    pass