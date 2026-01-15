from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_Event:

    def __init__(self, id: str, statemachine_Event19: "statemachine_Transition" = None, statemachine_Event: "statemachine_SM" = None):
        self.id = id
        self.statemachine_Event19 = statemachine_Event19
        self.statemachine_Event = statemachine_Event
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def statemachine_Event(self):
        return self.__statemachine_Event

    @statemachine_Event.setter
    def statemachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event", None)
        self.__statemachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_SM10"):
                opp_val = getattr(old_value, "statemachine_SM10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_SM10"):
                opp_val = getattr(value, "statemachine_SM10", None)
                if opp_val is None:
                    setattr(value, "statemachine_SM10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Event19(self):
        return self.__statemachine_Event19

    @statemachine_Event19.setter
    def statemachine_Event19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event19", None)
        self.__statemachine_Event19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition18"):
                opp_val = getattr(old_value, "statemachine_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition18"):
                opp_val = getattr(value, "statemachine_Transition18", None)
                setattr(value, "statemachine_Transition18", self)

class statemachine_Transition:

    pass
class statemachine_State:

    def __init__(self, id: str, statemachine_State: "statemachine_SM" = None, statemachine_State3: "statemachine_SM" = None, statemachine_State16: "statemachine_Transition" = None, statemachine_State6: "statemachine_SM" = None, statemachine_State13: "statemachine_Transition" = None):
        self.id = id
        self.statemachine_State = statemachine_State
        self.statemachine_State3 = statemachine_State3
        self.statemachine_State16 = statemachine_State16
        self.statemachine_State6 = statemachine_State6
        self.statemachine_State13 = statemachine_State13
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_SM5"):
                opp_val = getattr(old_value, "statemachine_SM5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_SM5"):
                opp_val = getattr(value, "statemachine_SM5", None)
                if opp_val is None:
                    setattr(value, "statemachine_SM5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State13(self):
        return self.__statemachine_State13

    @statemachine_State13.setter
    def statemachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State13", None)
        self.__statemachine_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition12"):
                opp_val = getattr(old_value, "statemachine_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition12"):
                opp_val = getattr(value, "statemachine_Transition12", None)
                setattr(value, "statemachine_Transition12", self)

    @property
    def statemachine_State16(self):
        return self.__statemachine_State16

    @statemachine_State16.setter
    def statemachine_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State16", None)
        self.__statemachine_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition15"):
                opp_val = getattr(old_value, "statemachine_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition15"):
                opp_val = getattr(value, "statemachine_Transition15", None)
                setattr(value, "statemachine_Transition15", self)

    @property
    def statemachine_State3(self):
        return self.__statemachine_State3

    @statemachine_State3.setter
    def statemachine_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State3", None)
        self.__statemachine_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_SM2"):
                opp_val = getattr(old_value, "statemachine_SM2", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_SM2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_SM2"):
                opp_val = getattr(value, "statemachine_SM2", None)
                setattr(value, "statemachine_SM2", self)

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_SM"):
                opp_val = getattr(old_value, "statemachine_SM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_SM"):
                opp_val = getattr(value, "statemachine_SM", None)
                if opp_val is None:
                    setattr(value, "statemachine_SM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_SM:

    pass