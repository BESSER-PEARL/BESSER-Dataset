from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_trace_Place:

    pass
class trace_petrinet_TracedPlace:

    def __init__(self, initialTokens: int, name: str, trace_petrinet_TracedPlace: "petrinet_trace_Place" = None, parent: set["Place_tokens_State"] = None):
        self.initialTokens = initialTokens
        self.name = name
        self.trace_petrinet_TracedPlace = trace_petrinet_TracedPlace
        self.parent = parent if parent is not None else set()
        
        pass
    @property
    def initialTokens(self):
        return self.__initialTokens

    @initialTokens.setter
    def initialTokens(self, initialTokens: int):
        self.__initialTokens = initialTokens


    @property
    def name(self):
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_petrinet_TracedPlace__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place_tokens_State67"):
                    opp_val = getattr(item, "Place_tokens_State67", None)
                    
                    if opp_val == self:
                        setattr(item, "Place_tokens_State67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place_tokens_State67"):
                    opp_val = getattr(item, "Place_tokens_State67", None)
                    
                    setattr(item, "Place_tokens_State67", self)
                    

class trace_Traced_TracedObjects:

    pass
class States_trace_GlobalState:

    pass
class trace_States_Place_tokens_State:

    def __init__(self, tokens: int, place_tokens_States: set["States_trace_GlobalState"] = None, tokensTrace: "petrinet_TracedPlace" = None):
        self.tokens = tokens
        self.place_tokens_States = place_tokens_States if place_tokens_States is not None else set()
        self.tokensTrace = tokensTrace
        
        pass
    @property
    def tokens(self):
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens


    @property
    def tokensTrace(self):
        return self.__tokensTrace

    @tokensTrace.setter
    def tokensTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_Place_tokens_State__tokensTrace", None)
        self.__tokensTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedPlace"):
                opp_val = getattr(old_value, "TracedPlace", None)
                if opp_val == self:
                    setattr(old_value, "TracedPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedPlace"):
                opp_val = getattr(value, "TracedPlace", None)
                setattr(value, "TracedPlace", self)

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
                if hasattr(item, "GlobalState62"):
                    opp_val = getattr(item, "GlobalState62", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState62"):
                    opp_val = getattr(item, "GlobalState62", None)
                    
                    setattr(item, "GlobalState62", self)
                    

class Events_trace_EObject:

    pass
class Events_trace_Transition:

    pass
class petrinet_TracedPlace:

    pass
class Events_trace_Net:

    pass
class Transition_fireExitEventOccurrence:

    pass
class Transition_fireEntryEventOccurrence:

    pass
class Transition_isEnabledExitEventOccurrence:

    pass
class Transition_isEnabledEntryEventOccurrence:

    pass
class Place_removeTokenExitEventOccurrence:

    pass
class Place_removeTokenEntryEventOccurrence:

    pass
class Place_addTokenExitEventOccurrence:

    pass
class Place_addTokenEntryEventOccurrence:

    pass
class Net_runExitEventOccurrence:

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
class Place_tokens_State:

    pass
class EventOccurrence:

    pass
class trace_Events_Net_runExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_isEnabledExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_fireExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_removeTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_removeTokenEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_mainExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_fireEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_mainEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_addTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Net_runEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Place_addTokenEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Transition_isEnabledEntryEventOccurrence(EventOccurrence):

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