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

class automaton_ParameterBinding:

    def __init__(self, symbolicName: str, value: str, ParameterBinding: "automaton_ParameterTable" = None, parameterBindings: "automaton_ParameterTable" = None):
        self.symbolicName = symbolicName
        self.value = value
        self.ParameterBinding = ParameterBinding
        self.parameterBindings = parameterBindings
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def symbolicName(self):
        return self.__symbolicName

    @symbolicName.setter
    def symbolicName(self, symbolicName: str):
        self.__symbolicName = symbolicName


    @property
    def ParameterBinding(self):
        return self.__ParameterBinding

    @ParameterBinding.setter
    def ParameterBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_ParameterBinding__ParameterBinding", None)
        self.__ParameterBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterTable"):
                opp_val = getattr(old_value, "parameterTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterTable"):
                opp_val = getattr(value, "parameterTable", None)
                if opp_val is None:
                    setattr(value, "parameterTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameterBindings(self):
        return self.__parameterBindings

    @parameterBindings.setter
    def parameterBindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_ParameterBinding__parameterBindings", None)
        self.__parameterBindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParameterTable62"):
                opp_val = getattr(old_value, "ParameterTable62", None)
                if opp_val == self:
                    setattr(old_value, "ParameterTable62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParameterTable62"):
                opp_val = getattr(value, "ParameterTable62", None)
                setattr(value, "ParameterTable62", self)

class TimedZone:

    pass
class automaton_HoldsFor(TimedZone):

    pass
class automaton_Within(TimedZone):

    pass
class automaton_EventPattern:

    pass
class TypedTransition:

    pass
class automaton_NegativeTransition(TypedTransition):

    pass
class automaton_Parameter:

    def __init__(self, position: int, symbolicName: str, Parameter: "automaton_TypedTransition" = None, parameters: "automaton_TypedTransition" = None):
        self.position = position
        self.symbolicName = symbolicName
        self.Parameter = Parameter
        self.parameters = parameters
        
        pass
    @property
    def symbolicName(self):
        return self.__symbolicName

    @symbolicName.setter
    def symbolicName(self, symbolicName: str):
        self.__symbolicName = symbolicName


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position


    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition48"):
                opp_val = getattr(old_value, "transition48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition48"):
                opp_val = getattr(value, "transition48", None)
                if opp_val is None:
                    setattr(value, "transition48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedTransition56"):
                opp_val = getattr(old_value, "TypedTransition56", None)
                if opp_val == self:
                    setattr(old_value, "TypedTransition56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedTransition56"):
                opp_val = getattr(value, "TypedTransition56", None)
                setattr(value, "TypedTransition56", self)

class automaton_Guard:

    pass
class Transition:

    pass
class automaton_EpsilonTransition(Transition):

    pass
class automaton_TypedTransition(Transition):

    pass
class automaton_Transition(ABC):

    pass
class State:

    pass
class automaton_ParameterTable:

    pass
class automaton_TrapState(State):

    pass
class automaton_FinalState(State):

    pass
class automaton_InitState(State):

    pass
class automaton_State:

    def __init__(self, label: str, automaton_State: "automaton_Automaton" = None, State: "automaton_EventToken" = None, preState: set["automaton_Transition"] = None, currentState: set["automaton_EventToken"] = None, automaton_State37: "automaton_Event" = None, inState: set["automaton_TimedZone"] = None, outState: set["automaton_TimedZone"] = None, postState: set["automaton_Transition"] = None, State45: "automaton_Transition" = None, State43: "automaton_Transition" = None, State52: "automaton_TimedZone" = None, State54: "automaton_TimedZone" = None):
        self.label = label
        self.automaton_State = automaton_State
        self.State = State
        self.preState = preState if preState is not None else set()
        self.currentState = currentState if currentState is not None else set()
        self.automaton_State37 = automaton_State37
        self.inState = inState if inState is not None else set()
        self.outState = outState if outState is not None else set()
        self.postState = postState if postState is not None else set()
        self.State45 = State45
        self.State43 = State43
        self.State52 = State52
        self.State54 = State54
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


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
                if hasattr(item, "TimedZone41"):
                    opp_val = getattr(item, "TimedZone41", None)
                    
                    if opp_val == self:
                        setattr(item, "TimedZone41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TimedZone41"):
                    opp_val = getattr(item, "TimedZone41", None)
                    
                    setattr(item, "TimedZone41", self)
                    

    @property
    def State54(self):
        return self.__State54

    @State54.setter
    def State54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State54", None)
        self.__State54 = value
        
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
    def State45(self):
        return self.__State45

    @State45.setter
    def State45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State45", None)
        self.__State45 = value
        
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
    def State52(self):
        return self.__State52

    @State52.setter
    def State52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State52", None)
        self.__State52 = value
        
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
    def State43(self):
        return self.__State43

    @State43.setter
    def State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__State43", None)
        self.__State43 = value
        
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
                if hasattr(item, "Transition34"):
                    opp_val = getattr(item, "Transition34", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition34"):
                    opp_val = getattr(item, "Transition34", None)
                    
                    setattr(item, "Transition34", self)
                    

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
    def automaton_State37(self):
        return self.__automaton_State37

    @automaton_State37.setter
    def automaton_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_State__automaton_State37", None)
        self.__automaton_State37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_Event38"):
                opp_val = getattr(old_value, "automaton_Event38", None)
                if opp_val == self:
                    setattr(old_value, "automaton_Event38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Event38"):
                opp_val = getattr(value, "automaton_Event38", None)
                setattr(value, "automaton_Event38", self)

class automaton_EventToken:

    pass
class automaton_Event:

    pass
class automaton_TimedZone(ABC):

    def __init__(self, time: str, automaton_TimedZone: "automaton_Automaton" = None, automaton_TimedZone30: "automaton_EventToken" = None, TimedZone: "automaton_State" = None, TimedZone41: "automaton_State" = None, inStateOf: "automaton_State" = None, outStateOf: "automaton_State" = None):
        self.time = time
        self.automaton_TimedZone = automaton_TimedZone
        self.automaton_TimedZone30 = automaton_TimedZone30
        self.TimedZone = TimedZone
        self.TimedZone41 = TimedZone41
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
    def outStateOf(self):
        return self.__outStateOf

    @outStateOf.setter
    def outStateOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__outStateOf", None)
        self.__outStateOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State54"):
                opp_val = getattr(old_value, "State54", None)
                if opp_val == self:
                    setattr(old_value, "State54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State54"):
                opp_val = getattr(value, "State54", None)
                setattr(value, "State54", self)

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
            if hasattr(old_value, "automaton_Automaton14"):
                opp_val = getattr(old_value, "automaton_Automaton14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_Automaton14"):
                opp_val = getattr(value, "automaton_Automaton14", None)
                if opp_val is None:
                    setattr(value, "automaton_Automaton14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automaton_TimedZone30(self):
        return self.__automaton_TimedZone30

    @automaton_TimedZone30.setter
    def automaton_TimedZone30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__automaton_TimedZone30", None)
        self.__automaton_TimedZone30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_EventToken29"):
                opp_val = getattr(old_value, "automaton_EventToken29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_EventToken29"):
                opp_val = getattr(value, "automaton_EventToken29", None)
                if opp_val is None:
                    setattr(value, "automaton_EventToken29", set([self]))
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
            if hasattr(old_value, "State52"):
                opp_val = getattr(old_value, "State52", None)
                if opp_val == self:
                    setattr(old_value, "State52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State52"):
                opp_val = getattr(value, "State52", None)
                setattr(value, "State52", self)

    @property
    def TimedZone41(self):
        return self.__TimedZone41

    @TimedZone41.setter
    def TimedZone41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_TimedZone__TimedZone41", None)
        self.__TimedZone41 = value
        
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

class automaton_Automaton:

    def __init__(self, eventPatternId: str, automaton_Automaton11: set["automaton_EventToken"] = None, automaton_Automaton: "automaton_InternalModel" = None, automaton_Automaton5: "automaton_InternalModel" = None, automaton_Automaton9: set["automaton_State"] = None, automaton_Automaton14: set["automaton_TimedZone"] = None, automaton_Automaton16: "automaton_InitState" = None, automaton_Automaton18: set["automaton_FinalState"] = None, automaton_Automaton20: "automaton_TrapState" = None):
        self.eventPatternId = eventPatternId
        self.automaton_Automaton11 = automaton_Automaton11 if automaton_Automaton11 is not None else set()
        self.automaton_Automaton = automaton_Automaton
        self.automaton_Automaton5 = automaton_Automaton5
        self.automaton_Automaton9 = automaton_Automaton9 if automaton_Automaton9 is not None else set()
        self.automaton_Automaton14 = automaton_Automaton14 if automaton_Automaton14 is not None else set()
        self.automaton_Automaton16 = automaton_Automaton16
        self.automaton_Automaton18 = automaton_Automaton18 if automaton_Automaton18 is not None else set()
        self.automaton_Automaton20 = automaton_Automaton20
        
        pass
    @property
    def eventPatternId(self):
        return self.__eventPatternId

    @eventPatternId.setter
    def eventPatternId(self, eventPatternId: str):
        self.__eventPatternId = eventPatternId


    @property
    def automaton_Automaton20(self):
        return self.__automaton_Automaton20

    @automaton_Automaton20.setter
    def automaton_Automaton20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton20", None)
        self.__automaton_Automaton20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_TrapState"):
                opp_val = getattr(old_value, "automaton_TrapState", None)
                if opp_val == self:
                    setattr(old_value, "automaton_TrapState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_TrapState"):
                opp_val = getattr(value, "automaton_TrapState", None)
                setattr(value, "automaton_TrapState", self)

    @property
    def automaton_Automaton18(self):
        return self.__automaton_Automaton18

    @automaton_Automaton18.setter
    def automaton_Automaton18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton18", None)
        self.__automaton_Automaton18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaton_FinalState"):
                    opp_val = getattr(item, "automaton_FinalState", None)
                    
                    if opp_val == self:
                        setattr(item, "automaton_FinalState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaton_FinalState"):
                    opp_val = getattr(item, "automaton_FinalState", None)
                    
                    setattr(item, "automaton_FinalState", self)
                    

    @property
    def automaton_Automaton5(self):
        return self.__automaton_Automaton5

    @automaton_Automaton5.setter
    def automaton_Automaton5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton5", None)
        self.__automaton_Automaton5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_InternalModel4"):
                opp_val = getattr(old_value, "automaton_InternalModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_InternalModel4"):
                opp_val = getattr(value, "automaton_InternalModel4", None)
                if opp_val is None:
                    setattr(value, "automaton_InternalModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automaton_Automaton14(self):
        return self.__automaton_Automaton14

    @automaton_Automaton14.setter
    def automaton_Automaton14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton14", None)
        self.__automaton_Automaton14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaton_TimedZone"):
                    opp_val = getattr(item, "automaton_TimedZone", None)
                    
                    if opp_val == self:
                        setattr(item, "automaton_TimedZone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaton_TimedZone"):
                    opp_val = getattr(item, "automaton_TimedZone", None)
                    
                    setattr(item, "automaton_TimedZone", self)
                    

    @property
    def automaton_Automaton9(self):
        return self.__automaton_Automaton9

    @automaton_Automaton9.setter
    def automaton_Automaton9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton9", None)
        self.__automaton_Automaton9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaton_State"):
                    opp_val = getattr(item, "automaton_State", None)
                    
                    if opp_val == self:
                        setattr(item, "automaton_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaton_State"):
                    opp_val = getattr(item, "automaton_State", None)
                    
                    setattr(item, "automaton_State", self)
                    

    @property
    def automaton_Automaton(self):
        return self.__automaton_Automaton

    @automaton_Automaton.setter
    def automaton_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton", None)
        self.__automaton_Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_InternalModel"):
                opp_val = getattr(old_value, "automaton_InternalModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_InternalModel"):
                opp_val = getattr(value, "automaton_InternalModel", None)
                if opp_val is None:
                    setattr(value, "automaton_InternalModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def automaton_Automaton16(self):
        return self.__automaton_Automaton16

    @automaton_Automaton16.setter
    def automaton_Automaton16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton16", None)
        self.__automaton_Automaton16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaton_InitState"):
                opp_val = getattr(old_value, "automaton_InitState", None)
                if opp_val == self:
                    setattr(old_value, "automaton_InitState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaton_InitState"):
                opp_val = getattr(value, "automaton_InitState", None)
                setattr(value, "automaton_InitState", self)

    @property
    def automaton_Automaton11(self):
        return self.__automaton_Automaton11

    @automaton_Automaton11.setter
    def automaton_Automaton11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaton_Automaton__automaton_Automaton11", None)
        self.__automaton_Automaton11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaton_EventToken12"):
                    opp_val = getattr(item, "automaton_EventToken12", None)
                    
                    if opp_val == self:
                        setattr(item, "automaton_EventToken12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaton_EventToken12"):
                    opp_val = getattr(item, "automaton_EventToken12", None)
                    
                    setattr(item, "automaton_EventToken12", self)
                    

class automaton_InternalModel:

    pass