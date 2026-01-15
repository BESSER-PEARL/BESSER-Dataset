from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsmcore_Constraint:

    pass
class fsmcore_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class fsmcore_Trigger:

    def __init__(self, expression: str, fsmcore_Trigger: "fsmcore_Transition" = None):
        self.expression = expression
        self.fsmcore_Trigger = fsmcore_Trigger
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def fsmcore_Trigger(self):
        return self.__fsmcore_Trigger

    @fsmcore_Trigger.setter
    def fsmcore_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsmcore_Trigger__fsmcore_Trigger", None)
        self.__fsmcore_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsmcore_Transition11"):
                opp_val = getattr(old_value, "fsmcore_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "fsmcore_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsmcore_Transition11"):
                opp_val = getattr(value, "fsmcore_Transition11", None)
                setattr(value, "fsmcore_Transition11", self)

class NamedElement:

    pass
class fsmcore_State(NamedElement):

    pass
class fsmcore_StateMachine(NamedElement):

    pass
class fsmcore_Program:

    pass
class fsmcore_Transition(NamedElement):

    pass