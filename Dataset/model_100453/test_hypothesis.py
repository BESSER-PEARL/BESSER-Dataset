import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stext_State,
    stext_EObject,
    Expression,
    stext_PrimitiveValueExpression,
    stext_NumericalUnaryExpression,
    stext_BitwiseAndExpression,
    stext_NumericalAddSubtractExpression,
    stext_ParenthesizedExpression,
    stext_BitwiseOrExpression,
    stext_AssignmentExpression,
    stext_BitwiseXorExpression,
    stext_ElementReferenceExpression,
    stext_LogicalRelationExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_LogicalNotExpression,
    stext_EventValueReferenceExpression,
    stext_FeatureCall,
    stext_LogicalAndExpression,
    stext_ShiftExpression,
    stext_ActiveStateReferenceExpression,
    stext_EventRaisingExpression,
    Effect,
    stext_ReactionEffect,
    Trigger,
    stext_ReactionTrigger,
    stext_LogicalOrExpression,
    stext_ConditionalExpression,
    EventSpec,
    stext_TimeEventSpec,
    stext_RegularEventSpec,
    stext_EventSpec,
    Reaction,
    Operation,
    Declaration,
    stext_LocalReaction,
    stext_OperationDefinition,
    Literal,
    stext_RealLiteral,
    stext_StringLiteral,
    stext_HexLiteral,
    stext_IntLiteral,
    stext_BoolLiteral,
    stext_Literal,
    Statement,
    stext_Expression,
    BuiltinEventSpec,
    stext_AlwaysEvent,
    stext_DefaultEvent,
    stext_OnCycleEvent,
    stext_ExitEvent,
    stext_EntryEvent,
    stext_BuiltinEventSpec,
    stext_Scope,
    ScopedElement,
    stext_TransitionSpecification,
    stext_StateSpecification,
    stext_StatechartSpecification,
    Property,
    Variable,
    stext_VariableDefinition,
    Event,
    stext_EventDefinition,
    NamedElement,
    StatechartScope,
    stext_InternalScope,
    stext_InterfaceScope,
    Scope,
    stext_SimpleScope,
    stext_StatechartScope,
    stext_TransitionReaction,
    DefRoot,
    stext_TransitionRoot,
    stext_StateRoot,
    stext_StatechartRoot,
    stext_DefRoot,
    stext_Root,
    Direction,
    ShiftOperator,
    RelationalOperator,
    AssignmentOperator,
    MultiplicativeOperator,
    AdditiveOperator,
    UnaryOperator,
    TimeEventType,
    TimeUnit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stext_state_is_not_abstract():
    assert not inspect.isabstract(stext_State)


def test_stext_state_constructor_exists():
    assert callable(stext_State.__init__)


def test_stext_state_constructor_args():
    sig = inspect.signature(stext_State.__init__)
    params = list(sig.parameters.keys())



def test_stext_eobject_is_not_abstract():
    assert not inspect.isabstract(stext_EObject)


def test_stext_eobject_constructor_exists():
    assert callable(stext_EObject.__init__)


def test_stext_eobject_constructor_args():
    sig = inspect.signature(stext_EObject.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext_primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(stext_PrimitiveValueExpression)


def test_stext_primitivevalueexpression_constructor_exists():
    assert callable(stext_PrimitiveValueExpression.__init__)


def test_stext_primitivevalueexpression_constructor_args():
    sig = inspect.signature(stext_PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_numericalunaryexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalUnaryExpression)


def test_stext_numericalunaryexpression_constructor_exists():
    assert callable(stext_NumericalUnaryExpression.__init__)


def test_stext_numericalunaryexpression_constructor_args():
    sig = inspect.signature(stext_NumericalUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_numericalunaryexpression_has_operator():
    assert hasattr(stext_NumericalUnaryExpression, "operator")
    descriptor = None
    for klass in stext_NumericalUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseAndExpression)


def test_stext_bitwiseandexpression_constructor_exists():
    assert callable(stext_BitwiseAndExpression.__init__)


def test_stext_bitwiseandexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_numericaladdsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalAddSubtractExpression)


def test_stext_numericaladdsubtractexpression_constructor_exists():
    assert callable(stext_NumericalAddSubtractExpression.__init__)


def test_stext_numericaladdsubtractexpression_constructor_args():
    sig = inspect.signature(stext_NumericalAddSubtractExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_numericaladdsubtractexpression_has_operator():
    assert hasattr(stext_NumericalAddSubtractExpression, "operator")
    descriptor = None
    for klass in stext_NumericalAddSubtractExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ParenthesizedExpression)


def test_stext_parenthesizedexpression_constructor_exists():
    assert callable(stext_ParenthesizedExpression.__init__)


def test_stext_parenthesizedexpression_constructor_args():
    sig = inspect.signature(stext_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseOrExpression)


def test_stext_bitwiseorexpression_constructor_exists():
    assert callable(stext_BitwiseOrExpression.__init__)


def test_stext_bitwiseorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(stext_AssignmentExpression)


def test_stext_assignmentexpression_constructor_exists():
    assert callable(stext_AssignmentExpression.__init__)


def test_stext_assignmentexpression_constructor_args():
    sig = inspect.signature(stext_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_assignmentexpression_has_operator():
    assert hasattr(stext_AssignmentExpression, "operator")
    descriptor = None
    for klass in stext_AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseXorExpression)


def test_stext_bitwisexorexpression_constructor_exists():
    assert callable(stext_BitwiseXorExpression.__init__)


def test_stext_bitwisexorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_elementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ElementReferenceExpression)


def test_stext_elementreferenceexpression_constructor_exists():
    assert callable(stext_ElementReferenceExpression.__init__)


def test_stext_elementreferenceexpression_constructor_args():
    sig = inspect.signature(stext_ElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationCall" in params, "Missing parameter 'operationCall'"

def test_stext_elementreferenceexpression_has_operationCall():
    assert hasattr(stext_ElementReferenceExpression, "operationCall")
    descriptor = None
    for klass in stext_ElementReferenceExpression.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)



def test_stext_logicalrelationexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalRelationExpression)


def test_stext_logicalrelationexpression_constructor_exists():
    assert callable(stext_LogicalRelationExpression.__init__)


def test_stext_logicalrelationexpression_constructor_args():
    sig = inspect.signature(stext_LogicalRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_logicalrelationexpression_has_operator():
    assert hasattr(stext_LogicalRelationExpression, "operator")
    descriptor = None
    for klass in stext_LogicalRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_numericalmultiplydivideexpression_is_not_abstract():
    assert not inspect.isabstract(stext_NumericalMultiplyDivideExpression)


def test_stext_numericalmultiplydivideexpression_constructor_exists():
    assert callable(stext_NumericalMultiplyDivideExpression.__init__)


def test_stext_numericalmultiplydivideexpression_constructor_args():
    sig = inspect.signature(stext_NumericalMultiplyDivideExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_numericalmultiplydivideexpression_has_operator():
    assert hasattr(stext_NumericalMultiplyDivideExpression, "operator")
    descriptor = None
    for klass in stext_NumericalMultiplyDivideExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalNotExpression)


def test_stext_logicalnotexpression_constructor_exists():
    assert callable(stext_LogicalNotExpression.__init__)


def test_stext_logicalnotexpression_constructor_args():
    sig = inspect.signature(stext_LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventvaluereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventValueReferenceExpression)


def test_stext_eventvaluereferenceexpression_constructor_exists():
    assert callable(stext_EventValueReferenceExpression.__init__)


def test_stext_eventvaluereferenceexpression_constructor_args():
    sig = inspect.signature(stext_EventValueReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_featurecall_is_not_abstract():
    assert not inspect.isabstract(stext_FeatureCall)


def test_stext_featurecall_constructor_exists():
    assert callable(stext_FeatureCall.__init__)


def test_stext_featurecall_constructor_args():
    sig = inspect.signature(stext_FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationCall" in params, "Missing parameter 'operationCall'"

def test_stext_featurecall_has_operationCall():
    assert hasattr(stext_FeatureCall, "operationCall")
    descriptor = None
    for klass in stext_FeatureCall.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)



def test_stext_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalAndExpression)


def test_stext_logicalandexpression_constructor_exists():
    assert callable(stext_LogicalAndExpression.__init__)


def test_stext_logicalandexpression_constructor_args():
    sig = inspect.signature(stext_LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ShiftExpression)


def test_stext_shiftexpression_constructor_exists():
    assert callable(stext_ShiftExpression.__init__)


def test_stext_shiftexpression_constructor_args():
    sig = inspect.signature(stext_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_shiftexpression_has_operator():
    assert hasattr(stext_ShiftExpression, "operator")
    descriptor = None
    for klass in stext_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_stext_activestatereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ActiveStateReferenceExpression)


def test_stext_activestatereferenceexpression_constructor_exists():
    assert callable(stext_ActiveStateReferenceExpression.__init__)


def test_stext_activestatereferenceexpression_constructor_args():
    sig = inspect.signature(stext_ActiveStateReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventraisingexpression_is_not_abstract():
    assert not inspect.isabstract(stext_EventRaisingExpression)


def test_stext_eventraisingexpression_constructor_exists():
    assert callable(stext_EventRaisingExpression.__init__)


def test_stext_eventraisingexpression_constructor_args():
    sig = inspect.signature(stext_EventRaisingExpression.__init__)
    params = list(sig.parameters.keys())



def test_effect_is_not_abstract():
    assert not inspect.isabstract(Effect)


def test_effect_constructor_exists():
    assert callable(Effect.__init__)


def test_effect_constructor_args():
    sig = inspect.signature(Effect.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactioneffect_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionEffect)


def test_stext_reactioneffect_constructor_exists():
    assert callable(stext_ReactionEffect.__init__)


def test_stext_reactioneffect_constructor_args():
    sig = inspect.signature(stext_ReactionEffect.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactiontrigger_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionTrigger)


def test_stext_reactiontrigger_constructor_exists():
    assert callable(stext_ReactionTrigger.__init__)


def test_stext_reactiontrigger_constructor_args():
    sig = inspect.signature(stext_ReactionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_stext_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalOrExpression)


def test_stext_logicalorexpression_constructor_exists():
    assert callable(stext_LogicalOrExpression.__init__)


def test_stext_logicalorexpression_constructor_args():
    sig = inspect.signature(stext_LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ConditionalExpression)


def test_stext_conditionalexpression_constructor_exists():
    assert callable(stext_ConditionalExpression.__init__)


def test_stext_conditionalexpression_constructor_args():
    sig = inspect.signature(stext_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_timeeventspec_is_not_abstract():
    assert not inspect.isabstract(stext_TimeEventSpec)


def test_stext_timeeventspec_constructor_exists():
    assert callable(stext_TimeEventSpec.__init__)


def test_stext_timeeventspec_constructor_args():
    sig = inspect.signature(stext_TimeEventSpec.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_stext_timeeventspec_has_type():
    assert hasattr(stext_TimeEventSpec, "type")
    descriptor = None
    for klass in stext_TimeEventSpec.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stext_timeeventspec_has_unit():
    assert hasattr(stext_TimeEventSpec, "unit")
    descriptor = None
    for klass in stext_TimeEventSpec.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_stext_regulareventspec_is_not_abstract():
    assert not inspect.isabstract(stext_RegularEventSpec)


def test_stext_regulareventspec_constructor_exists():
    assert callable(stext_RegularEventSpec.__init__)


def test_stext_regulareventspec_constructor_args():
    sig = inspect.signature(stext_RegularEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventspec_is_not_abstract():
    assert not inspect.isabstract(stext_EventSpec)


def test_stext_eventspec_constructor_exists():
    assert callable(stext_EventSpec.__init__)


def test_stext_eventspec_constructor_args():
    sig = inspect.signature(stext_EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_stext_localreaction_is_not_abstract():
    assert not inspect.isabstract(stext_LocalReaction)


def test_stext_localreaction_constructor_exists():
    assert callable(stext_LocalReaction.__init__)


def test_stext_localreaction_constructor_args():
    sig = inspect.signature(stext_LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_stext_operationdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_OperationDefinition)


def test_stext_operationdefinition_constructor_exists():
    assert callable(stext_OperationDefinition.__init__)


def test_stext_operationdefinition_constructor_args():
    sig = inspect.signature(stext_OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_stext_realliteral_is_not_abstract():
    assert not inspect.isabstract(stext_RealLiteral)


def test_stext_realliteral_constructor_exists():
    assert callable(stext_RealLiteral.__init__)


def test_stext_realliteral_constructor_args():
    sig = inspect.signature(stext_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_realliteral_has_value():
    assert hasattr(stext_RealLiteral, "value")
    descriptor = None
    for klass in stext_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_stringliteral_is_not_abstract():
    assert not inspect.isabstract(stext_StringLiteral)


def test_stext_stringliteral_constructor_exists():
    assert callable(stext_StringLiteral.__init__)


def test_stext_stringliteral_constructor_args():
    sig = inspect.signature(stext_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_stringliteral_has_value():
    assert hasattr(stext_StringLiteral, "value")
    descriptor = None
    for klass in stext_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_hexliteral_is_not_abstract():
    assert not inspect.isabstract(stext_HexLiteral)


def test_stext_hexliteral_constructor_exists():
    assert callable(stext_HexLiteral.__init__)


def test_stext_hexliteral_constructor_args():
    sig = inspect.signature(stext_HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_hexliteral_has_value():
    assert hasattr(stext_HexLiteral, "value")
    descriptor = None
    for klass in stext_HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_intliteral_is_not_abstract():
    assert not inspect.isabstract(stext_IntLiteral)


def test_stext_intliteral_constructor_exists():
    assert callable(stext_IntLiteral.__init__)


def test_stext_intliteral_constructor_args():
    sig = inspect.signature(stext_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_intliteral_has_value():
    assert hasattr(stext_IntLiteral, "value")
    descriptor = None
    for klass in stext_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_boolliteral_is_not_abstract():
    assert not inspect.isabstract(stext_BoolLiteral)


def test_stext_boolliteral_constructor_exists():
    assert callable(stext_BoolLiteral.__init__)


def test_stext_boolliteral_constructor_args():
    sig = inspect.signature(stext_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_boolliteral_has_value():
    assert hasattr(stext_BoolLiteral, "value")
    descriptor = None
    for klass in stext_BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_literal_is_not_abstract():
    assert not inspect.isabstract(stext_Literal)


def test_stext_literal_constructor_exists():
    assert callable(stext_Literal.__init__)


def test_stext_literal_constructor_args():
    sig = inspect.signature(stext_Literal.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_stext_expression_is_not_abstract():
    assert not inspect.isabstract(stext_Expression)


def test_stext_expression_constructor_exists():
    assert callable(stext_Expression.__init__)


def test_stext_expression_constructor_args():
    sig = inspect.signature(stext_Expression.__init__)
    params = list(sig.parameters.keys())



def test_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext_AlwaysEvent)


def test_stext_alwaysevent_constructor_exists():
    assert callable(stext_AlwaysEvent.__init__)


def test_stext_alwaysevent_constructor_args():
    sig = inspect.signature(stext_AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_defaultevent_is_not_abstract():
    assert not inspect.isabstract(stext_DefaultEvent)


def test_stext_defaultevent_constructor_exists():
    assert callable(stext_DefaultEvent.__init__)


def test_stext_defaultevent_constructor_args():
    sig = inspect.signature(stext_DefaultEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_oncycleevent_is_not_abstract():
    assert not inspect.isabstract(stext_OnCycleEvent)


def test_stext_oncycleevent_constructor_exists():
    assert callable(stext_OnCycleEvent.__init__)


def test_stext_oncycleevent_constructor_args():
    sig = inspect.signature(stext_OnCycleEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitevent_is_not_abstract():
    assert not inspect.isabstract(stext_ExitEvent)


def test_stext_exitevent_constructor_exists():
    assert callable(stext_ExitEvent.__init__)


def test_stext_exitevent_constructor_args():
    sig = inspect.signature(stext_ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_entryevent_is_not_abstract():
    assert not inspect.isabstract(stext_EntryEvent)


def test_stext_entryevent_constructor_exists():
    assert callable(stext_EntryEvent.__init__)


def test_stext_entryevent_constructor_args():
    sig = inspect.signature(stext_EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext_BuiltinEventSpec)


def test_stext_builtineventspec_constructor_exists():
    assert callable(stext_BuiltinEventSpec.__init__)


def test_stext_builtineventspec_constructor_args():
    sig = inspect.signature(stext_BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_scope_is_not_abstract():
    assert not inspect.isabstract(stext_Scope)


def test_stext_scope_constructor_exists():
    assert callable(stext_Scope.__init__)


def test_stext_scope_constructor_args():
    sig = inspect.signature(stext_Scope.__init__)
    params = list(sig.parameters.keys())



def test_scopedelement_is_not_abstract():
    assert not inspect.isabstract(ScopedElement)


def test_scopedelement_constructor_exists():
    assert callable(ScopedElement.__init__)


def test_scopedelement_constructor_args():
    sig = inspect.signature(ScopedElement.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionspecification_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionSpecification)


def test_stext_transitionspecification_constructor_exists():
    assert callable(stext_TransitionSpecification.__init__)


def test_stext_transitionspecification_constructor_args():
    sig = inspect.signature(stext_TransitionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_stext_statespecification_is_not_abstract():
    assert not inspect.isabstract(stext_StateSpecification)


def test_stext_statespecification_constructor_exists():
    assert callable(stext_StateSpecification.__init__)


def test_stext_statespecification_constructor_args():
    sig = inspect.signature(stext_StateSpecification.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartspecification_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartSpecification)


def test_stext_statechartspecification_constructor_exists():
    assert callable(stext_StatechartSpecification.__init__)


def test_stext_statechartspecification_constructor_args():
    sig = inspect.signature(stext_StatechartSpecification.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_stext_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(stext_VariableDefinition)


def test_stext_variabledefinition_constructor_exists():
    assert callable(stext_VariableDefinition.__init__)


def test_stext_variabledefinition_constructor_args():
    sig = inspect.signature(stext_VariableDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_stext_variabledefinition_has_external():
    assert hasattr(stext_VariableDefinition, "external")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_stext_variabledefinition_has_readonly():
    assert hasattr(stext_VariableDefinition, "readonly")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_EventDefinition)


def test_stext_eventdefinition_constructor_exists():
    assert callable(stext_EventDefinition.__init__)


def test_stext_eventdefinition_constructor_args():
    sig = inspect.signature(stext_EventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_stext_eventdefinition_has_direction():
    assert hasattr(stext_EventDefinition, "direction")
    descriptor = None
    for klass in stext_EventDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statechartscope_is_not_abstract():
    assert not inspect.isabstract(StatechartScope)


def test_statechartscope_constructor_exists():
    assert callable(StatechartScope.__init__)


def test_statechartscope_constructor_args():
    sig = inspect.signature(StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_internalscope_is_not_abstract():
    assert not inspect.isabstract(stext_InternalScope)


def test_stext_internalscope_constructor_exists():
    assert callable(stext_InternalScope.__init__)


def test_stext_internalscope_constructor_args():
    sig = inspect.signature(stext_InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext_InterfaceScope)


def test_stext_interfacescope_constructor_exists():
    assert callable(stext_InterfaceScope.__init__)


def test_stext_interfacescope_constructor_args():
    sig = inspect.signature(stext_InterfaceScope.__init__)
    params = list(sig.parameters.keys())



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext_simplescope_is_not_abstract():
    assert not inspect.isabstract(stext_SimpleScope)


def test_stext_simplescope_constructor_exists():
    assert callable(stext_SimpleScope.__init__)


def test_stext_simplescope_constructor_args():
    sig = inspect.signature(stext_SimpleScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartscope_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartScope)


def test_stext_statechartscope_constructor_exists():
    assert callable(stext_StatechartScope.__init__)


def test_stext_statechartscope_constructor_args():
    sig = inspect.signature(stext_StatechartScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionReaction)


def test_stext_transitionreaction_constructor_exists():
    assert callable(stext_TransitionReaction.__init__)


def test_stext_transitionreaction_constructor_args():
    sig = inspect.signature(stext_TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_defroot_is_not_abstract():
    assert not inspect.isabstract(DefRoot)


def test_defroot_constructor_exists():
    assert callable(DefRoot.__init__)


def test_defroot_constructor_args():
    sig = inspect.signature(DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionroot_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionRoot)


def test_stext_transitionroot_constructor_exists():
    assert callable(stext_TransitionRoot.__init__)


def test_stext_transitionroot_constructor_args():
    sig = inspect.signature(stext_TransitionRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_stateroot_is_not_abstract():
    assert not inspect.isabstract(stext_StateRoot)


def test_stext_stateroot_constructor_exists():
    assert callable(stext_StateRoot.__init__)


def test_stext_stateroot_constructor_args():
    sig = inspect.signature(stext_StateRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_statechartroot_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartRoot)


def test_stext_statechartroot_constructor_exists():
    assert callable(stext_StatechartRoot.__init__)


def test_stext_statechartroot_constructor_args():
    sig = inspect.signature(stext_StatechartRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_defroot_is_not_abstract():
    assert not inspect.isabstract(stext_DefRoot)


def test_stext_defroot_constructor_exists():
    assert callable(stext_DefRoot.__init__)


def test_stext_defroot_constructor_args():
    sig = inspect.signature(stext_DefRoot.__init__)
    params = list(sig.parameters.keys())



def test_stext_root_is_not_abstract():
    assert not inspect.isabstract(stext_Root)


def test_stext_root_constructor_exists():
    assert callable(stext_Root.__init__)


def test_stext_root_constructor_args():
    sig = inspect.signature(stext_Root.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "LOCAL",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "smallerEqual",
        "equals",
        "greaterEqual",
        "greater",
        "smaller",
        "notEquals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "multAssign",
        "addAssign",
        "leftShiftAssign",
        "divAssign",
        "orAssign",
        "assign",
        "subAssign",
        "rightShiftAssign",
        "modAssign",
        "andAssign",
        "xorAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mod",
        "mul",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "minus",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "negative",
        "positive",
        "complement",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_timeeventtype_exists():
    # Check that the Enumeration exists
    assert TimeEventType is not None

def test_timeeventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeEventType]
    expected_literals = [
        "after",
        "every",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeEventType"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "nanosecond",
        "second",
        "microsecond",
        "millisecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
stext_State_strategy = st.builds(
    stext_State,
)
stext_EObject_strategy = st.builds(
    stext_EObject,
)
Expression_strategy = st.builds(
    Expression,
)
stext_PrimitiveValueExpression_strategy = st.builds(
    stext_PrimitiveValueExpression,
)
stext_NumericalUnaryExpression_strategy = st.builds(
    stext_NumericalUnaryExpression,
    operator=
        safe_text
)
stext_BitwiseAndExpression_strategy = st.builds(
    stext_BitwiseAndExpression,
)
stext_NumericalAddSubtractExpression_strategy = st.builds(
    stext_NumericalAddSubtractExpression,
    operator=
        safe_text
)
stext_ParenthesizedExpression_strategy = st.builds(
    stext_ParenthesizedExpression,
)
stext_BitwiseOrExpression_strategy = st.builds(
    stext_BitwiseOrExpression,
)
stext_AssignmentExpression_strategy = st.builds(
    stext_AssignmentExpression,
    operator=
        safe_text
)
stext_BitwiseXorExpression_strategy = st.builds(
    stext_BitwiseXorExpression,
)
stext_ElementReferenceExpression_strategy = st.builds(
    stext_ElementReferenceExpression,
    operationCall=
        st.booleans()
)
stext_LogicalRelationExpression_strategy = st.builds(
    stext_LogicalRelationExpression,
    operator=
        safe_text
)
stext_NumericalMultiplyDivideExpression_strategy = st.builds(
    stext_NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
stext_LogicalNotExpression_strategy = st.builds(
    stext_LogicalNotExpression,
)
stext_EventValueReferenceExpression_strategy = st.builds(
    stext_EventValueReferenceExpression,
)
stext_FeatureCall_strategy = st.builds(
    stext_FeatureCall,
    operationCall=
        st.booleans()
)
stext_LogicalAndExpression_strategy = st.builds(
    stext_LogicalAndExpression,
)
stext_ShiftExpression_strategy = st.builds(
    stext_ShiftExpression,
    operator=
        safe_text
)
stext_ActiveStateReferenceExpression_strategy = st.builds(
    stext_ActiveStateReferenceExpression,
)
stext_EventRaisingExpression_strategy = st.builds(
    stext_EventRaisingExpression,
)
Effect_strategy = st.builds(
    Effect,
)
stext_ReactionEffect_strategy = st.builds(
    stext_ReactionEffect,
)
Trigger_strategy = st.builds(
    Trigger,
)
stext_ReactionTrigger_strategy = st.builds(
    stext_ReactionTrigger,
)
stext_LogicalOrExpression_strategy = st.builds(
    stext_LogicalOrExpression,
)
stext_ConditionalExpression_strategy = st.builds(
    stext_ConditionalExpression,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext_TimeEventSpec_strategy = st.builds(
    stext_TimeEventSpec,
    type=
        safe_text,
    unit=
        safe_text
)
stext_RegularEventSpec_strategy = st.builds(
    stext_RegularEventSpec,
)
stext_EventSpec_strategy = st.builds(
    stext_EventSpec,
)
Reaction_strategy = st.builds(
    Reaction,
)
Operation_strategy = st.builds(
    Operation,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext_LocalReaction_strategy = st.builds(
    stext_LocalReaction,
)
stext_OperationDefinition_strategy = st.builds(
    stext_OperationDefinition,
)
Literal_strategy = st.builds(
    Literal,
)
stext_RealLiteral_strategy = st.builds(
    stext_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
stext_StringLiteral_strategy = st.builds(
    stext_StringLiteral,
    value=
        safe_text
)
stext_HexLiteral_strategy = st.builds(
    stext_HexLiteral,
    value=
        st.integers()
)
stext_IntLiteral_strategy = st.builds(
    stext_IntLiteral,
    value=
        st.integers()
)
stext_BoolLiteral_strategy = st.builds(
    stext_BoolLiteral,
    value=
        st.booleans()
)
stext_Literal_strategy = st.builds(
    stext_Literal,
)
Statement_strategy = st.builds(
    Statement,
)
stext_Expression_strategy = st.builds(
    stext_Expression,
)
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext_AlwaysEvent_strategy = st.builds(
    stext_AlwaysEvent,
)
stext_DefaultEvent_strategy = st.builds(
    stext_DefaultEvent,
)
stext_OnCycleEvent_strategy = st.builds(
    stext_OnCycleEvent,
)
stext_ExitEvent_strategy = st.builds(
    stext_ExitEvent,
)
stext_EntryEvent_strategy = st.builds(
    stext_EntryEvent,
)
stext_BuiltinEventSpec_strategy = st.builds(
    stext_BuiltinEventSpec,
)
stext_Scope_strategy = st.builds(
    stext_Scope,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
stext_TransitionSpecification_strategy = st.builds(
    stext_TransitionSpecification,
)
stext_StateSpecification_strategy = st.builds(
    stext_StateSpecification,
)
stext_StatechartSpecification_strategy = st.builds(
    stext_StatechartSpecification,
)
Property_strategy = st.builds(
    Property,
)
Variable_strategy = st.builds(
    Variable,
)
stext_VariableDefinition_strategy = st.builds(
    stext_VariableDefinition,
    external=
        st.booleans(),
    readonly=
        st.booleans()
)
Event_strategy = st.builds(
    Event,
)
stext_EventDefinition_strategy = st.builds(
    stext_EventDefinition,
    direction=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StatechartScope_strategy = st.builds(
    StatechartScope,
)
stext_InternalScope_strategy = st.builds(
    stext_InternalScope,
)
stext_InterfaceScope_strategy = st.builds(
    stext_InterfaceScope,
)
Scope_strategy = st.builds(
    Scope,
)
stext_SimpleScope_strategy = st.builds(
    stext_SimpleScope,
)
stext_StatechartScope_strategy = st.builds(
    stext_StatechartScope,
)
stext_TransitionReaction_strategy = st.builds(
    stext_TransitionReaction,
)
DefRoot_strategy = st.builds(
    DefRoot,
)
stext_TransitionRoot_strategy = st.builds(
    stext_TransitionRoot,
)
stext_StateRoot_strategy = st.builds(
    stext_StateRoot,
)
stext_StatechartRoot_strategy = st.builds(
    stext_StatechartRoot,
)
stext_DefRoot_strategy = st.builds(
    stext_DefRoot,
)
stext_Root_strategy = st.builds(
    stext_Root,
)

@given(instance=stext_State_strategy)
@settings(max_examples=50)
def test_stext_state_instantiation(instance):
    assert isinstance(instance, stext_State)

@given(instance=stext_EObject_strategy)
@settings(max_examples=50)
def test_stext_eobject_instantiation(instance):
    assert isinstance(instance, stext_EObject)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stext_PrimitiveValueExpression_strategy)
@settings(max_examples=50)
def test_stext_primitivevalueexpression_instantiation(instance):
    assert isinstance(instance, stext_PrimitiveValueExpression)

@given(instance=stext_NumericalUnaryExpression_strategy)
@settings(max_examples=50)
def test_stext_numericalunaryexpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalUnaryExpression)



@given(instance=stext_NumericalUnaryExpression_strategy)
def test_stext_numericalunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseAndExpression)

@given(instance=stext_NumericalAddSubtractExpression_strategy)
@settings(max_examples=50)
def test_stext_numericaladdsubtractexpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalAddSubtractExpression)



@given(instance=stext_NumericalAddSubtractExpression_strategy)
def test_stext_numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_stext_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, stext_ParenthesizedExpression)

@given(instance=stext_BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseOrExpression)

@given(instance=stext_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_stext_assignmentexpression_instantiation(instance):
    assert isinstance(instance, stext_AssignmentExpression)



@given(instance=stext_AssignmentExpression_strategy)
def test_stext_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseXorExpression)

@given(instance=stext_ElementReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_elementreferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_ElementReferenceExpression)



@given(instance=stext_ElementReferenceExpression_strategy)
def test_stext_elementreferenceexpression_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original

@given(instance=stext_LogicalRelationExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalrelationexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalRelationExpression)



@given(instance=stext_LogicalRelationExpression_strategy)
def test_stext_logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=50)
def test_stext_numericalmultiplydivideexpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalMultiplyDivideExpression)



@given(instance=stext_NumericalMultiplyDivideExpression_strategy)
def test_stext_numericalmultiplydivideexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_LogicalNotExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalnotexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalNotExpression)

@given(instance=stext_EventValueReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_eventvaluereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_EventValueReferenceExpression)

@given(instance=stext_FeatureCall_strategy)
@settings(max_examples=50)
def test_stext_featurecall_instantiation(instance):
    assert isinstance(instance, stext_FeatureCall)



@given(instance=stext_FeatureCall_strategy)
def test_stext_featurecall_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original

@given(instance=stext_LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalandexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalAndExpression)

@given(instance=stext_ShiftExpression_strategy)
@settings(max_examples=50)
def test_stext_shiftexpression_instantiation(instance):
    assert isinstance(instance, stext_ShiftExpression)



@given(instance=stext_ShiftExpression_strategy)
def test_stext_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_ActiveStateReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_activestatereferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_ActiveStateReferenceExpression)

@given(instance=stext_EventRaisingExpression_strategy)
@settings(max_examples=50)
def test_stext_eventraisingexpression_instantiation(instance):
    assert isinstance(instance, stext_EventRaisingExpression)

@given(instance=Effect_strategy)
@settings(max_examples=50)
def test_effect_instantiation(instance):
    assert isinstance(instance, Effect)

@given(instance=stext_ReactionEffect_strategy)
@settings(max_examples=50)
def test_stext_reactioneffect_instantiation(instance):
    assert isinstance(instance, stext_ReactionEffect)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=stext_ReactionTrigger_strategy)
@settings(max_examples=50)
def test_stext_reactiontrigger_instantiation(instance):
    assert isinstance(instance, stext_ReactionTrigger)

@given(instance=stext_LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalorexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalOrExpression)

@given(instance=stext_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_stext_conditionalexpression_instantiation(instance):
    assert isinstance(instance, stext_ConditionalExpression)

@given(instance=EventSpec_strategy)
@settings(max_examples=50)
def test_eventspec_instantiation(instance):
    assert isinstance(instance, EventSpec)

@given(instance=stext_TimeEventSpec_strategy)
@settings(max_examples=50)
def test_stext_timeeventspec_instantiation(instance):
    assert isinstance(instance, stext_TimeEventSpec)



@given(instance=stext_TimeEventSpec_strategy)
def test_stext_timeeventspec_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stext_TimeEventSpec_strategy)
def test_stext_timeeventspec_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=stext_RegularEventSpec_strategy)
@settings(max_examples=50)
def test_stext_regulareventspec_instantiation(instance):
    assert isinstance(instance, stext_RegularEventSpec)

@given(instance=stext_EventSpec_strategy)
@settings(max_examples=50)
def test_stext_eventspec_instantiation(instance):
    assert isinstance(instance, stext_EventSpec)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=stext_LocalReaction_strategy)
@settings(max_examples=50)
def test_stext_localreaction_instantiation(instance):
    assert isinstance(instance, stext_LocalReaction)

@given(instance=stext_OperationDefinition_strategy)
@settings(max_examples=50)
def test_stext_operationdefinition_instantiation(instance):
    assert isinstance(instance, stext_OperationDefinition)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=stext_RealLiteral_strategy)
@settings(max_examples=50)
def test_stext_realliteral_instantiation(instance):
    assert isinstance(instance, stext_RealLiteral)



@given(instance=stext_RealLiteral_strategy)
def test_stext_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_StringLiteral_strategy)
@settings(max_examples=50)
def test_stext_stringliteral_instantiation(instance):
    assert isinstance(instance, stext_StringLiteral)



@given(instance=stext_StringLiteral_strategy)
def test_stext_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_HexLiteral_strategy)
@settings(max_examples=50)
def test_stext_hexliteral_instantiation(instance):
    assert isinstance(instance, stext_HexLiteral)



@given(instance=stext_HexLiteral_strategy)
def test_stext_hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_IntLiteral_strategy)
@settings(max_examples=50)
def test_stext_intliteral_instantiation(instance):
    assert isinstance(instance, stext_IntLiteral)



@given(instance=stext_IntLiteral_strategy)
def test_stext_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_BoolLiteral_strategy)
@settings(max_examples=50)
def test_stext_boolliteral_instantiation(instance):
    assert isinstance(instance, stext_BoolLiteral)



@given(instance=stext_BoolLiteral_strategy)
def test_stext_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_Literal_strategy)
@settings(max_examples=50)
def test_stext_literal_instantiation(instance):
    assert isinstance(instance, stext_Literal)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=stext_Expression_strategy)
@settings(max_examples=50)
def test_stext_expression_instantiation(instance):
    assert isinstance(instance, stext_Expression)

@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_builtineventspec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)

@given(instance=stext_AlwaysEvent_strategy)
@settings(max_examples=50)
def test_stext_alwaysevent_instantiation(instance):
    assert isinstance(instance, stext_AlwaysEvent)

@given(instance=stext_DefaultEvent_strategy)
@settings(max_examples=50)
def test_stext_defaultevent_instantiation(instance):
    assert isinstance(instance, stext_DefaultEvent)

@given(instance=stext_OnCycleEvent_strategy)
@settings(max_examples=50)
def test_stext_oncycleevent_instantiation(instance):
    assert isinstance(instance, stext_OnCycleEvent)

@given(instance=stext_ExitEvent_strategy)
@settings(max_examples=50)
def test_stext_exitevent_instantiation(instance):
    assert isinstance(instance, stext_ExitEvent)

@given(instance=stext_EntryEvent_strategy)
@settings(max_examples=50)
def test_stext_entryevent_instantiation(instance):
    assert isinstance(instance, stext_EntryEvent)

@given(instance=stext_BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_stext_builtineventspec_instantiation(instance):
    assert isinstance(instance, stext_BuiltinEventSpec)

@given(instance=stext_Scope_strategy)
@settings(max_examples=50)
def test_stext_scope_instantiation(instance):
    assert isinstance(instance, stext_Scope)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=stext_TransitionSpecification_strategy)
@settings(max_examples=50)
def test_stext_transitionspecification_instantiation(instance):
    assert isinstance(instance, stext_TransitionSpecification)

@given(instance=stext_StateSpecification_strategy)
@settings(max_examples=50)
def test_stext_statespecification_instantiation(instance):
    assert isinstance(instance, stext_StateSpecification)

@given(instance=stext_StatechartSpecification_strategy)
@settings(max_examples=50)
def test_stext_statechartspecification_instantiation(instance):
    assert isinstance(instance, stext_StatechartSpecification)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=stext_VariableDefinition_strategy)
@settings(max_examples=50)
def test_stext_variabledefinition_instantiation(instance):
    assert isinstance(instance, stext_VariableDefinition)



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=stext_EventDefinition_strategy)
@settings(max_examples=50)
def test_stext_eventdefinition_instantiation(instance):
    assert isinstance(instance, stext_EventDefinition)



@given(instance=stext_EventDefinition_strategy)
def test_stext_eventdefinition_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StatechartScope_strategy)
@settings(max_examples=50)
def test_statechartscope_instantiation(instance):
    assert isinstance(instance, StatechartScope)

@given(instance=stext_InternalScope_strategy)
@settings(max_examples=50)
def test_stext_internalscope_instantiation(instance):
    assert isinstance(instance, stext_InternalScope)

@given(instance=stext_InterfaceScope_strategy)
@settings(max_examples=50)
def test_stext_interfacescope_instantiation(instance):
    assert isinstance(instance, stext_InterfaceScope)

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=stext_SimpleScope_strategy)
@settings(max_examples=50)
def test_stext_simplescope_instantiation(instance):
    assert isinstance(instance, stext_SimpleScope)

@given(instance=stext_StatechartScope_strategy)
@settings(max_examples=50)
def test_stext_statechartscope_instantiation(instance):
    assert isinstance(instance, stext_StatechartScope)

@given(instance=stext_TransitionReaction_strategy)
@settings(max_examples=50)
def test_stext_transitionreaction_instantiation(instance):
    assert isinstance(instance, stext_TransitionReaction)

@given(instance=DefRoot_strategy)
@settings(max_examples=50)
def test_defroot_instantiation(instance):
    assert isinstance(instance, DefRoot)

@given(instance=stext_TransitionRoot_strategy)
@settings(max_examples=50)
def test_stext_transitionroot_instantiation(instance):
    assert isinstance(instance, stext_TransitionRoot)

@given(instance=stext_StateRoot_strategy)
@settings(max_examples=50)
def test_stext_stateroot_instantiation(instance):
    assert isinstance(instance, stext_StateRoot)

@given(instance=stext_StatechartRoot_strategy)
@settings(max_examples=50)
def test_stext_statechartroot_instantiation(instance):
    assert isinstance(instance, stext_StatechartRoot)

@given(instance=stext_DefRoot_strategy)
@settings(max_examples=50)
def test_stext_defroot_instantiation(instance):
    assert isinstance(instance, stext_DefRoot)

@given(instance=stext_Root_strategy)
@settings(max_examples=50)
def test_stext_root_instantiation(instance):
    assert isinstance(instance, stext_Root)
