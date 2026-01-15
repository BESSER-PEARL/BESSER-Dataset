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
            if hasattr(old_value, "cpsml_Function79"):
                opp_val = getattr(old_value, "cpsml_Function79", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function79"):
                opp_val = getattr(value, "cpsml_Function79", None)
                setattr(value, "cpsml_Function79", self)

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
            if hasattr(old_value, "cpsml_Function77"):
                opp_val = getattr(old_value, "cpsml_Function77", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function77"):
                opp_val = getattr(value, "cpsml_Function77", None)
                setattr(value, "cpsml_Function77", self)

class cpsml_Function:

    def __init__(self, name: str, cpsml_Function75: "cpsml_IndeVariable" = None, cpsml_Function: "cpsml_ODE" = None, cpsml_Function77: "cpsml_DeVariable" = None, cpsml_Function79: "cpsml_Fright" = None):
        self.name = name
        self.cpsml_Function75 = cpsml_Function75
        self.cpsml_Function = cpsml_Function
        self.cpsml_Function77 = cpsml_Function77
        self.cpsml_Function79 = cpsml_Function79
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_Function79(self):
        return self.__cpsml_Function79

    @cpsml_Function79.setter
    def cpsml_Function79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function79", None)
        self.__cpsml_Function79 = value
        
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
    def cpsml_Function75(self):
        return self.__cpsml_Function75

    @cpsml_Function75.setter
    def cpsml_Function75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function75", None)
        self.__cpsml_Function75 = value
        
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
    def cpsml_Function77(self):
        return self.__cpsml_Function77

    @cpsml_Function77.setter
    def cpsml_Function77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function77", None)
        self.__cpsml_Function77 = value
        
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
            if hasattr(old_value, "cpsml_ODE69"):
                opp_val = getattr(old_value, "cpsml_ODE69", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE69"):
                opp_val = getattr(value, "cpsml_ODE69", None)
                setattr(value, "cpsml_ODE69", self)

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
            if hasattr(old_value, "cpsml_Function75"):
                opp_val = getattr(old_value, "cpsml_Function75", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function75"):
                opp_val = getattr(value, "cpsml_Function75", None)
                setattr(value, "cpsml_Function75", self)

class cpsml_Interval:

    def __init__(self, name: str, left: float, right: float, subinterval: float, cpsml_Interval: "cpsml_ODE" = None):
        self.name = name
        self.left = left
        self.right = right
        self.subinterval = subinterval
        self.cpsml_Interval = cpsml_Interval
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def right(self) -> float:
        return self.__right

    @right.setter
    def right(self, right: float):
        self.__right = right

    @property
    def subinterval(self) -> float:
        return self.__subinterval

    @subinterval.setter
    def subinterval(self, subinterval: float):
        self.__subinterval = subinterval

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
            if hasattr(old_value, "cpsml_ODE73"):
                opp_val = getattr(old_value, "cpsml_ODE73", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE73"):
                opp_val = getattr(value, "cpsml_ODE73", None)
                setattr(value, "cpsml_ODE73", self)

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
            if hasattr(old_value, "cpsml_ODE71"):
                opp_val = getattr(old_value, "cpsml_ODE71", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE71"):
                opp_val = getattr(value, "cpsml_ODE71", None)
                setattr(value, "cpsml_ODE71", self)

class Transition:

    pass
class cpsml_ComTransition(Transition):

    pass
class cpsml_ProbTransition(Transition):

    def __init__(self, probability: float, cpsml_ProbTransition: "cpsml_System" = None, 34: "cpsml_State" = None, 31: "cpsml_State" = None, 63: "cpsml_State" = None, 66: "cpsml_State" = None):
        self.probability = probability
        self.cpsml_ProbTransition = cpsml_ProbTransition
        self.34 = 34
        self.31 = 31
        self.63 = 63
        self.66 = 66
        
    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def 34(self):
        return self.__34

    @34.setter
    def 34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__34", None)
        self.__34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "33"):
                opp_val = getattr(old_value, "33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "33"):
                opp_val = getattr(value, "33", None)
                if opp_val is None:
                    setattr(value, "33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 66(self):
        return self.__66

    @66.setter
    def 66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__66", None)
        self.__66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "67"):
                opp_val = getattr(old_value, "67", None)
                if opp_val == self:
                    setattr(old_value, "67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "67"):
                opp_val = getattr(value, "67", None)
                setattr(value, "67", self)

    @property
    def cpsml_ProbTransition(self):
        return self.__cpsml_ProbTransition

    @cpsml_ProbTransition.setter
    def cpsml_ProbTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__cpsml_ProbTransition", None)
        self.__cpsml_ProbTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System20"):
                opp_val = getattr(old_value, "cpsml_System20", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_System20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System20"):
                opp_val = getattr(value, "cpsml_System20", None)
                setattr(value, "cpsml_System20", self)

    @property
    def 31(self):
        return self.__31

    @31.setter
    def 31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__31", None)
        self.__31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "30"):
                opp_val = getattr(old_value, "30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "30"):
                opp_val = getattr(value, "30", None)
                if opp_val is None:
                    setattr(value, "30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 63(self):
        return self.__63

    @63.setter
    def 63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__63", None)
        self.__63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "64"):
                opp_val = getattr(old_value, "64", None)
                if opp_val == self:
                    setattr(old_value, "64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "64"):
                opp_val = getattr(value, "64", None)
                setattr(value, "64", self)

class cpsml_ODE:

    def __init__(self, name: str, cpsml_ODE: "cpsml_System" = None, cpsml_ODE23: "cpsml_State" = None, cpsml_ODE46: "cpsml_State" = None, cpsml_ODE71: "cpsml_Condition" = None, cpsml_ODE73: "cpsml_Interval" = None, cpsml_ODE69: "cpsml_Function" = None):
        self.name = name
        self.cpsml_ODE = cpsml_ODE
        self.cpsml_ODE23 = cpsml_ODE23
        self.cpsml_ODE46 = cpsml_ODE46
        self.cpsml_ODE71 = cpsml_ODE71
        self.cpsml_ODE73 = cpsml_ODE73
        self.cpsml_ODE69 = cpsml_ODE69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpsml_ODE71(self):
        return self.__cpsml_ODE71

    @cpsml_ODE71.setter
    def cpsml_ODE71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE71", None)
        self.__cpsml_ODE71 = value
        
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
    def cpsml_ODE73(self):
        return self.__cpsml_ODE73

    @cpsml_ODE73.setter
    def cpsml_ODE73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE73", None)
        self.__cpsml_ODE73 = value
        
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
    def cpsml_ODE46(self):
        return self.__cpsml_ODE46

    @cpsml_ODE46.setter
    def cpsml_ODE46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE46", None)
        self.__cpsml_ODE46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State45"):
                opp_val = getattr(old_value, "cpsml_State45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State45"):
                opp_val = getattr(value, "cpsml_State45", None)
                if opp_val is None:
                    setattr(value, "cpsml_State45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_ODE23(self):
        return self.__cpsml_ODE23

    @cpsml_ODE23.setter
    def cpsml_ODE23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE23", None)
        self.__cpsml_ODE23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State22"):
                opp_val = getattr(old_value, "cpsml_State22", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State22"):
                opp_val = getattr(value, "cpsml_State22", None)
                setattr(value, "cpsml_State22", self)

    @property
    def cpsml_ODE69(self):
        return self.__cpsml_ODE69

    @cpsml_ODE69.setter
    def cpsml_ODE69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE69", None)
        self.__cpsml_ODE69 = value
        
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

    def __init__(self, guard: str, action: str, name: str, event: str, cpsml_Transition: "cpsml_System" = None, cpsml_Transition43: "cpsml_State" = None, cpsml_Transition54: "cpsml_Variable" = None):
        self.guard = guard
        self.action = action
        self.name = name
        self.event = event
        self.cpsml_Transition = cpsml_Transition
        self.cpsml_Transition43 = cpsml_Transition43
        self.cpsml_Transition54 = cpsml_Transition54
        
    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

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
    def cpsml_Transition54(self):
        return self.__cpsml_Transition54

    @cpsml_Transition54.setter
    def cpsml_Transition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition54", None)
        self.__cpsml_Transition54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable55"):
                opp_val = getattr(old_value, "cpsml_Variable55", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable55"):
                opp_val = getattr(value, "cpsml_Variable55", None)
                setattr(value, "cpsml_Variable55", self)

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
    def cpsml_Transition43(self):
        return self.__cpsml_Transition43

    @cpsml_Transition43.setter
    def cpsml_Transition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition43", None)
        self.__cpsml_Transition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State42"):
                opp_val = getattr(old_value, "cpsml_State42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State42"):
                opp_val = getattr(value, "cpsml_State42", None)
                if opp_val is None:
                    setattr(value, "cpsml_State42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def holds(self):
        # TODO: Implement holds method
        pass

class cpsml_State:

    def __init__(self, name: bool, cpsml_State: "cpsml_System" = None, cpsml_State10: "cpsml_System" = None, cpsml_State15: "cpsml_System" = None, cpsml_State18: "cpsml_System" = None, 33: set["cpsml_ProbTransition"] = None, cpsml_State37: "cpsml_State" = None, cpsml_State35: set["cpsml_State"] = None, cpsml_State40: "cpsml_State" = None, cpsml_State38: "cpsml_State" = None, cpsml_State42: set["cpsml_Transition"] = None, cpsml_State22: "cpsml_ODE" = None, : set["cpsml_ComTransition"] = None, 27: set["cpsml_ComTransition"] = None, 30: set["cpsml_ProbTransition"] = None, 58: "cpsml_ComTransition" = None, 61: "cpsml_ComTransition" = None, cpsml_State45: set["cpsml_ODE"] = None, cpsml_State48: set["cpsml_Variable"] = None, cpsml_State51: "cpsml_Variable" = None, 64: "cpsml_ProbTransition" = None, 67: "cpsml_ProbTransition" = None):
        self.name = name
        self.cpsml_State = cpsml_State
        self.cpsml_State10 = cpsml_State10
        self.cpsml_State15 = cpsml_State15
        self.cpsml_State18 = cpsml_State18
        self.33 = 33 if 33 is not None else set()
        self.cpsml_State37 = cpsml_State37
        self.cpsml_State35 = cpsml_State35 if cpsml_State35 is not None else set()
        self.cpsml_State40 = cpsml_State40
        self.cpsml_State38 = cpsml_State38
        self.cpsml_State42 = cpsml_State42 if cpsml_State42 is not None else set()
        self.cpsml_State22 = cpsml_State22
        self. =  if  is not None else set()
        self.27 = 27 if 27 is not None else set()
        self.30 = 30 if 30 is not None else set()
        self.58 = 58
        self.61 = 61
        self.cpsml_State45 = cpsml_State45 if cpsml_State45 is not None else set()
        self.cpsml_State48 = cpsml_State48 if cpsml_State48 is not None else set()
        self.cpsml_State51 = cpsml_State51
        self.64 = 64
        self.67 = 67
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def 64(self):
        return self.__64

    @64.setter
    def 64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__64", None)
        self.__64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "63"):
                opp_val = getattr(old_value, "63", None)
                if opp_val == self:
                    setattr(old_value, "63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "63"):
                opp_val = getattr(value, "63", None)
                setattr(value, "63", self)

    @property
    def cpsml_State18(self):
        return self.__cpsml_State18

    @cpsml_State18.setter
    def cpsml_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State18", None)
        self.__cpsml_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System17"):
                opp_val = getattr(old_value, "cpsml_System17", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_System17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System17"):
                opp_val = getattr(value, "cpsml_System17", None)
                setattr(value, "cpsml_System17", self)

    @property
    def 33(self):
        return self.__33

    @33.setter
    def 33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__33", None)
        self.__33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "34"):
                    opp_val = getattr(item, "34", None)
                    
                    if opp_val == self:
                        setattr(item, "34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "34"):
                    opp_val = getattr(item, "34", None)
                    
                    setattr(item, "34", self)
                    

    @property
    def cpsml_State37(self):
        return self.__cpsml_State37

    @cpsml_State37.setter
    def cpsml_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State37", None)
        self.__cpsml_State37 = value
        
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
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__30", None)
        self.__30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "31"):
                    opp_val = getattr(item, "31", None)
                    
                    if opp_val == self:
                        setattr(item, "31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "31"):
                    opp_val = getattr(item, "31", None)
                    
                    setattr(item, "31", self)
                    

    @property
    def 67(self):
        return self.__67

    @67.setter
    def 67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__67", None)
        self.__67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "66"):
                opp_val = getattr(old_value, "66", None)
                if opp_val == self:
                    setattr(old_value, "66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "66"):
                opp_val = getattr(value, "66", None)
                setattr(value, "66", self)

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
                if hasattr(item, "cpsml_State37"):
                    opp_val = getattr(item, "cpsml_State37", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_State37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_State37"):
                    opp_val = getattr(item, "cpsml_State37", None)
                    
                    setattr(item, "cpsml_State37", self)
                    

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "25"):
                    opp_val = getattr(item, "25", None)
                    
                    if opp_val == self:
                        setattr(item, "25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "25"):
                    opp_val = getattr(item, "25", None)
                    
                    setattr(item, "25", self)
                    

    @property
    def cpsml_State15(self):
        return self.__cpsml_State15

    @cpsml_State15.setter
    def cpsml_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State15", None)
        self.__cpsml_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_System14"):
                opp_val = getattr(old_value, "cpsml_System14", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_System14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_System14"):
                opp_val = getattr(value, "cpsml_System14", None)
                setattr(value, "cpsml_System14", self)

    @property
    def cpsml_State22(self):
        return self.__cpsml_State22

    @cpsml_State22.setter
    def cpsml_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State22", None)
        self.__cpsml_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ODE23"):
                opp_val = getattr(old_value, "cpsml_ODE23", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE23"):
                opp_val = getattr(value, "cpsml_ODE23", None)
                setattr(value, "cpsml_ODE23", self)

    @property
    def cpsml_State48(self):
        return self.__cpsml_State48

    @cpsml_State48.setter
    def cpsml_State48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State48", None)
        self.__cpsml_State48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Variable49"):
                    opp_val = getattr(item, "cpsml_Variable49", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Variable49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Variable49"):
                    opp_val = getattr(item, "cpsml_Variable49", None)
                    
                    setattr(item, "cpsml_Variable49", self)
                    

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
            if hasattr(old_value, "cpsml_State40"):
                opp_val = getattr(old_value, "cpsml_State40", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State40"):
                opp_val = getattr(value, "cpsml_State40", None)
                setattr(value, "cpsml_State40", self)

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
    def cpsml_State42(self):
        return self.__cpsml_State42

    @cpsml_State42.setter
    def cpsml_State42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State42", None)
        self.__cpsml_State42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Transition43"):
                    opp_val = getattr(item, "cpsml_Transition43", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Transition43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Transition43"):
                    opp_val = getattr(item, "cpsml_Transition43", None)
                    
                    setattr(item, "cpsml_Transition43", self)
                    

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
    def cpsml_State51(self):
        return self.__cpsml_State51

    @cpsml_State51.setter
    def cpsml_State51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State51", None)
        self.__cpsml_State51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable52"):
                opp_val = getattr(old_value, "cpsml_Variable52", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable52"):
                opp_val = getattr(value, "cpsml_Variable52", None)
                setattr(value, "cpsml_Variable52", self)

    @property
    def 58(self):
        return self.__58

    @58.setter
    def 58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__58", None)
        self.__58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "57"):
                opp_val = getattr(old_value, "57", None)
                if opp_val == self:
                    setattr(old_value, "57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "57"):
                opp_val = getattr(value, "57", None)
                setattr(value, "57", self)

    @property
    def 61(self):
        return self.__61

    @61.setter
    def 61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__61", None)
        self.__61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "60"):
                opp_val = getattr(old_value, "60", None)
                if opp_val == self:
                    setattr(old_value, "60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "60"):
                opp_val = getattr(value, "60", None)
                setattr(value, "60", self)

    @property
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__27", None)
        self.__27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "28"):
                    opp_val = getattr(item, "28", None)
                    
                    if opp_val == self:
                        setattr(item, "28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "28"):
                    opp_val = getattr(item, "28", None)
                    
                    setattr(item, "28", self)
                    

    @property
    def cpsml_State40(self):
        return self.__cpsml_State40

    @cpsml_State40.setter
    def cpsml_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State40", None)
        self.__cpsml_State40 = value
        
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
    def cpsml_State45(self):
        return self.__cpsml_State45

    @cpsml_State45.setter
    def cpsml_State45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State45", None)
        self.__cpsml_State45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_ODE46"):
                    opp_val = getattr(item, "cpsml_ODE46", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_ODE46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_ODE46"):
                    opp_val = getattr(item, "cpsml_ODE46", None)
                    
                    setattr(item, "cpsml_ODE46", self)
                    

class cpsml_System:

    def __init__(self, name: str, ran: str, sub: int, y0label: int, cpsml_System: set["cpsml_Variable"] = None, cpsml_System2: "cpsml_Variable" = None, cpsml_System20: "cpsml_ProbTransition" = None, cpsml_System5: set["cpsml_State"] = None, cpsml_System7: set["cpsml_Transition"] = None, cpsml_System9: "cpsml_State" = None, cpsml_System12: set["cpsml_ODE"] = None, cpsml_System14: "cpsml_State" = None, cpsml_System17: "cpsml_State" = None):
        self.name = name
        self.ran = ran
        self.sub = sub
        self.y0label = y0label
        self.cpsml_System = cpsml_System if cpsml_System is not None else set()
        self.cpsml_System2 = cpsml_System2
        self.cpsml_System20 = cpsml_System20
        self.cpsml_System5 = cpsml_System5 if cpsml_System5 is not None else set()
        self.cpsml_System7 = cpsml_System7 if cpsml_System7 is not None else set()
        self.cpsml_System9 = cpsml_System9
        self.cpsml_System12 = cpsml_System12 if cpsml_System12 is not None else set()
        self.cpsml_System14 = cpsml_System14
        self.cpsml_System17 = cpsml_System17
        
    @property
    def ran(self) -> str:
        return self.__ran

    @ran.setter
    def ran(self, ran: str):
        self.__ran = ran

    @property
    def y0label(self) -> int:
        return self.__y0label

    @y0label.setter
    def y0label(self, y0label: int):
        self.__y0label = y0label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sub(self) -> int:
        return self.__sub

    @sub.setter
    def sub(self, sub: int):
        self.__sub = sub

    @property
    def cpsml_System14(self):
        return self.__cpsml_System14

    @cpsml_System14.setter
    def cpsml_System14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System14", None)
        self.__cpsml_System14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State15"):
                opp_val = getattr(old_value, "cpsml_State15", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State15"):
                opp_val = getattr(value, "cpsml_State15", None)
                setattr(value, "cpsml_State15", self)

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
    def cpsml_System20(self):
        return self.__cpsml_System20

    @cpsml_System20.setter
    def cpsml_System20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System20", None)
        self.__cpsml_System20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_ProbTransition"):
                opp_val = getattr(old_value, "cpsml_ProbTransition", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ProbTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ProbTransition"):
                opp_val = getattr(value, "cpsml_ProbTransition", None)
                setattr(value, "cpsml_ProbTransition", self)

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
    def cpsml_System17(self):
        return self.__cpsml_System17

    @cpsml_System17.setter
    def cpsml_System17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_System__cpsml_System17", None)
        self.__cpsml_System17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State18"):
                opp_val = getattr(old_value, "cpsml_State18", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State18"):
                opp_val = getattr(value, "cpsml_State18", None)
                setattr(value, "cpsml_State18", self)

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

    def main(self):
        # TODO: Implement main method
        pass

    def RealizeInitializeModel(self, arguments: str):
        # TODO: Implement RealizeInitializeModel method
        pass

    def callscilab(self):
        # TODO: Implement callscilab method
        pass

    def dojump(self):
        # TODO: Implement dojump method
        pass

class cpsml_Variable:

    def __init__(self, value: float, Globalnv: float, cpsml_Variable: "cpsml_System" = None, cpsml_Variable3: "cpsml_System" = None, cpsml_Variable49: "cpsml_State" = None, cpsml_Variable52: "cpsml_State" = None, cpsml_Variable55: "cpsml_Transition" = None):
        self.value = value
        self.Globalnv = Globalnv
        self.cpsml_Variable = cpsml_Variable
        self.cpsml_Variable3 = cpsml_Variable3
        self.cpsml_Variable49 = cpsml_Variable49
        self.cpsml_Variable52 = cpsml_Variable52
        self.cpsml_Variable55 = cpsml_Variable55
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def Globalnv(self) -> float:
        return self.__Globalnv

    @Globalnv.setter
    def Globalnv(self, Globalnv: float):
        self.__Globalnv = Globalnv

    @property
    def cpsml_Variable49(self):
        return self.__cpsml_Variable49

    @cpsml_Variable49.setter
    def cpsml_Variable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable49", None)
        self.__cpsml_Variable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State48"):
                opp_val = getattr(old_value, "cpsml_State48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State48"):
                opp_val = getattr(value, "cpsml_State48", None)
                if opp_val is None:
                    setattr(value, "cpsml_State48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_Variable55(self):
        return self.__cpsml_Variable55

    @cpsml_Variable55.setter
    def cpsml_Variable55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable55", None)
        self.__cpsml_Variable55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Transition54"):
                opp_val = getattr(old_value, "cpsml_Transition54", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Transition54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Transition54"):
                opp_val = getattr(value, "cpsml_Transition54", None)
                setattr(value, "cpsml_Transition54", self)

    @property
    def cpsml_Variable52(self):
        return self.__cpsml_Variable52

    @cpsml_Variable52.setter
    def cpsml_Variable52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable52", None)
        self.__cpsml_Variable52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State51"):
                opp_val = getattr(old_value, "cpsml_State51", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State51"):
                opp_val = getattr(value, "cpsml_State51", None)
                setattr(value, "cpsml_State51", self)

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
