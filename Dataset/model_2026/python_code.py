from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeOfChannel(Enum):
    Synchronous = "Synchronous"
    Asynchronous = "Asynchronous"
class Event(Enum):
    SEND = "SEND"
    RECEIVE = "RECEIVE"


############################################
# Definition of Classes
############################################

class amf_Transition:

    def __init__(self, event: str, amf_Transition11: "amf_State" = None, amf_Transition14: "amf_Channel" = None, amf_Transition: "amf_Statemachine" = None, amf_Transition17: "amf_State" = None):
        self.event = event
        self.amf_Transition11 = amf_Transition11
        self.amf_Transition14 = amf_Transition14
        self.amf_Transition = amf_Transition
        self.amf_Transition17 = amf_Transition17
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def amf_Transition17(self):
        return self.__amf_Transition17

    @amf_Transition17.setter
    def amf_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Transition__amf_Transition17", None)
        self.__amf_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_State18"):
                opp_val = getattr(old_value, "amf_State18", None)
                if opp_val == self:
                    setattr(old_value, "amf_State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_State18"):
                opp_val = getattr(value, "amf_State18", None)
                setattr(value, "amf_State18", self)

    @property
    def amf_Transition(self):
        return self.__amf_Transition

    @amf_Transition.setter
    def amf_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Transition__amf_Transition", None)
        self.__amf_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Statemachine9"):
                opp_val = getattr(old_value, "amf_Statemachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Statemachine9"):
                opp_val = getattr(value, "amf_Statemachine9", None)
                if opp_val is None:
                    setattr(value, "amf_Statemachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amf_Transition14(self):
        return self.__amf_Transition14

    @amf_Transition14.setter
    def amf_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Transition__amf_Transition14", None)
        self.__amf_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Channel15"):
                opp_val = getattr(old_value, "amf_Channel15", None)
                if opp_val == self:
                    setattr(old_value, "amf_Channel15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Channel15"):
                opp_val = getattr(value, "amf_Channel15", None)
                setattr(value, "amf_Channel15", self)

    @property
    def amf_Transition11(self):
        return self.__amf_Transition11

    @amf_Transition11.setter
    def amf_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Transition__amf_Transition11", None)
        self.__amf_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_State12"):
                opp_val = getattr(old_value, "amf_State12", None)
                if opp_val == self:
                    setattr(old_value, "amf_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_State12"):
                opp_val = getattr(value, "amf_State12", None)
                setattr(value, "amf_State12", self)

class amf_State:

    def __init__(self, name: str, amf_State12: "amf_Transition" = None, amf_State: "amf_Statemachine" = None, amf_State7: "amf_Statemachine" = None, amf_State18: "amf_Transition" = None):
        self.name = name
        self.amf_State12 = amf_State12
        self.amf_State = amf_State
        self.amf_State7 = amf_State7
        self.amf_State18 = amf_State18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amf_State7(self):
        return self.__amf_State7

    @amf_State7.setter
    def amf_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_State__amf_State7", None)
        self.__amf_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Statemachine6"):
                opp_val = getattr(old_value, "amf_Statemachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Statemachine6"):
                opp_val = getattr(value, "amf_Statemachine6", None)
                if opp_val is None:
                    setattr(value, "amf_Statemachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amf_State12(self):
        return self.__amf_State12

    @amf_State12.setter
    def amf_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_State__amf_State12", None)
        self.__amf_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Transition11"):
                opp_val = getattr(old_value, "amf_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "amf_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Transition11"):
                opp_val = getattr(value, "amf_Transition11", None)
                setattr(value, "amf_Transition11", self)

    @property
    def amf_State18(self):
        return self.__amf_State18

    @amf_State18.setter
    def amf_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_State__amf_State18", None)
        self.__amf_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Transition17"):
                opp_val = getattr(old_value, "amf_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "amf_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Transition17"):
                opp_val = getattr(value, "amf_Transition17", None)
                setattr(value, "amf_Transition17", self)

    @property
    def amf_State(self):
        return self.__amf_State

    @amf_State.setter
    def amf_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_State__amf_State", None)
        self.__amf_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Statemachine4"):
                opp_val = getattr(old_value, "amf_Statemachine4", None)
                if opp_val == self:
                    setattr(old_value, "amf_Statemachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Statemachine4"):
                opp_val = getattr(value, "amf_Statemachine4", None)
                setattr(value, "amf_Statemachine4", self)

class amf_Statemachine:

    def __init__(self, name: str, amf_Statemachine: "amf_Network" = None, amf_Statemachine4: "amf_State" = None, amf_Statemachine6: set["amf_State"] = None, amf_Statemachine9: set["amf_Transition"] = None):
        self.name = name
        self.amf_Statemachine = amf_Statemachine
        self.amf_Statemachine4 = amf_Statemachine4
        self.amf_Statemachine6 = amf_Statemachine6 if amf_Statemachine6 is not None else set()
        self.amf_Statemachine9 = amf_Statemachine9 if amf_Statemachine9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amf_Statemachine6(self):
        return self.__amf_Statemachine6

    @amf_Statemachine6.setter
    def amf_Statemachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Statemachine__amf_Statemachine6", None)
        self.__amf_Statemachine6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amf_State7"):
                    opp_val = getattr(item, "amf_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "amf_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amf_State7"):
                    opp_val = getattr(item, "amf_State7", None)
                    
                    setattr(item, "amf_State7", self)
                    

    @property
    def amf_Statemachine(self):
        return self.__amf_Statemachine

    @amf_Statemachine.setter
    def amf_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Statemachine__amf_Statemachine", None)
        self.__amf_Statemachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Network2"):
                opp_val = getattr(old_value, "amf_Network2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Network2"):
                opp_val = getattr(value, "amf_Network2", None)
                if opp_val is None:
                    setattr(value, "amf_Network2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amf_Statemachine4(self):
        return self.__amf_Statemachine4

    @amf_Statemachine4.setter
    def amf_Statemachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Statemachine__amf_Statemachine4", None)
        self.__amf_Statemachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_State"):
                opp_val = getattr(old_value, "amf_State", None)
                if opp_val == self:
                    setattr(old_value, "amf_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_State"):
                opp_val = getattr(value, "amf_State", None)
                setattr(value, "amf_State", self)

    @property
    def amf_Statemachine9(self):
        return self.__amf_Statemachine9

    @amf_Statemachine9.setter
    def amf_Statemachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Statemachine__amf_Statemachine9", None)
        self.__amf_Statemachine9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amf_Transition"):
                    opp_val = getattr(item, "amf_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "amf_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amf_Transition"):
                    opp_val = getattr(item, "amf_Transition", None)
                    
                    setattr(item, "amf_Transition", self)
                    

class amf_Channel:

    def __init__(self, Type: str, name: str, amf_Channel: "amf_Network" = None, amf_Channel15: "amf_Transition" = None):
        self.Type = Type
        self.name = name
        self.amf_Channel = amf_Channel
        self.amf_Channel15 = amf_Channel15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def amf_Channel15(self):
        return self.__amf_Channel15

    @amf_Channel15.setter
    def amf_Channel15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Channel__amf_Channel15", None)
        self.__amf_Channel15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Transition14"):
                opp_val = getattr(old_value, "amf_Transition14", None)
                if opp_val == self:
                    setattr(old_value, "amf_Transition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Transition14"):
                opp_val = getattr(value, "amf_Transition14", None)
                setattr(value, "amf_Transition14", self)

    @property
    def amf_Channel(self):
        return self.__amf_Channel

    @amf_Channel.setter
    def amf_Channel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Channel__amf_Channel", None)
        self.__amf_Channel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amf_Network"):
                opp_val = getattr(old_value, "amf_Network", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amf_Network"):
                opp_val = getattr(value, "amf_Network", None)
                if opp_val is None:
                    setattr(value, "amf_Network", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class amf_Network:

    def __init__(self, name: str, amf_Network: set["amf_Channel"] = None, amf_Network2: set["amf_Statemachine"] = None):
        self.name = name
        self.amf_Network = amf_Network if amf_Network is not None else set()
        self.amf_Network2 = amf_Network2 if amf_Network2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amf_Network(self):
        return self.__amf_Network

    @amf_Network.setter
    def amf_Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Network__amf_Network", None)
        self.__amf_Network = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amf_Channel"):
                    opp_val = getattr(item, "amf_Channel", None)
                    
                    if opp_val == self:
                        setattr(item, "amf_Channel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amf_Channel"):
                    opp_val = getattr(item, "amf_Channel", None)
                    
                    setattr(item, "amf_Channel", self)
                    

    @property
    def amf_Network2(self):
        return self.__amf_Network2

    @amf_Network2.setter
    def amf_Network2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amf_Network__amf_Network2", None)
        self.__amf_Network2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "amf_Statemachine"):
                    opp_val = getattr(item, "amf_Statemachine", None)
                    
                    if opp_val == self:
                        setattr(item, "amf_Statemachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "amf_Statemachine"):
                    opp_val = getattr(item, "amf_Statemachine", None)
                    
                    setattr(item, "amf_Statemachine", self)
                    
