import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statechartexpressions::PrimaryExpression,
    statechartexpressions::MultiplicativeExpression,
    statechartexpressions::UnaryExpression,
    statechartexpressions::AdditiveExpression,
    statechartexpressions::EqualityExpression,
    statechartexpressions::ShiftExpression,
    statechartexpressions::RelationalExpression,
    statechartexpressions::BitwiseXorExpression,
    statechartexpressions::BooleanAndExpression,
    statechartexpressions::BitwiseAndExpression,
    statechartexpressions::BitwiseOrExpression,
    statechartexpressions::Procedure,
    statechartexpressions::ConditionalExpression,
    statechartexpressions::Variable,
    PrimaryExpression,
    statechartexpressions::NestedExpression,
    statechartexpressions::LiteralValue,
    TimeExpression,
    statechartexpressions::TimeConstant,
    Statement,
    statechartexpressions::EventRaising,
    statechartexpressions::ProcedureCall,
    statechartexpressions::VariableAssignment,
    statechartexpressions::Event,
    statechartexpressions::Statement,
    statechartexpressions::VariableReference,
    statechartexpressions::TimeExpression,
    Event,
    statechartexpressions::TimeEvent,
    statechartexpressions::SignalEvent,
    statechartexpressions::BooleanOrExpression,
    statechartexpressions::Trigger,
    Expression,
    statechartexpressions::ActionExpression,
    statechartexpressions::GuardExpression,
    statechartexpressions::TriggerExpression,
    statechartexpressions::Expression,
    AssignmentOperator,
    UnaryOperator,
    TimeUnit,
    ShiftOperator,
    MultiplicativeOperator,
    AdditiveOperator,
    EqualityOperator,
    RelationalOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechartexpressions::primaryexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::PrimaryExpression)


def test_statechartexpressions::primaryexpression_constructor_exists():
    assert callable(statechartexpressions::PrimaryExpression.__init__)


def test_statechartexpressions::primaryexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::multiplicativeexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::MultiplicativeExpression)


def test_statechartexpressions::multiplicativeexpression_constructor_exists():
    assert callable(statechartexpressions::MultiplicativeExpression.__init__)


def test_statechartexpressions::multiplicativeexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::MultiplicativeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::multiplicativeexpression_has_operator():
    assert hasattr(statechartexpressions::MultiplicativeExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::MultiplicativeExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::UnaryExpression)


def test_statechartexpressions::unaryexpression_constructor_exists():
    assert callable(statechartexpressions::UnaryExpression.__init__)


def test_statechartexpressions::unaryexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::unaryexpression_has_operator():
    assert hasattr(statechartexpressions::UnaryExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::additiveexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::AdditiveExpression)


def test_statechartexpressions::additiveexpression_constructor_exists():
    assert callable(statechartexpressions::AdditiveExpression.__init__)


def test_statechartexpressions::additiveexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::AdditiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::additiveexpression_has_operator():
    assert hasattr(statechartexpressions::AdditiveExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::AdditiveExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::EqualityExpression)


def test_statechartexpressions::equalityexpression_constructor_exists():
    assert callable(statechartexpressions::EqualityExpression.__init__)


def test_statechartexpressions::equalityexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::EqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::equalityexpression_has_operator():
    assert hasattr(statechartexpressions::EqualityExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::EqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::ShiftExpression)


def test_statechartexpressions::shiftexpression_constructor_exists():
    assert callable(statechartexpressions::ShiftExpression.__init__)


def test_statechartexpressions::shiftexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::shiftexpression_has_operator():
    assert hasattr(statechartexpressions::ShiftExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::RelationalExpression)


def test_statechartexpressions::relationalexpression_constructor_exists():
    assert callable(statechartexpressions::RelationalExpression.__init__)


def test_statechartexpressions::relationalexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::relationalexpression_has_operator():
    assert hasattr(statechartexpressions::RelationalExpression, "operator")
    descriptor = None
    for klass in statechartexpressions::RelationalExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::BitwiseXorExpression)


def test_statechartexpressions::bitwisexorexpression_constructor_exists():
    assert callable(statechartexpressions::BitwiseXorExpression.__init__)


def test_statechartexpressions::bitwisexorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::booleanandexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::BooleanAndExpression)


def test_statechartexpressions::booleanandexpression_constructor_exists():
    assert callable(statechartexpressions::BooleanAndExpression.__init__)


def test_statechartexpressions::booleanandexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::BooleanAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::BitwiseAndExpression)


def test_statechartexpressions::bitwiseandexpression_constructor_exists():
    assert callable(statechartexpressions::BitwiseAndExpression.__init__)


def test_statechartexpressions::bitwiseandexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::BitwiseOrExpression)


def test_statechartexpressions::bitwiseorexpression_constructor_exists():
    assert callable(statechartexpressions::BitwiseOrExpression.__init__)


def test_statechartexpressions::bitwiseorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::procedure_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Procedure)


def test_statechartexpressions::procedure_constructor_exists():
    assert callable(statechartexpressions::Procedure.__init__)


def test_statechartexpressions::procedure_constructor_args():
    sig = inspect.signature(statechartexpressions::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions::procedure_has_identifier():
    assert hasattr(statechartexpressions::Procedure, "identifier")
    descriptor = None
    for klass in statechartexpressions::Procedure.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::ConditionalExpression)


def test_statechartexpressions::conditionalexpression_constructor_exists():
    assert callable(statechartexpressions::ConditionalExpression.__init__)


def test_statechartexpressions::conditionalexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::variable_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Variable)


def test_statechartexpressions::variable_constructor_exists():
    assert callable(statechartexpressions::Variable.__init__)


def test_statechartexpressions::variable_constructor_args():
    sig = inspect.signature(statechartexpressions::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions::variable_has_identifier():
    assert hasattr(statechartexpressions::Variable, "identifier")
    descriptor = None
    for klass in statechartexpressions::Variable.__mro__:
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



def test_statechartexpressions::nestedexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::NestedExpression)


def test_statechartexpressions::nestedexpression_constructor_exists():
    assert callable(statechartexpressions::NestedExpression.__init__)


def test_statechartexpressions::nestedexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::NestedExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::literalvalue_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::LiteralValue)


def test_statechartexpressions::literalvalue_constructor_exists():
    assert callable(statechartexpressions::LiteralValue.__init__)


def test_statechartexpressions::literalvalue_constructor_args():
    sig = inspect.signature(statechartexpressions::LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_statechartexpressions::literalvalue_has_value():
    assert hasattr(statechartexpressions::LiteralValue, "value")
    descriptor = None
    for klass in statechartexpressions::LiteralValue.__mro__:
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



def test_statechartexpressions::timeconstant_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::TimeConstant)


def test_statechartexpressions::timeconstant_constructor_exists():
    assert callable(statechartexpressions::TimeConstant.__init__)


def test_statechartexpressions::timeconstant_constructor_args():
    sig = inspect.signature(statechartexpressions::TimeConstant.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "value" in params, "Missing parameter 'value'"

def test_statechartexpressions::timeconstant_has_unit():
    assert hasattr(statechartexpressions::TimeConstant, "unit")
    descriptor = None
    for klass in statechartexpressions::TimeConstant.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_statechartexpressions::timeconstant_has_value():
    assert hasattr(statechartexpressions::TimeConstant, "value")
    descriptor = None
    for klass in statechartexpressions::TimeConstant.__mro__:
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



def test_statechartexpressions::eventraising_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::EventRaising)


def test_statechartexpressions::eventraising_constructor_exists():
    assert callable(statechartexpressions::EventRaising.__init__)


def test_statechartexpressions::eventraising_constructor_args():
    sig = inspect.signature(statechartexpressions::EventRaising.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::procedurecall_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::ProcedureCall)


def test_statechartexpressions::procedurecall_constructor_exists():
    assert callable(statechartexpressions::ProcedureCall.__init__)


def test_statechartexpressions::procedurecall_constructor_args():
    sig = inspect.signature(statechartexpressions::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::variableassignment_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::VariableAssignment)


def test_statechartexpressions::variableassignment_constructor_exists():
    assert callable(statechartexpressions::VariableAssignment.__init__)


def test_statechartexpressions::variableassignment_constructor_args():
    sig = inspect.signature(statechartexpressions::VariableAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_statechartexpressions::variableassignment_has_operator():
    assert hasattr(statechartexpressions::VariableAssignment, "operator")
    descriptor = None
    for klass in statechartexpressions::VariableAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::event_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Event)


def test_statechartexpressions::event_constructor_exists():
    assert callable(statechartexpressions::Event.__init__)


def test_statechartexpressions::event_constructor_args():
    sig = inspect.signature(statechartexpressions::Event.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::statement_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Statement)


def test_statechartexpressions::statement_constructor_exists():
    assert callable(statechartexpressions::Statement.__init__)


def test_statechartexpressions::statement_constructor_args():
    sig = inspect.signature(statechartexpressions::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::variablereference_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::VariableReference)


def test_statechartexpressions::variablereference_constructor_exists():
    assert callable(statechartexpressions::VariableReference.__init__)


def test_statechartexpressions::variablereference_constructor_args():
    sig = inspect.signature(statechartexpressions::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::timeexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::TimeExpression)


def test_statechartexpressions::timeexpression_constructor_exists():
    assert callable(statechartexpressions::TimeExpression.__init__)


def test_statechartexpressions::timeexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::timeevent_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::TimeEvent)


def test_statechartexpressions::timeevent_constructor_exists():
    assert callable(statechartexpressions::TimeEvent.__init__)


def test_statechartexpressions::timeevent_constructor_args():
    sig = inspect.signature(statechartexpressions::TimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::signalevent_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::SignalEvent)


def test_statechartexpressions::signalevent_constructor_exists():
    assert callable(statechartexpressions::SignalEvent.__init__)


def test_statechartexpressions::signalevent_constructor_args():
    sig = inspect.signature(statechartexpressions::SignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_statechartexpressions::signalevent_has_identifier():
    assert hasattr(statechartexpressions::SignalEvent, "identifier")
    descriptor = None
    for klass in statechartexpressions::SignalEvent.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_statechartexpressions::booleanorexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::BooleanOrExpression)


def test_statechartexpressions::booleanorexpression_constructor_exists():
    assert callable(statechartexpressions::BooleanOrExpression.__init__)


def test_statechartexpressions::booleanorexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::BooleanOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::trigger_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Trigger)


def test_statechartexpressions::trigger_constructor_exists():
    assert callable(statechartexpressions::Trigger.__init__)


def test_statechartexpressions::trigger_constructor_args():
    sig = inspect.signature(statechartexpressions::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::actionexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::ActionExpression)


def test_statechartexpressions::actionexpression_constructor_exists():
    assert callable(statechartexpressions::ActionExpression.__init__)


def test_statechartexpressions::actionexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::guardexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::GuardExpression)


def test_statechartexpressions::guardexpression_constructor_exists():
    assert callable(statechartexpressions::GuardExpression.__init__)


def test_statechartexpressions::guardexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::GuardExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::triggerexpression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::TriggerExpression)


def test_statechartexpressions::triggerexpression_constructor_exists():
    assert callable(statechartexpressions::TriggerExpression.__init__)


def test_statechartexpressions::triggerexpression_constructor_args():
    sig = inspect.signature(statechartexpressions::TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_statechartexpressions::expression_is_not_abstract():
    assert not inspect.isabstract(statechartexpressions::Expression)


def test_statechartexpressions::expression_constructor_exists():
    assert callable(statechartexpressions::Expression.__init__)


def test_statechartexpressions::expression_constructor_args():
    sig = inspect.signature(statechartexpressions::Expression.__init__)
    params = list(sig.parameters.keys())

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "modAssign",
        "leftShiftAssign",
        "rightShiftAssign",
        "subAssign",
        "divAssign",
        "xorAssign",
        "addAssign",
        "orAssign",
        "andAssign",
        "assign",
        "multAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "complement",
        "negative",
        "not_",
        "positive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

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

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "right",
        "left",
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

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "greaterEqual",
        "smallerEqual",
        "greater",
        "smaller",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"


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
statechartexpressions::PrimaryExpression_strategy = st.builds(
    statechartexpressions::PrimaryExpression,
)
statechartexpressions::MultiplicativeExpression_strategy = st.builds(
    statechartexpressions::MultiplicativeExpression,
    operator=
        safe_text
)
statechartexpressions::UnaryExpression_strategy = st.builds(
    statechartexpressions::UnaryExpression,
    operator=
        safe_text
)
statechartexpressions::AdditiveExpression_strategy = st.builds(
    statechartexpressions::AdditiveExpression,
    operator=
        safe_text
)
statechartexpressions::EqualityExpression_strategy = st.builds(
    statechartexpressions::EqualityExpression,
    operator=
        safe_text
)
statechartexpressions::ShiftExpression_strategy = st.builds(
    statechartexpressions::ShiftExpression,
    operator=
        safe_text
)
statechartexpressions::RelationalExpression_strategy = st.builds(
    statechartexpressions::RelationalExpression,
    operator=
        safe_text
)
statechartexpressions::BitwiseXorExpression_strategy = st.builds(
    statechartexpressions::BitwiseXorExpression,
)
statechartexpressions::BooleanAndExpression_strategy = st.builds(
    statechartexpressions::BooleanAndExpression,
)
statechartexpressions::BitwiseAndExpression_strategy = st.builds(
    statechartexpressions::BitwiseAndExpression,
)
statechartexpressions::BitwiseOrExpression_strategy = st.builds(
    statechartexpressions::BitwiseOrExpression,
)
statechartexpressions::Procedure_strategy = st.builds(
    statechartexpressions::Procedure,
    identifier=
        safe_text
)
statechartexpressions::ConditionalExpression_strategy = st.builds(
    statechartexpressions::ConditionalExpression,
)
statechartexpressions::Variable_strategy = st.builds(
    statechartexpressions::Variable,
    identifier=
        safe_text
)
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
statechartexpressions::NestedExpression_strategy = st.builds(
    statechartexpressions::NestedExpression,
)
statechartexpressions::LiteralValue_strategy = st.builds(
    statechartexpressions::LiteralValue,
    value=
        safe_text
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
statechartexpressions::TimeConstant_strategy = st.builds(
    statechartexpressions::TimeConstant,
    unit=
        safe_text,
    value=
        st.integers()
)
Statement_strategy = st.builds(
    Statement,
)
statechartexpressions::EventRaising_strategy = st.builds(
    statechartexpressions::EventRaising,
)
statechartexpressions::ProcedureCall_strategy = st.builds(
    statechartexpressions::ProcedureCall,
)
statechartexpressions::VariableAssignment_strategy = st.builds(
    statechartexpressions::VariableAssignment,
    operator=
        safe_text
)
statechartexpressions::Event_strategy = st.builds(
    statechartexpressions::Event,
)
statechartexpressions::Statement_strategy = st.builds(
    statechartexpressions::Statement,
)
statechartexpressions::VariableReference_strategy = st.builds(
    statechartexpressions::VariableReference,
)
statechartexpressions::TimeExpression_strategy = st.builds(
    statechartexpressions::TimeExpression,
)
Event_strategy = st.builds(
    Event,
)
statechartexpressions::TimeEvent_strategy = st.builds(
    statechartexpressions::TimeEvent,
)
statechartexpressions::SignalEvent_strategy = st.builds(
    statechartexpressions::SignalEvent,
    identifier=
        safe_text
)
statechartexpressions::BooleanOrExpression_strategy = st.builds(
    statechartexpressions::BooleanOrExpression,
)
statechartexpressions::Trigger_strategy = st.builds(
    statechartexpressions::Trigger,
)
Expression_strategy = st.builds(
    Expression,
)
statechartexpressions::ActionExpression_strategy = st.builds(
    statechartexpressions::ActionExpression,
)
statechartexpressions::GuardExpression_strategy = st.builds(
    statechartexpressions::GuardExpression,
)
statechartexpressions::TriggerExpression_strategy = st.builds(
    statechartexpressions::TriggerExpression,
)
statechartexpressions::Expression_strategy = st.builds(
    statechartexpressions::Expression,
)

@given(instance=statechartexpressions::PrimaryExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::primaryexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::PrimaryExpression)

@given(instance=statechartexpressions::MultiplicativeExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::multiplicativeexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::MultiplicativeExpression)

@given(instance=statechartexpressions::MultiplicativeExpression_strategy)
def test_statechartexpressions::multiplicativeexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::MultiplicativeExpression_strategy)
def test_statechartexpressions::multiplicativeexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::UnaryExpression)

@given(instance=statechartexpressions::UnaryExpression_strategy)
def test_statechartexpressions::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::UnaryExpression_strategy)
def test_statechartexpressions::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::AdditiveExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::additiveexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::AdditiveExpression)

@given(instance=statechartexpressions::AdditiveExpression_strategy)
def test_statechartexpressions::additiveexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::AdditiveExpression_strategy)
def test_statechartexpressions::additiveexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::EqualityExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::equalityexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::EqualityExpression)

@given(instance=statechartexpressions::EqualityExpression_strategy)
def test_statechartexpressions::equalityexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::EqualityExpression_strategy)
def test_statechartexpressions::equalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::ShiftExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::shiftexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::ShiftExpression)

@given(instance=statechartexpressions::ShiftExpression_strategy)
def test_statechartexpressions::shiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::ShiftExpression_strategy)
def test_statechartexpressions::shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::RelationalExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::relationalexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::RelationalExpression)

@given(instance=statechartexpressions::RelationalExpression_strategy)
def test_statechartexpressions::relationalexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::RelationalExpression_strategy)
def test_statechartexpressions::relationalexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::BitwiseXorExpression)

@given(instance=statechartexpressions::BooleanAndExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::booleanandexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::BooleanAndExpression)

@given(instance=statechartexpressions::BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::BitwiseAndExpression)

@given(instance=statechartexpressions::BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::BitwiseOrExpression)

@given(instance=statechartexpressions::Procedure_strategy)
@settings(max_examples=50)
def test_statechartexpressions::procedure_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Procedure)

@given(instance=statechartexpressions::Procedure_strategy)
def test_statechartexpressions::procedure_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=statechartexpressions::Procedure_strategy)
def test_statechartexpressions::procedure_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=statechartexpressions::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::conditionalexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::ConditionalExpression)

@given(instance=statechartexpressions::Variable_strategy)
@settings(max_examples=50)
def test_statechartexpressions::variable_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Variable)

@given(instance=statechartexpressions::Variable_strategy)
def test_statechartexpressions::variable_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=statechartexpressions::Variable_strategy)
def test_statechartexpressions::variable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=statechartexpressions::NestedExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::nestedexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::NestedExpression)

@given(instance=statechartexpressions::LiteralValue_strategy)
@settings(max_examples=50)
def test_statechartexpressions::literalvalue_instantiation(instance):
    assert isinstance(instance, statechartexpressions::LiteralValue)

@given(instance=statechartexpressions::LiteralValue_strategy)
def test_statechartexpressions::literalvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=statechartexpressions::LiteralValue_strategy)
def test_statechartexpressions::literalvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TimeExpression_strategy)
@settings(max_examples=50)
def test_timeexpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)

@given(instance=statechartexpressions::TimeConstant_strategy)
@settings(max_examples=50)
def test_statechartexpressions::timeconstant_instantiation(instance):
    assert isinstance(instance, statechartexpressions::TimeConstant)

@given(instance=statechartexpressions::TimeConstant_strategy)
def test_statechartexpressions::timeconstant_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=statechartexpressions::TimeConstant_strategy)
def test_statechartexpressions::timeconstant_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=statechartexpressions::TimeConstant_strategy)
def test_statechartexpressions::timeconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=statechartexpressions::TimeConstant_strategy)
def test_statechartexpressions::timeconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=statechartexpressions::EventRaising_strategy)
@settings(max_examples=50)
def test_statechartexpressions::eventraising_instantiation(instance):
    assert isinstance(instance, statechartexpressions::EventRaising)

@given(instance=statechartexpressions::ProcedureCall_strategy)
@settings(max_examples=50)
def test_statechartexpressions::procedurecall_instantiation(instance):
    assert isinstance(instance, statechartexpressions::ProcedureCall)

@given(instance=statechartexpressions::VariableAssignment_strategy)
@settings(max_examples=50)
def test_statechartexpressions::variableassignment_instantiation(instance):
    assert isinstance(instance, statechartexpressions::VariableAssignment)

@given(instance=statechartexpressions::VariableAssignment_strategy)
def test_statechartexpressions::variableassignment_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=statechartexpressions::VariableAssignment_strategy)
def test_statechartexpressions::variableassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=statechartexpressions::Event_strategy)
@settings(max_examples=50)
def test_statechartexpressions::event_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Event)

@given(instance=statechartexpressions::Statement_strategy)
@settings(max_examples=50)
def test_statechartexpressions::statement_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Statement)

@given(instance=statechartexpressions::VariableReference_strategy)
@settings(max_examples=50)
def test_statechartexpressions::variablereference_instantiation(instance):
    assert isinstance(instance, statechartexpressions::VariableReference)

@given(instance=statechartexpressions::TimeExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::timeexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::TimeExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=statechartexpressions::TimeEvent_strategy)
@settings(max_examples=50)
def test_statechartexpressions::timeevent_instantiation(instance):
    assert isinstance(instance, statechartexpressions::TimeEvent)

@given(instance=statechartexpressions::SignalEvent_strategy)
@settings(max_examples=50)
def test_statechartexpressions::signalevent_instantiation(instance):
    assert isinstance(instance, statechartexpressions::SignalEvent)

@given(instance=statechartexpressions::SignalEvent_strategy)
def test_statechartexpressions::signalevent_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=statechartexpressions::SignalEvent_strategy)
def test_statechartexpressions::signalevent_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=statechartexpressions::BooleanOrExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::booleanorexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::BooleanOrExpression)

@given(instance=statechartexpressions::Trigger_strategy)
@settings(max_examples=50)
def test_statechartexpressions::trigger_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Trigger)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=statechartexpressions::ActionExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::actionexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::ActionExpression)

@given(instance=statechartexpressions::GuardExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::guardexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::GuardExpression)

@given(instance=statechartexpressions::TriggerExpression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::triggerexpression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::TriggerExpression)

@given(instance=statechartexpressions::Expression_strategy)
@settings(max_examples=50)
def test_statechartexpressions::expression_instantiation(instance):
    assert isinstance(instance, statechartexpressions::Expression)
