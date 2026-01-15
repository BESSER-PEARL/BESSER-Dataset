from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StateMachinesModule_State:

    pass
class StateMachinesModule_StateMachine:

    pass
class StateMachinesModule_Constraint:

    def __init__(self, StateMachinesModule_Constraint: "StateMachinesModule_Transition" = None):
        self.StateMachinesModule_Constraint = StateMachinesModule_Constraint
        
    @property
    def StateMachinesModule_Constraint(self):
        return self.__StateMachinesModule_Constraint

    @StateMachinesModule_Constraint.setter
    def StateMachinesModule_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachinesModule_Constraint__StateMachinesModule_Constraint", None)
        self.__StateMachinesModule_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachinesModule_Transition4"):
                opp_val = getattr(old_value, "StateMachinesModule_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "StateMachinesModule_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachinesModule_Transition4"):
                opp_val = getattr(value, "StateMachinesModule_Transition4", None)
                setattr(value, "StateMachinesModule_Transition4", self)

    def eval(self) -> bool:
        # TODO: Implement eval method
        pass

class StateMachinesModule_Transition:

    pass