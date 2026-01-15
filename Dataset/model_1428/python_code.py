from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class statemachine_Transition:

    pass
class statemachine_Event:

    def __init__(self, name: str, statemachine_Event: "statemachine_Statemachine" = None, statemachine_Event13: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_Event = statemachine_Event
        self.statemachine_Event13 = statemachine_Event13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Event13(self):
        return self.__statemachine_Event13

    @statemachine_Event13.setter
    def statemachine_Event13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event13", None)
        self.__statemachine_Event13 = value
        
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
    def statemachine_Event(self):
        return self.__statemachine_Event

    @statemachine_Event.setter
    def statemachine_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Event__statemachine_Event", None)
        self.__statemachine_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine2"):
                opp_val = getattr(old_value, "statemachine_Statemachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine2"):
                opp_val = getattr(value, "statemachine_Statemachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_State:

    def __init__(self, name: str, statemachine_State16: "statemachine_Transition" = None, statemachine_State: "statemachine_Statemachine" = None, statemachine_State7: "statemachine_Statemachine" = None, statemachine_State10: "statemachine_Transition" = None):
        self.name = name
        self.statemachine_State16 = statemachine_State16
        self.statemachine_State = statemachine_State
        self.statemachine_State7 = statemachine_State7
        self.statemachine_State10 = statemachine_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_State7(self):
        return self.__statemachine_State7

    @statemachine_State7.setter
    def statemachine_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State7", None)
        self.__statemachine_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine6"):
                opp_val = getattr(old_value, "statemachine_Statemachine6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Statemachine6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine6"):
                opp_val = getattr(value, "statemachine_Statemachine6", None)
                setattr(value, "statemachine_Statemachine6", self)

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
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statemachine"):
                opp_val = getattr(old_value, "statemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statemachine"):
                opp_val = getattr(value, "statemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State10(self):
        return self.__statemachine_State10

    @statemachine_State10.setter
    def statemachine_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State10", None)
        self.__statemachine_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition9"):
                opp_val = getattr(old_value, "statemachine_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition9"):
                opp_val = getattr(value, "statemachine_Transition9", None)
                setattr(value, "statemachine_Transition9", self)

class statemachine_Statemachine:

    def __init__(self, name: str, statemachine_Statemachine: set["statemachine_State"] = None, statemachine_Statemachine2: set["statemachine_Event"] = None, statemachine_Statemachine4: set["statemachine_Transition"] = None, statemachine_Statemachine6: "statemachine_State" = None):
        self.name = name
        self.statemachine_Statemachine = statemachine_Statemachine if statemachine_Statemachine is not None else set()
        self.statemachine_Statemachine2 = statemachine_Statemachine2 if statemachine_Statemachine2 is not None else set()
        self.statemachine_Statemachine4 = statemachine_Statemachine4 if statemachine_Statemachine4 is not None else set()
        self.statemachine_Statemachine6 = statemachine_Statemachine6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statemachine_Statemachine2(self):
        return self.__statemachine_Statemachine2

    @statemachine_Statemachine2.setter
    def statemachine_Statemachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine2", None)
        self.__statemachine_Statemachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Event"):
                    opp_val = getattr(item, "statemachine_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Event"):
                    opp_val = getattr(item, "statemachine_Event", None)
                    
                    setattr(item, "statemachine_Event", self)
                    

    @property
    def statemachine_Statemachine4(self):
        return self.__statemachine_Statemachine4

    @statemachine_Statemachine4.setter
    def statemachine_Statemachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine4", None)
        self.__statemachine_Statemachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition"):
                    opp_val = getattr(item, "statemachine_Transition", None)
                    
                    setattr(item, "statemachine_Transition", self)
                    

    @property
    def statemachine_Statemachine(self):
        return self.__statemachine_Statemachine

    @statemachine_Statemachine.setter
    def statemachine_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine", None)
        self.__statemachine_Statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State"):
                    opp_val = getattr(item, "statemachine_State", None)
                    
                    setattr(item, "statemachine_State", self)
                    

    @property
    def statemachine_Statemachine6(self):
        return self.__statemachine_Statemachine6

    @statemachine_Statemachine6.setter
    def statemachine_Statemachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine6", None)
        self.__statemachine_Statemachine6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State7"):
                opp_val = getattr(old_value, "statemachine_State7", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State7"):
                opp_val = getattr(value, "statemachine_State7", None)
                setattr(value, "statemachine_State7", self)
