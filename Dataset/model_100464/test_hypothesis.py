import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stext_Declaration,
    Expression,
    stext_OperationCall,
    stext_LogicalAndExpression,
    stext_ElementReferenceExpression,
    stext_PrimitiveValueExpression,
    stext_BitwiseXorExpression,
    stext_BitwiseAndExpression,
    stext_LogicalRelationExpression,
    stext_BitwiseOrExpression,
    stext_NumericalUnaryExpression,
    stext_NumericalMultiplyDivideExpression,
    stext_NumericalAddSubtractExpression,
    stext_LogicalOrExpression,
    stext_ShiftExpression,
    stext_ConditionalExpression,
    stext_Statement,
    Effect,
    stext_ReactionEffect,
    Trigger,
    stext_ReactionTrigger,
    stext_LogicalNotExpression,
    Event,
    stext_EventDefinition,
    Scope,
    stext_InterfaceScope,
    stext_InternalScope,
    stext_SimpleScope,
    Variable,
    stext_VariableDefinition,
    stext_Variable,
    Statement,
    stext_Assignment,
    BuiltinEventSpec,
    stext_ExitEvent,
    stext_OnCycleEvent,
    stext_AlwaysEvent,
    stext_EntryEvent,
    stext_Event,
    EventSpec,
    stext_BuiltinEventSpec,
    stext_TimeEventSpec,
    stext_RegularEventSpec,
    stext_EventSpec,
    stext_EventRaising,
    ReactionProperty,
    stext_ExitPointSpec,
    stext_ReactionPriority,
    stext_ReactionProperty,
    TransitionStatement,
    stext_ReactionProperties,
    Reaction,
    stext_TransitionReaction,
    Declaration,
    stext_Operation,
    stext_Clock,
    stext_Exitpoint,
    stext_LocalReaction,
    stext_Expression,
    stext_EventDerivation,
    stext_Scope,
    stext_TransitionStatement,
    stext_StateDeclaration,
    stext_Entrypoint,
    stext_EntryPointSpec,
    stext_DefRoot,
    stext_Root,
    stext_StatechartDefinition,
    DefRoot,
    stext_TransitionRoot,
    stext_StateRoot,
    stext_StatechartRoot,
    RelationalOperator,
    Type,
    ShiftOperator,
    MultiplicativeOperator,
    TimeUnit,
    AdditiveOperator,
    TimeEventType,
    AssignmentOperator,
    Direction,
    UnaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stext_declaration_is_not_abstract():
    assert not inspect.isabstract(stext_Declaration)


def test_stext_declaration_constructor_exists():
    assert callable(stext_Declaration.__init__)


def test_stext_declaration_constructor_args():
    sig = inspect.signature(stext_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext_operationcall_is_not_abstract():
    assert not inspect.isabstract(stext_OperationCall)


def test_stext_operationcall_constructor_exists():
    assert callable(stext_OperationCall.__init__)


def test_stext_operationcall_constructor_args():
    sig = inspect.signature(stext_OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_stext_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalAndExpression)


def test_stext_logicalandexpression_constructor_exists():
    assert callable(stext_LogicalAndExpression.__init__)


def test_stext_logicalandexpression_constructor_args():
    sig = inspect.signature(stext_LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_elementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ElementReferenceExpression)


def test_stext_elementreferenceexpression_constructor_exists():
    assert callable(stext_ElementReferenceExpression.__init__)


def test_stext_elementreferenceexpression_constructor_args():
    sig = inspect.signature(stext_ElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(stext_PrimitiveValueExpression)


def test_stext_primitivevalueexpression_constructor_exists():
    assert callable(stext_PrimitiveValueExpression.__init__)


def test_stext_primitivevalueexpression_constructor_args():
    sig = inspect.signature(stext_PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_stext_primitivevalueexpression_has_value():
    assert hasattr(stext_PrimitiveValueExpression, "value")
    descriptor = None
    for klass in stext_PrimitiveValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_stext_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseXorExpression)


def test_stext_bitwisexorexpression_constructor_exists():
    assert callable(stext_BitwiseXorExpression.__init__)


def test_stext_bitwisexorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseAndExpression)


def test_stext_bitwiseandexpression_constructor_exists():
    assert callable(stext_BitwiseAndExpression.__init__)


def test_stext_bitwiseandexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



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



def test_stext_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_BitwiseOrExpression)


def test_stext_bitwiseorexpression_constructor_exists():
    assert callable(stext_BitwiseOrExpression.__init__)


def test_stext_bitwiseorexpression_constructor_args():
    sig = inspect.signature(stext_BitwiseOrExpression.__init__)
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



def test_stext_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalOrExpression)


def test_stext_logicalorexpression_constructor_exists():
    assert callable(stext_LogicalOrExpression.__init__)


def test_stext_logicalorexpression_constructor_args():
    sig = inspect.signature(stext_LogicalOrExpression.__init__)
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



def test_stext_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(stext_ConditionalExpression)


def test_stext_conditionalexpression_constructor_exists():
    assert callable(stext_ConditionalExpression.__init__)


def test_stext_conditionalexpression_constructor_args():
    sig = inspect.signature(stext_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_stext_statement_is_not_abstract():
    assert not inspect.isabstract(stext_Statement)


def test_stext_statement_constructor_exists():
    assert callable(stext_Statement.__init__)


def test_stext_statement_constructor_args():
    sig = inspect.signature(stext_Statement.__init__)
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



def test_stext_logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(stext_LogicalNotExpression)


def test_stext_logicalnotexpression_constructor_exists():
    assert callable(stext_LogicalNotExpression.__init__)


def test_stext_logicalnotexpression_constructor_args():
    sig = inspect.signature(stext_LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



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
    assert "type" in params, "Missing parameter 'type'"

def test_stext_eventdefinition_has_direction():
    assert hasattr(stext_EventDefinition, "direction")
    descriptor = None
    for klass in stext_EventDefinition.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_stext_eventdefinition_has_type():
    assert hasattr(stext_EventDefinition, "type")
    descriptor = None
    for klass in stext_EventDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_scope_is_not_abstract():
    assert not inspect.isabstract(Scope)


def test_scope_constructor_exists():
    assert callable(Scope.__init__)


def test_scope_constructor_args():
    sig = inspect.signature(Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext_interfacescope_is_not_abstract():
    assert not inspect.isabstract(stext_InterfaceScope)


def test_stext_interfacescope_constructor_exists():
    assert callable(stext_InterfaceScope.__init__)


def test_stext_interfacescope_constructor_args():
    sig = inspect.signature(stext_InterfaceScope.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_stext_interfacescope_has_name():
    assert hasattr(stext_InterfaceScope, "name")
    descriptor = None
    for klass in stext_InterfaceScope.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_stext_internalscope_is_not_abstract():
    assert not inspect.isabstract(stext_InternalScope)


def test_stext_internalscope_constructor_exists():
    assert callable(stext_InternalScope.__init__)


def test_stext_internalscope_constructor_args():
    sig = inspect.signature(stext_InternalScope.__init__)
    params = list(sig.parameters.keys())



def test_stext_simplescope_is_not_abstract():
    assert not inspect.isabstract(stext_SimpleScope)


def test_stext_simplescope_constructor_exists():
    assert callable(stext_SimpleScope.__init__)


def test_stext_simplescope_constructor_args():
    sig = inspect.signature(stext_SimpleScope.__init__)
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
    assert "initialValue" in params, "Missing parameter 'initialValue'"
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "type" in params, "Missing parameter 'type'"
    assert "external" in params, "Missing parameter 'external'"

def test_stext_variabledefinition_has_initialValue():
    assert hasattr(stext_VariableDefinition, "initialValue")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
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

def test_stext_variabledefinition_has_type():
    assert hasattr(stext_VariableDefinition, "type")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_stext_variabledefinition_has_external():
    assert hasattr(stext_VariableDefinition, "external")
    descriptor = None
    for klass in stext_VariableDefinition.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)



def test_stext_variable_is_not_abstract():
    assert not inspect.isabstract(stext_Variable)


def test_stext_variable_constructor_exists():
    assert callable(stext_Variable.__init__)


def test_stext_variable_constructor_args():
    sig = inspect.signature(stext_Variable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_stext_assignment_is_not_abstract():
    assert not inspect.isabstract(stext_Assignment)


def test_stext_assignment_constructor_exists():
    assert callable(stext_Assignment.__init__)


def test_stext_assignment_constructor_args():
    sig = inspect.signature(stext_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_stext_assignment_has_operator():
    assert hasattr(stext_Assignment, "operator")
    descriptor = None
    for klass in stext_Assignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(BuiltinEventSpec)


def test_builtineventspec_constructor_exists():
    assert callable(BuiltinEventSpec.__init__)


def test_builtineventspec_constructor_args():
    sig = inspect.signature(BuiltinEventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitevent_is_not_abstract():
    assert not inspect.isabstract(stext_ExitEvent)


def test_stext_exitevent_constructor_exists():
    assert callable(stext_ExitEvent.__init__)


def test_stext_exitevent_constructor_args():
    sig = inspect.signature(stext_ExitEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_oncycleevent_is_not_abstract():
    assert not inspect.isabstract(stext_OnCycleEvent)


def test_stext_oncycleevent_constructor_exists():
    assert callable(stext_OnCycleEvent.__init__)


def test_stext_oncycleevent_constructor_args():
    sig = inspect.signature(stext_OnCycleEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_alwaysevent_is_not_abstract():
    assert not inspect.isabstract(stext_AlwaysEvent)


def test_stext_alwaysevent_constructor_exists():
    assert callable(stext_AlwaysEvent.__init__)


def test_stext_alwaysevent_constructor_args():
    sig = inspect.signature(stext_AlwaysEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_entryevent_is_not_abstract():
    assert not inspect.isabstract(stext_EntryEvent)


def test_stext_entryevent_constructor_exists():
    assert callable(stext_EntryEvent.__init__)


def test_stext_entryevent_constructor_args():
    sig = inspect.signature(stext_EntryEvent.__init__)
    params = list(sig.parameters.keys())



def test_stext_event_is_not_abstract():
    assert not inspect.isabstract(stext_Event)


def test_stext_event_constructor_exists():
    assert callable(stext_Event.__init__)


def test_stext_event_constructor_args():
    sig = inspect.signature(stext_Event.__init__)
    params = list(sig.parameters.keys())



def test_eventspec_is_not_abstract():
    assert not inspect.isabstract(EventSpec)


def test_eventspec_constructor_exists():
    assert callable(EventSpec.__init__)


def test_eventspec_constructor_args():
    sig = inspect.signature(EventSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_builtineventspec_is_not_abstract():
    assert not inspect.isabstract(stext_BuiltinEventSpec)


def test_stext_builtineventspec_constructor_exists():
    assert callable(stext_BuiltinEventSpec.__init__)


def test_stext_builtineventspec_constructor_args():
    sig = inspect.signature(stext_BuiltinEventSpec.__init__)
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
    assert "value" in params, "Missing parameter 'value'"

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

def test_stext_timeeventspec_has_value():
    assert hasattr(stext_TimeEventSpec, "value")
    descriptor = None
    for klass in stext_TimeEventSpec.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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



def test_stext_eventraising_is_not_abstract():
    assert not inspect.isabstract(stext_EventRaising)


def test_stext_eventraising_constructor_exists():
    assert callable(stext_EventRaising.__init__)


def test_stext_eventraising_constructor_args():
    sig = inspect.signature(stext_EventRaising.__init__)
    params = list(sig.parameters.keys())



def test_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(ReactionProperty)


def test_reactionproperty_constructor_exists():
    assert callable(ReactionProperty.__init__)


def test_reactionproperty_constructor_args():
    sig = inspect.signature(ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitpointspec_is_not_abstract():
    assert not inspect.isabstract(stext_ExitPointSpec)


def test_stext_exitpointspec_constructor_exists():
    assert callable(stext_ExitPointSpec.__init__)


def test_stext_exitpointspec_constructor_args():
    sig = inspect.signature(stext_ExitPointSpec.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactionpriority_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionPriority)


def test_stext_reactionpriority_constructor_exists():
    assert callable(stext_ReactionPriority.__init__)


def test_stext_reactionpriority_constructor_args():
    sig = inspect.signature(stext_ReactionPriority.__init__)
    params = list(sig.parameters.keys())
    assert "priority" in params, "Missing parameter 'priority'"

def test_stext_reactionpriority_has_priority():
    assert hasattr(stext_ReactionPriority, "priority")
    descriptor = None
    for klass in stext_ReactionPriority.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)



def test_stext_reactionproperty_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionProperty)


def test_stext_reactionproperty_constructor_exists():
    assert callable(stext_ReactionProperty.__init__)


def test_stext_reactionproperty_constructor_args():
    sig = inspect.signature(stext_ReactionProperty.__init__)
    params = list(sig.parameters.keys())



def test_transitionstatement_is_not_abstract():
    assert not inspect.isabstract(TransitionStatement)


def test_transitionstatement_constructor_exists():
    assert callable(TransitionStatement.__init__)


def test_transitionstatement_constructor_args():
    sig = inspect.signature(TransitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_stext_reactionproperties_is_not_abstract():
    assert not inspect.isabstract(stext_ReactionProperties)


def test_stext_reactionproperties_constructor_exists():
    assert callable(stext_ReactionProperties.__init__)


def test_stext_reactionproperties_constructor_args():
    sig = inspect.signature(stext_ReactionProperties.__init__)
    params = list(sig.parameters.keys())



def test_reaction_is_not_abstract():
    assert not inspect.isabstract(Reaction)


def test_reaction_constructor_exists():
    assert callable(Reaction.__init__)


def test_reaction_constructor_args():
    sig = inspect.signature(Reaction.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionreaction_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionReaction)


def test_stext_transitionreaction_constructor_exists():
    assert callable(stext_TransitionReaction.__init__)


def test_stext_transitionreaction_constructor_args():
    sig = inspect.signature(stext_TransitionReaction.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_stext_operation_is_not_abstract():
    assert not inspect.isabstract(stext_Operation)


def test_stext_operation_constructor_exists():
    assert callable(stext_Operation.__init__)


def test_stext_operation_constructor_args():
    sig = inspect.signature(stext_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "paramTypes" in params, "Missing parameter 'paramTypes'"
    assert "type" in params, "Missing parameter 'type'"

def test_stext_operation_has_paramTypes():
    assert hasattr(stext_Operation, "paramTypes")
    descriptor = None
    for klass in stext_Operation.__mro__:
        if "paramTypes" in klass.__dict__:
            descriptor = klass.__dict__["paramTypes"]
            break
    assert isinstance(descriptor, property)

def test_stext_operation_has_type():
    assert hasattr(stext_Operation, "type")
    descriptor = None
    for klass in stext_Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_stext_clock_is_not_abstract():
    assert not inspect.isabstract(stext_Clock)


def test_stext_clock_constructor_exists():
    assert callable(stext_Clock.__init__)


def test_stext_clock_constructor_args():
    sig = inspect.signature(stext_Clock.__init__)
    params = list(sig.parameters.keys())



def test_stext_exitpoint_is_not_abstract():
    assert not inspect.isabstract(stext_Exitpoint)


def test_stext_exitpoint_constructor_exists():
    assert callable(stext_Exitpoint.__init__)


def test_stext_exitpoint_constructor_args():
    sig = inspect.signature(stext_Exitpoint.__init__)
    params = list(sig.parameters.keys())



def test_stext_localreaction_is_not_abstract():
    assert not inspect.isabstract(stext_LocalReaction)


def test_stext_localreaction_constructor_exists():
    assert callable(stext_LocalReaction.__init__)


def test_stext_localreaction_constructor_args():
    sig = inspect.signature(stext_LocalReaction.__init__)
    params = list(sig.parameters.keys())



def test_stext_expression_is_not_abstract():
    assert not inspect.isabstract(stext_Expression)


def test_stext_expression_constructor_exists():
    assert callable(stext_Expression.__init__)


def test_stext_expression_constructor_args():
    sig = inspect.signature(stext_Expression.__init__)
    params = list(sig.parameters.keys())



def test_stext_eventderivation_is_not_abstract():
    assert not inspect.isabstract(stext_EventDerivation)


def test_stext_eventderivation_constructor_exists():
    assert callable(stext_EventDerivation.__init__)


def test_stext_eventderivation_constructor_args():
    sig = inspect.signature(stext_EventDerivation.__init__)
    params = list(sig.parameters.keys())



def test_stext_scope_is_not_abstract():
    assert not inspect.isabstract(stext_Scope)


def test_stext_scope_constructor_exists():
    assert callable(stext_Scope.__init__)


def test_stext_scope_constructor_args():
    sig = inspect.signature(stext_Scope.__init__)
    params = list(sig.parameters.keys())



def test_stext_transitionstatement_is_not_abstract():
    assert not inspect.isabstract(stext_TransitionStatement)


def test_stext_transitionstatement_constructor_exists():
    assert callable(stext_TransitionStatement.__init__)


def test_stext_transitionstatement_constructor_args():
    sig = inspect.signature(stext_TransitionStatement.__init__)
    params = list(sig.parameters.keys())



def test_stext_statedeclaration_is_not_abstract():
    assert not inspect.isabstract(stext_StateDeclaration)


def test_stext_statedeclaration_constructor_exists():
    assert callable(stext_StateDeclaration.__init__)


def test_stext_statedeclaration_constructor_args():
    sig = inspect.signature(stext_StateDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_stext_entrypoint_is_not_abstract():
    assert not inspect.isabstract(stext_Entrypoint)


def test_stext_entrypoint_constructor_exists():
    assert callable(stext_Entrypoint.__init__)


def test_stext_entrypoint_constructor_args():
    sig = inspect.signature(stext_Entrypoint.__init__)
    params = list(sig.parameters.keys())



def test_stext_entrypointspec_is_not_abstract():
    assert not inspect.isabstract(stext_EntryPointSpec)


def test_stext_entrypointspec_constructor_exists():
    assert callable(stext_EntryPointSpec.__init__)


def test_stext_entrypointspec_constructor_args():
    sig = inspect.signature(stext_EntryPointSpec.__init__)
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



def test_stext_statechartdefinition_is_not_abstract():
    assert not inspect.isabstract(stext_StatechartDefinition)


def test_stext_statechartdefinition_constructor_exists():
    assert callable(stext_StatechartDefinition.__init__)


def test_stext_statechartdefinition_constructor_args():
    sig = inspect.signature(stext_StatechartDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_stext_statechartdefinition_has_namespace():
    assert hasattr(stext_StatechartDefinition, "namespace")
    descriptor = None
    for klass in stext_StatechartDefinition.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



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

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "notEquals",
        "smallerEqual",
        "equals",
        "smaller",
        "greater",
        "greaterEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "boolean",
        "string",
        "void",
        "real",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

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

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mod",
        "div",
        "mul",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_timeunit_exists():
    # Check that the Enumeration exists
    assert TimeUnit is not None

def test_timeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnit]
    expected_literals = [
        "nanosecond",
        "second",
        "millisecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnit"

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

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "andAssign",
        "modAssign",
        "assign",
        "rightShiftAssign",
        "divAssign",
        "orAssign",
        "addAssign",
        "leftShiftAssign",
        "xorAssign",
        "subAssign",
        "multAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

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

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "complement",
        "negative",
        "positive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"


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
stext_Declaration_strategy = st.builds(
    stext_Declaration,
)
Expression_strategy = st.builds(
    Expression,
)
stext_OperationCall_strategy = st.builds(
    stext_OperationCall,
)
stext_LogicalAndExpression_strategy = st.builds(
    stext_LogicalAndExpression,
)
stext_ElementReferenceExpression_strategy = st.builds(
    stext_ElementReferenceExpression,
)
stext_PrimitiveValueExpression_strategy = st.builds(
    stext_PrimitiveValueExpression,
    value=
        safe_text
)
stext_BitwiseXorExpression_strategy = st.builds(
    stext_BitwiseXorExpression,
)
stext_BitwiseAndExpression_strategy = st.builds(
    stext_BitwiseAndExpression,
)
stext_LogicalRelationExpression_strategy = st.builds(
    stext_LogicalRelationExpression,
    operator=
        safe_text
)
stext_BitwiseOrExpression_strategy = st.builds(
    stext_BitwiseOrExpression,
)
stext_NumericalUnaryExpression_strategy = st.builds(
    stext_NumericalUnaryExpression,
    operator=
        safe_text
)
stext_NumericalMultiplyDivideExpression_strategy = st.builds(
    stext_NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
stext_NumericalAddSubtractExpression_strategy = st.builds(
    stext_NumericalAddSubtractExpression,
    operator=
        safe_text
)
stext_LogicalOrExpression_strategy = st.builds(
    stext_LogicalOrExpression,
)
stext_ShiftExpression_strategy = st.builds(
    stext_ShiftExpression,
    operator=
        safe_text
)
stext_ConditionalExpression_strategy = st.builds(
    stext_ConditionalExpression,
)
stext_Statement_strategy = st.builds(
    stext_Statement,
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
stext_LogicalNotExpression_strategy = st.builds(
    stext_LogicalNotExpression,
)
Event_strategy = st.builds(
    Event,
)
stext_EventDefinition_strategy = st.builds(
    stext_EventDefinition,
    direction=
        safe_text,
    type=
        safe_text
)
Scope_strategy = st.builds(
    Scope,
)
stext_InterfaceScope_strategy = st.builds(
    stext_InterfaceScope,
    name=
        safe_text
)
stext_InternalScope_strategy = st.builds(
    stext_InternalScope,
)
stext_SimpleScope_strategy = st.builds(
    stext_SimpleScope,
)
Variable_strategy = st.builds(
    Variable,
)
stext_VariableDefinition_strategy = st.builds(
    stext_VariableDefinition,
    initialValue=
        safe_text,
    readonly=
        st.booleans(),
    type=
        safe_text,
    external=
        st.booleans()
)
stext_Variable_strategy = st.builds(
    stext_Variable,
)
Statement_strategy = st.builds(
    Statement,
)
stext_Assignment_strategy = st.builds(
    stext_Assignment,
    operator=
        safe_text
)
BuiltinEventSpec_strategy = st.builds(
    BuiltinEventSpec,
)
stext_ExitEvent_strategy = st.builds(
    stext_ExitEvent,
)
stext_OnCycleEvent_strategy = st.builds(
    stext_OnCycleEvent,
)
stext_AlwaysEvent_strategy = st.builds(
    stext_AlwaysEvent,
)
stext_EntryEvent_strategy = st.builds(
    stext_EntryEvent,
)
stext_Event_strategy = st.builds(
    stext_Event,
)
EventSpec_strategy = st.builds(
    EventSpec,
)
stext_BuiltinEventSpec_strategy = st.builds(
    stext_BuiltinEventSpec,
)
stext_TimeEventSpec_strategy = st.builds(
    stext_TimeEventSpec,
    type=
        safe_text,
    unit=
        safe_text,
    value=
        st.integers()
)
stext_RegularEventSpec_strategy = st.builds(
    stext_RegularEventSpec,
)
stext_EventSpec_strategy = st.builds(
    stext_EventSpec,
)
stext_EventRaising_strategy = st.builds(
    stext_EventRaising,
)
ReactionProperty_strategy = st.builds(
    ReactionProperty,
)
stext_ExitPointSpec_strategy = st.builds(
    stext_ExitPointSpec,
)
stext_ReactionPriority_strategy = st.builds(
    stext_ReactionPriority,
    priority=
        st.integers()
)
stext_ReactionProperty_strategy = st.builds(
    stext_ReactionProperty,
)
TransitionStatement_strategy = st.builds(
    TransitionStatement,
)
stext_ReactionProperties_strategy = st.builds(
    stext_ReactionProperties,
)
Reaction_strategy = st.builds(
    Reaction,
)
stext_TransitionReaction_strategy = st.builds(
    stext_TransitionReaction,
)
Declaration_strategy = st.builds(
    Declaration,
)
stext_Operation_strategy = st.builds(
    stext_Operation,
    paramTypes=
        safe_text,
    type=
        safe_text
)
stext_Clock_strategy = st.builds(
    stext_Clock,
)
stext_Exitpoint_strategy = st.builds(
    stext_Exitpoint,
)
stext_LocalReaction_strategy = st.builds(
    stext_LocalReaction,
)
stext_Expression_strategy = st.builds(
    stext_Expression,
)
stext_EventDerivation_strategy = st.builds(
    stext_EventDerivation,
)
stext_Scope_strategy = st.builds(
    stext_Scope,
)
stext_TransitionStatement_strategy = st.builds(
    stext_TransitionStatement,
)
stext_StateDeclaration_strategy = st.builds(
    stext_StateDeclaration,
)
stext_Entrypoint_strategy = st.builds(
    stext_Entrypoint,
)
stext_EntryPointSpec_strategy = st.builds(
    stext_EntryPointSpec,
)
stext_DefRoot_strategy = st.builds(
    stext_DefRoot,
)
stext_Root_strategy = st.builds(
    stext_Root,
)
stext_StatechartDefinition_strategy = st.builds(
    stext_StatechartDefinition,
    namespace=
        safe_text
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

@given(instance=stext_Declaration_strategy)
@settings(max_examples=50)
def test_stext_declaration_instantiation(instance):
    assert isinstance(instance, stext_Declaration)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=stext_OperationCall_strategy)
@settings(max_examples=50)
def test_stext_operationcall_instantiation(instance):
    assert isinstance(instance, stext_OperationCall)

@given(instance=stext_LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalandexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalAndExpression)

@given(instance=stext_ElementReferenceExpression_strategy)
@settings(max_examples=50)
def test_stext_elementreferenceexpression_instantiation(instance):
    assert isinstance(instance, stext_ElementReferenceExpression)

@given(instance=stext_PrimitiveValueExpression_strategy)
@settings(max_examples=50)
def test_stext_primitivevalueexpression_instantiation(instance):
    assert isinstance(instance, stext_PrimitiveValueExpression)



@given(instance=stext_PrimitiveValueExpression_strategy)
def test_stext_primitivevalueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseXorExpression)

@given(instance=stext_BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseAndExpression)

@given(instance=stext_LogicalRelationExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalrelationexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalRelationExpression)



@given(instance=stext_LogicalRelationExpression_strategy)
def test_stext_logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_stext_bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, stext_BitwiseOrExpression)

@given(instance=stext_NumericalUnaryExpression_strategy)
@settings(max_examples=50)
def test_stext_numericalunaryexpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalUnaryExpression)



@given(instance=stext_NumericalUnaryExpression_strategy)
def test_stext_numericalunaryexpression_operator_setter(instance):
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

@given(instance=stext_NumericalAddSubtractExpression_strategy)
@settings(max_examples=50)
def test_stext_numericaladdsubtractexpression_instantiation(instance):
    assert isinstance(instance, stext_NumericalAddSubtractExpression)



@given(instance=stext_NumericalAddSubtractExpression_strategy)
def test_stext_numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalorexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalOrExpression)

@given(instance=stext_ShiftExpression_strategy)
@settings(max_examples=50)
def test_stext_shiftexpression_instantiation(instance):
    assert isinstance(instance, stext_ShiftExpression)



@given(instance=stext_ShiftExpression_strategy)
def test_stext_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=stext_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_stext_conditionalexpression_instantiation(instance):
    assert isinstance(instance, stext_ConditionalExpression)

@given(instance=stext_Statement_strategy)
@settings(max_examples=50)
def test_stext_statement_instantiation(instance):
    assert isinstance(instance, stext_Statement)

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

@given(instance=stext_LogicalNotExpression_strategy)
@settings(max_examples=50)
def test_stext_logicalnotexpression_instantiation(instance):
    assert isinstance(instance, stext_LogicalNotExpression)

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



@given(instance=stext_EventDefinition_strategy)
def test_stext_eventdefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Scope_strategy)
@settings(max_examples=50)
def test_scope_instantiation(instance):
    assert isinstance(instance, Scope)

@given(instance=stext_InterfaceScope_strategy)
@settings(max_examples=50)
def test_stext_interfacescope_instantiation(instance):
    assert isinstance(instance, stext_InterfaceScope)



@given(instance=stext_InterfaceScope_strategy)
def test_stext_interfacescope_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stext_InternalScope_strategy)
@settings(max_examples=50)
def test_stext_internalscope_instantiation(instance):
    assert isinstance(instance, stext_InternalScope)

@given(instance=stext_SimpleScope_strategy)
@settings(max_examples=50)
def test_stext_simplescope_instantiation(instance):
    assert isinstance(instance, stext_SimpleScope)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=stext_VariableDefinition_strategy)
@settings(max_examples=50)
def test_stext_variabledefinition_instantiation(instance):
    assert isinstance(instance, stext_VariableDefinition)



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=stext_VariableDefinition_strategy)
def test_stext_variabledefinition_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=stext_Variable_strategy)
@settings(max_examples=50)
def test_stext_variable_instantiation(instance):
    assert isinstance(instance, stext_Variable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=stext_Assignment_strategy)
@settings(max_examples=50)
def test_stext_assignment_instantiation(instance):
    assert isinstance(instance, stext_Assignment)



@given(instance=stext_Assignment_strategy)
def test_stext_assignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_builtineventspec_instantiation(instance):
    assert isinstance(instance, BuiltinEventSpec)

@given(instance=stext_ExitEvent_strategy)
@settings(max_examples=50)
def test_stext_exitevent_instantiation(instance):
    assert isinstance(instance, stext_ExitEvent)

@given(instance=stext_OnCycleEvent_strategy)
@settings(max_examples=50)
def test_stext_oncycleevent_instantiation(instance):
    assert isinstance(instance, stext_OnCycleEvent)

@given(instance=stext_AlwaysEvent_strategy)
@settings(max_examples=50)
def test_stext_alwaysevent_instantiation(instance):
    assert isinstance(instance, stext_AlwaysEvent)

@given(instance=stext_EntryEvent_strategy)
@settings(max_examples=50)
def test_stext_entryevent_instantiation(instance):
    assert isinstance(instance, stext_EntryEvent)

@given(instance=stext_Event_strategy)
@settings(max_examples=50)
def test_stext_event_instantiation(instance):
    assert isinstance(instance, stext_Event)

@given(instance=EventSpec_strategy)
@settings(max_examples=50)
def test_eventspec_instantiation(instance):
    assert isinstance(instance, EventSpec)

@given(instance=stext_BuiltinEventSpec_strategy)
@settings(max_examples=50)
def test_stext_builtineventspec_instantiation(instance):
    assert isinstance(instance, stext_BuiltinEventSpec)

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



@given(instance=stext_TimeEventSpec_strategy)
def test_stext_timeeventspec_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=stext_RegularEventSpec_strategy)
@settings(max_examples=50)
def test_stext_regulareventspec_instantiation(instance):
    assert isinstance(instance, stext_RegularEventSpec)

@given(instance=stext_EventSpec_strategy)
@settings(max_examples=50)
def test_stext_eventspec_instantiation(instance):
    assert isinstance(instance, stext_EventSpec)

@given(instance=stext_EventRaising_strategy)
@settings(max_examples=50)
def test_stext_eventraising_instantiation(instance):
    assert isinstance(instance, stext_EventRaising)

@given(instance=ReactionProperty_strategy)
@settings(max_examples=50)
def test_reactionproperty_instantiation(instance):
    assert isinstance(instance, ReactionProperty)

@given(instance=stext_ExitPointSpec_strategy)
@settings(max_examples=50)
def test_stext_exitpointspec_instantiation(instance):
    assert isinstance(instance, stext_ExitPointSpec)

@given(instance=stext_ReactionPriority_strategy)
@settings(max_examples=50)
def test_stext_reactionpriority_instantiation(instance):
    assert isinstance(instance, stext_ReactionPriority)



@given(instance=stext_ReactionPriority_strategy)
def test_stext_reactionpriority_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original

@given(instance=stext_ReactionProperty_strategy)
@settings(max_examples=50)
def test_stext_reactionproperty_instantiation(instance):
    assert isinstance(instance, stext_ReactionProperty)

@given(instance=TransitionStatement_strategy)
@settings(max_examples=50)
def test_transitionstatement_instantiation(instance):
    assert isinstance(instance, TransitionStatement)

@given(instance=stext_ReactionProperties_strategy)
@settings(max_examples=50)
def test_stext_reactionproperties_instantiation(instance):
    assert isinstance(instance, stext_ReactionProperties)

@given(instance=Reaction_strategy)
@settings(max_examples=50)
def test_reaction_instantiation(instance):
    assert isinstance(instance, Reaction)

@given(instance=stext_TransitionReaction_strategy)
@settings(max_examples=50)
def test_stext_transitionreaction_instantiation(instance):
    assert isinstance(instance, stext_TransitionReaction)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=stext_Operation_strategy)
@settings(max_examples=50)
def test_stext_operation_instantiation(instance):
    assert isinstance(instance, stext_Operation)



@given(instance=stext_Operation_strategy)
def test_stext_operation_paramTypes_setter(instance):
    original = instance.paramTypes
    instance.paramTypes = original
    assert instance.paramTypes == original



@given(instance=stext_Operation_strategy)
def test_stext_operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=stext_Clock_strategy)
@settings(max_examples=50)
def test_stext_clock_instantiation(instance):
    assert isinstance(instance, stext_Clock)

@given(instance=stext_Exitpoint_strategy)
@settings(max_examples=50)
def test_stext_exitpoint_instantiation(instance):
    assert isinstance(instance, stext_Exitpoint)

@given(instance=stext_LocalReaction_strategy)
@settings(max_examples=50)
def test_stext_localreaction_instantiation(instance):
    assert isinstance(instance, stext_LocalReaction)

@given(instance=stext_Expression_strategy)
@settings(max_examples=50)
def test_stext_expression_instantiation(instance):
    assert isinstance(instance, stext_Expression)

@given(instance=stext_EventDerivation_strategy)
@settings(max_examples=50)
def test_stext_eventderivation_instantiation(instance):
    assert isinstance(instance, stext_EventDerivation)

@given(instance=stext_Scope_strategy)
@settings(max_examples=50)
def test_stext_scope_instantiation(instance):
    assert isinstance(instance, stext_Scope)

@given(instance=stext_TransitionStatement_strategy)
@settings(max_examples=50)
def test_stext_transitionstatement_instantiation(instance):
    assert isinstance(instance, stext_TransitionStatement)

@given(instance=stext_StateDeclaration_strategy)
@settings(max_examples=50)
def test_stext_statedeclaration_instantiation(instance):
    assert isinstance(instance, stext_StateDeclaration)

@given(instance=stext_Entrypoint_strategy)
@settings(max_examples=50)
def test_stext_entrypoint_instantiation(instance):
    assert isinstance(instance, stext_Entrypoint)

@given(instance=stext_EntryPointSpec_strategy)
@settings(max_examples=50)
def test_stext_entrypointspec_instantiation(instance):
    assert isinstance(instance, stext_EntryPointSpec)

@given(instance=stext_DefRoot_strategy)
@settings(max_examples=50)
def test_stext_defroot_instantiation(instance):
    assert isinstance(instance, stext_DefRoot)

@given(instance=stext_Root_strategy)
@settings(max_examples=50)
def test_stext_root_instantiation(instance):
    assert isinstance(instance, stext_Root)

@given(instance=stext_StatechartDefinition_strategy)
@settings(max_examples=50)
def test_stext_statechartdefinition_instantiation(instance):
    assert isinstance(instance, stext_StatechartDefinition)



@given(instance=stext_StatechartDefinition_strategy)
def test_stext_statechartdefinition_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

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
