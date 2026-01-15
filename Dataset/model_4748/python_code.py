from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Axis(Enum):
    component = "component"
    internalinterface = "internalinterface"
    interface = "interface"
    attribute = "attribute"
    binding = "binding"
    child = "child"
    parent = "parent"
    descendant = "descendant"
    ancestor = "ancestor"
    sibling = "sibling"
    descendantorself = "descendantorself"
    ancestororself = "ancestororself"
    siblingorself = "siblingorself"


############################################
# Definition of Classes
############################################

class OperatorExp:

    pass
class FPath_BinaryOperatorExp(OperatorExp):

    pass
class Test:

    pass
class FPath_NameTest(Test):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class FPath_WildcardTest(Test):

    pass
class FPath_UnaryOperatorExp(OperatorExp):

    pass
class Expression:

    pass
class FPath_NumberExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class FPath_VariableExp(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class FPath_FunctionCallExp(Expression):

    def __init__(self, name: str, FPath_FunctionCallExp: set["FPath_Expression"] = None):
        self.name = name
        self.FPath_FunctionCallExp = FPath_FunctionCallExp if FPath_FunctionCallExp is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def FPath_FunctionCallExp(self):
        return self.__FPath_FunctionCallExp

    @FPath_FunctionCallExp.setter
    def FPath_FunctionCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FPath_FunctionCallExp__FPath_FunctionCallExp", None)
        self.__FPath_FunctionCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FPath_Expression"):
                    opp_val = getattr(item, "FPath_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "FPath_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FPath_Expression"):
                    opp_val = getattr(item, "FPath_Expression", None)
                    
                    setattr(item, "FPath_Expression", self)
                    

class FPath_StringExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class FPath_OperatorExp(Expression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class FPath_PathExp(Expression):

    pass
class FPath_ContextExp(Expression):

    pass
class LocatedElement:

    pass
class FPath_Step(LocatedElement):

    def __init__(self, axis: str, FPath_Step13: "FPath_Test" = None, FPath_Step15: set["FPath_Expression"] = None, FPath_Step: "FPath_PathExp" = None):
        self.axis = axis
        self.FPath_Step13 = FPath_Step13
        self.FPath_Step15 = FPath_Step15 if FPath_Step15 is not None else set()
        self.FPath_Step = FPath_Step
        
    @property
    def axis(self) -> str:
        return self.__axis

    @axis.setter
    def axis(self, axis: str):
        self.__axis = axis

    @property
    def FPath_Step(self):
        return self.__FPath_Step

    @FPath_Step.setter
    def FPath_Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FPath_Step__FPath_Step", None)
        self.__FPath_Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FPath_PathExp4"):
                opp_val = getattr(old_value, "FPath_PathExp4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FPath_PathExp4"):
                opp_val = getattr(value, "FPath_PathExp4", None)
                if opp_val is None:
                    setattr(value, "FPath_PathExp4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FPath_Step13(self):
        return self.__FPath_Step13

    @FPath_Step13.setter
    def FPath_Step13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FPath_Step__FPath_Step13", None)
        self.__FPath_Step13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FPath_Test"):
                opp_val = getattr(old_value, "FPath_Test", None)
                if opp_val == self:
                    setattr(old_value, "FPath_Test", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FPath_Test"):
                opp_val = getattr(value, "FPath_Test", None)
                setattr(value, "FPath_Test", self)

    @property
    def FPath_Step15(self):
        return self.__FPath_Step15

    @FPath_Step15.setter
    def FPath_Step15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FPath_Step__FPath_Step15", None)
        self.__FPath_Step15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FPath_Expression16"):
                    opp_val = getattr(item, "FPath_Expression16", None)
                    
                    if opp_val == self:
                        setattr(item, "FPath_Expression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FPath_Expression16"):
                    opp_val = getattr(item, "FPath_Expression16", None)
                    
                    setattr(item, "FPath_Expression16", self)
                    

class FPath_Test(LocatedElement):

    pass
class FPath_Expression(LocatedElement):

    pass
class FPath_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore
