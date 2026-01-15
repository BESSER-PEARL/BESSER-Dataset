from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class trace_petrinet_TracedPlace:

    def __init__(self, initialTokens: int, name: str, trace_petrinet_TracedPlace: "petrinet_trace_Place" = None, Place_tokens_State68: set["Place_tokens_State"] = None):
        self.initialTokens = initialTokens
        self.name = name
        self.trace_petrinet_TracedPlace = trace_petrinet_TracedPlace
        self.Place_tokens_State68 = Place_tokens_State68 if Place_tokens_State68 is not None else set()
        
    @property
    def initialTokens(self) -> int:
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trace_petrinet_TracedPlace(self):
        return self.__trace_petrinet_TracedPlace

    @trace_petrinet_TracedPlace.setter
    def trace_petrinet_TracedPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_petrinet_TracedPlace__trace_petrinet_TracedPlace", None)
        self.__trace_petrinet_TracedPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_trace_Place"):
                opp_val = getattr(old_value, "petrinet_trace_Place", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_trace_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_trace_Place"):
                opp_val = getattr(value, "petrinet_trace_Place", None)
                setattr(value, "petrinet_trace_Place", self)

    @property
    def Place_tokens_State68(self):
        return self.__Place_tokens_State68

    @Place_tokens_State68.setter
    def Place_tokens_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_petrinet_TracedPlace__Place_tokens_State68", None)
        self.__Place_tokens_State68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "States69"):
                    opp_val = getattr(item, "States69", None)
                    
                    if opp_val == self:
                        setattr(item, "States69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "States69"):
                    opp_val = getattr(item, "States69", None)
                    
                    setattr(item, "States69", self)
                    

class trace_Traced_TracedObjects:

    pass
class States_trace_GlobalState:

    pass
class petrinet_trace_Place:

    pass
class Events_trace_EObject:

    pass
class Events_trace_Transition:

    pass
class trace_States_Place_tokens_State:

    def __init__(self, tokens: int, petrinet: "petrinet_TracedPlace" = None, place_tokens_States: set["States_trace_GlobalState"] = None):
        self.tokens = tokens
        self.petrinet = petrinet
        self.place_tokens_States = place_tokens_States if place_tokens_States is not None else set()
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def place_tokens_States(self):
        return self.__place_tokens_States

    @place_tokens_States.setter
    def place_tokens_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_Place_tokens_State__place_tokens_States", None)
        self.__place_tokens_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState63"):
                    opp_val = getattr(item, "GlobalState63", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState63"):
                    opp_val = getattr(item, "GlobalState63", None)
                    
                    setattr(item, "GlobalState63", self)
                    

    @property
    def petrinet(self):
        return self.__petrinet

    @petrinet.setter
    def petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_Place_tokens_State__petrinet", None)
        self.__petrinet = value
        
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

class petrinet_TracedPlace:

    pass
class Transition_isEnabledExitEventOccurrence:

    pass
class Transition_isEnabledEntryEventOccurrence:

    pass
class Place_removeTokenExitEventOccurrence:

    pass
class Place_removeTokenEntryEventOccurrence:

    pass
class Events_trace_Net:

    pass
class Transition_fireExitEventOccurrence:

    pass
class Transition_fireEntryEventOccurrence:

    pass
class Net_runEntryEventOccurrence:

    pass
class Net_mainExitEventOccurrence:

    pass
class Net_mainEntryEventOccurrence:

    pass
class trace_Events_Events:

    pass
class Events_trace_GlobalState:

    pass
class trace_Events_EventOccurrence(ABC):

    pass
class trace_Net:

    pass
class trace_Transition:

    pass
class Place_addTokenExitEventOccurrence:

    pass
class Place_addTokenEntryEventOccurrence:

    pass
class Place_tokens_State:

    pass
class Net_runExitEventOccurrence:

    pass
class EventOccurrence:

    pass
class trace_Events_Place_removeTokenEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_isEnabledEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_removeTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_runEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_runExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_mainExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_mainEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_fireExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_fireEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_isEnabledExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_addTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_addTokenEntryEventOccurrence(EventOccurrence):

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