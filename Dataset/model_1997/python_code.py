from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model2_trace_A:

    pass
class trace_model2_TracedA:

    pass
class trace_model2Configuration_TracedC:

    pass
class trace_model2Configuration_TracedB:

    pass
class trace_Traced_TracedObjects:

    pass
class trace_States_A_a_State:

    def __init__(self, a: int, model2: "model2_TracedA" = None, a_a_States: set["States_trace_GlobalState"] = None):
        self.a = a
        self.model2 = model2
        self.a_a_States = a_a_States if a_a_States is not None else set()
        
    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

    @property
    def model2(self):
        return self.__model2

    @model2.setter
    def model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_A_a_State__model2", None)
        self.__model2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced45"):
                opp_val = getattr(old_value, "Traced45", None)
                if opp_val == self:
                    setattr(old_value, "Traced45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced45"):
                opp_val = getattr(value, "Traced45", None)
                setattr(value, "Traced45", self)

    @property
    def a_a_States(self):
        return self.__a_a_States

    @a_a_States.setter
    def a_a_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_A_a_State__a_a_States", None)
        self.__a_a_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState47"):
                    opp_val = getattr(item, "GlobalState47", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState47"):
                    opp_val = getattr(item, "GlobalState47", None)
                    
                    setattr(item, "GlobalState47", self)
                    

class States_trace_F:

    pass
class trace_States_C_c_State:

    pass
class States_trace_GlobalState:

    pass
class trace_States_B_b_State:

    def __init__(self, b: int, model2Configuration: "model2Configuration_TracedB" = None, b_b_States: set["States_trace_GlobalState"] = None):
        self.b = b
        self.model2Configuration = model2Configuration
        self.b_b_States = b_b_States if b_b_States is not None else set()
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def model2Configuration(self):
        return self.__model2Configuration

    @model2Configuration.setter
    def model2Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_B_b_State__model2Configuration", None)
        self.__model2Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced"):
                opp_val = getattr(old_value, "Traced", None)
                if opp_val == self:
                    setattr(old_value, "Traced", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced"):
                opp_val = getattr(value, "Traced", None)
                setattr(value, "Traced", self)

    @property
    def b_b_States(self):
        return self.__b_b_States

    @b_b_States.setter
    def b_b_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_B_b_State__b_b_States", None)
        self.__b_b_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState37"):
                    opp_val = getattr(item, "GlobalState37", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState37"):
                    opp_val = getattr(item, "GlobalState37", None)
                    
                    setattr(item, "GlobalState37", self)
                    

class model2Configuration_TracedB:

    pass
class model2Configuration_TracedC:

    pass
class model2_TracedA:

    pass
class C_doCExitEventOccurrence:

    pass
class C_doCEntryEventOccurrence:

    pass
class A_doAExitEventOccurrence:

    pass
class A_doAEntryEventOccurrence:

    pass
class trace_Events_Events:

    pass
class Events_trace_GlobalState:

    pass
class trace_Events_EventOccurrence(ABC):

    pass
class trace_F:

    pass
class C_c_State:

    pass
class B_b_State:

    pass
class EventOccurrence:

    pass
class trace_Events_A_doAEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_A_doAExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_C_doCEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_C_doCExitEventOccurrence(EventOccurrence):

    pass
class trace_StaticObjectsPools:

    pass
class TracedObjects:

    pass
class Events:

    pass
class trace_GlobalState:

    pass
class trace_Trace:

    pass
class A_a_State:

    pass