from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class cpsml_Fright:

    def __init__(self, name: str, cpsml_Fright: "cpsml_Function" = None):
        self.name = name
        self.cpsml_Fright = cpsml_Fright
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_Fright(self):
        return self.__cpsml_Fright

    @cpsml_Fright.setter
    def cpsml_Fright(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Fright__cpsml_Fright", None)
        self.__cpsml_Fright = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Function61"):
                opp_val = getattr(old_value, "cpsml_Function61", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function61"):
                opp_val = getattr(value, "cpsml_Function61", None)
                setattr(value, "cpsml_Function61", self)

class cpsml_DeVariable:

    def __init__(self, name: str, cpsml_DeVariable: "cpsml_Function" = None):
        self.name = name
        self.cpsml_DeVariable = cpsml_DeVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_DeVariable(self):
        return self.__cpsml_DeVariable

    @cpsml_DeVariable.setter
    def cpsml_DeVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_DeVariable__cpsml_DeVariable", None)
        self.__cpsml_DeVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Function59"):
                opp_val = getattr(old_value, "cpsml_Function59", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function59"):
                opp_val = getattr(value, "cpsml_Function59", None)
                setattr(value, "cpsml_Function59", self)

class cpsml_IndeVariable:

    def __init__(self, name: str, cpsml_IndeVariable: "cpsml_Function" = None):
        self.name = name
        self.cpsml_IndeVariable = cpsml_IndeVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_IndeVariable(self):
        return self.__cpsml_IndeVariable

    @cpsml_IndeVariable.setter
    def cpsml_IndeVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_IndeVariable__cpsml_IndeVariable", None)
        self.__cpsml_IndeVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Function57"):
                opp_val = getattr(old_value, "cpsml_Function57", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function57"):
                opp_val = getattr(value, "cpsml_Function57", None)
                setattr(value, "cpsml_Function57", self)

class cpsml_Interval:

    def __init__(self, name: str, left: float, right: float, subinterval: float, cpsml_Interval: "cpsml_ODE" = None):
        self.name = name
        self.left = left
        self.right = right
        self.subinterval = subinterval
        self.cpsml_Interval = cpsml_Interval
        
    @property
    def subinterval(self) -> float:
        return self.__subinterval

    @subinterval.setter
    def subinterval(self, subinterval: float):
        self.__subinterval = subinterval

    @property
    def right(self) -> float:
        return self.__right

    @right.setter
    def right(self, right: float):
        self.__right = right

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def left(self) -> float:
        return self.__left

    @left.setter
    def left(self, left: float):
        self.__left = left

    @property
    def cpsml_Interval(self):
        return self.__cpsml_Interval

    @cpsml_Interval.setter
    def cpsml_Interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Interval__cpsml_Interval", None)
        self.__cpsml_Interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ODE55"):
                opp_val = getattr(old_value, "cpsml_ODE55", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE55"):
                opp_val = getattr(value, "cpsml_ODE55", None)
                setattr(value, "cpsml_ODE55", self)

class cpsml_Condition:

    def __init__(self, name: str, cpsml_Condition: "cpsml_ODE" = None):
        self.name = name
        self.cpsml_Condition = cpsml_Condition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_Condition(self):
        return self.__cpsml_Condition

    @cpsml_Condition.setter
    def cpsml_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Condition__cpsml_Condition", None)
        self.__cpsml_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ODE53"):
                opp_val = getattr(old_value, "cpsml_ODE53", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE53"):
                opp_val = getattr(value, "cpsml_ODE53", None)
                setattr(value, "cpsml_ODE53", self)

class cpsml_Function:

    def __init__(self, name: str, cpsml_Function: "cpsml_ODE" = None, cpsml_Function57: "cpsml_IndeVariable" = None, cpsml_Function59: "cpsml_DeVariable" = None, cpsml_Function61: "cpsml_Fright" = None):
        self.name = name
        self.cpsml_Function = cpsml_Function
        self.cpsml_Function57 = cpsml_Function57
        self.cpsml_Function59 = cpsml_Function59
        self.cpsml_Function61 = cpsml_Function61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_Function61(self):
        return self.__cpsml_Function61

    @cpsml_Function61.setter
    def cpsml_Function61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function61", None)
        self.__cpsml_Function61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Fright"):
                opp_val = getattr(old_value, "cpsml_Fright", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Fright", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Fright"):
                opp_val = getattr(value, "cpsml_Fright", None)
                setattr(value, "cpsml_Fright", self)

    @property
    def cpsml_Function57(self):
        return self.__cpsml_Function57

    @cpsml_Function57.setter
    def cpsml_Function57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function57", None)
        self.__cpsml_Function57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_IndeVariable"):
                opp_val = getattr(old_value, "cpsml_IndeVariable", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_IndeVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_IndeVariable"):
                opp_val = getattr(value, "cpsml_IndeVariable", None)
                setattr(value, "cpsml_IndeVariable", self)

    @property
    def cpsml_Function59(self):
        return self.__cpsml_Function59

    @cpsml_Function59.setter
    def cpsml_Function59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function59", None)
        self.__cpsml_Function59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_DeVariable"):
                opp_val = getattr(old_value, "cpsml_DeVariable", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_DeVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_DeVariable"):
                opp_val = getattr(value, "cpsml_DeVariable", None)
                setattr(value, "cpsml_DeVariable", self)

    @property
    def cpsml_Function(self):
        return self.__cpsml_Function

    @cpsml_Function.setter
    def cpsml_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function", None)
        self.__cpsml_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ODE51"):
                opp_val = getattr(old_value, "cpsml_ODE51", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE51"):
                opp_val = getattr(value, "cpsml_ODE51", None)
                setattr(value, "cpsml_ODE51", self)

class Transition:

    pass
class cpsml_ProbTransition(Transition):

    def __init__(self, probability: float, ProbTransition: "cpsml_State" = None, ProbTransition21: "cpsml_State" = None, outgoingProbTransitions: "cpsml_State" = None, incomingProbTransitions: "cpsml_State" = None):
        self.probability = probability
        self.ProbTransition = ProbTransition
        self.ProbTransition21 = ProbTransition21
        self.outgoingProbTransitions = outgoingProbTransitions
        self.incomingProbTransitions = incomingProbTransitions
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def outgoingProbTransitions(self):
        return self.__outgoingProbTransitions

    @outgoingProbTransitions.setter
    def outgoingProbTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__outgoingProbTransitions", None)
        self.__outgoingProbTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State47"):
                opp_val = getattr(old_value, "State47", None)
                if opp_val == self:
                    setattr(old_value, "State47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State47"):
                opp_val = getattr(value, "State47", None)
                setattr(value, "State47", self)

    @property
    def ProbTransition(self):
        return self.__ProbTransition

    @ProbTransition.setter
    def ProbTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__ProbTransition", None)
        self.__ProbTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "psrc"):
                opp_val = getattr(old_value, "psrc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "psrc"):
                opp_val = getattr(value, "psrc", None)
                if opp_val is None:
                    setattr(value, "psrc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingProbTransitions(self):
        return self.__incomingProbTransitions

    @incomingProbTransitions.setter
    def incomingProbTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__incomingProbTransitions", None)
        self.__incomingProbTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State49"):
                opp_val = getattr(old_value, "State49", None)
                if opp_val == self:
                    setattr(old_value, "State49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State49"):
                opp_val = getattr(value, "State49", None)
                setattr(value, "State49", self)

    @property
    def ProbTransition21(self):
        return self.__ProbTransition21

    @ProbTransition21.setter
    def ProbTransition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__ProbTransition21", None)
        self.__ProbTransition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ptgt"):
                opp_val = getattr(old_value, "ptgt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ptgt"):
                opp_val = getattr(value, "ptgt", None)
                if opp_val is None:
                    setattr(value, "ptgt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cpsml_ComTransition(Transition):

    pass
class cpsml_ODE:

    def __init__(self, name: str, cpsml_ODE: "cpsml_System" = None, cpsml_ODE15: "cpsml_State" = None, cpsml_ODE33: "cpsml_State" = None, cpsml_ODE51: "cpsml_Function" = None, cpsml_ODE53: "cpsml_Condition" = None, cpsml_ODE55: "cpsml_Interval" = None):
        self.name = name
        self.cpsml_ODE = cpsml_ODE
        self.cpsml_ODE15 = cpsml_ODE15
        self.cpsml_ODE33 = cpsml_ODE33
        self.cpsml_ODE51 = cpsml_ODE51
        self.cpsml_ODE53 = cpsml_ODE53
        self.cpsml_ODE55 = cpsml_ODE55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_ODE(self):
        return self.__cpsml_ODE

    @cpsml_ODE.setter
    def cpsml_ODE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE", None)
        self.__cpsml_ODE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System12"):
                opp_val = getattr(old_value, "cpsml_System12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System12"):
                opp_val = getattr(value, "cpsml_System12", None)
                if opp_val is None:
                    setattr(value, "cpsml_System12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_ODE33(self):
        return self.__cpsml_ODE33

    @cpsml_ODE33.setter
    def cpsml_ODE33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE33", None)
        self.__cpsml_ODE33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State32"):
                opp_val = getattr(old_value, "cpsml_State32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State32"):
                opp_val = getattr(value, "cpsml_State32", None)
                if opp_val is None:
                    setattr(value, "cpsml_State32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_ODE53(self):
        return self.__cpsml_ODE53

    @cpsml_ODE53.setter
    def cpsml_ODE53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE53", None)
        self.__cpsml_ODE53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Condition"):
                opp_val = getattr(old_value, "cpsml_Condition", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Condition"):
                opp_val = getattr(value, "cpsml_Condition", None)
                setattr(value, "cpsml_Condition", self)

    @property
    def cpsml_ODE55(self):
        return self.__cpsml_ODE55

    @cpsml_ODE55.setter
    def cpsml_ODE55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE55", None)
        self.__cpsml_ODE55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Interval"):
                opp_val = getattr(old_value, "cpsml_Interval", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Interval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Interval"):
                opp_val = getattr(value, "cpsml_Interval", None)
                setattr(value, "cpsml_Interval", self)

    @property
    def cpsml_ODE15(self):
        return self.__cpsml_ODE15

    @cpsml_ODE15.setter
    def cpsml_ODE15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE15", None)
        self.__cpsml_ODE15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State14"):
                opp_val = getattr(old_value, "cpsml_State14", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State14"):
                opp_val = getattr(value, "cpsml_State14", None)
                setattr(value, "cpsml_State14", self)

    @property
    def cpsml_ODE51(self):
        return self.__cpsml_ODE51

    @cpsml_ODE51.setter
    def cpsml_ODE51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE51", None)
        self.__cpsml_ODE51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Function"):
                opp_val = getattr(old_value, "cpsml_Function", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function"):
                opp_val = getattr(value, "cpsml_Function", None)
                setattr(value, "cpsml_Function", self)

class cpsml_Transition(ABC):

    def __init__(self, name: str, event: str, guard: str, action: str, cpsml_Transition: "cpsml_System" = None, cpsml_Transition30: "cpsml_State" = None, cpsml_Transition41: "cpsml_Variable" = None):
        self.name = name
        self.event = event
        self.guard = guard
        self.action = action
        self.cpsml_Transition = cpsml_Transition
        self.cpsml_Transition30 = cpsml_Transition30
        self.cpsml_Transition41 = cpsml_Transition41
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def cpsml_Transition(self):
        return self.__cpsml_Transition

    @cpsml_Transition.setter
    def cpsml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition", None)
        self.__cpsml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System7"):
                opp_val = getattr(old_value, "cpsml_System7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System7"):
                opp_val = getattr(value, "cpsml_System7", None)
                if opp_val is None:
                    setattr(value, "cpsml_System7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_Transition41(self):
        return self.__cpsml_Transition41

    @cpsml_Transition41.setter
    def cpsml_Transition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition41", None)
        self.__cpsml_Transition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable42"):
                opp_val = getattr(old_value, "cpsml_Variable42", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable42"):
                opp_val = getattr(value, "cpsml_Variable42", None)
                setattr(value, "cpsml_Variable42", self)

    @property
    def cpsml_Transition30(self):
        return self.__cpsml_Transition30

    @cpsml_Transition30.setter
    def cpsml_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition30", None)
        self.__cpsml_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State29"):
                opp_val = getattr(old_value, "cpsml_State29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State29"):
                opp_val = getattr(value, "cpsml_State29", None)
                if opp_val is None:
                    setattr(value, "cpsml_State29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cpsml_State:

    def __init__(self, name: str, cpsml_State: "cpsml_System" = None, cpsml_State10: "cpsml_System" = None, cpsml_State14: "cpsml_ODE" = None, csrc: set["cpsml_ComTransition"] = None, ctgt: set["cpsml_ComTransition"] = None, psrc: set["cpsml_ProbTransition"] = None, ptgt: set["cpsml_ProbTransition"] = None, cpsml_State24: "cpsml_State" = None, cpsml_State22: set["cpsml_State"] = None, cpsml_State27: "cpsml_State" = None, cpsml_State25: "cpsml_State" = None, cpsml_State29: set["cpsml_Transition"] = None, cpsml_State32: set["cpsml_ODE"] = None, cpsml_State35: set["cpsml_Variable"] = None, cpsml_State38: "cpsml_Variable" = None, State: "cpsml_ComTransition" = None, State45: "cpsml_ComTransition" = None, State47: "cpsml_ProbTransition" = None, State49: "cpsml_ProbTransition" = None):
        self.name = name
        self.cpsml_State = cpsml_State
        self.cpsml_State10 = cpsml_State10
        self.cpsml_State14 = cpsml_State14
        self.csrc = csrc if csrc is not None else set()
        self.ctgt = ctgt if ctgt is not None else set()
        self.psrc = psrc if psrc is not None else set()
        self.ptgt = ptgt if ptgt is not None else set()
        self.cpsml_State24 = cpsml_State24
        self.cpsml_State22 = cpsml_State22 if cpsml_State22 is not None else set()
        self.cpsml_State27 = cpsml_State27
        self.cpsml_State25 = cpsml_State25
        self.cpsml_State29 = cpsml_State29 if cpsml_State29 is not None else set()
        self.cpsml_State32 = cpsml_State32 if cpsml_State32 is not None else set()
        self.cpsml_State35 = cpsml_State35 if cpsml_State35 is not None else set()
        self.cpsml_State38 = cpsml_State38
        self.State = State
        self.State45 = State45
        self.State47 = State47
        self.State49 = State49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingComTransitions"):
                opp_val = getattr(old_value, "outgoingComTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingComTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingComTransitions"):
                opp_val = getattr(value, "outgoingComTransitions", None)
                setattr(value, "outgoingComTransitions", self)

    @property
    def cpsml_State14(self):
        return self.__cpsml_State14

    @cpsml_State14.setter
    def cpsml_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State14", None)
        self.__cpsml_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ODE15"):
                opp_val = getattr(old_value, "cpsml_ODE15", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE15"):
                opp_val = getattr(value, "cpsml_ODE15", None)
                setattr(value, "cpsml_ODE15", self)

    @property
    def cpsml_State38(self):
        return self.__cpsml_State38

    @cpsml_State38.setter
    def cpsml_State38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State38", None)
        self.__cpsml_State38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable39"):
                opp_val = getattr(old_value, "cpsml_Variable39", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable39"):
                opp_val = getattr(value, "cpsml_Variable39", None)
                setattr(value, "cpsml_Variable39", self)

    @property
    def cpsml_State32(self):
        return self.__cpsml_State32

    @cpsml_State32.setter
    def cpsml_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State32", None)
        self.__cpsml_State32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_ODE33"):
                    opp_val = getattr(item, "cpsml_ODE33", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_ODE33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_ODE33"):
                    opp_val = getattr(item, "cpsml_ODE33", None)
                    
                    setattr(item, "cpsml_ODE33", self)
                    

    @property
    def cpsml_State27(self):
        return self.__cpsml_State27

    @cpsml_State27.setter
    def cpsml_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State27", None)
        self.__cpsml_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State25"):
                opp_val = getattr(old_value, "cpsml_State25", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State25"):
                opp_val = getattr(value, "cpsml_State25", None)
                setattr(value, "cpsml_State25", self)

    @property
    def cpsml_State29(self):
        return self.__cpsml_State29

    @cpsml_State29.setter
    def cpsml_State29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State29", None)
        self.__cpsml_State29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Transition30"):
                    opp_val = getattr(item, "cpsml_Transition30", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Transition30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Transition30"):
                    opp_val = getattr(item, "cpsml_Transition30", None)
                    
                    setattr(item, "cpsml_Transition30", self)
                    

    @property
    def cpsml_State22(self):
        return self.__cpsml_State22

    @cpsml_State22.setter
    def cpsml_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State22", None)
        self.__cpsml_State22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_State24"):
                    opp_val = getattr(item, "cpsml_State24", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_State24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_State24"):
                    opp_val = getattr(item, "cpsml_State24", None)
                    
                    setattr(item, "cpsml_State24", self)
                    

    @property
    def State47(self):
        return self.__State47

    @State47.setter
    def State47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State47", None)
        self.__State47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingProbTransitions"):
                opp_val = getattr(old_value, "outgoingProbTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingProbTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingProbTransitions"):
                opp_val = getattr(value, "outgoingProbTransitions", None)
                setattr(value, "outgoingProbTransitions", self)

    @property
    def cpsml_State25(self):
        return self.__cpsml_State25

    @cpsml_State25.setter
    def cpsml_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State25", None)
        self.__cpsml_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State27"):
                opp_val = getattr(old_value, "cpsml_State27", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State27"):
                opp_val = getattr(value, "cpsml_State27", None)
                setattr(value, "cpsml_State27", self)

    @property
    def cpsml_State(self):
        return self.__cpsml_State

    @cpsml_State.setter
    def cpsml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State", None)
        self.__cpsml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System5"):
                opp_val = getattr(old_value, "cpsml_System5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System5"):
                opp_val = getattr(value, "cpsml_System5", None)
                if opp_val is None:
                    setattr(value, "cpsml_System5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def csrc(self):
        return self.__csrc

    @csrc.setter
    def csrc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__csrc", None)
        self.__csrc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComTransition"):
                    opp_val = getattr(item, "ComTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "ComTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComTransition"):
                    opp_val = getattr(item, "ComTransition", None)
                    
                    setattr(item, "ComTransition", self)
                    

    @property
    def cpsml_State10(self):
        return self.__cpsml_State10

    @cpsml_State10.setter
    def cpsml_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State10", None)
        self.__cpsml_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System9"):
                opp_val = getattr(old_value, "cpsml_System9", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_System9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System9"):
                opp_val = getattr(value, "cpsml_System9", None)
                setattr(value, "cpsml_System9", self)

    @property
    def psrc(self):
        return self.__psrc

    @psrc.setter
    def psrc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__psrc", None)
        self.__psrc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProbTransition"):
                    opp_val = getattr(item, "ProbTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "ProbTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProbTransition"):
                    opp_val = getattr(item, "ProbTransition", None)
                    
                    setattr(item, "ProbTransition", self)
                    

    @property
    def cpsml_State35(self):
        return self.__cpsml_State35

    @cpsml_State35.setter
    def cpsml_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State35", None)
        self.__cpsml_State35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Variable36"):
                    opp_val = getattr(item, "cpsml_Variable36", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Variable36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Variable36"):
                    opp_val = getattr(item, "cpsml_Variable36", None)
                    
                    setattr(item, "cpsml_Variable36", self)
                    

    @property
    def ctgt(self):
        return self.__ctgt

    @ctgt.setter
    def ctgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__ctgt", None)
        self.__ctgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComTransition18"):
                    opp_val = getattr(item, "ComTransition18", None)
                    
                    if opp_val == self:
                        setattr(item, "ComTransition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComTransition18"):
                    opp_val = getattr(item, "ComTransition18", None)
                    
                    setattr(item, "ComTransition18", self)
                    

    @property
    def cpsml_State24(self):
        return self.__cpsml_State24

    @cpsml_State24.setter
    def cpsml_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State24", None)
        self.__cpsml_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State22"):
                opp_val = getattr(old_value, "cpsml_State22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State22"):
                opp_val = getattr(value, "cpsml_State22", None)
                if opp_val is None:
                    setattr(value, "cpsml_State22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ptgt(self):
        return self.__ptgt

    @ptgt.setter
    def ptgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__ptgt", None)
        self.__ptgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProbTransition21"):
                    opp_val = getattr(item, "ProbTransition21", None)
                    
                    if opp_val == self:
                        setattr(item, "ProbTransition21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProbTransition21"):
                    opp_val = getattr(item, "ProbTransition21", None)
                    
                    setattr(item, "ProbTransition21", self)
                    

    @property
    def State49(self):
        return self.__State49

    @State49.setter
    def State49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State49", None)
        self.__State49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingProbTransitions"):
                opp_val = getattr(old_value, "incomingProbTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingProbTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingProbTransitions"):
                opp_val = getattr(value, "incomingProbTransitions", None)
                setattr(value, "incomingProbTransitions", self)

    @property
    def State45(self):
        return self.__State45

    @State45.setter
    def State45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State45", None)
        self.__State45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingComTransitions"):
                opp_val = getattr(old_value, "incomingComTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingComTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingComTransitions"):
                opp_val = getattr(value, "incomingComTransitions", None)
                setattr(value, "incomingComTransitions", self)

class cpsml_Variable:

    def __init__(self, value: float, cpsml_Variable: "cpsml_System" = None, cpsml_Variable3: "cpsml_System" = None, cpsml_Variable36: "cpsml_State" = None, cpsml_Variable39: "cpsml_State" = None, cpsml_Variable42: "cpsml_Transition" = None):
        self.value = value
        self.cpsml_Variable = cpsml_Variable
        self.cpsml_Variable3 = cpsml_Variable3
        self.cpsml_Variable36 = cpsml_Variable36
        self.cpsml_Variable39 = cpsml_Variable39
        self.cpsml_Variable42 = cpsml_Variable42
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def cpsml_Variable39(self):
        return self.__cpsml_Variable39

    @cpsml_Variable39.setter
    def cpsml_Variable39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable39", None)
        self.__cpsml_Variable39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State38"):
                opp_val = getattr(old_value, "cpsml_State38", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State38"):
                opp_val = getattr(value, "cpsml_State38", None)
                setattr(value, "cpsml_State38", self)

    @property
    def cpsml_Variable36(self):
        return self.__cpsml_Variable36

    @cpsml_Variable36.setter
    def cpsml_Variable36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable36", None)
        self.__cpsml_Variable36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State35"):
                opp_val = getattr(old_value, "cpsml_State35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State35"):
                opp_val = getattr(value, "cpsml_State35", None)
                if opp_val is None:
                    setattr(value, "cpsml_State35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_Variable(self):
        return self.__cpsml_Variable

    @cpsml_Variable.setter
    def cpsml_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable", None)
        self.__cpsml_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System"):
                opp_val = getattr(old_value, "cpsml_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System"):
                opp_val = getattr(value, "cpsml_System", None)
                if opp_val is None:
                    setattr(value, "cpsml_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_Variable42(self):
        return self.__cpsml_Variable42

    @cpsml_Variable42.setter
    def cpsml_Variable42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable42", None)
        self.__cpsml_Variable42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Transition41"):
                opp_val = getattr(old_value, "cpsml_Transition41", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Transition41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Transition41"):
                opp_val = getattr(value, "cpsml_Transition41", None)
                setattr(value, "cpsml_Transition41", self)

    @property
    def cpsml_Variable3(self):
        return self.__cpsml_Variable3

    @cpsml_Variable3.setter
    def cpsml_Variable3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable3", None)
        self.__cpsml_Variable3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System2"):
                opp_val = getattr(old_value, "cpsml_System2", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_System2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System2"):
                opp_val = getattr(value, "cpsml_System2", None)
                setattr(value, "cpsml_System2", self)

class cpsml_System:

    def __init__(self, name: str, cpsml_System: set["cpsml_Variable"] = None, cpsml_System2: "cpsml_Variable" = None, cpsml_System5: set["cpsml_State"] = None, cpsml_System7: set["cpsml_Transition"] = None, cpsml_System9: "cpsml_State" = None, cpsml_System12: set["cpsml_ODE"] = None):
        self.name = name
        self.cpsml_System = cpsml_System if cpsml_System is not None else set()
        self.cpsml_System2 = cpsml_System2
        self.cpsml_System5 = cpsml_System5 if cpsml_System5 is not None else set()
        self.cpsml_System7 = cpsml_System7 if cpsml_System7 is not None else set()
        self.cpsml_System9 = cpsml_System9
        self.cpsml_System12 = cpsml_System12 if cpsml_System12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_System5(self):
        return self.__cpsml_System5

    @cpsml_System5.setter
    def cpsml_System5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System5", None)
        self.__cpsml_System5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_State"):
                    opp_val = getattr(item, "cpsml_State", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_State"):
                    opp_val = getattr(item, "cpsml_State", None)
                    
                    setattr(item, "cpsml_State", self)
                    

    @property
    def cpsml_System(self):
        return self.__cpsml_System

    @cpsml_System.setter
    def cpsml_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System", None)
        self.__cpsml_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Variable"):
                    opp_val = getattr(item, "cpsml_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Variable"):
                    opp_val = getattr(item, "cpsml_Variable", None)
                    
                    setattr(item, "cpsml_Variable", self)
                    

    @property
    def cpsml_System9(self):
        return self.__cpsml_System9

    @cpsml_System9.setter
    def cpsml_System9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System9", None)
        self.__cpsml_System9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State10"):
                opp_val = getattr(old_value, "cpsml_State10", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State10"):
                opp_val = getattr(value, "cpsml_State10", None)
                setattr(value, "cpsml_State10", self)

    @property
    def cpsml_System12(self):
        return self.__cpsml_System12

    @cpsml_System12.setter
    def cpsml_System12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System12", None)
        self.__cpsml_System12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_ODE"):
                    opp_val = getattr(item, "cpsml_ODE", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_ODE", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_ODE"):
                    opp_val = getattr(item, "cpsml_ODE", None)
                    
                    setattr(item, "cpsml_ODE", self)
                    

    @property
    def cpsml_System2(self):
        return self.__cpsml_System2

    @cpsml_System2.setter
    def cpsml_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System2", None)
        self.__cpsml_System2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable3"):
                opp_val = getattr(old_value, "cpsml_Variable3", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable3"):
                opp_val = getattr(value, "cpsml_Variable3", None)
                setattr(value, "cpsml_Variable3", self)

    @property
    def cpsml_System7(self):
        return self.__cpsml_System7

    @cpsml_System7.setter
    def cpsml_System7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System7", None)
        self.__cpsml_System7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Transition"):
                    opp_val = getattr(item, "cpsml_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Transition"):
                    opp_val = getattr(item, "cpsml_Transition", None)
                    
                    setattr(item, "cpsml_Transition", self)
                    
