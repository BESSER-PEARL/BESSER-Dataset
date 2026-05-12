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
    every = "every"
    after = "after"


############################################
# Definition of Classes
############################################

class stext_State:

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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


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

class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

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
class BuiltinEventSpec:

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class stext_BuiltinEventSpec(EventSpec):

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
class stext_TransitionSpecification:

    pass
class Reaction:

    pass
class stext_TransitionReaction(Reaction):

    pass
class Declaration:

    pass
class stext_LocalReaction(Declaration, Reaction):

    pass
class TypeAlias:

    pass
class stext_TypeAliasDefinition(TypeAlias, Declaration):

    pass
class Operation:

    pass
class stext_OperationDefinition(Operation):

    pass
class stext_Expression:

    pass
class Property:

    pass
class stext_VariableDefinition(Property):

    pass
class Event:

    pass
class stext_EventDefinition(Event):

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