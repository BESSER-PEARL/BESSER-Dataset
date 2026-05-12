from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventContext(Enum):
    CHRONICLE = "CHRONICLE"
    RECENT = "RECENT"
    UNRESTRICTED = "UNRESTRICTED"
    IMMEDIATE = "IMMEDIATE"
    STRICT_IMMEDIATE = "STRICT_IMMEDIATE"


############################################
# Definition of Classes
############################################

class automaton_AtomicEventPattern:

    pass
class automaton_Guard:

    pass
class Transition:

    pass
class automaton_EpsilonTransition(Transition):

    pass
class automaton_TypedTransition(Transition):

    pass
class TimedZone:

    pass
class automaton_HoldsFor(TimedZone):

    pass
class automaton_Within(TimedZone):

    pass
class State:

    pass
class automaton_TrapState(State):

    pass
class automaton_FinalState(State):

    pass
class automaton_InitState(State):

    pass
class automaton_TimedZone(ABC):

    def __init__(self, time: str, automaton_TimedZone19: "automaton_EventToken" = None, automaton_TimedZone: "automaton_Automaton" = None, TimedZone: "automaton_State" = None, TimedZone29: "automaton_State" = None, inStateOf: "automaton_State" = None, outStateOf: "automaton_State" = None):
        self.time = time
        self.automaton_TimedZone19 = automaton_TimedZone19
        self.automaton_TimedZone = automaton_TimedZone
        self.TimedZone = TimedZone
        self.TimedZone29 = TimedZone29
        self.inStateOf = inStateOf
        self.outStateOf = outStateOf
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time


    @property
    def TimedZone(self):
        return self.__TimedZone

    @TimedZone.setter
    def TimedZone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__TimedZone", None)
        self.__TimedZone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inState"):
                opp_val = getattr(old_value, "inState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inState"):
                opp_val = getattr(value, "inState", None)
                if opp_val is None:
                    setattr(value, "inState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inStateOf(self):
        return self.__inStateOf

    @inStateOf.setter
    def inStateOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__inStateOf", None)
        self.__inStateOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State38"):
                opp_val = getattr(old_value, "State38", None)
                if opp_val == self:
                    setattr(old_value, "State38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State38"):
                opp_val = getattr(value, "State38", None)
                setattr(value, "State38", self)

    @property
    def TimedZone29(self):
        return self.__TimedZone29

    @TimedZone29.setter
    def TimedZone29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__TimedZone29", None)
        self.__TimedZone29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outState"):
                opp_val = getattr(old_value, "outState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outState"):
                opp_val = getattr(value, "outState", None)
                if opp_val is None:
                    setattr(value, "outState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automaton_TimedZone(self):
        return self.__automaton_TimedZone

    @automaton_TimedZone.setter
    def automaton_TimedZone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__automaton_TimedZone", None)
        self.__automaton_TimedZone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_Automaton9"):
                opp_val = getattr(old_value, "automaton_Automaton9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Automaton9"):
                opp_val = getattr(value, "automaton_Automaton9", None)
                if opp_val is None:
                    setattr(value, "automaton_Automaton9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automaton_TimedZone19(self):
        return self.__automaton_TimedZone19

    @automaton_TimedZone19.setter
    def automaton_TimedZone19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__automaton_TimedZone19", None)
        self.__automaton_TimedZone19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_EventToken18"):
                opp_val = getattr(old_value, "automaton_EventToken18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_EventToken18"):
                opp_val = getattr(value, "automaton_EventToken18", None)
                if opp_val is None:
                    setattr(value, "automaton_EventToken18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outStateOf(self):
        return self.__outStateOf

    @outStateOf.setter
    def outStateOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__outStateOf", None)
        self.__outStateOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State40"):
                opp_val = getattr(old_value, "State40", None)
                if opp_val == self:
                    setattr(old_value, "State40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State40"):
                opp_val = getattr(value, "State40", None)
                setattr(value, "State40", self)

class automaton_EventToken:

    pass
class automaton_EventPattern:

    pass
class automaton_State:

    def __init__(self, label: str, State: "automaton_EventToken" = None, postState: set["automaton_Transition"] = None, preState: set["automaton_Transition"] = None, automaton_State: "automaton_Automaton" = None, inState: set["automaton_TimedZone"] = None, outState: set["automaton_TimedZone"] = None, State31: "automaton_Transition" = None, State33: "automaton_Transition" = None, currentState: set["automaton_EventToken"] = None, automaton_State25: "automaton_Event" = None, State38: "automaton_TimedZone" = None, State40: "automaton_TimedZone" = None):
        self.label = label
        self.State = State
        self.postState = postState if postState is not None else set()
        self.preState = preState if preState is not None else set()
        self.automaton_State = automaton_State
        self.inState = inState if inState is not None else set()
        self.outState = outState if outState is not None else set()
        self.State31 = State31
        self.State33 = State33
        self.currentState = currentState if currentState is not None else set()
        self.automaton_State25 = automaton_State25
        self.State38 = State38
        self.State40 = State40
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def automaton_State25(self):
        return self.__automaton_State25

    @automaton_State25.setter
    def automaton_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__automaton_State25", None)
        self.__automaton_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_Event26"):
                opp_val = getattr(old_value, "automaton_Event26", None)
                if opp_val == self:
                    setattr(old_value, "automaton_Event26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Event26"):
                opp_val = getattr(value, "automaton_Event26", None)
                setattr(value, "automaton_Event26", self)

    @property
    def currentState(self):
        return self.__currentState

    @currentState.setter
    def currentState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__currentState", None)
        self.__currentState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventToken"):
                    opp_val = getattr(item, "EventToken", None)
                    
                    if opp_val == self:
                        setattr(item, "EventToken", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventToken"):
                    opp_val = getattr(item, "EventToken", None)
                    
                    setattr(item, "EventToken", self)
                    

    @property
    def preState(self):
        return self.__preState

    @preState.setter
    def preState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__preState", None)
        self.__preState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition22"):
                    opp_val = getattr(item, "Transition22", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition22"):
                    opp_val = getattr(item, "Transition22", None)
                    
                    setattr(item, "Transition22", self)
                    

    @property
    def State31(self):
        return self.__State31

    @State31.setter
    def State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State31", None)
        self.__State31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outTransitions"):
                opp_val = getattr(old_value, "outTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outTransitions"):
                opp_val = getattr(value, "outTransitions", None)
                setattr(value, "outTransitions", self)

    @property
    def inState(self):
        return self.__inState

    @inState.setter
    def inState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__inState", None)
        self.__inState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TimedZone"):
                    opp_val = getattr(item, "TimedZone", None)
                    
                    if opp_val == self:
                        setattr(item, "TimedZone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TimedZone"):
                    opp_val = getattr(item, "TimedZone", None)
                    
                    setattr(item, "TimedZone", self)
                    

    @property
    def automaton_State(self):
        return self.__automaton_State

    @automaton_State.setter
    def automaton_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__automaton_State", None)
        self.__automaton_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_Automaton4"):
                opp_val = getattr(old_value, "automaton_Automaton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Automaton4"):
                opp_val = getattr(value, "automaton_Automaton4", None)
                if opp_val is None:
                    setattr(value, "automaton_Automaton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventTokens"):
                opp_val = getattr(old_value, "eventTokens", None)
                if opp_val == self:
                    setattr(old_value, "eventTokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventTokens"):
                opp_val = getattr(value, "eventTokens", None)
                setattr(value, "eventTokens", self)

    @property
    def State40(self):
        return self.__State40

    @State40.setter
    def State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State40", None)
        self.__State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outStateOf"):
                opp_val = getattr(old_value, "outStateOf", None)
                if opp_val == self:
                    setattr(old_value, "outStateOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outStateOf"):
                opp_val = getattr(value, "outStateOf", None)
                setattr(value, "outStateOf", self)

    @property
    def postState(self):
        return self.__postState

    @postState.setter
    def postState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__postState", None)
        self.__postState = value if value is not None else set()
        
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
    def State38(self):
        return self.__State38

    @State38.setter
    def State38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State38", None)
        self.__State38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inStateOf"):
                opp_val = getattr(old_value, "inStateOf", None)
                if opp_val == self:
                    setattr(old_value, "inStateOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inStateOf"):
                opp_val = getattr(value, "inStateOf", None)
                setattr(value, "inStateOf", self)

    @property
    def State33(self):
        return self.__State33

    @State33.setter
    def State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State33", None)
        self.__State33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTransitions"):
                opp_val = getattr(old_value, "inTransitions", None)
                if opp_val == self:
                    setattr(old_value, "inTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTransitions"):
                opp_val = getattr(value, "inTransitions", None)
                setattr(value, "inTransitions", self)

    @property
    def outState(self):
        return self.__outState

    @outState.setter
    def outState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__outState", None)
        self.__outState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TimedZone29"):
                    opp_val = getattr(item, "TimedZone29", None)
                    
                    if opp_val == self:
                        setattr(item, "TimedZone29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TimedZone29"):
                    opp_val = getattr(item, "TimedZone29", None)
                    
                    setattr(item, "TimedZone29", self)
                    

class automaton_Transition(ABC):

    pass
class automaton_Event:

    pass
class automaton_Automaton:

    pass
class automaton_InternalModel:

    def __init__(self, context: str, automaton_InternalModel: set["automaton_Automaton"] = None, automaton_InternalModel2: "automaton_Event" = None):
        self.context = context
        self.automaton_InternalModel = automaton_InternalModel if automaton_InternalModel is not None else set()
        self.automaton_InternalModel2 = automaton_InternalModel2
        
        pass
    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def automaton_InternalModel(self):
        return self.__automaton_InternalModel

    @automaton_InternalModel.setter
    def automaton_InternalModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_InternalModel__automaton_InternalModel", None)
        self.__automaton_InternalModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaton_Automaton"):
                    opp_val = getattr(item, "automaton_Automaton", None)
                    
                    if opp_val == self:
                        setattr(item, "automaton_Automaton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaton_Automaton"):
                    opp_val = getattr(item, "automaton_Automaton", None)
                    
                    setattr(item, "automaton_Automaton", self)
                    

    @property
    def automaton_InternalModel2(self):
        return self.__automaton_InternalModel2

    @automaton_InternalModel2.setter
    def automaton_InternalModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_InternalModel__automaton_InternalModel2", None)
        self.__automaton_InternalModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_Event"):
                opp_val = getattr(old_value, "automaton_Event", None)
                if opp_val == self:
                    setattr(old_value, "automaton_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Event"):
                opp_val = getattr(value, "automaton_Event", None)
                setattr(value, "automaton_Event", self)
