from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class trace_GlobalState:

    pass
class trace_Trace:

    pass
class trace_Traced_TracedObjects:

    pass
class trace_States_A_a_State:

    def __init__(self, a: int, aTrace: "model2_TracedA" = None, a_a_States: set["States_trace_GlobalState"] = None):
        self.a = a
        self.aTrace = aTrace
        self.a_a_States = a_a_States if a_a_States is not None else set()
        
        pass
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a


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
                if hasattr(item, "GlobalState43"):
                    opp_val = getattr(item, "GlobalState43", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState43"):
                    opp_val = getattr(item, "GlobalState43", None)
                    
                    setattr(item, "GlobalState43", self)
                    

    @property
    def aTrace(self):
        return self.__aTrace

    @aTrace.setter
    def aTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_A_a_State__aTrace", None)
        self.__aTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedA"):
                opp_val = getattr(old_value, "TracedA", None)
                if opp_val == self:
                    setattr(old_value, "TracedA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedA"):
                opp_val = getattr(value, "TracedA", None)
                setattr(value, "TracedA", self)

class model2_trace_A:

    pass
class trace_model2_TracedA:

    pass
class trace_model2Configuration_TracedC:

    pass
class trace_model2Configuration_TracedB:

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
class States_trace_F:

    pass
class trace_States_C_c_State:

    pass
class States_trace_GlobalState:

    pass
class trace_States_B_b_State:

    def __init__(self, b: int, bTrace: "model2Configuration_TracedB" = None, b_b_States: set["States_trace_GlobalState"] = None):
        self.b = b
        self.bTrace = bTrace
        self.b_b_States = b_b_States if b_b_States is not None else set()
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b


    @property
    def bTrace(self):
        return self.__bTrace

    @bTrace.setter
    def bTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_B_b_State__bTrace", None)
        self.__bTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedB"):
                opp_val = getattr(old_value, "TracedB", None)
                if opp_val == self:
                    setattr(old_value, "TracedB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedB"):
                opp_val = getattr(value, "TracedB", None)
                setattr(value, "TracedB", self)

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
                if hasattr(item, "GlobalState36"):
                    opp_val = getattr(item, "GlobalState36", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState36"):
                    opp_val = getattr(item, "GlobalState36", None)
                    
                    setattr(item, "GlobalState36", self)
                    

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
class A_a_State:

    pass
class C_c_State:

    pass
class B_b_State:

    pass
class EventOccurrence:

    pass
class trace_Events_C_doCEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_A_doAExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_C_doCExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_A_doAEntryEventOccurrence(EventOccurrence):

    pass
class trace_StaticObjectsPools:

    pass
class TracedObjects:

    pass
class Events:

    pass