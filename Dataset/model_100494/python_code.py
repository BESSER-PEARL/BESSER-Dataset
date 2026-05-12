from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BehaviorKind(Enum):
    ACTIVITY = "ACTIVITY"
    STATE_MACHINE = "STATE_MACHINE"
    OPAQUE_BEHAVIOR = "OPAQUE_BEHAVIOR"


############################################
# Definition of Classes
############################################

class TimeEventRule:

    pass
class umlTransition_AbsoluteTimeEventRule(TimeEventRule):

    pass
class umlTransition_RelativeTimeEventRule(TimeEventRule):

    pass
class umlTransition_NamedElement:

    pass
class EventRule:

    pass
class umlTransition_TimeEventRule(EventRule):

    def __init__(self, expr: str):
        self.expr = expr
        
        pass
    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr


class umlTransition_ChangeEventRule(EventRule):

    def __init__(self, exp: str):
        self.exp = exp
        
        pass
    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp: str):
        self.__exp = exp


class umlTransition_AnyReceiveEventRule(EventRule):

    def __init__(self, isAReceiveEvent: str):
        self.isAReceiveEvent = isAReceiveEvent
        
        pass
    @property
    def isAReceiveEvent(self):
        return self.__isAReceiveEvent

    @isAReceiveEvent.setter
    def isAReceiveEvent(self, isAReceiveEvent: str):
        self.__isAReceiveEvent = isAReceiveEvent


class umlTransition_CallOrSignalEventRule(EventRule):

    pass
class umlTransition_EffectRule:

    def __init__(self, kind: str, behaviorName: str, umlTransition_EffectRule: "umlTransition_TransitionRule" = None):
        self.kind = kind
        self.behaviorName = behaviorName
        self.umlTransition_EffectRule = umlTransition_EffectRule
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def behaviorName(self):
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName


    @property
    def umlTransition_EffectRule(self):
        return self.__umlTransition_EffectRule

    @umlTransition_EffectRule.setter
    def umlTransition_EffectRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTransition_EffectRule__umlTransition_EffectRule", None)
        self.__umlTransition_EffectRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlTransition_TransitionRule4"):
                opp_val = getattr(old_value, "umlTransition_TransitionRule4", None)
                if opp_val == self:
                    setattr(old_value, "umlTransition_TransitionRule4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlTransition_TransitionRule4"):
                opp_val = getattr(value, "umlTransition_TransitionRule4", None)
                setattr(value, "umlTransition_TransitionRule4", self)

class umlTransition_GuardRule:

    def __init__(self, constraint: str, umlTransition_GuardRule: "umlTransition_TransitionRule" = None):
        self.constraint = constraint
        self.umlTransition_GuardRule = umlTransition_GuardRule
        
        pass
    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint


    @property
    def umlTransition_GuardRule(self):
        return self.__umlTransition_GuardRule

    @umlTransition_GuardRule.setter
    def umlTransition_GuardRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlTransition_GuardRule__umlTransition_GuardRule", None)
        self.__umlTransition_GuardRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlTransition_TransitionRule2"):
                opp_val = getattr(old_value, "umlTransition_TransitionRule2", None)
                if opp_val == self:
                    setattr(old_value, "umlTransition_TransitionRule2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlTransition_TransitionRule2"):
                opp_val = getattr(value, "umlTransition_TransitionRule2", None)
                setattr(value, "umlTransition_TransitionRule2", self)

class umlTransition_EventRule:

    pass
class umlTransition_TransitionRule:

    pass