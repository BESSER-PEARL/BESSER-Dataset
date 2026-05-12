import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statechartexpressions_PrimaryExpression,
    statechartexpressions_MultiplicativeExpression,
    statechartexpressions_UnaryExpression,
    statechartexpressions_AdditiveExpression,
    statechartexpressions_EqualityExpression,
    statechartexpressions_ShiftExpression,
    statechartexpressions_RelationalExpression,
    statechartexpressions_BitwiseXorExpression,
    statechartexpressions_BooleanAndExpression,
    statechartexpressions_BitwiseAndExpression,
    statechartexpressions_BitwiseOrExpression,
    statechartexpressions_Procedure,
    statechartexpressions_ConditionalExpression,
    statechartexpressions_Variable,
    PrimaryExpression,
    statechartexpressions_NestedExpression,
    statechartexpressions_LiteralValue,
    TimeExpression,
    statechartexpressions_TimeConstant,
    Statement,
    statechartexpressions_EventRaising,
    statechartexpressions_ProcedureCall,
    statechartexpressions_VariableAssignment,
    statechartexpressions_Event,
    statechartexpressions_Statement,
    statechartexpressions_VariableReference,
    statechartexpressions_TimeExpression,
    Event,
    statechartexpressions_TimeEvent,
    statechartexpressions_SignalEvent,
    statechartexpressions_BooleanOrExpression,
    statechartexpressions_Trigger,
    Expression,
    statechartexpressions_GuardExpression,
    statechartexpressions_ActionExpression,
    statechartexpressions_TriggerExpression,
    statechartexpressions_Expression,
    TimeUnit,
    MultiplicativeOperator,
    AdditiveOperator,
    UnaryOperator,
    ShiftOperator,
    RelationalOperator,
    EqualityOperator,
    AssignmentOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechartexpressions_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_PrimaryExpression)


def test_statechartexpressions_primaryexpression_constructor_exists():
    assert callable(statechartexpressions_PrimaryExpression.__init__)


def test_statechartexpressions_primaryexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_MultiplicativeExpression)


def test_statechartexpressions_multiplicativeexpression_constructor_exists():
    assert callable(statechartexpressions_MultiplicativeExpression.__init__)


def test_statechartexpressions_multiplicativeexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_multiplicativeexpression_has_operator():
    assert hasattr(statechartexpressions_MultiplicativeExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_MultiplicativeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_UnaryExpression)


def test_statechartexpressions_unaryexpression_constructor_exists():
    assert callable(statechartexpressions_UnaryExpression.__init__)


def test_statechartexpressions_unaryexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_unaryexpression_has_operator():
    assert hasattr(statechartexpressions_UnaryExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_additiveexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_AdditiveExpression)


def test_statechartexpressions_additiveexpression_constructor_exists():
    assert callable(statechartexpressions_AdditiveExpression.__init__)


def test_statechartexpressions_additiveexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_additiveexpression_has_operator():
    assert hasattr(statechartexpressions_AdditiveExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_AdditiveExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_EqualityExpression)


def test_statechartexpressions_equalityexpression_constructor_exists():
    assert callable(statechartexpressions_EqualityExpression.__init__)


def test_statechartexpressions_equalityexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_equalityexpression_has_operator():
    assert hasattr(statechartexpressions_EqualityExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_EqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_ShiftExpression)


def test_statechartexpressions_shiftexpression_constructor_exists():
    assert callable(statechartexpressions_ShiftExpression.__init__)


def test_statechartexpressions_shiftexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_shiftexpression_has_operator():
    assert hasattr(statechartexpressions_ShiftExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_relationalexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_RelationalExpression)


def test_statechartexpressions_relationalexpression_constructor_exists():
    assert callable(statechartexpressions_RelationalExpression.__init__)


def test_statechartexpressions_relationalexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_relationalexpression_has_operator():
    assert hasattr(statechartexpressions_RelationalExpression, "operator")
    descriptor = None
    for klass in statechartexpressions_RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_BitwiseXorExpression)


def test_statechartexpressions_bitwisexorexpression_constructor_exists():
    assert callable(statechartexpressions_BitwiseXorExpression.__init__)


def test_statechartexpressions_bitwisexorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_booleanandexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_BooleanAndExpression)


def test_statechartexpressions_booleanandexpression_constructor_exists():
    assert callable(statechartexpressions_BooleanAndExpression.__init__)


def test_statechartexpressions_booleanandexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_BooleanAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_BitwiseAndExpression)


def test_statechartexpressions_bitwiseandexpression_constructor_exists():
    assert callable(statechartexpressions_BitwiseAndExpression.__init__)


def test_statechartexpressions_bitwiseandexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_BitwiseOrExpression)


def test_statechartexpressions_bitwiseorexpression_constructor_exists():
    assert callable(statechartexpressions_BitwiseOrExpression.__init__)


def test_statechartexpressions_bitwiseorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_procedure_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Procedure)


def test_statechartexpressions_procedure_constructor_exists():
    assert callable(statechartexpressions_Procedure.__init__)


def test_statechartexpressions_procedure_constructor_args():
    sig = inspect.signature(statechartexpressions_Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions_procedure_has_identifier():
    assert hasattr(statechartexpressions_Procedure, "identifier")
    descriptor = None
    for klass in statechartexpressions_Procedure.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_ConditionalExpression)


def test_statechartexpressions_conditionalexpression_constructor_exists():
    assert callable(statechartexpressions_ConditionalExpression.__init__)


def test_statechartexpressions_conditionalexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_variable_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Variable)


def test_statechartexpressions_variable_constructor_exists():
    assert callable(statechartexpressions_Variable.__init__)


def test_statechartexpressions_variable_constructor_args():
    sig = inspect.signature(statechartexpressions_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions_variable_has_identifier():
    assert hasattr(statechartexpressions_Variable, "identifier")
    descriptor = None
    for klass in statechartexpressions_Variable.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_nestedexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_NestedExpression)


def test_statechartexpressions_nestedexpression_constructor_exists():
    assert callable(statechartexpressions_NestedExpression.__init__)


def test_statechartexpressions_nestedexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_literalvalue_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_LiteralValue)


def test_statechartexpressions_literalvalue_constructor_exists():
    assert callable(statechartexpressions_LiteralValue.__init__)


def test_statechartexpressions_literalvalue_constructor_args():
    sig = inspect.signature(statechartexpressions_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statechartexpressions_literalvalue_has_value():
    assert hasattr(statechartexpressions_LiteralValue, "value")
    descriptor = None
    for klass in statechartexpressions_LiteralValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_timeexpression_is_not_abstract():
    assert not inspect.isabstract(TimeExpression)


def test_timeexpression_constructor_exists():
    assert callable(TimeExpression.__init__)


def test_timeexpression_constructor_args():
    sig = inspect.signature(TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_timeconstant_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_TimeConstant)


def test_statechartexpressions_timeconstant_constructor_exists():
    assert callable(statechartexpressions_TimeConstant.__init__)


def test_statechartexpressions_timeconstant_constructor_args():
    sig = inspect.signature(statechartexpressions_TimeConstant.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_statechartexpressions_timeconstant_has_unit():
    assert hasattr(statechartexpressions_TimeConstant, "unit")
    descriptor = None
    for klass in statechartexpressions_TimeConstant.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_statechartexpressions_timeconstant_has_value():
    assert hasattr(statechartexpressions_TimeConstant, "value")
    descriptor = None
    for klass in statechartexpressions_TimeConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_eventraising_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_EventRaising)


def test_statechartexpressions_eventraising_constructor_exists():
    assert callable(statechartexpressions_EventRaising.__init__)


def test_statechartexpressions_eventraising_constructor_args():
    sig = inspect.signature(statechartexpressions_EventRaising.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_procedurecall_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_ProcedureCall)


def test_statechartexpressions_procedurecall_constructor_exists():
    assert callable(statechartexpressions_ProcedureCall.__init__)


def test_statechartexpressions_procedurecall_constructor_args():
    sig = inspect.signature(statechartexpressions_ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_variableassignment_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_VariableAssignment)


def test_statechartexpressions_variableassignment_constructor_exists():
    assert callable(statechartexpressions_VariableAssignment.__init__)


def test_statechartexpressions_variableassignment_constructor_args():
    sig = inspect.signature(statechartexpressions_VariableAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions_variableassignment_has_operator():
    assert hasattr(statechartexpressions_VariableAssignment, "operator")
    descriptor = None
    for klass in statechartexpressions_VariableAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_event_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Event)


def test_statechartexpressions_event_constructor_exists():
    assert callable(statechartexpressions_Event.__init__)


def test_statechartexpressions_event_constructor_args():
    sig = inspect.signature(statechartexpressions_Event.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_statement_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Statement)


def test_statechartexpressions_statement_constructor_exists():
    assert callable(statechartexpressions_Statement.__init__)


def test_statechartexpressions_statement_constructor_args():
    sig = inspect.signature(statechartexpressions_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_variablereference_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_VariableReference)


def test_statechartexpressions_variablereference_constructor_exists():
    assert callable(statechartexpressions_VariableReference.__init__)


def test_statechartexpressions_variablereference_constructor_args():
    sig = inspect.signature(statechartexpressions_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_timeexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_TimeExpression)


def test_statechartexpressions_timeexpression_constructor_exists():
    assert callable(statechartexpressions_TimeExpression.__init__)


def test_statechartexpressions_timeexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_timeevent_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_TimeEvent)


def test_statechartexpressions_timeevent_constructor_exists():
    assert callable(statechartexpressions_TimeEvent.__init__)


def test_statechartexpressions_timeevent_constructor_args():
    sig = inspect.signature(statechartexpressions_TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_signalevent_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_SignalEvent)


def test_statechartexpressions_signalevent_constructor_exists():
    assert callable(statechartexpressions_SignalEvent.__init__)


def test_statechartexpressions_signalevent_constructor_args():
    sig = inspect.signature(statechartexpressions_SignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions_signalevent_has_identifier():
    assert hasattr(statechartexpressions_SignalEvent, "identifier")
    descriptor = None
    for klass in statechartexpressions_SignalEvent.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions_booleanorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_BooleanOrExpression)


def test_statechartexpressions_booleanorexpression_constructor_exists():
    assert callable(statechartexpressions_BooleanOrExpression.__init__)


def test_statechartexpressions_booleanorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_BooleanOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_trigger_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Trigger)


def test_statechartexpressions_trigger_constructor_exists():
    assert callable(statechartexpressions_Trigger.__init__)


def test_statechartexpressions_trigger_constructor_args():
    sig = inspect.signature(statechartexpressions_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_guardexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_GuardExpression)


def test_statechartexpressions_guardexpression_constructor_exists():
    assert callable(statechartexpressions_GuardExpression.__init__)


def test_statechartexpressions_guardexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_GuardExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_actionexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_ActionExpression)


def test_statechartexpressions_actionexpression_constructor_exists():
    assert callable(statechartexpressions_ActionExpression.__init__)


def test_statechartexpressions_actionexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_TriggerExpression)


def test_statechartexpressions_triggerexpression_constructor_exists():
    assert callable(statechartexpressions_TriggerExpression.__init__)


def test_statechartexpressions_triggerexpression_constructor_args():
    sig = inspect.signature(statechartexpressions_TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions_expression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions_Expression)


def test_statechartexpressions_expression_constructor_exists():
    assert callable(statechartexpressions_Expression.__init__)


def test_statechartexpressions_expression_constructor_args():
    sig = inspect.signature(statechartexpressions_Expression.__init__)
    params = list(sig.parameters.keys())

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

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mul",
        "mod",
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
        "complement",
        "not_",
        "positive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

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
        "greaterEqual",
        "smaller",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_equalityoperator_exists():
    # Check that the Enumeration exists
    assert EqualityOperator is not None

def test_equalityoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EqualityOperator]
    expected_literals = [
        "equals",
        "notEquals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EqualityOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "multAssign",
        "subAssign",
        "modAssign",
        "leftShiftAssign",
        "divAssign",
        "andAssign",
        "xorAssign",
        "addAssign",
        "rightShiftAssign",
        "orAssign",
        "assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"


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
statechartexpressions_PrimaryExpression_strategy = st.builds(
    statechartexpressions_PrimaryExpression,
)
statechartexpressions_MultiplicativeExpression_strategy = st.builds(
    statechartexpressions_MultiplicativeExpression,
    operator=
        safe_text
)
statechartexpressions_UnaryExpression_strategy = st.builds(
    statechartexpressions_UnaryExpression,
    operator=
        safe_text
)
statechartexpressions_AdditiveExpression_strategy = st.builds(
    statechartexpressions_AdditiveExpression,
    operator=
        safe_text
)
statechartexpressions_EqualityExpression_strategy = st.builds(
    statechartexpressions_EqualityExpression,
    operator=
        safe_text
)
statechartexpressions_ShiftExpression_strategy = st.builds(
    statechartexpressions_ShiftExpression,
    operator=
        safe_text
)
statechartexpressions_RelationalExpression_strategy = st.builds(
    statechartexpressions_RelationalExpression,
    operator=
        safe_text
)
statechartexpressions_BitwiseXorExpression_strategy = st.builds(
    statechartexpressions_BitwiseXorExpression,
)
statechartexpressions_BooleanAndExpression_strategy = st.builds(
    statechartexpressions_BooleanAndExpression,
)
statechartexpressions_BitwiseAndExpression_strategy = st.builds(
    statechartexpressions_BitwiseAndExpression,
)
statechartexpressions_BitwiseOrExpression_strategy = st.builds(
    statechartexpressions_BitwiseOrExpression,
)
statechartexpressions_Procedure_strategy = st.builds(
    statechartexpressions_Procedure,
    identifier=
        safe_text
)
statechartexpressions_ConditionalExpression_strategy = st.builds(
    statechartexpressions_ConditionalExpression,
)
statechartexpressions_Variable_strategy = st.builds(
    statechartexpressions_Variable,
    identifier=
        safe_text
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
statechartexpressions_NestedExpression_strategy = st.builds(
    statechartexpressions_NestedExpression,
)
statechartexpressions_LiteralValue_strategy = st.builds(
    statechartexpressions_LiteralValue,
    value=
        safe_text
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
statechartexpressions_TimeConstant_strategy = st.builds(
    statechartexpressions_TimeConstant,
    unit=
        safe_text,
    value=
        st.integers()
)
Statement_strategy = st.builds(
    Statement,
)
statechartexpressions_EventRaising_strategy = st.builds(
    statechartexpressions_EventRaising,
)
statechartexpressions_ProcedureCall_strategy = st.builds(
    statechartexpressions_ProcedureCall,
)
statechartexpressions_VariableAssignment_strategy = st.builds(
    statechartexpressions_VariableAssignment,
    operator=
        safe_text
)
statechartexpressions_Event_strategy = st.builds(
    statechartexpressions_Event,
)
statechartexpressions_Statement_strategy = st.builds(
    statechartexpressions_Statement,
)
statechartexpressions_VariableReference_strategy = st.builds(
    statechartexpressions_VariableReference,
)
statechartexpressions_TimeExpression_strategy = st.builds(
    statechartexpressions_TimeExpression,
)
Event_strategy = st.builds(
    Event,
)
statechartexpressions_TimeEvent_strategy = st.builds(
    statechartexpressions_TimeEvent,
)
statechartexpressions_SignalEvent_strategy = st.builds(
    statechartexpressions_SignalEvent,
    identifier=
        safe_text
)
statechartexpressions_BooleanOrExpression_strategy = st.builds(
    statechartexpressions_BooleanOrExpression,
)
statechartexpressions_Trigger_strategy = st.builds(
    statechartexpressions_Trigger,
)
Expression_strategy = st.builds(
    Expression,
)
statechartexpressions_GuardExpression_strategy = st.builds(
    statechartexpressions_GuardExpression,
)
statechartexpressions_ActionExpression_strategy = st.builds(
    statechartexpressions_ActionExpression,
)
statechartexpressions_TriggerExpression_strategy = st.builds(
    statechartexpressions_TriggerExpression,
)
statechartexpressions_Expression_strategy = st.builds(
    statechartexpressions_Expression,
)

@given(instance=statechartexpressions_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_primaryexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_PrimaryExpression)

@given(instance=statechartexpressions_MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_MultiplicativeExpression)



@given(instance=statechartexpressions_MultiplicativeExpression_strategy)
def test_statechartexpressions_multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_UnaryExpression)



@given(instance=statechartexpressions_UnaryExpression_strategy)
def test_statechartexpressions_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_AdditiveExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_additiveexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_AdditiveExpression)



@given(instance=statechartexpressions_AdditiveExpression_strategy)
def test_statechartexpressions_additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_EqualityExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_equalityexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_EqualityExpression)



@given(instance=statechartexpressions_EqualityExpression_strategy)
def test_statechartexpressions_equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_ShiftExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_shiftexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_ShiftExpression)



@given(instance=statechartexpressions_ShiftExpression_strategy)
def test_statechartexpressions_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_RelationalExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_relationalexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_RelationalExpression)



@given(instance=statechartexpressions_RelationalExpression_strategy)
def test_statechartexpressions_relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_BitwiseXorExpression)

@given(instance=statechartexpressions_BooleanAndExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_booleanandexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_BooleanAndExpression)

@given(instance=statechartexpressions_BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_BitwiseAndExpression)

@given(instance=statechartexpressions_BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_BitwiseOrExpression)

@given(instance=statechartexpressions_Procedure_strategy)
@settings(max_examples=50)
def test_statechartexpressions_procedure_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Procedure)



@given(instance=statechartexpressions_Procedure_strategy)
def test_statechartexpressions_procedure_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=statechartexpressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_ConditionalExpression)

@given(instance=statechartexpressions_Variable_strategy)
@settings(max_examples=50)
def test_statechartexpressions_variable_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Variable)



@given(instance=statechartexpressions_Variable_strategy)
def test_statechartexpressions_variable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=statechartexpressions_NestedExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_nestedexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_NestedExpression)

@given(instance=statechartexpressions_LiteralValue_strategy)
@settings(max_examples=50)
def test_statechartexpressions_literalvalue_instantiation(instance):
    assert isinstance(instance, statechartexpressions_LiteralValue)



@given(instance=statechartexpressions_LiteralValue_strategy)
def test_statechartexpressions_literalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TimeExpression_strategy)
@settings(max_examples=50)
def test_timeexpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)

@given(instance=statechartexpressions_TimeConstant_strategy)
@settings(max_examples=50)
def test_statechartexpressions_timeconstant_instantiation(instance):
    assert isinstance(instance, statechartexpressions_TimeConstant)



@given(instance=statechartexpressions_TimeConstant_strategy)
def test_statechartexpressions_timeconstant_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=statechartexpressions_TimeConstant_strategy)
def test_statechartexpressions_timeconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=statechartexpressions_EventRaising_strategy)
@settings(max_examples=50)
def test_statechartexpressions_eventraising_instantiation(instance):
    assert isinstance(instance, statechartexpressions_EventRaising)

@given(instance=statechartexpressions_ProcedureCall_strategy)
@settings(max_examples=50)
def test_statechartexpressions_procedurecall_instantiation(instance):
    assert isinstance(instance, statechartexpressions_ProcedureCall)

@given(instance=statechartexpressions_VariableAssignment_strategy)
@settings(max_examples=50)
def test_statechartexpressions_variableassignment_instantiation(instance):
    assert isinstance(instance, statechartexpressions_VariableAssignment)



@given(instance=statechartexpressions_VariableAssignment_strategy)
def test_statechartexpressions_variableassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions_Event_strategy)
@settings(max_examples=50)
def test_statechartexpressions_event_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Event)

@given(instance=statechartexpressions_Statement_strategy)
@settings(max_examples=50)
def test_statechartexpressions_statement_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Statement)

@given(instance=statechartexpressions_VariableReference_strategy)
@settings(max_examples=50)
def test_statechartexpressions_variablereference_instantiation(instance):
    assert isinstance(instance, statechartexpressions_VariableReference)

@given(instance=statechartexpressions_TimeExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_timeexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_TimeExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statechartexpressions_TimeEvent_strategy)
@settings(max_examples=50)
def test_statechartexpressions_timeevent_instantiation(instance):
    assert isinstance(instance, statechartexpressions_TimeEvent)

@given(instance=statechartexpressions_SignalEvent_strategy)
@settings(max_examples=50)
def test_statechartexpressions_signalevent_instantiation(instance):
    assert isinstance(instance, statechartexpressions_SignalEvent)



@given(instance=statechartexpressions_SignalEvent_strategy)
def test_statechartexpressions_signalevent_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=statechartexpressions_BooleanOrExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_booleanorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_BooleanOrExpression)

@given(instance=statechartexpressions_Trigger_strategy)
@settings(max_examples=50)
def test_statechartexpressions_trigger_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Trigger)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=statechartexpressions_GuardExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_guardexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_GuardExpression)

@given(instance=statechartexpressions_ActionExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_actionexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_ActionExpression)

@given(instance=statechartexpressions_TriggerExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_triggerexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_TriggerExpression)

@given(instance=statechartexpressions_Expression_strategy)
@settings(max_examples=50)
def test_statechartexpressions_expression_instantiation(instance):
    assert isinstance(instance, statechartexpressions_Expression)
