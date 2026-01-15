from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simplefsm_Transition:

    pass
class simplefsm_State:

    def __init__(self, name: str, 1: "simplefsm_FSM" = None, simplefsm_State: "simplefsm_FSM" = None, 4: "simplefsm_FSM" = None, 7: set["simplefsm_Transition"] = None, 10: set["simplefsm_Transition"] = None, 14: "simplefsm_Transition" = None, 17: "simplefsm_Transition" = None):
        self.name = name
        self.1 = 1
        self.simplefsm_State = simplefsm_State
        self.4 = 4
        self.7 = 7 if 7 is not None else set()
        self.10 = 10 if 10 is not None else set()
        self.14 = 14
        self.17 = 17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__7", None)
        self.__7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    if opp_val == self:
                        setattr(item, "8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    setattr(item, "8", self)
                    

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__14", None)
        self.__14 = value
        
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
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__10", None)
        self.__10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    if opp_val == self:
                        setattr(item, "11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    setattr(item, "11", self)
                    

    @property
    def simplefsm_State(self):
        return self.__simplefsm_State

    @simplefsm_State.setter
    def simplefsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__simplefsm_State", None)
        self.__simplefsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplefsm_FSM"):
                opp_val = getattr(old_value, "simplefsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "simplefsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplefsm_FSM"):
                opp_val = getattr(value, "simplefsm_FSM", None)
                setattr(value, "simplefsm_FSM", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if opp_val == self:
                    setattr(old_value, "5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                setattr(value, "5", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__1", None)
        self.__1 = value
        
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

class simplefsm_FSM:

    pass