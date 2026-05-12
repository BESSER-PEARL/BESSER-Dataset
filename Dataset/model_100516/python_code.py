from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionOperation(Enum):
    any = "any"
    contains = "contains"
    containsAll = "containsAll"
    first = "first"
    get = "get"
    isEmpty = "isEmpty"
    last = "last"
    size = "size"
class ScenarioKind(Enum):
    assumption = "assumption"
    specification = "specification"
    requirement = "requirement"
    existential = "existential"


############################################
# Definition of Classes
############################################

class sml_VariableDeclaration:

    def __init__(self, name: str, sml_VariableDeclaration: "sml_Expression" = None, sml_VariableDeclaration131: "sml_VariableAssignment" = None):
        self.name = name
        self.sml_VariableDeclaration = sml_VariableDeclaration
        self.sml_VariableDeclaration131 = sml_VariableDeclaration131
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_VariableDeclaration131(self):
        return self.__sml_VariableDeclaration131

    @sml_VariableDeclaration131.setter
    def sml_VariableDeclaration131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_VariableDeclaration__sml_VariableDeclaration131", None)
        self.__sml_VariableDeclaration131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_VariableAssignment"):
                opp_val = getattr(old_value, "sml_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "sml_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_VariableAssignment"):
                opp_val = getattr(value, "sml_VariableAssignment", None)
                setattr(value, "sml_VariableAssignment", self)

    @property
    def sml_VariableDeclaration(self):
        return self.__sml_VariableDeclaration

    @sml_VariableDeclaration.setter
    def sml_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_VariableDeclaration__sml_VariableDeclaration", None)
        self.__sml_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Expression128"):
                opp_val = getattr(old_value, "sml_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "sml_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Expression128"):
                opp_val = getattr(value, "sml_Expression128", None)
                setattr(value, "sml_Expression128", self)

class ExpressionAndVariables:

    pass
class sml_ExpressionOrRegion:

    pass
class ExpressionOrRegion:

    pass
class sml_ExpressionAndVariables(ExpressionOrRegion):

    pass
class sml_ExpressionRegion(ExpressionOrRegion):

    pass
class sml_Message:

    pass
class Condition:

    pass
class sml_InterruptCondition(Condition):

    pass
class sml_ViolationCondition(Condition):

    pass
class sml_WaitCondition(Condition):

    def __init__(self, strict: bool, requested: bool):
        self.strict = strict
        self.requested = requested
        
        pass
    @property
    def requested(self):
        return self.__requested

    @requested.setter
    def requested(self, requested: bool):
        self.__requested = requested


    @property
    def strict(self):
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict


class sml_ConditionExpression:

    pass
class sml_LoopCondition:

    pass
class sml_CaseCondition:

    pass
class sml_Case:

    pass
class sml_Expression(ExpressionAndVariables):

    pass
class ParameterExpression:

    pass
class sml_VariableBindingParameter(ParameterExpression):

    pass
class sml_ExpressionParameter(ParameterExpression):

    pass
class sml_RandomParameter(ParameterExpression):

    pass
class sml_ParameterExpression:

    pass
class sml_ParameterBinding:

    pass
class sml_ConstraintBlock:

    pass
class sml_VariableExpression(ExpressionAndVariables):

    pass
class InteractionFragment:

    pass
class sml_Parallel(InteractionFragment):

    pass
class sml_ModalMessage(InteractionFragment):

    def __init__(self, strict: bool, requested: bool, sml_ModalMessage62: "sml_SmlETypedElement" = None, sml_ModalMessage65: set["sml_ParameterBinding"] = None, sml_ModalMessage: "sml_Role" = None, sml_ModalMessage59: "sml_Role" = None):
        self.strict = strict
        self.requested = requested
        self.sml_ModalMessage62 = sml_ModalMessage62
        self.sml_ModalMessage65 = sml_ModalMessage65 if sml_ModalMessage65 is not None else set()
        self.sml_ModalMessage = sml_ModalMessage
        self.sml_ModalMessage59 = sml_ModalMessage59
        
        pass
    @property
    def strict(self):
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict


    @property
    def requested(self):
        return self.__requested

    @requested.setter
    def requested(self, requested: bool):
        self.__requested = requested


    @property
    def sml_ModalMessage62(self):
        return self.__sml_ModalMessage62

    @sml_ModalMessage62.setter
    def sml_ModalMessage62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_ModalMessage__sml_ModalMessage62", None)
        self.__sml_ModalMessage62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_SmlETypedElement63"):
                opp_val = getattr(old_value, "sml_SmlETypedElement63", None)
                if opp_val == self:
                    setattr(old_value, "sml_SmlETypedElement63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_SmlETypedElement63"):
                opp_val = getattr(value, "sml_SmlETypedElement63", None)
                setattr(value, "sml_SmlETypedElement63", self)

    @property
    def sml_ModalMessage59(self):
        return self.__sml_ModalMessage59

    @sml_ModalMessage59.setter
    def sml_ModalMessage59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_ModalMessage__sml_ModalMessage59", None)
        self.__sml_ModalMessage59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Role60"):
                opp_val = getattr(old_value, "sml_Role60", None)
                if opp_val == self:
                    setattr(old_value, "sml_Role60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Role60"):
                opp_val = getattr(value, "sml_Role60", None)
                setattr(value, "sml_Role60", self)

    @property
    def sml_ModalMessage65(self):
        return self.__sml_ModalMessage65

    @sml_ModalMessage65.setter
    def sml_ModalMessage65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_ModalMessage__sml_ModalMessage65", None)
        self.__sml_ModalMessage65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_ParameterBinding"):
                    opp_val = getattr(item, "sml_ParameterBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_ParameterBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_ParameterBinding"):
                    opp_val = getattr(item, "sml_ParameterBinding", None)
                    
                    setattr(item, "sml_ParameterBinding", self)
                    

    @property
    def sml_ModalMessage(self):
        return self.__sml_ModalMessage

    @sml_ModalMessage.setter
    def sml_ModalMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_ModalMessage__sml_ModalMessage", None)
        self.__sml_ModalMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Role57"):
                opp_val = getattr(old_value, "sml_Role57", None)
                if opp_val == self:
                    setattr(old_value, "sml_Role57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Role57"):
                opp_val = getattr(value, "sml_Role57", None)
                setattr(value, "sml_Role57", self)

class sml_Loop(InteractionFragment):

    pass
class sml_Condition(InteractionFragment):

    pass
class sml_Alternative(InteractionFragment):

    pass
class sml_VariableFragment(InteractionFragment):

    pass
class sml_InteractionFragment:

    pass
class BindingExpression:

    pass
class sml_FeatureAccessBindingExpression(BindingExpression):

    pass
class sml_BindingExpression:

    pass
class sml_Interaction(InteractionFragment):

    pass
class sml_RoleBindingConstraint:

    pass
class sml_SmlEStructuralFeature:

    def __init__(self, name: str, sml_SmlEStructuralFeature: "sml_StructuralFeatureValue" = None):
        self.name = name
        self.sml_SmlEStructuralFeature = sml_SmlEStructuralFeature
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEStructuralFeature(self):
        return self.__sml_SmlEStructuralFeature

    @sml_SmlEStructuralFeature.setter
    def sml_SmlEStructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEStructuralFeature__sml_SmlEStructuralFeature", None)
        self.__sml_SmlEStructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_StructuralFeatureValue149"):
                opp_val = getattr(old_value, "sml_StructuralFeatureValue149", None)
                if opp_val == self:
                    setattr(old_value, "sml_StructuralFeatureValue149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_StructuralFeatureValue149"):
                opp_val = getattr(value, "sml_StructuralFeatureValue149", None)
                setattr(value, "sml_StructuralFeatureValue149", self)

class sml_SmlEClassifier:

    def __init__(self, name: str, sml_SmlEClassifier: "sml_TypedVariableDeclaration" = None):
        self.name = name
        self.sml_SmlEClassifier = sml_SmlEClassifier
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEClassifier(self):
        return self.__sml_SmlEClassifier

    @sml_SmlEClassifier.setter
    def sml_SmlEClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEClassifier__sml_SmlEClassifier", None)
        self.__sml_SmlEClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_TypedVariableDeclaration"):
                opp_val = getattr(old_value, "sml_TypedVariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "sml_TypedVariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_TypedVariableDeclaration"):
                opp_val = getattr(value, "sml_TypedVariableDeclaration", None)
                setattr(value, "sml_TypedVariableDeclaration", self)

class AbstractRanges:

    pass
class sml_StringRanges(AbstractRanges):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class sml_EnumRanges(AbstractRanges):

    pass
class sml_IntegerRanges(AbstractRanges):

    def __init__(self, min: int, max: int, values: int):
        self.min = min
        self.max = max
        self.values = values
        
        pass
    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min


    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max


    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values


class sml_AbstractRanges:

    pass
class sml_RangesForParameter:

    pass
class sml_Scenario:

    def __init__(self, singular: bool, kind: str, name: str, sml_Scenario: "sml_Collaboration" = None, sml_Scenario42: set["sml_RoleBindingConstraint"] = None, sml_Scenario44: "sml_Interaction" = None):
        self.singular = singular
        self.kind = kind
        self.name = name
        self.sml_Scenario = sml_Scenario
        self.sml_Scenario42 = sml_Scenario42 if sml_Scenario42 is not None else set()
        self.sml_Scenario44 = sml_Scenario44
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def singular(self):
        return self.__singular

    @singular.setter
    def singular(self, singular: bool):
        self.__singular = singular


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_Scenario42(self):
        return self.__sml_Scenario42

    @sml_Scenario42.setter
    def sml_Scenario42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Scenario__sml_Scenario42", None)
        self.__sml_Scenario42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_RoleBindingConstraint"):
                    opp_val = getattr(item, "sml_RoleBindingConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_RoleBindingConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_RoleBindingConstraint"):
                    opp_val = getattr(item, "sml_RoleBindingConstraint", None)
                    
                    setattr(item, "sml_RoleBindingConstraint", self)
                    

    @property
    def sml_Scenario44(self):
        return self.__sml_Scenario44

    @sml_Scenario44.setter
    def sml_Scenario44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Scenario__sml_Scenario44", None)
        self.__sml_Scenario44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Interaction"):
                opp_val = getattr(old_value, "sml_Interaction", None)
                if opp_val == self:
                    setattr(old_value, "sml_Interaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Interaction"):
                opp_val = getattr(value, "sml_Interaction", None)
                setattr(value, "sml_Interaction", self)

    @property
    def sml_Scenario(self):
        return self.__sml_Scenario

    @sml_Scenario.setter
    def sml_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Scenario__sml_Scenario", None)
        self.__sml_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Collaboration20"):
                opp_val = getattr(old_value, "sml_Collaboration20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Collaboration20"):
                opp_val = getattr(value, "sml_Collaboration20", None)
                if opp_val is None:
                    setattr(value, "sml_Collaboration20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_Role:

    def __init__(self, static: bool, name: str, sml_Role: "sml_Collaboration" = None, sml_Role47: "sml_RoleBindingConstraint" = None, sml_Role39: "sml_SmlEClass" = None, sml_Role57: "sml_ModalMessage" = None, sml_Role60: "sml_ModalMessage" = None, sml_Role105: "sml_Message" = None, sml_Role108: "sml_Message" = None):
        self.static = static
        self.name = name
        self.sml_Role = sml_Role
        self.sml_Role47 = sml_Role47
        self.sml_Role39 = sml_Role39
        self.sml_Role57 = sml_Role57
        self.sml_Role60 = sml_Role60
        self.sml_Role105 = sml_Role105
        self.sml_Role108 = sml_Role108
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_Role105(self):
        return self.__sml_Role105

    @sml_Role105.setter
    def sml_Role105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role105", None)
        self.__sml_Role105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Message104"):
                opp_val = getattr(old_value, "sml_Message104", None)
                if opp_val == self:
                    setattr(old_value, "sml_Message104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Message104"):
                opp_val = getattr(value, "sml_Message104", None)
                setattr(value, "sml_Message104", self)

    @property
    def sml_Role57(self):
        return self.__sml_Role57

    @sml_Role57.setter
    def sml_Role57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role57", None)
        self.__sml_Role57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_ModalMessage"):
                opp_val = getattr(old_value, "sml_ModalMessage", None)
                if opp_val == self:
                    setattr(old_value, "sml_ModalMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_ModalMessage"):
                opp_val = getattr(value, "sml_ModalMessage", None)
                setattr(value, "sml_ModalMessage", self)

    @property
    def sml_Role108(self):
        return self.__sml_Role108

    @sml_Role108.setter
    def sml_Role108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role108", None)
        self.__sml_Role108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Message107"):
                opp_val = getattr(old_value, "sml_Message107", None)
                if opp_val == self:
                    setattr(old_value, "sml_Message107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Message107"):
                opp_val = getattr(value, "sml_Message107", None)
                setattr(value, "sml_Message107", self)

    @property
    def sml_Role60(self):
        return self.__sml_Role60

    @sml_Role60.setter
    def sml_Role60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role60", None)
        self.__sml_Role60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_ModalMessage59"):
                opp_val = getattr(old_value, "sml_ModalMessage59", None)
                if opp_val == self:
                    setattr(old_value, "sml_ModalMessage59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_ModalMessage59"):
                opp_val = getattr(value, "sml_ModalMessage59", None)
                setattr(value, "sml_ModalMessage59", self)

    @property
    def sml_Role(self):
        return self.__sml_Role

    @sml_Role.setter
    def sml_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role", None)
        self.__sml_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Collaboration18"):
                opp_val = getattr(old_value, "sml_Collaboration18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Collaboration18"):
                opp_val = getattr(value, "sml_Collaboration18", None)
                if opp_val is None:
                    setattr(value, "sml_Collaboration18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_Role47(self):
        return self.__sml_Role47

    @sml_Role47.setter
    def sml_Role47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role47", None)
        self.__sml_Role47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_RoleBindingConstraint46"):
                opp_val = getattr(old_value, "sml_RoleBindingConstraint46", None)
                if opp_val == self:
                    setattr(old_value, "sml_RoleBindingConstraint46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_RoleBindingConstraint46"):
                opp_val = getattr(value, "sml_RoleBindingConstraint46", None)
                setattr(value, "sml_RoleBindingConstraint46", self)

    @property
    def sml_Role39(self):
        return self.__sml_Role39

    @sml_Role39.setter
    def sml_Role39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Role__sml_Role39", None)
        self.__sml_Role39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_SmlEClass40"):
                opp_val = getattr(old_value, "sml_SmlEClass40", None)
                if opp_val == self:
                    setattr(old_value, "sml_SmlEClass40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_SmlEClass40"):
                opp_val = getattr(value, "sml_SmlEClass40", None)
                setattr(value, "sml_SmlEClass40", self)

class sml_SmlEEnumLiteral:

    def __init__(self, name: str, sml_SmlEEnumLiteral: "sml_EnumRanges" = None, sml_SmlEEnumLiteral135: "sml_EnumValue" = None):
        self.name = name
        self.sml_SmlEEnumLiteral = sml_SmlEEnumLiteral
        self.sml_SmlEEnumLiteral135 = sml_SmlEEnumLiteral135
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEEnumLiteral135(self):
        return self.__sml_SmlEEnumLiteral135

    @sml_SmlEEnumLiteral135.setter
    def sml_SmlEEnumLiteral135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEEnumLiteral__sml_SmlEEnumLiteral135", None)
        self.__sml_SmlEEnumLiteral135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_EnumValue134"):
                opp_val = getattr(old_value, "sml_EnumValue134", None)
                if opp_val == self:
                    setattr(old_value, "sml_EnumValue134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_EnumValue134"):
                opp_val = getattr(value, "sml_EnumValue134", None)
                setattr(value, "sml_EnumValue134", self)

    @property
    def sml_SmlEEnumLiteral(self):
        return self.__sml_SmlEEnumLiteral

    @sml_SmlEEnumLiteral.setter
    def sml_SmlEEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEEnumLiteral__sml_SmlEEnumLiteral", None)
        self.__sml_SmlEEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_EnumRanges"):
                opp_val = getattr(old_value, "sml_EnumRanges", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_EnumRanges"):
                opp_val = getattr(value, "sml_EnumRanges", None)
                if opp_val is None:
                    setattr(value, "sml_EnumRanges", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_SmlEEnum:

    def __init__(self, name: str, sml_SmlEEnum: "sml_EnumValue" = None):
        self.name = name
        self.sml_SmlEEnum = sml_SmlEEnum
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEEnum(self):
        return self.__sml_SmlEEnum

    @sml_SmlEEnum.setter
    def sml_SmlEEnum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEEnum__sml_SmlEEnum", None)
        self.__sml_SmlEEnum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_EnumValue"):
                opp_val = getattr(old_value, "sml_EnumValue", None)
                if opp_val == self:
                    setattr(old_value, "sml_EnumValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_EnumValue"):
                opp_val = getattr(value, "sml_EnumValue", None)
                setattr(value, "sml_EnumValue", self)

class sml_Collaboration:

    def __init__(self, name: str, sml_Collaboration: "sml_Specification" = None, sml_Collaboration16: "sml_Specification" = None, sml_Collaboration18: set["sml_Role"] = None, sml_Collaboration20: set["sml_Scenario"] = None, sml_Collaboration22: set["sml_Import"] = None, sml_Collaboration25: set["sml_SmlEPackage"] = None):
        self.name = name
        self.sml_Collaboration = sml_Collaboration
        self.sml_Collaboration16 = sml_Collaboration16
        self.sml_Collaboration18 = sml_Collaboration18 if sml_Collaboration18 is not None else set()
        self.sml_Collaboration20 = sml_Collaboration20 if sml_Collaboration20 is not None else set()
        self.sml_Collaboration22 = sml_Collaboration22 if sml_Collaboration22 is not None else set()
        self.sml_Collaboration25 = sml_Collaboration25 if sml_Collaboration25 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_Collaboration16(self):
        return self.__sml_Collaboration16

    @sml_Collaboration16.setter
    def sml_Collaboration16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration16", None)
        self.__sml_Collaboration16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification15"):
                opp_val = getattr(old_value, "sml_Specification15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification15"):
                opp_val = getattr(value, "sml_Specification15", None)
                if opp_val is None:
                    setattr(value, "sml_Specification15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_Collaboration20(self):
        return self.__sml_Collaboration20

    @sml_Collaboration20.setter
    def sml_Collaboration20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration20", None)
        self.__sml_Collaboration20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Scenario"):
                    opp_val = getattr(item, "sml_Scenario", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Scenario", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Scenario"):
                    opp_val = getattr(item, "sml_Scenario", None)
                    
                    setattr(item, "sml_Scenario", self)
                    

    @property
    def sml_Collaboration22(self):
        return self.__sml_Collaboration22

    @sml_Collaboration22.setter
    def sml_Collaboration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration22", None)
        self.__sml_Collaboration22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Import23"):
                    opp_val = getattr(item, "sml_Import23", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Import23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Import23"):
                    opp_val = getattr(item, "sml_Import23", None)
                    
                    setattr(item, "sml_Import23", self)
                    

    @property
    def sml_Collaboration25(self):
        return self.__sml_Collaboration25

    @sml_Collaboration25.setter
    def sml_Collaboration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration25", None)
        self.__sml_Collaboration25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_SmlEPackage26"):
                    opp_val = getattr(item, "sml_SmlEPackage26", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_SmlEPackage26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_SmlEPackage26"):
                    opp_val = getattr(item, "sml_SmlEPackage26", None)
                    
                    setattr(item, "sml_SmlEPackage26", self)
                    

    @property
    def sml_Collaboration18(self):
        return self.__sml_Collaboration18

    @sml_Collaboration18.setter
    def sml_Collaboration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration18", None)
        self.__sml_Collaboration18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Role"):
                    opp_val = getattr(item, "sml_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Role"):
                    opp_val = getattr(item, "sml_Role", None)
                    
                    setattr(item, "sml_Role", self)
                    

    @property
    def sml_Collaboration(self):
        return self.__sml_Collaboration

    @sml_Collaboration.setter
    def sml_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Collaboration__sml_Collaboration", None)
        self.__sml_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification13"):
                opp_val = getattr(old_value, "sml_Specification13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification13"):
                opp_val = getattr(value, "sml_Specification13", None)
                if opp_val is None:
                    setattr(value, "sml_Specification13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_EventParameterRanges:

    pass
class sml_SmlETypedElement:

    def __init__(self, name: str, sml_SmlETypedElement: "sml_Specification" = None, sml_SmlETypedElement29: "sml_EventParameterRanges" = None, sml_SmlETypedElement34: "sml_RangesForParameter" = None, sml_SmlETypedElement63: "sml_ModalMessage" = None, sml_SmlETypedElement111: "sml_Message" = None):
        self.name = name
        self.sml_SmlETypedElement = sml_SmlETypedElement
        self.sml_SmlETypedElement29 = sml_SmlETypedElement29
        self.sml_SmlETypedElement34 = sml_SmlETypedElement34
        self.sml_SmlETypedElement63 = sml_SmlETypedElement63
        self.sml_SmlETypedElement111 = sml_SmlETypedElement111
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlETypedElement29(self):
        return self.__sml_SmlETypedElement29

    @sml_SmlETypedElement29.setter
    def sml_SmlETypedElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlETypedElement__sml_SmlETypedElement29", None)
        self.__sml_SmlETypedElement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_EventParameterRanges28"):
                opp_val = getattr(old_value, "sml_EventParameterRanges28", None)
                if opp_val == self:
                    setattr(old_value, "sml_EventParameterRanges28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_EventParameterRanges28"):
                opp_val = getattr(value, "sml_EventParameterRanges28", None)
                setattr(value, "sml_EventParameterRanges28", self)

    @property
    def sml_SmlETypedElement34(self):
        return self.__sml_SmlETypedElement34

    @sml_SmlETypedElement34.setter
    def sml_SmlETypedElement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlETypedElement__sml_SmlETypedElement34", None)
        self.__sml_SmlETypedElement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_RangesForParameter33"):
                opp_val = getattr(old_value, "sml_RangesForParameter33", None)
                if opp_val == self:
                    setattr(old_value, "sml_RangesForParameter33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_RangesForParameter33"):
                opp_val = getattr(value, "sml_RangesForParameter33", None)
                setattr(value, "sml_RangesForParameter33", self)

    @property
    def sml_SmlETypedElement(self):
        return self.__sml_SmlETypedElement

    @sml_SmlETypedElement.setter
    def sml_SmlETypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlETypedElement__sml_SmlETypedElement", None)
        self.__sml_SmlETypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification9"):
                opp_val = getattr(old_value, "sml_Specification9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification9"):
                opp_val = getattr(value, "sml_Specification9", None)
                if opp_val is None:
                    setattr(value, "sml_Specification9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_SmlETypedElement111(self):
        return self.__sml_SmlETypedElement111

    @sml_SmlETypedElement111.setter
    def sml_SmlETypedElement111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlETypedElement__sml_SmlETypedElement111", None)
        self.__sml_SmlETypedElement111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Message110"):
                opp_val = getattr(old_value, "sml_Message110", None)
                if opp_val == self:
                    setattr(old_value, "sml_Message110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Message110"):
                opp_val = getattr(value, "sml_Message110", None)
                setattr(value, "sml_Message110", self)

    @property
    def sml_SmlETypedElement63(self):
        return self.__sml_SmlETypedElement63

    @sml_SmlETypedElement63.setter
    def sml_SmlETypedElement63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlETypedElement__sml_SmlETypedElement63", None)
        self.__sml_SmlETypedElement63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_ModalMessage62"):
                opp_val = getattr(old_value, "sml_ModalMessage62", None)
                if opp_val == self:
                    setattr(old_value, "sml_ModalMessage62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_ModalMessage62"):
                opp_val = getattr(value, "sml_ModalMessage62", None)
                setattr(value, "sml_ModalMessage62", self)

class sml_SmlEClass:

    def __init__(self, name: str, sml_SmlEClass: "sml_Specification" = None, sml_SmlEClass7: "sml_Specification" = None, sml_SmlEClass40: "sml_Role" = None):
        self.name = name
        self.sml_SmlEClass = sml_SmlEClass
        self.sml_SmlEClass7 = sml_SmlEClass7
        self.sml_SmlEClass40 = sml_SmlEClass40
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEClass(self):
        return self.__sml_SmlEClass

    @sml_SmlEClass.setter
    def sml_SmlEClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEClass__sml_SmlEClass", None)
        self.__sml_SmlEClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification4"):
                opp_val = getattr(old_value, "sml_Specification4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification4"):
                opp_val = getattr(value, "sml_Specification4", None)
                if opp_val is None:
                    setattr(value, "sml_Specification4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_SmlEClass40(self):
        return self.__sml_SmlEClass40

    @sml_SmlEClass40.setter
    def sml_SmlEClass40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEClass__sml_SmlEClass40", None)
        self.__sml_SmlEClass40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Role39"):
                opp_val = getattr(old_value, "sml_Role39", None)
                if opp_val == self:
                    setattr(old_value, "sml_Role39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Role39"):
                opp_val = getattr(value, "sml_Role39", None)
                setattr(value, "sml_Role39", self)

    @property
    def sml_SmlEClass7(self):
        return self.__sml_SmlEClass7

    @sml_SmlEClass7.setter
    def sml_SmlEClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEClass__sml_SmlEClass7", None)
        self.__sml_SmlEClass7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification6"):
                opp_val = getattr(old_value, "sml_Specification6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification6"):
                opp_val = getattr(value, "sml_Specification6", None)
                if opp_val is None:
                    setattr(value, "sml_Specification6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_SmlEPackage:

    def __init__(self, name: str, sml_SmlEPackage: "sml_Specification" = None, sml_SmlEPackage26: "sml_Collaboration" = None, sml_SmlEPackage119: "sml_Document" = None):
        self.name = name
        self.sml_SmlEPackage = sml_SmlEPackage
        self.sml_SmlEPackage26 = sml_SmlEPackage26
        self.sml_SmlEPackage119 = sml_SmlEPackage119
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_SmlEPackage119(self):
        return self.__sml_SmlEPackage119

    @sml_SmlEPackage119.setter
    def sml_SmlEPackage119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEPackage__sml_SmlEPackage119", None)
        self.__sml_SmlEPackage119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Document118"):
                opp_val = getattr(old_value, "sml_Document118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Document118"):
                opp_val = getattr(value, "sml_Document118", None)
                if opp_val is None:
                    setattr(value, "sml_Document118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_SmlEPackage(self):
        return self.__sml_SmlEPackage

    @sml_SmlEPackage.setter
    def sml_SmlEPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEPackage__sml_SmlEPackage", None)
        self.__sml_SmlEPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification2"):
                opp_val = getattr(old_value, "sml_Specification2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification2"):
                opp_val = getattr(value, "sml_Specification2", None)
                if opp_val is None:
                    setattr(value, "sml_Specification2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_SmlEPackage26(self):
        return self.__sml_SmlEPackage26

    @sml_SmlEPackage26.setter
    def sml_SmlEPackage26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_SmlEPackage__sml_SmlEPackage26", None)
        self.__sml_SmlEPackage26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Collaboration25"):
                opp_val = getattr(old_value, "sml_Collaboration25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Collaboration25"):
                opp_val = getattr(value, "sml_Collaboration25", None)
                if opp_val is None:
                    setattr(value, "sml_Collaboration25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_Import:

    def __init__(self, importURI: str, sml_Import: "sml_Specification" = None, sml_Import23: "sml_Collaboration" = None, sml_Import116: "sml_Document" = None):
        self.importURI = importURI
        self.sml_Import = sml_Import
        self.sml_Import23 = sml_Import23
        self.sml_Import116 = sml_Import116
        
        pass
    @property
    def importURI(self):
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI


    @property
    def sml_Import(self):
        return self.__sml_Import

    @sml_Import.setter
    def sml_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Import__sml_Import", None)
        self.__sml_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Specification"):
                opp_val = getattr(old_value, "sml_Specification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Specification"):
                opp_val = getattr(value, "sml_Specification", None)
                if opp_val is None:
                    setattr(value, "sml_Specification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_Import23(self):
        return self.__sml_Import23

    @sml_Import23.setter
    def sml_Import23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Import__sml_Import23", None)
        self.__sml_Import23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Collaboration22"):
                opp_val = getattr(old_value, "sml_Collaboration22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Collaboration22"):
                opp_val = getattr(value, "sml_Collaboration22", None)
                if opp_val is None:
                    setattr(value, "sml_Collaboration22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sml_Import116(self):
        return self.__sml_Import116

    @sml_Import116.setter
    def sml_Import116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Import__sml_Import116", None)
        self.__sml_Import116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Document"):
                opp_val = getattr(old_value, "sml_Document", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Document"):
                opp_val = getattr(value, "sml_Document", None)
                if opp_val is None:
                    setattr(value, "sml_Document", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sml_StructuralFeatureValue:

    pass
class sml_CollectionAccess:

    def __init__(self, collectionOperation: str, sml_CollectionAccess: "sml_Expression" = None, sml_CollectionAccess147: "sml_FeatureAccess" = None):
        self.collectionOperation = collectionOperation
        self.sml_CollectionAccess = sml_CollectionAccess
        self.sml_CollectionAccess147 = sml_CollectionAccess147
        
        pass
    @property
    def collectionOperation(self):
        return self.__collectionOperation

    @collectionOperation.setter
    def collectionOperation(self, collectionOperation: str):
        self.__collectionOperation = collectionOperation


    @property
    def sml_CollectionAccess147(self):
        return self.__sml_CollectionAccess147

    @sml_CollectionAccess147.setter
    def sml_CollectionAccess147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_CollectionAccess__sml_CollectionAccess147", None)
        self.__sml_CollectionAccess147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_FeatureAccess146"):
                opp_val = getattr(old_value, "sml_FeatureAccess146", None)
                if opp_val == self:
                    setattr(old_value, "sml_FeatureAccess146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_FeatureAccess146"):
                opp_val = getattr(value, "sml_FeatureAccess146", None)
                setattr(value, "sml_FeatureAccess146", self)

    @property
    def sml_CollectionAccess(self):
        return self.__sml_CollectionAccess

    @sml_CollectionAccess.setter
    def sml_CollectionAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_CollectionAccess__sml_CollectionAccess", None)
        self.__sml_CollectionAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Expression139"):
                opp_val = getattr(old_value, "sml_Expression139", None)
                if opp_val == self:
                    setattr(old_value, "sml_Expression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Expression139"):
                opp_val = getattr(value, "sml_Expression139", None)
                setattr(value, "sml_Expression139", self)

class sml_Variable:

    def __init__(self, name: str, sml_Variable: "sml_VariableValue" = None, sml_Variable142: "sml_FeatureAccess" = None):
        self.name = name
        self.sml_Variable = sml_Variable
        self.sml_Variable142 = sml_Variable142
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_Variable142(self):
        return self.__sml_Variable142

    @sml_Variable142.setter
    def sml_Variable142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Variable__sml_Variable142", None)
        self.__sml_Variable142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_FeatureAccess141"):
                opp_val = getattr(old_value, "sml_FeatureAccess141", None)
                if opp_val == self:
                    setattr(old_value, "sml_FeatureAccess141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_FeatureAccess141"):
                opp_val = getattr(value, "sml_FeatureAccess141", None)
                setattr(value, "sml_FeatureAccess141", self)

    @property
    def sml_Variable(self):
        return self.__sml_Variable

    @sml_Variable.setter
    def sml_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Variable__sml_Variable", None)
        self.__sml_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_VariableValue137"):
                opp_val = getattr(old_value, "sml_VariableValue137", None)
                if opp_val == self:
                    setattr(old_value, "sml_VariableValue137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_VariableValue137"):
                opp_val = getattr(value, "sml_VariableValue137", None)
                setattr(value, "sml_VariableValue137", self)

class sml_Document:

    pass
class Value:

    pass
class sml_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class sml_EnumValue(Value):

    pass
class sml_FeatureAccess(Value):

    pass
class sml_NullValue(Value):

    pass
class sml_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sml_VariableValue(Value):

    pass
class sml_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Expression:

    pass
class sml_BinaryOperationExpression(Expression):

    def __init__(self, operator: str, sml_BinaryOperationExpression: "sml_Expression" = None, sml_BinaryOperationExpression153: "sml_Expression" = None):
        self.operator = operator
        self.sml_BinaryOperationExpression = sml_BinaryOperationExpression
        self.sml_BinaryOperationExpression153 = sml_BinaryOperationExpression153
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def sml_BinaryOperationExpression153(self):
        return self.__sml_BinaryOperationExpression153

    @sml_BinaryOperationExpression153.setter
    def sml_BinaryOperationExpression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_BinaryOperationExpression__sml_BinaryOperationExpression153", None)
        self.__sml_BinaryOperationExpression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Expression154"):
                opp_val = getattr(old_value, "sml_Expression154", None)
                if opp_val == self:
                    setattr(old_value, "sml_Expression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Expression154"):
                opp_val = getattr(value, "sml_Expression154", None)
                setattr(value, "sml_Expression154", self)

    @property
    def sml_BinaryOperationExpression(self):
        return self.__sml_BinaryOperationExpression

    @sml_BinaryOperationExpression.setter
    def sml_BinaryOperationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_BinaryOperationExpression__sml_BinaryOperationExpression", None)
        self.__sml_BinaryOperationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Expression151"):
                opp_val = getattr(old_value, "sml_Expression151", None)
                if opp_val == self:
                    setattr(old_value, "sml_Expression151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Expression151"):
                opp_val = getattr(value, "sml_Expression151", None)
                setattr(value, "sml_Expression151", self)

class sml_UnaryOperationExpression(Expression):

    def __init__(self, operator: str, sml_UnaryOperationExpression: "sml_Expression" = None):
        self.operator = operator
        self.sml_UnaryOperationExpression = sml_UnaryOperationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def sml_UnaryOperationExpression(self):
        return self.__sml_UnaryOperationExpression

    @sml_UnaryOperationExpression.setter
    def sml_UnaryOperationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_UnaryOperationExpression__sml_UnaryOperationExpression", None)
        self.__sml_UnaryOperationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_Expression156"):
                opp_val = getattr(old_value, "sml_Expression156", None)
                if opp_val == self:
                    setattr(old_value, "sml_Expression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_Expression156"):
                opp_val = getattr(value, "sml_Expression156", None)
                setattr(value, "sml_Expression156", self)

class sml_Value(Expression):

    pass
class VariableExpression:

    pass
class sml_TypedVariableDeclaration(VariableExpression):

    def __init__(self, name: str, sml_TypedVariableDeclaration: "sml_SmlEClassifier" = None):
        self.name = name
        self.sml_TypedVariableDeclaration = sml_TypedVariableDeclaration
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_TypedVariableDeclaration(self):
        return self.__sml_TypedVariableDeclaration

    @sml_TypedVariableDeclaration.setter
    def sml_TypedVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_TypedVariableDeclaration__sml_TypedVariableDeclaration", None)
        self.__sml_TypedVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sml_SmlEClassifier"):
                opp_val = getattr(old_value, "sml_SmlEClassifier", None)
                if opp_val == self:
                    setattr(old_value, "sml_SmlEClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sml_SmlEClassifier"):
                opp_val = getattr(value, "sml_SmlEClassifier", None)
                setattr(value, "sml_SmlEClassifier", self)

class sml_VariableAssignment(VariableExpression):

    pass
class sml_Specification:

    def __init__(self, name: str, sml_Specification: set["sml_Import"] = None, sml_Specification2: set["sml_SmlEPackage"] = None, sml_Specification4: set["sml_SmlEClass"] = None, sml_Specification6: set["sml_SmlEClass"] = None, sml_Specification9: set["sml_SmlETypedElement"] = None, sml_Specification11: set["sml_EventParameterRanges"] = None, sml_Specification13: set["sml_Collaboration"] = None, sml_Specification15: set["sml_Collaboration"] = None):
        self.name = name
        self.sml_Specification = sml_Specification if sml_Specification is not None else set()
        self.sml_Specification2 = sml_Specification2 if sml_Specification2 is not None else set()
        self.sml_Specification4 = sml_Specification4 if sml_Specification4 is not None else set()
        self.sml_Specification6 = sml_Specification6 if sml_Specification6 is not None else set()
        self.sml_Specification9 = sml_Specification9 if sml_Specification9 is not None else set()
        self.sml_Specification11 = sml_Specification11 if sml_Specification11 is not None else set()
        self.sml_Specification13 = sml_Specification13 if sml_Specification13 is not None else set()
        self.sml_Specification15 = sml_Specification15 if sml_Specification15 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sml_Specification13(self):
        return self.__sml_Specification13

    @sml_Specification13.setter
    def sml_Specification13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification13", None)
        self.__sml_Specification13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Collaboration"):
                    opp_val = getattr(item, "sml_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Collaboration"):
                    opp_val = getattr(item, "sml_Collaboration", None)
                    
                    setattr(item, "sml_Collaboration", self)
                    

    @property
    def sml_Specification(self):
        return self.__sml_Specification

    @sml_Specification.setter
    def sml_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification", None)
        self.__sml_Specification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Import"):
                    opp_val = getattr(item, "sml_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Import"):
                    opp_val = getattr(item, "sml_Import", None)
                    
                    setattr(item, "sml_Import", self)
                    

    @property
    def sml_Specification2(self):
        return self.__sml_Specification2

    @sml_Specification2.setter
    def sml_Specification2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification2", None)
        self.__sml_Specification2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_SmlEPackage"):
                    opp_val = getattr(item, "sml_SmlEPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_SmlEPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_SmlEPackage"):
                    opp_val = getattr(item, "sml_SmlEPackage", None)
                    
                    setattr(item, "sml_SmlEPackage", self)
                    

    @property
    def sml_Specification6(self):
        return self.__sml_Specification6

    @sml_Specification6.setter
    def sml_Specification6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification6", None)
        self.__sml_Specification6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_SmlEClass7"):
                    opp_val = getattr(item, "sml_SmlEClass7", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_SmlEClass7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_SmlEClass7"):
                    opp_val = getattr(item, "sml_SmlEClass7", None)
                    
                    setattr(item, "sml_SmlEClass7", self)
                    

    @property
    def sml_Specification4(self):
        return self.__sml_Specification4

    @sml_Specification4.setter
    def sml_Specification4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification4", None)
        self.__sml_Specification4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_SmlEClass"):
                    opp_val = getattr(item, "sml_SmlEClass", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_SmlEClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_SmlEClass"):
                    opp_val = getattr(item, "sml_SmlEClass", None)
                    
                    setattr(item, "sml_SmlEClass", self)
                    

    @property
    def sml_Specification9(self):
        return self.__sml_Specification9

    @sml_Specification9.setter
    def sml_Specification9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification9", None)
        self.__sml_Specification9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_SmlETypedElement"):
                    opp_val = getattr(item, "sml_SmlETypedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_SmlETypedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_SmlETypedElement"):
                    opp_val = getattr(item, "sml_SmlETypedElement", None)
                    
                    setattr(item, "sml_SmlETypedElement", self)
                    

    @property
    def sml_Specification11(self):
        return self.__sml_Specification11

    @sml_Specification11.setter
    def sml_Specification11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification11", None)
        self.__sml_Specification11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_EventParameterRanges"):
                    opp_val = getattr(item, "sml_EventParameterRanges", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_EventParameterRanges", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_EventParameterRanges"):
                    opp_val = getattr(item, "sml_EventParameterRanges", None)
                    
                    setattr(item, "sml_EventParameterRanges", self)
                    

    @property
    def sml_Specification15(self):
        return self.__sml_Specification15

    @sml_Specification15.setter
    def sml_Specification15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sml_Specification__sml_Specification15", None)
        self.__sml_Specification15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sml_Collaboration16"):
                    opp_val = getattr(item, "sml_Collaboration16", None)
                    
                    if opp_val == self:
                        setattr(item, "sml_Collaboration16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sml_Collaboration16"):
                    opp_val = getattr(item, "sml_Collaboration16", None)
                    
                    setattr(item, "sml_Collaboration16", self)
                    
