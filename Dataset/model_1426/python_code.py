from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractEvent:

    pass
class martinfowlerdsl_Event(AbstractEvent):

    def __init__(self, resetting: bool, martinfowlerdsl_Event: "martinfowlerdsl_Transition" = None):
        self.resetting = resetting
        self.martinfowlerdsl_Event = martinfowlerdsl_Event
        
    @property
    def resetting(self) -> bool:
        return self.__resetting

    @resetting.setter
    def resetting(self, resetting: bool):
        self.__resetting = resetting

    @property
    def martinfowlerdsl_Event(self):
        return self.__martinfowlerdsl_Event

    @martinfowlerdsl_Event.setter
    def martinfowlerdsl_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_Event__martinfowlerdsl_Event", None)
        self.__martinfowlerdsl_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "martinfowlerdsl_Transition13"):
                opp_val = getattr(old_value, "martinfowlerdsl_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "martinfowlerdsl_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "martinfowlerdsl_Transition13"):
                opp_val = getattr(value, "martinfowlerdsl_Transition13", None)
                setattr(value, "martinfowlerdsl_Transition13", self)

class martinfowlerdsl_Transition:

    pass
class martinfowlerdsl_State:

    def __init__(self, name: str, martinfowlerdsl_State: "martinfowlerdsl_StateMachine" = None, martinfowlerdsl_State3: "martinfowlerdsl_StateMachine" = None, martinfowlerdsl_State7: set["martinfowlerdsl_Command"] = None, State: "martinfowlerdsl_Transition" = None, martinfowlerdsl_State11: "martinfowlerdsl_Transition" = None, source: set["martinfowlerdsl_Transition"] = None):
        self.name = name
        self.martinfowlerdsl_State = martinfowlerdsl_State
        self.martinfowlerdsl_State3 = martinfowlerdsl_State3
        self.martinfowlerdsl_State7 = martinfowlerdsl_State7 if martinfowlerdsl_State7 is not None else set()
        self.State = State
        self.martinfowlerdsl_State11 = martinfowlerdsl_State11
        self.source = source if source is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_State__source", None)
        self.__source = value if value is not None else set()
        
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
        old_value = getattr(self, f"_martinfowlerdsl_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def martinfowlerdsl_State(self):
        return self.__martinfowlerdsl_State

    @martinfowlerdsl_State.setter
    def martinfowlerdsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_State__martinfowlerdsl_State", None)
        self.__martinfowlerdsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "martinfowlerdsl_StateMachine"):
                opp_val = getattr(old_value, "martinfowlerdsl_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "martinfowlerdsl_StateMachine"):
                opp_val = getattr(value, "martinfowlerdsl_StateMachine", None)
                if opp_val is None:
                    setattr(value, "martinfowlerdsl_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def martinfowlerdsl_State3(self):
        return self.__martinfowlerdsl_State3

    @martinfowlerdsl_State3.setter
    def martinfowlerdsl_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_State__martinfowlerdsl_State3", None)
        self.__martinfowlerdsl_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "martinfowlerdsl_StateMachine2"):
                opp_val = getattr(old_value, "martinfowlerdsl_StateMachine2", None)
                if opp_val == self:
                    setattr(old_value, "martinfowlerdsl_StateMachine2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "martinfowlerdsl_StateMachine2"):
                opp_val = getattr(value, "martinfowlerdsl_StateMachine2", None)
                setattr(value, "martinfowlerdsl_StateMachine2", self)

    @property
    def martinfowlerdsl_State11(self):
        return self.__martinfowlerdsl_State11

    @martinfowlerdsl_State11.setter
    def martinfowlerdsl_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_State__martinfowlerdsl_State11", None)
        self.__martinfowlerdsl_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "martinfowlerdsl_Transition"):
                opp_val = getattr(old_value, "martinfowlerdsl_Transition", None)
                if opp_val == self:
                    setattr(old_value, "martinfowlerdsl_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "martinfowlerdsl_Transition"):
                opp_val = getattr(value, "martinfowlerdsl_Transition", None)
                setattr(value, "martinfowlerdsl_Transition", self)

    @property
    def martinfowlerdsl_State7(self):
        return self.__martinfowlerdsl_State7

    @martinfowlerdsl_State7.setter
    def martinfowlerdsl_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_State__martinfowlerdsl_State7", None)
        self.__martinfowlerdsl_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "martinfowlerdsl_Command"):
                    opp_val = getattr(item, "martinfowlerdsl_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "martinfowlerdsl_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "martinfowlerdsl_Command"):
                    opp_val = getattr(item, "martinfowlerdsl_Command", None)
                    
                    setattr(item, "martinfowlerdsl_Command", self)
                    

class martinfowlerdsl_StateMachine:

    pass
class martinfowlerdsl_Command(AbstractEvent):

    pass
class martinfowlerdsl_AbstractEvent(ABC):

    def __init__(self, name: str, code: str, martinfowlerdsl_AbstractEvent: "martinfowlerdsl_StateMachine" = None):
        self.name = name
        self.code = code
        self.martinfowlerdsl_AbstractEvent = martinfowlerdsl_AbstractEvent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def martinfowlerdsl_AbstractEvent(self):
        return self.__martinfowlerdsl_AbstractEvent

    @martinfowlerdsl_AbstractEvent.setter
    def martinfowlerdsl_AbstractEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_martinfowlerdsl_AbstractEvent__martinfowlerdsl_AbstractEvent", None)
        self.__martinfowlerdsl_AbstractEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "martinfowlerdsl_StateMachine5"):
                opp_val = getattr(old_value, "martinfowlerdsl_StateMachine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "martinfowlerdsl_StateMachine5"):
                opp_val = getattr(value, "martinfowlerdsl_StateMachine5", None)
                if opp_val is None:
                    setattr(value, "martinfowlerdsl_StateMachine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
