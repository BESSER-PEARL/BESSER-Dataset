from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class TimeEventType(Enum):
    after = "after"
    every = "every"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"


############################################
# Definition of Classes
############################################

class BuiltinEventSpec:

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class stext_State:

    pass
class Expression:

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class Trigger:

    pass
class stext_DefaultTrigger(Trigger):

    pass
class stext_ReactionTrigger(Trigger):

    pass
class stext_Import:

    def __init__(self, importedNamespace: str, stext_Import: "stext_ImportScope" = None):
        self.importedNamespace = importedNamespace
        self.stext_Import = stext_Import
        
        pass
    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


    @property
    def stext_Import(self):
        return self.__stext_Import

    @stext_Import.setter
    def stext_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_Import__stext_Import", None)
        self.__stext_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_ImportScope"):
                opp_val = getattr(old_value, "stext_ImportScope", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_ImportScope"):
                opp_val = getattr(value, "stext_ImportScope", None)
                if opp_val is None:
                    setattr(value, "stext_ImportScope", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class StatechartScope:

    pass
class stext_ImportScope(StatechartScope):

    pass
class stext_InternalScope(StatechartScope):

    pass
class stext_InterfaceScope(StatechartScope, NamedElement):

    pass
class Scope:

    pass
class stext_SimpleScope(Scope):

    pass
class stext_StatechartScope(Scope):

    pass
class stext_Scope:

    pass
class ScopedElement:

    pass
class EventSpec:

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, type: str, unit: str, stext_TimeEventSpec: "stext_Expression" = None):
        self.type = type
        self.unit = unit
        self.stext_TimeEventSpec = stext_TimeEventSpec
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def type(self):
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
        
        pass
    @property
    def exitpoint(self):
        return self.__exitpoint

    @exitpoint.setter
    def exitpoint(self, exitpoint: str):
        self.__exitpoint = exitpoint


class stext_EntryPointSpec(ReactionProperty):

    def __init__(self, entrypoint: str):
        self.entrypoint = entrypoint
        
        pass
    @property
    def entrypoint(self):
        return self.__entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint: str):
        self.__entrypoint = entrypoint


class stext_Guard:

    pass
class Reaction:

    pass
class stext_TransitionReaction(Reaction):

    pass
class Operation:

    pass
class Declaration:

    pass
class stext_LocalReaction(Reaction, Declaration):

    pass
class stext_OperationDefinition(Operation, Declaration):

    pass
class stext_Expression:

    pass
class Property:

    pass
class Variable:

    pass
class stext_VariableDefinition(Variable, Property):

    def __init__(self, readonly: bool, external: bool, stext_VariableDefinition: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.stext_VariableDefinition = stext_VariableDefinition
        
        pass
    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly


    @property
    def external(self):
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external


    @property
    def stext_VariableDefinition(self):
        return self.__stext_VariableDefinition

    @stext_VariableDefinition.setter
    def stext_VariableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_VariableDefinition__stext_VariableDefinition", None)
        self.__stext_VariableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression"):
                opp_val = getattr(old_value, "stext_Expression", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression"):
                opp_val = getattr(value, "stext_Expression", None)
                setattr(value, "stext_Expression", self)

class Event:

    pass
class stext_EventDefinition(Event):

    def __init__(self, direction: str):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class stext_TransitionSpecification:

    pass
class stext_StateSpecification:

    pass
class stext_StatechartSpecification(ScopedElement):

    pass
class DefRoot:

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StateRoot(DefRoot):

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_DefRoot:

    pass
class stext_Root:

    pass