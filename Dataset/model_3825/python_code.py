from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"
class TimeEventType(Enum):
    after = "after"
    every = "every"


############################################
# Definition of Classes
############################################

class stext_State:

    pass
class Expression:

    pass
class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class BuiltinEventSpec:

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class Trigger:

    pass
class stext_DefaultTrigger(Trigger):

    pass
class stext_ReactionTrigger(Trigger):

    pass
class EventSpec:

    pass
class stext_BuiltinEventSpec(EventSpec):

    pass
class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

    pass
class ReactionProperty:

    pass
class stext_ExitPointSpec(ReactionProperty):

    def __init__(self, exitpoint: str):
        self.exitpoint = exitpoint
        
    @property
    def exitpoint(self) -> str:
        return self.__exitpoint

    @exitpoint.setter
    def exitpoint(self, exitpoint: str):
        self.__exitpoint = exitpoint

class stext_EntryPointSpec(ReactionProperty):

    def __init__(self, entrypoint: str):
        self.entrypoint = entrypoint
        
    @property
    def entrypoint(self) -> str:
        return self.__entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint: str):
        self.__entrypoint = entrypoint

class stext_Guard:

    pass
class Reaction:

    pass
class stext_LocalReaction(Reaction):

    pass
class Declaration:

    pass
class TypeAlias:

    pass
class stext_TypeAliasDefinition(Declaration, TypeAlias):

    pass
class Operation:

    pass
class stext_OperationDefinition(Operation):

    pass
class stext_Expression:

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, type: str, unit: str, stext_TimeEventSpec: "stext_Expression" = None):
        self.type = type
        self.unit = unit
        self.stext_TimeEventSpec = stext_TimeEventSpec
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def stext_TimeEventSpec(self):
        return self.__stext_TimeEventSpec

    @stext_TimeEventSpec.setter
    def stext_TimeEventSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_TimeEventSpec__stext_TimeEventSpec", None)
        self.__stext_TimeEventSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression15"):
                opp_val = getattr(old_value, "stext_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression15"):
                opp_val = getattr(value, "stext_Expression15", None)
                setattr(value, "stext_Expression15", self)

class stext_Package:

    pass
class NamedElement:

    pass
class StatechartScope:

    pass
class stext_InternalScope(StatechartScope):

    pass
class stext_ImportScope(StatechartScope):

    pass
class stext_InterfaceScope(NamedElement, StatechartScope):

    pass
class Scope:

    pass
class stext_SimpleScope(Scope):

    pass
class stext_StatechartScope(Scope):

    pass
class stext_TransitionReaction(Reaction):

    pass
class stext_Scope:

    pass
class ScopedElement:

    pass
class stext_TransitionSpecification:

    pass
class Property:

    pass
class stext_VariableDefinition(Property):

    pass
class Event:

    pass
class stext_EventDefinition(Event):

    pass
class stext_StatechartSpecification(ScopedElement):

    pass
class DefRoot:

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_DefRoot:

    pass
class stext_Root:

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StateSpecification:

    pass
class stext_StateRoot(DefRoot):

    pass