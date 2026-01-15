from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimeUnit(Enum):
    NANOSECONDS = "NANOSECONDS"
    MICROSECONDS = "MICROSECONDS"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"


############################################
# Definition of Classes
############################################

class MRPTrace_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class MRPTrace_RDMElement:

    pass
class MRPTrace_TraceEntry:

    def __init__(self, description: str, MRPTrace_TraceEntry: "MRPTrace_Trace" = None, MRPTrace_TraceEntry5: "MRPTrace_TraceEntry" = None, MRPTrace_TraceEntry3: "MRPTrace_TraceEntry" = None, MRPTrace_TraceEntry7: set["MRPTrace_RDMElement"] = None, MRPTrace_TraceEntry9: "MRPTrace_Event" = None):
        self.description = description
        self.MRPTrace_TraceEntry = MRPTrace_TraceEntry
        self.MRPTrace_TraceEntry5 = MRPTrace_TraceEntry5
        self.MRPTrace_TraceEntry3 = MRPTrace_TraceEntry3
        self.MRPTrace_TraceEntry7 = MRPTrace_TraceEntry7 if MRPTrace_TraceEntry7 is not None else set()
        self.MRPTrace_TraceEntry9 = MRPTrace_TraceEntry9
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def MRPTrace_TraceEntry3(self):
        return self.__MRPTrace_TraceEntry3

    @MRPTrace_TraceEntry3.setter
    def MRPTrace_TraceEntry3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_TraceEntry__MRPTrace_TraceEntry3", None)
        self.__MRPTrace_TraceEntry3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_TraceEntry5"):
                opp_val = getattr(old_value, "MRPTrace_TraceEntry5", None)
                if opp_val == self:
                    setattr(old_value, "MRPTrace_TraceEntry5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_TraceEntry5"):
                opp_val = getattr(value, "MRPTrace_TraceEntry5", None)
                setattr(value, "MRPTrace_TraceEntry5", self)

    @property
    def MRPTrace_TraceEntry5(self):
        return self.__MRPTrace_TraceEntry5

    @MRPTrace_TraceEntry5.setter
    def MRPTrace_TraceEntry5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_TraceEntry__MRPTrace_TraceEntry5", None)
        self.__MRPTrace_TraceEntry5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_TraceEntry3"):
                opp_val = getattr(old_value, "MRPTrace_TraceEntry3", None)
                if opp_val == self:
                    setattr(old_value, "MRPTrace_TraceEntry3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_TraceEntry3"):
                opp_val = getattr(value, "MRPTrace_TraceEntry3", None)
                setattr(value, "MRPTrace_TraceEntry3", self)

    @property
    def MRPTrace_TraceEntry9(self):
        return self.__MRPTrace_TraceEntry9

    @MRPTrace_TraceEntry9.setter
    def MRPTrace_TraceEntry9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_TraceEntry__MRPTrace_TraceEntry9", None)
        self.__MRPTrace_TraceEntry9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_Event"):
                opp_val = getattr(old_value, "MRPTrace_Event", None)
                if opp_val == self:
                    setattr(old_value, "MRPTrace_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_Event"):
                opp_val = getattr(value, "MRPTrace_Event", None)
                setattr(value, "MRPTrace_Event", self)

    @property
    def MRPTrace_TraceEntry7(self):
        return self.__MRPTrace_TraceEntry7

    @MRPTrace_TraceEntry7.setter
    def MRPTrace_TraceEntry7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_TraceEntry__MRPTrace_TraceEntry7", None)
        self.__MRPTrace_TraceEntry7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MRPTrace_RDMElement"):
                    opp_val = getattr(item, "MRPTrace_RDMElement", None)
                    
                    if opp_val == self:
                        setattr(item, "MRPTrace_RDMElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MRPTrace_RDMElement"):
                    opp_val = getattr(item, "MRPTrace_RDMElement", None)
                    
                    setattr(item, "MRPTrace_RDMElement", self)
                    

    @property
    def MRPTrace_TraceEntry(self):
        return self.__MRPTrace_TraceEntry

    @MRPTrace_TraceEntry.setter
    def MRPTrace_TraceEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_TraceEntry__MRPTrace_TraceEntry", None)
        self.__MRPTrace_TraceEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_Trace2"):
                opp_val = getattr(old_value, "MRPTrace_Trace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_Trace2"):
                opp_val = getattr(value, "MRPTrace_Trace2", None)
                if opp_val is None:
                    setattr(value, "MRPTrace_Trace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class MRPTrace_Event(NamedElement):

    def __init__(self, time: str, MRPTrace_Event: "MRPTrace_TraceEntry" = None):
        self.time = time
        self.MRPTrace_Event = MRPTrace_Event
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def MRPTrace_Event(self):
        return self.__MRPTrace_Event

    @MRPTrace_Event.setter
    def MRPTrace_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_Event__MRPTrace_Event", None)
        self.__MRPTrace_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_TraceEntry9"):
                opp_val = getattr(old_value, "MRPTrace_TraceEntry9", None)
                if opp_val == self:
                    setattr(old_value, "MRPTrace_TraceEntry9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_TraceEntry9"):
                opp_val = getattr(value, "MRPTrace_TraceEntry9", None)
                setattr(value, "MRPTrace_TraceEntry9", self)

class MRPTrace_Trace(NamedElement):

    def __init__(self, granularity: str, MRPTrace_Trace: "MRPTrace_TraceModel" = None, MRPTrace_Trace2: set["MRPTrace_TraceEntry"] = None):
        self.granularity = granularity
        self.MRPTrace_Trace = MRPTrace_Trace
        self.MRPTrace_Trace2 = MRPTrace_Trace2 if MRPTrace_Trace2 is not None else set()
        
    @property
    def granularity(self) -> str:
        return self.__granularity

    @granularity.setter
    def granularity(self, granularity: str):
        self.__granularity = granularity

    @property
    def MRPTrace_Trace2(self):
        return self.__MRPTrace_Trace2

    @MRPTrace_Trace2.setter
    def MRPTrace_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_Trace__MRPTrace_Trace2", None)
        self.__MRPTrace_Trace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MRPTrace_TraceEntry"):
                    opp_val = getattr(item, "MRPTrace_TraceEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "MRPTrace_TraceEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MRPTrace_TraceEntry"):
                    opp_val = getattr(item, "MRPTrace_TraceEntry", None)
                    
                    setattr(item, "MRPTrace_TraceEntry", self)
                    

    @property
    def MRPTrace_Trace(self):
        return self.__MRPTrace_Trace

    @MRPTrace_Trace.setter
    def MRPTrace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MRPTrace_Trace__MRPTrace_Trace", None)
        self.__MRPTrace_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MRPTrace_TraceModel"):
                opp_val = getattr(old_value, "MRPTrace_TraceModel", None)
                if opp_val == self:
                    setattr(old_value, "MRPTrace_TraceModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MRPTrace_TraceModel"):
                opp_val = getattr(value, "MRPTrace_TraceModel", None)
                setattr(value, "MRPTrace_TraceModel", self)

class MRPTrace_TraceModel:

    pass