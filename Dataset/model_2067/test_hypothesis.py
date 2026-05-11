import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IntegerExpression,
    Variable,
    activitydiagram::IntegerVariable,
    Expression,
    activitydiagram::Value,
    activitydiagram::BooleanExpression,
    activitydiagram::IntegerExpression,
    activitydiagram::Expression,
    FinalNode,
    activitydiagram::FlowFinalNode,
    activitydiagram::ActivityFinalNode,
    VariableAssignment,
    activitydiagram::IntegerVariableAssignment,
    activitydiagram::BooleanVariableAssignment,
    activitydiagram::IntegerBinaryExpression,
    Value,
    activitydiagram::IntegerValue,
    BooleanExpression,
    activitydiagram::BooleanUnaryExpression,
    activitydiagram::BooleanValue,
    activitydiagram::BooleanBinaryExpression,
    activitydiagram::IntegerComparisonExpression,
    Action,
    activitydiagram::OpaqueAction,
    ActivityNode,
    activitydiagram::Action,
    activitydiagram::BooleanVariable,
    ActivityEdge,
    activitydiagram::ControlFlow,
    ControlNode,
    activitydiagram::ForkNode,
    activitydiagram::FinalNode,
    activitydiagram::JoinNode,
    activitydiagram::DecisionNode,
    activitydiagram::MergeNode,
    activitydiagram::InitialNode,
    activitydiagram::ControlNode,
    activitydiagram::AcceptEventAction,
    activitydiagram::VariableAssignment,
    activitydiagram::Variable,
    NamedElement,
    activitydiagram::ActivityEdge,
    activitydiagram::Event,
    activitydiagram::ActivityNode,
    activitydiagram::Activity,
    activitydiagram::NamedElement,
    BooleanBinaryOperator,
    BooleanUnaryOperator,
    IntegerCalculationOperator,
    IntegerComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_integerexpression_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression)


def test_integerexpression_constructor_exists():
    assert callable(IntegerExpression.__init__)


def test_integerexpression_constructor_args():
    sig = inspect.signature(IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerVariable)


def test_activitydiagram::integervariable_constructor_exists():
    assert callable(activitydiagram::IntegerVariable.__init__)


def test_activitydiagram::integervariable_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_activitydiagram::integervariable_has_initialValue():
    assert hasattr(activitydiagram::IntegerVariable, "initialValue")
    descriptor = None
    for klass in activitydiagram::IntegerVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::value_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Value)


def test_activitydiagram::value_constructor_exists():
    assert callable(activitydiagram::Value.__init__)


def test_activitydiagram::value_constructor_args():
    sig = inspect.signature(activitydiagram::Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanExpression)


def test_activitydiagram::booleanexpression_constructor_exists():
    assert callable(activitydiagram::BooleanExpression.__init__)


def test_activitydiagram::booleanexpression_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integerexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerExpression)


def test_activitydiagram::integerexpression_constructor_exists():
    assert callable(activitydiagram::IntegerExpression.__init__)


def test_activitydiagram::integerexpression_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::expression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Expression)


def test_activitydiagram::expression_constructor_exists():
    assert callable(activitydiagram::Expression.__init__)


def test_activitydiagram::expression_constructor_args():
    sig = inspect.signature(activitydiagram::Expression.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::FlowFinalNode)


def test_activitydiagram::flowfinalnode_constructor_exists():
    assert callable(activitydiagram::FlowFinalNode.__init__)


def test_activitydiagram::flowfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityFinalNode)


def test_activitydiagram::activityfinalnode_constructor_exists():
    assert callable(activitydiagram::ActivityFinalNode.__init__)


def test_activitydiagram::activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_variableassignment_is_not_abstract():
    assert not inspect.isabstract(VariableAssignment)


def test_variableassignment_constructor_exists():
    assert callable(VariableAssignment.__init__)


def test_variableassignment_constructor_args():
    sig = inspect.signature(VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integervariableassignment_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerVariableAssignment)


def test_activitydiagram::integervariableassignment_constructor_exists():
    assert callable(activitydiagram::IntegerVariableAssignment.__init__)


def test_activitydiagram::integervariableassignment_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerVariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::booleanvariableassignment_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanVariableAssignment)


def test_activitydiagram::booleanvariableassignment_constructor_exists():
    assert callable(activitydiagram::BooleanVariableAssignment.__init__)


def test_activitydiagram::booleanvariableassignment_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanVariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integerbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerBinaryExpression)


def test_activitydiagram::integerbinaryexpression_constructor_exists():
    assert callable(activitydiagram::IntegerBinaryExpression.__init__)


def test_activitydiagram::integerbinaryexpression_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_activitydiagram::integerbinaryexpression_has_operator():
    assert hasattr(activitydiagram::IntegerBinaryExpression, "operator")
    descriptor = None
    for klass in activitydiagram::IntegerBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integervalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerValue)


def test_activitydiagram::integervalue_constructor_exists():
    assert callable(activitydiagram::IntegerValue.__init__)


def test_activitydiagram::integervalue_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_activitydiagram::integervalue_has_value():
    assert hasattr(activitydiagram::IntegerValue, "value")
    descriptor = None
    for klass in activitydiagram::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanUnaryExpression)


def test_activitydiagram::booleanunaryexpression_constructor_exists():
    assert callable(activitydiagram::BooleanUnaryExpression.__init__)


def test_activitydiagram::booleanunaryexpression_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_activitydiagram::booleanunaryexpression_has_operator():
    assert hasattr(activitydiagram::BooleanUnaryExpression, "operator")
    descriptor = None
    for klass in activitydiagram::BooleanUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanValue)


def test_activitydiagram::booleanvalue_constructor_exists():
    assert callable(activitydiagram::BooleanValue.__init__)


def test_activitydiagram::booleanvalue_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_activitydiagram::booleanvalue_has_value():
    assert hasattr(activitydiagram::BooleanValue, "value")
    descriptor = None
    for klass in activitydiagram::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanBinaryExpression)


def test_activitydiagram::booleanbinaryexpression_constructor_exists():
    assert callable(activitydiagram::BooleanBinaryExpression.__init__)


def test_activitydiagram::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_activitydiagram::booleanbinaryexpression_has_operator():
    assert hasattr(activitydiagram::BooleanBinaryExpression, "operator")
    descriptor = None
    for klass in activitydiagram::BooleanBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerComparisonExpression)


def test_activitydiagram::integercomparisonexpression_constructor_exists():
    assert callable(activitydiagram::IntegerComparisonExpression.__init__)


def test_activitydiagram::integercomparisonexpression_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_activitydiagram::integercomparisonexpression_has_operator():
    assert hasattr(activitydiagram::IntegerComparisonExpression, "operator")
    descriptor = None
    for klass in activitydiagram::IntegerComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::OpaqueAction)


def test_activitydiagram::opaqueaction_constructor_exists():
    assert callable(activitydiagram::OpaqueAction.__init__)


def test_activitydiagram::opaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::action_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Action)


def test_activitydiagram::action_constructor_exists():
    assert callable(activitydiagram::Action.__init__)


def test_activitydiagram::action_constructor_args():
    sig = inspect.signature(activitydiagram::Action.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanVariable)


def test_activitydiagram::booleanvariable_constructor_exists():
    assert callable(activitydiagram::BooleanVariable.__init__)


def test_activitydiagram::booleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_activitydiagram::booleanvariable_has_initialValue():
    assert hasattr(activitydiagram::BooleanVariable, "initialValue")
    descriptor = None
    for klass in activitydiagram::BooleanVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::controlflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlFlow)


def test_activitydiagram::controlflow_constructor_exists():
    assert callable(activitydiagram::ControlFlow.__init__)


def test_activitydiagram::controlflow_constructor_args():
    sig = inspect.signature(activitydiagram::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ForkNode)


def test_activitydiagram::forknode_constructor_exists():
    assert callable(activitydiagram::ForkNode.__init__)


def test_activitydiagram::forknode_constructor_args():
    sig = inspect.signature(activitydiagram::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::finalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::FinalNode)


def test_activitydiagram::finalnode_constructor_exists():
    assert callable(activitydiagram::FinalNode.__init__)


def test_activitydiagram::finalnode_constructor_args():
    sig = inspect.signature(activitydiagram::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::JoinNode)


def test_activitydiagram::joinnode_constructor_exists():
    assert callable(activitydiagram::JoinNode.__init__)


def test_activitydiagram::joinnode_constructor_args():
    sig = inspect.signature(activitydiagram::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::DecisionNode)


def test_activitydiagram::decisionnode_constructor_exists():
    assert callable(activitydiagram::DecisionNode.__init__)


def test_activitydiagram::decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::MergeNode)


def test_activitydiagram::mergenode_constructor_exists():
    assert callable(activitydiagram::MergeNode.__init__)


def test_activitydiagram::mergenode_constructor_args():
    sig = inspect.signature(activitydiagram::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::InitialNode)


def test_activitydiagram::initialnode_constructor_exists():
    assert callable(activitydiagram::InitialNode.__init__)


def test_activitydiagram::initialnode_constructor_args():
    sig = inspect.signature(activitydiagram::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::controlnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlNode)


def test_activitydiagram::controlnode_constructor_exists():
    assert callable(activitydiagram::ControlNode.__init__)


def test_activitydiagram::controlnode_constructor_args():
    sig = inspect.signature(activitydiagram::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::AcceptEventAction)


def test_activitydiagram::accepteventaction_constructor_exists():
    assert callable(activitydiagram::AcceptEventAction.__init__)


def test_activitydiagram::accepteventaction_constructor_args():
    sig = inspect.signature(activitydiagram::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::variableassignment_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::VariableAssignment)


def test_activitydiagram::variableassignment_constructor_exists():
    assert callable(activitydiagram::VariableAssignment.__init__)


def test_activitydiagram::variableassignment_constructor_args():
    sig = inspect.signature(activitydiagram::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::variable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Variable)


def test_activitydiagram::variable_constructor_exists():
    assert callable(activitydiagram::Variable.__init__)


def test_activitydiagram::variable_constructor_args():
    sig = inspect.signature(activitydiagram::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activitydiagram::variable_has_name():
    assert hasattr(activitydiagram::Variable, "name")
    descriptor = None
    for klass in activitydiagram::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityEdge)


def test_activitydiagram::activityedge_constructor_exists():
    assert callable(activitydiagram::ActivityEdge.__init__)


def test_activitydiagram::activityedge_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::event_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Event)


def test_activitydiagram::event_constructor_exists():
    assert callable(activitydiagram::Event.__init__)


def test_activitydiagram::event_constructor_args():
    sig = inspect.signature(activitydiagram::Event.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityNode)


def test_activitydiagram::activitynode_constructor_exists():
    assert callable(activitydiagram::ActivityNode.__init__)


def test_activitydiagram::activitynode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_activitydiagram::activitynode_has_running():
    assert hasattr(activitydiagram::ActivityNode, "running")
    descriptor = None
    for klass in activitydiagram::ActivityNode.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Activity)


def test_activitydiagram::activity_constructor_exists():
    assert callable(activitydiagram::Activity.__init__)


def test_activitydiagram::activity_constructor_args():
    sig = inspect.signature(activitydiagram::Activity.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::NamedElement)


def test_activitydiagram::namedelement_constructor_exists():
    assert callable(activitydiagram::NamedElement.__init__)


def test_activitydiagram::namedelement_constructor_args():
    sig = inspect.signature(activitydiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activitydiagram::namedelement_has_name():
    assert hasattr(activitydiagram::NamedElement, "name")
    descriptor = None
    for klass in activitydiagram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_booleanbinaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanBinaryOperator is not None

def test_booleanbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanBinaryOperator]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanBinaryOperator"

def test_booleanunaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanUnaryOperator is not None

def test_booleanunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanUnaryOperator]
    expected_literals = [
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanUnaryOperator"

def test_integercalculationoperator_exists():
    # Check that the Enumeration exists
    assert IntegerCalculationOperator is not None

def test_integercalculationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerCalculationOperator]
    expected_literals = [
        "ADD",
        "SUBRACT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerCalculationOperator"

def test_integercomparisonoperator_exists():
    # Check that the Enumeration exists
    assert IntegerComparisonOperator is not None

def test_integercomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerComparisonOperator]
    expected_literals = [
        "SMALLER_EQUALS",
        "GREATER",
        "GREATER_EQUALS",
        "EQUALS",
        "SMALLER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerComparisonOperator"


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
IntegerExpression_strategy = st.builds(
    IntegerExpression,
)
Variable_strategy = st.builds(
    Variable,
)
activitydiagram::IntegerVariable_strategy = st.builds(
    activitydiagram::IntegerVariable,
    initialValue=
        st.integers()
)
Expression_strategy = st.builds(
    Expression,
)
activitydiagram::Value_strategy = st.builds(
    activitydiagram::Value,
)
activitydiagram::BooleanExpression_strategy = st.builds(
    activitydiagram::BooleanExpression,
)
activitydiagram::IntegerExpression_strategy = st.builds(
    activitydiagram::IntegerExpression,
)
activitydiagram::Expression_strategy = st.builds(
    activitydiagram::Expression,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
activitydiagram::FlowFinalNode_strategy = st.builds(
    activitydiagram::FlowFinalNode,
)
activitydiagram::ActivityFinalNode_strategy = st.builds(
    activitydiagram::ActivityFinalNode,
)
VariableAssignment_strategy = st.builds(
    VariableAssignment,
)
activitydiagram::IntegerVariableAssignment_strategy = st.builds(
    activitydiagram::IntegerVariableAssignment,
)
activitydiagram::BooleanVariableAssignment_strategy = st.builds(
    activitydiagram::BooleanVariableAssignment,
)
activitydiagram::IntegerBinaryExpression_strategy = st.builds(
    activitydiagram::IntegerBinaryExpression,
    operator=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
activitydiagram::IntegerValue_strategy = st.builds(
    activitydiagram::IntegerValue,
    value=
        st.integers()
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
activitydiagram::BooleanUnaryExpression_strategy = st.builds(
    activitydiagram::BooleanUnaryExpression,
    operator=
        safe_text
)
activitydiagram::BooleanValue_strategy = st.builds(
    activitydiagram::BooleanValue,
    value=
        st.booleans()
)
activitydiagram::BooleanBinaryExpression_strategy = st.builds(
    activitydiagram::BooleanBinaryExpression,
    operator=
        safe_text
)
activitydiagram::IntegerComparisonExpression_strategy = st.builds(
    activitydiagram::IntegerComparisonExpression,
    operator=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
activitydiagram::OpaqueAction_strategy = st.builds(
    activitydiagram::OpaqueAction,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
activitydiagram::Action_strategy = st.builds(
    activitydiagram::Action,
)
activitydiagram::BooleanVariable_strategy = st.builds(
    activitydiagram::BooleanVariable,
    initialValue=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
activitydiagram::ControlFlow_strategy = st.builds(
    activitydiagram::ControlFlow,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
activitydiagram::ForkNode_strategy = st.builds(
    activitydiagram::ForkNode,
)
activitydiagram::FinalNode_strategy = st.builds(
    activitydiagram::FinalNode,
)
activitydiagram::JoinNode_strategy = st.builds(
    activitydiagram::JoinNode,
)
activitydiagram::DecisionNode_strategy = st.builds(
    activitydiagram::DecisionNode,
)
activitydiagram::MergeNode_strategy = st.builds(
    activitydiagram::MergeNode,
)
activitydiagram::InitialNode_strategy = st.builds(
    activitydiagram::InitialNode,
)
activitydiagram::ControlNode_strategy = st.builds(
    activitydiagram::ControlNode,
)
activitydiagram::AcceptEventAction_strategy = st.builds(
    activitydiagram::AcceptEventAction,
)
activitydiagram::VariableAssignment_strategy = st.builds(
    activitydiagram::VariableAssignment,
)
activitydiagram::Variable_strategy = st.builds(
    activitydiagram::Variable,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
activitydiagram::ActivityEdge_strategy = st.builds(
    activitydiagram::ActivityEdge,
)
activitydiagram::Event_strategy = st.builds(
    activitydiagram::Event,
)
activitydiagram::ActivityNode_strategy = st.builds(
    activitydiagram::ActivityNode,
    running=
        st.booleans()
)
activitydiagram::Activity_strategy = st.builds(
    activitydiagram::Activity,
)
activitydiagram::NamedElement_strategy = st.builds(
    activitydiagram::NamedElement,
    name=
        safe_text
)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=activitydiagram::IntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::integervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerVariable)

@given(instance=activitydiagram::IntegerVariable_strategy)
def test_activitydiagram::integervariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, int)


@given(instance=activitydiagram::IntegerVariable_strategy)
def test_activitydiagram::integervariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=activitydiagram::Value_strategy)
@settings(max_examples=50)
def test_activitydiagram::value_instantiation(instance):
    assert isinstance(instance, activitydiagram::Value)

@given(instance=activitydiagram::BooleanExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanExpression)

@given(instance=activitydiagram::IntegerExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::integerexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerExpression)

@given(instance=activitydiagram::Expression_strategy)
@settings(max_examples=50)
def test_activitydiagram::expression_instantiation(instance):
    assert isinstance(instance, activitydiagram::Expression)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=activitydiagram::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::flowfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::FlowFinalNode)

@given(instance=activitydiagram::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityFinalNode)

@given(instance=VariableAssignment_strategy)
@settings(max_examples=50)
def test_variableassignment_instantiation(instance):
    assert isinstance(instance, VariableAssignment)

@given(instance=activitydiagram::IntegerVariableAssignment_strategy)
@settings(max_examples=50)
def test_activitydiagram::integervariableassignment_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerVariableAssignment)

@given(instance=activitydiagram::BooleanVariableAssignment_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanvariableassignment_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanVariableAssignment)

@given(instance=activitydiagram::IntegerBinaryExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::integerbinaryexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerBinaryExpression)

@given(instance=activitydiagram::IntegerBinaryExpression_strategy)
def test_activitydiagram::integerbinaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=activitydiagram::IntegerBinaryExpression_strategy)
def test_activitydiagram::integerbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=activitydiagram::IntegerValue_strategy)
@settings(max_examples=50)
def test_activitydiagram::integervalue_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerValue)

@given(instance=activitydiagram::IntegerValue_strategy)
def test_activitydiagram::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=activitydiagram::IntegerValue_strategy)
def test_activitydiagram::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=activitydiagram::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanUnaryExpression)

@given(instance=activitydiagram::BooleanUnaryExpression_strategy)
def test_activitydiagram::booleanunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=activitydiagram::BooleanUnaryExpression_strategy)
def test_activitydiagram::booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=activitydiagram::BooleanValue_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanvalue_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanValue)

@given(instance=activitydiagram::BooleanValue_strategy)
def test_activitydiagram::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=activitydiagram::BooleanValue_strategy)
def test_activitydiagram::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=activitydiagram::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanBinaryExpression)

@given(instance=activitydiagram::BooleanBinaryExpression_strategy)
def test_activitydiagram::booleanbinaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=activitydiagram::BooleanBinaryExpression_strategy)
def test_activitydiagram::booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=activitydiagram::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_activitydiagram::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerComparisonExpression)

@given(instance=activitydiagram::IntegerComparisonExpression_strategy)
def test_activitydiagram::integercomparisonexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=activitydiagram::IntegerComparisonExpression_strategy)
def test_activitydiagram::integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=activitydiagram::OpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::opaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::OpaqueAction)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=activitydiagram::Action_strategy)
@settings(max_examples=50)
def test_activitydiagram::action_instantiation(instance):
    assert isinstance(instance, activitydiagram::Action)

@given(instance=activitydiagram::BooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanVariable)

@given(instance=activitydiagram::BooleanVariable_strategy)
def test_activitydiagram::booleanvariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, bool)


@given(instance=activitydiagram::BooleanVariable_strategy)
def test_activitydiagram::booleanvariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=activitydiagram::ControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::controlflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlFlow)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=activitydiagram::ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ForkNode)

@given(instance=activitydiagram::FinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::finalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::FinalNode)

@given(instance=activitydiagram::JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::JoinNode)

@given(instance=activitydiagram::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::DecisionNode)

@given(instance=activitydiagram::MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::MergeNode)

@given(instance=activitydiagram::InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::InitialNode)

@given(instance=activitydiagram::ControlNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::controlnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlNode)

@given(instance=activitydiagram::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::accepteventaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::AcceptEventAction)

@given(instance=activitydiagram::VariableAssignment_strategy)
@settings(max_examples=50)
def test_activitydiagram::variableassignment_instantiation(instance):
    assert isinstance(instance, activitydiagram::VariableAssignment)

@given(instance=activitydiagram::Variable_strategy)
@settings(max_examples=50)
def test_activitydiagram::variable_instantiation(instance):
    assert isinstance(instance, activitydiagram::Variable)

@given(instance=activitydiagram::Variable_strategy)
def test_activitydiagram::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=activitydiagram::Variable_strategy)
def test_activitydiagram::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=activitydiagram::ActivityEdge_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityedge_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityEdge)

@given(instance=activitydiagram::Event_strategy)
@settings(max_examples=50)
def test_activitydiagram::event_instantiation(instance):
    assert isinstance(instance, activitydiagram::Event)

@given(instance=activitydiagram::ActivityNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activitynode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityNode)

@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_running_type(instance):
    assert isinstance(instance.running, bool)


@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=activitydiagram::Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram::activity_instantiation(instance):
    assert isinstance(instance, activitydiagram::Activity)

@given(instance=activitydiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_activitydiagram::namedelement_instantiation(instance):
    assert isinstance(instance, activitydiagram::NamedElement)

@given(instance=activitydiagram::NamedElement_strategy)
def test_activitydiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=activitydiagram::NamedElement_strategy)
def test_activitydiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
