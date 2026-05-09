from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class cpsml_Fright:

    def __init__(self, name: str, cpsml_Fright: "cpsml_Function" = None):
        self.name = name
        self.cpsml_Fright = cpsml_Fright
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "cpsml_Function69"):
                opp_val = getattr(old_value, "cpsml_Function69", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function69"):
                opp_val = getattr(value, "cpsml_Function69", None)
                setattr(value, "cpsml_Function69", self)

class cpsml_DeVariable:

    def __init__(self, name: str, cpsml_DeVariable: "cpsml_Function" = None):
        self.name = name
        self.cpsml_DeVariable = cpsml_DeVariable
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "cpsml_Function67"):
                opp_val = getattr(old_value, "cpsml_Function67", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function67"):
                opp_val = getattr(value, "cpsml_Function67", None)
                setattr(value, "cpsml_Function67", self)

class cpsml_Condition:

    def __init__(self, name: str, cpsml_Condition: "cpsml_ODE" = None):
        self.name = name
        self.cpsml_Condition = cpsml_Condition
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "cpsml_ODE61"):
                opp_val = getattr(old_value, "cpsml_ODE61", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE61"):
                opp_val = getattr(value, "cpsml_ODE61", None)
                setattr(value, "cpsml_ODE61", self)

class cpsml_Function:

    def __init__(self, name: str, cpsml_Function65: "cpsml_IndeVariable" = None, cpsml_Function: "cpsml_ODE" = None, cpsml_Function67: "cpsml_DeVariable" = None, cpsml_Function69: "cpsml_Fright" = None):
        self.name = name
        self.cpsml_Function65 = cpsml_Function65
        self.cpsml_Function = cpsml_Function
        self.cpsml_Function67 = cpsml_Function67
        self.cpsml_Function69 = cpsml_Function69
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "cpsml_ODE59"):
                opp_val = getattr(old_value, "cpsml_ODE59", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE59"):
                opp_val = getattr(value, "cpsml_ODE59", None)
                setattr(value, "cpsml_ODE59", self)

    @property
    def cpsml_Function65(self):
        return self.__cpsml_Function65

    @cpsml_Function65.setter
    def cpsml_Function65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function65", None)
        self.__cpsml_Function65 = value
        
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
    def cpsml_Function69(self):
        return self.__cpsml_Function69

    @cpsml_Function69.setter
    def cpsml_Function69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function69", None)
        self.__cpsml_Function69 = value
        
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
    def cpsml_Function67(self):
        return self.__cpsml_Function67

    @cpsml_Function67.setter
    def cpsml_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Function__cpsml_Function67", None)
        self.__cpsml_Function67 = value
        
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

class Transition:

    pass
class cpsml_IndeVariable:

    def __init__(self, name: str, cpsml_IndeVariable: "cpsml_Function" = None):
        self.name = name
        self.cpsml_IndeVariable = cpsml_IndeVariable
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "cpsml_Function65"):
                opp_val = getattr(old_value, "cpsml_Function65", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Function65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Function65"):
                opp_val = getattr(value, "cpsml_Function65", None)
                setattr(value, "cpsml_Function65", self)

class cpsml_Interval:

    def __init__(self, name: str, left: float, right: float, subinterval: float, cpsml_Interval: "cpsml_ODE" = None):
        self.name = name
        self.left = left
        self.right = right
        self.subinterval = subinterval
        self.cpsml_Interval = cpsml_Interval
        
        pass
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: float):
        self.__right = right


    @property
    def subinterval(self):
        return self.__subinterval

    @subinterval.setter
    def subinterval(self, subinterval: float):
        self.__subinterval = subinterval


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def left(self):
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
            if hasattr(old_value, "cpsml_ODE63"):
                opp_val = getattr(old_value, "cpsml_ODE63", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_ODE63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_ODE63"):
                opp_val = getattr(value, "cpsml_ODE63", None)
                setattr(value, "cpsml_ODE63", self)

class cpsml_ComTransition(Transition):

    pass
class cpsml_ProbTransition(Transition):

    def __init__(self, probability: float, ProbTransition: "cpsml_State" = None, ProbTransition29: "cpsml_State" = None, cpsml_ProbTransition: "cpsml_System" = None, outgoingProbTransitions: "cpsml_State" = None, incomingProbTransitions: "cpsml_State" = None):
        self.probability = probability
        self.ProbTransition = ProbTransition
        self.ProbTransition29 = ProbTransition29
        self.cpsml_ProbTransition = cpsml_ProbTransition
        self.outgoingProbTransitions = outgoingProbTransitions
        self.incomingProbTransitions = incomingProbTransitions
        
        pass
    @property
    def probability(self):
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability


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
    def ProbTransition29(self):
        return self.__ProbTransition29

    @ProbTransition29.setter
    def ProbTransition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ProbTransition__ProbTransition29", None)
        self.__ProbTransition29 = value
        
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
            if hasattr(old_value, "State55"):
                opp_val = getattr(old_value, "State55", None)
                if opp_val == self:
                    setattr(old_value, "State55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State55"):
                opp_val = getattr(value, "State55", None)
                setattr(value, "State55", self)

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
            if hasattr(old_value, "State57"):
                opp_val = getattr(old_value, "State57", None)
                if opp_val == self:
                    setattr(old_value, "State57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State57"):
                opp_val = getattr(value, "State57", None)
                setattr(value, "State57", self)

class cpsml_Transition(ABC):

    def __init__(self, name: str, event: str, guard: str, action: str, cpsml_Transition: "cpsml_System" = None, cpsml_Transition38: "cpsml_State" = None, cpsml_Transition49: "cpsml_Variable" = None):
        self.name = name
        self.event = event
        self.guard = guard
        self.action = action
        self.cpsml_Transition = cpsml_Transition
        self.cpsml_Transition38 = cpsml_Transition38
        self.cpsml_Transition49 = cpsml_Transition49
        
        pass
    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard


    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def cpsml_Transition38(self):
        return self.__cpsml_Transition38

    @cpsml_Transition38.setter
    def cpsml_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition38", None)
        self.__cpsml_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State37"):
                opp_val = getattr(old_value, "cpsml_State37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State37"):
                opp_val = getattr(value, "cpsml_State37", None)
                if opp_val is None:
                    setattr(value, "cpsml_State37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpsml_Transition49(self):
        return self.__cpsml_Transition49

    @cpsml_Transition49.setter
    def cpsml_Transition49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Transition__cpsml_Transition49", None)
        self.__cpsml_Transition49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable50"):
                opp_val = getattr(old_value, "cpsml_Variable50", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable50"):
                opp_val = getattr(value, "cpsml_Variable50", None)
                setattr(value, "cpsml_Variable50", self)

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

    def holds(self):
        # TODO: Implement holds method
        pass

class cpsml_State:

    def __init__(self, name: bool, csrc: set["cpsml_ComTransition"] = None, ctgt: set["cpsml_ComTransition"] = None, psrc: set["cpsml_ProbTransition"] = None, ptgt: set["cpsml_ProbTransition"] = None, cpsml_State32: "cpsml_State" = None, cpsml_State30: set["cpsml_State"] = None, cpsml_State10: "cpsml_System" = None, cpsml_State15: "cpsml_System" = None, cpsml_State: "cpsml_System" = None, cpsml_State37: set["cpsml_Transition"] = None, cpsml_State40: set["cpsml_ODE"] = None, cpsml_State43: set["cpsml_Variable"] = None, cpsml_State18: "cpsml_System" = None, cpsml_State22: "cpsml_ODE" = None, cpsml_State35: "cpsml_State" = None, cpsml_State33: "cpsml_State" = None, cpsml_State46: "cpsml_Variable" = None, State: "cpsml_ComTransition" = None, State53: "cpsml_ComTransition" = None, State55: "cpsml_ProbTransition" = None, State57: "cpsml_ProbTransition" = None):
        self.name = name
        self.csrc = csrc if csrc is not None else set()
        self.ctgt = ctgt if ctgt is not None else set()
        self.psrc = psrc if psrc is not None else set()
        self.ptgt = ptgt if ptgt is not None else set()
        self.cpsml_State32 = cpsml_State32
        self.cpsml_State30 = cpsml_State30 if cpsml_State30 is not None else set()
        self.cpsml_State10 = cpsml_State10
        self.cpsml_State15 = cpsml_State15
        self.cpsml_State = cpsml_State
        self.cpsml_State37 = cpsml_State37 if cpsml_State37 is not None else set()
        self.cpsml_State40 = cpsml_State40 if cpsml_State40 is not None else set()
        self.cpsml_State43 = cpsml_State43 if cpsml_State43 is not None else set()
        self.cpsml_State18 = cpsml_State18
        self.cpsml_State22 = cpsml_State22
        self.cpsml_State35 = cpsml_State35
        self.cpsml_State33 = cpsml_State33
        self.cpsml_State46 = cpsml_State46
        self.State = State
        self.State53 = State53
        self.State55 = State55
        self.State57 = State57
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


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
                if hasattr(item, "ProbTransition29"):
                    opp_val = getattr(item, "ProbTransition29", None)
                    
                    if opp_val == self:
                        setattr(item, "ProbTransition29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProbTransition29"):
                    opp_val = getattr(item, "ProbTransition29", None)
                    
                    setattr(item, "ProbTransition29", self)
                    

    @property
    def State57(self):
        return self.__State57

    @State57.setter
    def State57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State57", None)
        self.__State57 = value
        
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
    def cpsml_State35(self):
        return self.__cpsml_State35

    @cpsml_State35.setter
    def cpsml_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State35", None)
        self.__cpsml_State35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State33"):
                opp_val = getattr(old_value, "cpsml_State33", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State33"):
                opp_val = getattr(value, "cpsml_State33", None)
                setattr(value, "cpsml_State33", self)

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
    def cpsml_State30(self):
        return self.__cpsml_State30

    @cpsml_State30.setter
    def cpsml_State30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State30", None)
        self.__cpsml_State30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_State32"):
                    opp_val = getattr(item, "cpsml_State32", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_State32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_State32"):
                    opp_val = getattr(item, "cpsml_State32", None)
                    
                    setattr(item, "cpsml_State32", self)
                    

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
    def cpsml_State43(self):
        return self.__cpsml_State43

    @cpsml_State43.setter
    def cpsml_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State43", None)
        self.__cpsml_State43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Variable44"):
                    opp_val = getattr(item, "cpsml_Variable44", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Variable44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Variable44"):
                    opp_val = getattr(item, "cpsml_Variable44", None)
                    
                    setattr(item, "cpsml_Variable44", self)
                    

    @property
    def State55(self):
        return self.__State55

    @State55.setter
    def State55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State55", None)
        self.__State55 = value
        
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
    def cpsml_State40(self):
        return self.__cpsml_State40

    @cpsml_State40.setter
    def cpsml_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State40", None)
        self.__cpsml_State40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_ODE41"):
                    opp_val = getattr(item, "cpsml_ODE41", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_ODE41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_ODE41"):
                    opp_val = getattr(item, "cpsml_ODE41", None)
                    
                    setattr(item, "cpsml_ODE41", self)
                    

    @property
    def cpsml_State33(self):
        return self.__cpsml_State33

    @cpsml_State33.setter
    def cpsml_State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State33", None)
        self.__cpsml_State33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State35"):
                opp_val = getattr(old_value, "cpsml_State35", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State35"):
                opp_val = getattr(value, "cpsml_State35", None)
                setattr(value, "cpsml_State35", self)

    @property
    def cpsml_State32(self):
        return self.__cpsml_State32

    @cpsml_State32.setter
    def cpsml_State32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State32", None)
        self.__cpsml_State32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State30"):
                opp_val = getattr(old_value, "cpsml_State30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State30"):
                opp_val = getattr(value, "cpsml_State30", None)
                if opp_val is None:
                    setattr(value, "cpsml_State30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "ComTransition26"):
                    opp_val = getattr(item, "ComTransition26", None)
                    
                    if opp_val == self:
                        setattr(item, "ComTransition26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComTransition26"):
                    opp_val = getattr(item, "ComTransition26", None)
                    
                    setattr(item, "ComTransition26", self)
                    

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
    def State53(self):
        return self.__State53

    @State53.setter
    def State53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__State53", None)
        self.__State53 = value
        
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
    def cpsml_State46(self):
        return self.__cpsml_State46

    @cpsml_State46.setter
    def cpsml_State46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State46", None)
        self.__cpsml_State46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Variable47"):
                opp_val = getattr(old_value, "cpsml_Variable47", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Variable47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Variable47"):
                opp_val = getattr(value, "cpsml_Variable47", None)
                setattr(value, "cpsml_Variable47", self)

    @property
    def cpsml_State37(self):
        return self.__cpsml_State37

    @cpsml_State37.setter
    def cpsml_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_State__cpsml_State37", None)
        self.__cpsml_State37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cpsml_Transition38"):
                    opp_val = getattr(item, "cpsml_Transition38", None)
                    
                    if opp_val == self:
                        setattr(item, "cpsml_Transition38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cpsml_Transition38"):
                    opp_val = getattr(item, "cpsml_Transition38", None)
                    
                    setattr(item, "cpsml_Transition38", self)
                    

class cpsml_Variable:

    def __init__(self, value: float, Globalnv: float, cpsml_Variable: "cpsml_System" = None, cpsml_Variable3: "cpsml_System" = None, cpsml_Variable44: "cpsml_State" = None, cpsml_Variable47: "cpsml_State" = None, cpsml_Variable50: "cpsml_Transition" = None):
        self.value = value
        self.Globalnv = Globalnv
        self.cpsml_Variable = cpsml_Variable
        self.cpsml_Variable3 = cpsml_Variable3
        self.cpsml_Variable44 = cpsml_Variable44
        self.cpsml_Variable47 = cpsml_Variable47
        self.cpsml_Variable50 = cpsml_Variable50
        
        pass
    @property
    def Globalnv(self):
        return self.__Globalnv

    @Globalnv.setter
    def Globalnv(self, Globalnv: float):
        self.__Globalnv = Globalnv


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


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

    @property
    def cpsml_Variable47(self):
        return self.__cpsml_Variable47

    @cpsml_Variable47.setter
    def cpsml_Variable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable47", None)
        self.__cpsml_Variable47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State46"):
                opp_val = getattr(old_value, "cpsml_State46", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_State46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State46"):
                opp_val = getattr(value, "cpsml_State46", None)
                setattr(value, "cpsml_State46", self)

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
    def cpsml_Variable50(self):
        return self.__cpsml_Variable50

    @cpsml_Variable50.setter
    def cpsml_Variable50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable50", None)
        self.__cpsml_Variable50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_Transition49"):
                opp_val = getattr(old_value, "cpsml_Transition49", None)
                if opp_val == self:
                    setattr(old_value, "cpsml_Transition49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_Transition49"):
                opp_val = getattr(value, "cpsml_Transition49", None)
                setattr(value, "cpsml_Transition49", self)

    @property
    def cpsml_Variable44(self):
        return self.__cpsml_Variable44

    @cpsml_Variable44.setter
    def cpsml_Variable44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_Variable__cpsml_Variable44", None)
        self.__cpsml_Variable44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State43"):
                opp_val = getattr(old_value, "cpsml_State43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State43"):
                opp_val = getattr(value, "cpsml_State43", None)
                if opp_val is None:
                    setattr(value, "cpsml_State43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cpsml_System:

    def __init__(self, name: str, ran: str, sub: int, y0label: int, cpsml_System9: "cpsml_State" = None, cpsml_System12: set["cpsml_ODE"] = None, cpsml_System14: "cpsml_State" = None, cpsml_System: set["cpsml_Variable"] = None, cpsml_System2: "cpsml_Variable" = None, cpsml_System5: set["cpsml_State"] = None, cpsml_System7: set["cpsml_Transition"] = None, cpsml_System17: "cpsml_State" = None, cpsml_System20: "cpsml_ProbTransition" = None):
        self.name = name
        self.ran = ran
        self.sub = sub
        self.y0label = y0label
        self.cpsml_System9 = cpsml_System9
        self.cpsml_System12 = cpsml_System12 if cpsml_System12 is not None else set()
        self.cpsml_System14 = cpsml_System14
        self.cpsml_System = cpsml_System if cpsml_System is not None else set()
        self.cpsml_System2 = cpsml_System2
        self.cpsml_System5 = cpsml_System5 if cpsml_System5 is not None else set()
        self.cpsml_System7 = cpsml_System7 if cpsml_System7 is not None else set()
        self.cpsml_System17 = cpsml_System17
        self.cpsml_System20 = cpsml_System20
        
        pass
    @property
    def sub(self):
        return self.__sub

    @sub.setter
    def sub(self, sub: int):
        self.__sub = sub


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ran(self):
        return self.__ran

    @ran.setter
    def ran(self, ran: str):
        self.__ran = ran


    @property
    def y0label(self):
        return self.__y0label

    @y0label.setter
    def y0label(self, y0label: int):
        self.__y0label = y0label


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
                    

    def RealizeInitializeModel(self, cpsml_arguments):
        # TODO: Implement RealizeInitializeModel method
        pass

    def dojump(self):
        # TODO: Implement dojump method
        pass

    def callscilab(self):
        # TODO: Implement callscilab method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class cpsml_ODE:

    def __init__(self, name: str, cpsml_ODE: "cpsml_System" = None, cpsml_ODE41: "cpsml_State" = None, cpsml_ODE23: "cpsml_State" = None, cpsml_ODE63: "cpsml_Interval" = None, cpsml_ODE59: "cpsml_Function" = None, cpsml_ODE61: "cpsml_Condition" = None):
        self.name = name
        self.cpsml_ODE = cpsml_ODE
        self.cpsml_ODE41 = cpsml_ODE41
        self.cpsml_ODE23 = cpsml_ODE23
        self.cpsml_ODE63 = cpsml_ODE63
        self.cpsml_ODE59 = cpsml_ODE59
        self.cpsml_ODE61 = cpsml_ODE61
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def cpsml_ODE59(self):
        return self.__cpsml_ODE59

    @cpsml_ODE59.setter
    def cpsml_ODE59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE59", None)
        self.__cpsml_ODE59 = value
        
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

    @property
    def cpsml_ODE63(self):
        return self.__cpsml_ODE63

    @cpsml_ODE63.setter
    def cpsml_ODE63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE63", None)
        self.__cpsml_ODE63 = value
        
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
    def cpsml_ODE61(self):
        return self.__cpsml_ODE61

    @cpsml_ODE61.setter
    def cpsml_ODE61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE61", None)
        self.__cpsml_ODE61 = value
        
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
    def cpsml_ODE41(self):
        return self.__cpsml_ODE41

    @cpsml_ODE41.setter
    def cpsml_ODE41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpsml_ODE__cpsml_ODE41", None)
        self.__cpsml_ODE41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpsml_State40"):
                opp_val = getattr(old_value, "cpsml_State40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpsml_State40"):
                opp_val = getattr(value, "cpsml_State40", None)
                if opp_val is None:
                    setattr(value, "cpsml_State40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
