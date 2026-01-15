from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Constraint:

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_Operation:

    def __init__(self, isQuery: bool, UML2_Operation: "UML2_Constraint" = None):
        self.isQuery = isQuery
        self.UML2_Operation = UML2_Operation
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def UML2_Operation(self):
        return self.__UML2_Operation

    @UML2_Operation.setter
    def UML2_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation", None)
        self.__UML2_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint"):
                opp_val = getattr(old_value, "UML2_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint"):
                opp_val = getattr(value, "UML2_Constraint", None)
                setattr(value, "UML2_Constraint", self)

class UML2_Constraint:

    pass
class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass