from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Transition:

    pass
class Step:

    pass
class StepToTransition:

    pass
class TransitionToStep:

    pass
class Connection:

    pass
class Grafcet_StepToTransition(Connection):

    pass
class Grafcet_TransitionToStep(Connection):

    pass
class Grafcet:

    pass
class LocatedElement:

    pass
class Grafcet_NamedElement(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Grafcet_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class Element:

    pass
class Grafcet_Step(Element):

    def __init__(self, isInitial: str, isActive: str, action: str, to: set["TransitionToStep"] = None, from_: set["StepToTransition"] = None, Element: "Grafcet_Grafcet" = None):
        self.isInitial = isInitial
        self.isActive = isActive
        self.action = action
        self.to = to if to is not None else set()
        self.from_ = from_ if from_ is not None else set()
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: str):
        self.__isInitial = isInitial


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grafcet_Step__from_", None)
        self.__from_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StepToTransition"):
                    opp_val = getattr(item, "StepToTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "StepToTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StepToTransition"):
                    opp_val = getattr(item, "StepToTransition", None)
                    
                    setattr(item, "StepToTransition", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grafcet_Step__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionToStep"):
                    opp_val = getattr(item, "TransitionToStep", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionToStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionToStep"):
                    opp_val = getattr(item, "TransitionToStep", None)
                    
                    setattr(item, "TransitionToStep", self)
                    

class Grafcet_Transition(Element):

    def __init__(self, condition: str, to7: set["StepToTransition"] = None, from_10: set["TransitionToStep"] = None, Element: "Grafcet_Grafcet" = None):
        self.condition = condition
        self.to7 = to7 if to7 is not None else set()
        self.from_10 = from_10 if from_10 is not None else set()
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def to7(self):
        return self.__to7

    @to7.setter
    def to7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grafcet_Transition__to7", None)
        self.__to7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StepToTransition8"):
                    opp_val = getattr(item, "StepToTransition8", None)
                    
                    if opp_val == self:
                        setattr(item, "StepToTransition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StepToTransition8"):
                    opp_val = getattr(item, "StepToTransition8", None)
                    
                    setattr(item, "StepToTransition8", self)
                    

    @property
    def from_10(self):
        return self.__from_10

    @from_10.setter
    def from_10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Grafcet_Transition__from_10", None)
        self.__from_10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransitionToStep11"):
                    opp_val = getattr(item, "TransitionToStep11", None)
                    
                    if opp_val == self:
                        setattr(item, "TransitionToStep11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransitionToStep11"):
                    opp_val = getattr(item, "TransitionToStep11", None)
                    
                    setattr(item, "TransitionToStep11", self)
                    

class NamedElement:

    pass
class Grafcet_Element(NamedElement):

    pass
class Grafcet_Connection(NamedElement):

    pass
class Grafcet_Grafcet(NamedElement):

    pass