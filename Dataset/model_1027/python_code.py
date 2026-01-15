from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mydsl_State:

    def __init__(self, name: str, mydsl_State: "mydsl_FSM" = None, mydsl_State5: "mydsl_Transition" = None, mydsl_State8: "mydsl_Transition" = None):
        self.name = name
        self.mydsl_State = mydsl_State
        self.mydsl_State5 = mydsl_State5
        self.mydsl_State8 = mydsl_State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_State5(self):
        return self.__mydsl_State5

    @mydsl_State5.setter
    def mydsl_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_State__mydsl_State5", None)
        self.__mydsl_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Transition4"):
                opp_val = getattr(old_value, "mydsl_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Transition4"):
                opp_val = getattr(value, "mydsl_Transition4", None)
                setattr(value, "mydsl_Transition4", self)

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
    def mydsl_State8(self):
        return self.__mydsl_State8

    @mydsl_State8.setter
    def mydsl_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_State__mydsl_State8", None)
        self.__mydsl_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_Transition7"):
                opp_val = getattr(old_value, "mydsl_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_Transition7"):
                opp_val = getattr(value, "mydsl_Transition7", None)
                setattr(value, "mydsl_Transition7", self)

class mydsl_FSM:

    def __init__(self, name: str, mydsl_FSM2: set["mydsl_Transition"] = None, mydsl_FSM: set["mydsl_State"] = None):
        self.name = name
        self.mydsl_FSM2 = mydsl_FSM2 if mydsl_FSM2 is not None else set()
        self.mydsl_FSM = mydsl_FSM if mydsl_FSM is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class State:

    pass
class mydsl_FinalState(State):

    pass
class mydsl_IntitialState(State):

    pass
class mydsl_Transition:

    def __init__(self, name: str, mydsl_Transition: "mydsl_FSM" = None, mydsl_Transition4: "mydsl_State" = None, mydsl_Transition7: "mydsl_State" = None):
        self.name = name
        self.mydsl_Transition = mydsl_Transition
        self.mydsl_Transition4 = mydsl_Transition4
        self.mydsl_Transition7 = mydsl_Transition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mydsl_Transition7(self):
        return self.__mydsl_Transition7

    @mydsl_Transition7.setter
    def mydsl_Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Transition__mydsl_Transition7", None)
        self.__mydsl_Transition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_State8"):
                opp_val = getattr(old_value, "mydsl_State8", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_State8"):
                opp_val = getattr(value, "mydsl_State8", None)
                setattr(value, "mydsl_State8", self)

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
    def mydsl_Transition4(self):
        return self.__mydsl_Transition4

    @mydsl_Transition4.setter
    def mydsl_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mydsl_Transition__mydsl_Transition4", None)
        self.__mydsl_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mydsl_State5"):
                opp_val = getattr(old_value, "mydsl_State5", None)
                if opp_val == self:
                    setattr(old_value, "mydsl_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mydsl_State5"):
                opp_val = getattr(value, "mydsl_State5", None)
                setattr(value, "mydsl_State5", self)
