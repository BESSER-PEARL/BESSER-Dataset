from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinetv3Trace_petrinetv3_TracedTransition:

    pass
class petrinetv3Trace_petrinetv3_TracedToken:

    pass
class petrinetv3_petrinetv3Trace_Token:

    pass
class petrinetv3_petrinetv3Trace_Place:

    pass
class petrinetv3Trace_petrinetv3_TracedPlace:

    pass
class petrinetv3Trace_States_Transition_clock_Value:

    def __init__(self, clock: int, clockSequence: "petrinetv3_TracedTransition" = None, transition_clock_Values: set["State"] = None):
        self.clock = clock
        self.clockSequence = clockSequence
        self.transition_clock_Values = transition_clock_Values if transition_clock_Values is not None else set()
        
        pass
    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, clock: int):
        self.__clock = clock


    @property
    def clockSequence(self):
        return self.__clockSequence

    @clockSequence.setter
    def clockSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3Trace_States_Transition_clock_Value__clockSequence", None)
        self.__clockSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedTransition"):
                opp_val = getattr(old_value, "TracedTransition", None)
                if opp_val == self:
                    setattr(old_value, "TracedTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedTransition"):
                opp_val = getattr(value, "TracedTransition", None)
                setattr(value, "TracedTransition", self)

    @property
    def transition_clock_Values(self):
        return self.__transition_clock_Values

    @transition_clock_Values.setter
    def transition_clock_Values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3Trace_States_Transition_clock_Value__transition_clock_Values", None)
        self.__transition_clock_Values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State36"):
                    opp_val = getattr(item, "State36", None)
                    
                    if opp_val == self:
                        setattr(item, "State36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State36"):
                    opp_val = getattr(item, "State36", None)
                    
                    setattr(item, "State36", self)
                    

class petrinetv3_petrinetv3Trace_Net:

    pass
class petrinetv3_petrinetv3Trace_Transition:

    pass
class petrinetv3Trace_States_Place_tokens_Value:

    pass
class MSEOccurrence:

    pass
class petrinetv3Trace_Steps_Step(MSEOccurrence):

    pass
class SmallStep:

    pass
class petrinetv3Trace_Steps_RootImplicitStep(SmallStep):

    pass
class Transition_clock_Value:

    pass
class Place_tokens_Value:

    pass
class petrinetv3Trace_States_State:

    pass
class BigStep:

    pass
class petrinetv3Trace_Steps_Petrinetv3_Net_Run(BigStep):

    def __init__(self, petrinetv3Trace_Steps_Petrinetv3_Net_Run: set["Petrinetv3_Net_Run_AbstractSubStep"] = None):
        self.petrinetv3Trace_Steps_Petrinetv3_Net_Run = petrinetv3Trace_Steps_Petrinetv3_Net_Run if petrinetv3Trace_Steps_Petrinetv3_Net_Run is not None else set()
        
        pass
    @property
    def petrinetv3Trace_Steps_Petrinetv3_Net_Run(self):
        return self.__petrinetv3Trace_Steps_Petrinetv3_Net_Run

    @petrinetv3Trace_Steps_Petrinetv3_Net_Run.setter
    def petrinetv3Trace_Steps_Petrinetv3_Net_Run(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetv3Trace_Steps_Petrinetv3_Net_Run__petrinetv3Trace_Steps_Petrinetv3_Net_Run", None)
        self.__petrinetv3Trace_Steps_Petrinetv3_Net_Run = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Petrinetv3_Net_Run_AbstractSubStep"):
                    opp_val = getattr(item, "Petrinetv3_Net_Run_AbstractSubStep", None)
                    
                    if opp_val == self:
                        setattr(item, "Petrinetv3_Net_Run_AbstractSubStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Petrinetv3_Net_Run_AbstractSubStep"):
                    opp_val = getattr(item, "Petrinetv3_Net_Run_AbstractSubStep", None)
                    
                    setattr(item, "Petrinetv3_Net_Run_AbstractSubStep", self)
                    

    def getCaller(self) :
        # TODO: Implement getCaller method
        pass

class Steps_SmallStep:

    pass
class Steps_Petrinetv3_Net_Run_AbstractSubStep:

    pass
class petrinetv3Trace_Steps_Petrinetv3_Net_Initialize(Steps_SmallStep, Steps_Petrinetv3_Net_Run_AbstractSubStep):

    def __init__(self):
        
        pass
    def getCaller(self) :
        # TODO: Implement getCaller method
        pass

class State:

    pass
class Step:

    pass
class petrinetv3Trace_Steps_SmallStep(Step):

    pass
class petrinetv3Trace_Steps_BigStep(Step):

    pass
class petrinetv3_TracedTransition:

    pass
class petrinetv3_TracedToken:

    pass
class petrinetv3Trace_Steps_Petrinetv3_Transition_Fire(Steps_SmallStep, Steps_Petrinetv3_Net_Run_AbstractSubStep):

    def __init__(self):
        
        pass
    def getCaller(self) :
        # TODO: Implement getCaller method
        pass

class petrinetv3Trace_Steps_Petrinetv3_Net_TickEnabledTransitions(Steps_SmallStep, Steps_Petrinetv3_Net_Run_AbstractSubStep):

    def __init__(self):
        
        pass
    def getCaller(self) :
        # TODO: Implement getCaller method
        pass

class petrinetv3Trace_Steps_Petrinetv3_Net_Run_ImplicitStep(Steps_SmallStep, Steps_Petrinetv3_Net_Run_AbstractSubStep):

    pass
class petrinetv3Trace_Steps_Petrinetv3_Net_Run_AbstractSubStep(ABC):

    pass
class Petrinetv3_Net_Run_AbstractSubStep:

    pass
class Petrinetv3_Transition_Fire:

    pass
class Petrinetv3_Net_TickEnabledTransitions:

    pass
class Petrinetv3_Net_Run:

    pass
class Petrinetv3_Net_Initialize:

    pass
class petrinetv3Trace_Trace:

    pass
class petrinetv3_TracedPlace:

    pass