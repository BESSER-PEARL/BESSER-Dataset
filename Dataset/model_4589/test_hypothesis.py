import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IntegerExpression,
    adwithoutruntime::IntegerCalculationExpression,
    BooleanExpression,
    adwithoutruntime::BooleanBinaryExpression,
    adwithoutruntime::BooleanUnaryExpression,
    adwithoutruntime::IntegerComparisonExpression,
    adwithoutruntime::Expression,
    Action,
    adwithoutruntime::OpaqueAction,
    Expression,
    adwithoutruntime::BooleanExpression,
    adwithoutruntime::IntegerExpression,
    Value,
    adwithoutruntime::IntegerValue,
    adwithoutruntime::BooleanValue,
    Variable,
    adwithoutruntime::IntegerVariable,
    adwithoutruntime::Value,
    FinalNode,
    adwithoutruntime::ActivityFinalNode,
    ControlNode,
    adwithoutruntime::JoinNode,
    adwithoutruntime::MergeNode,
    adwithoutruntime::FinalNode,
    adwithoutruntime::DecisionNode,
    adwithoutruntime::ForkNode,
    adwithoutruntime::InitialNode,
    adwithoutruntime::NamedElement,
    NamedElement,
    adwithoutruntime::Activity,
    ExecutableNode,
    adwithoutruntime::Action,
    ActivityNode,
    adwithoutruntime::ExecutableNode,
    adwithoutruntime::ControlNode,
    adwithoutruntime::BooleanVariable,
    ActivityEdge,
    adwithoutruntime::ControlFlow,
    adwithoutruntime::Variable,
    adwithoutruntime::ActivityEdge,
    adwithoutruntime::ActivityNode,
    BooleanUnaryOperator,
    IntegerComparisonOperator,
    BooleanBinaryOperator,
    IntegerCalculationOperator,
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



def test_adwithoutruntime::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::IntegerCalculationExpression)


def test_adwithoutruntime::integercalculationexpression_constructor_exists():
    assert callable(adwithoutruntime::IntegerCalculationExpression.__init__)


def test_adwithoutruntime::integercalculationexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime::integercalculationexpression_has_operator():
    assert hasattr(adwithoutruntime::IntegerCalculationExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime::IntegerCalculationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::BooleanBinaryExpression)


def test_adwithoutruntime::booleanbinaryexpression_constructor_exists():
    assert callable(adwithoutruntime::BooleanBinaryExpression.__init__)


def test_adwithoutruntime::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime::booleanbinaryexpression_has_operator():
    assert hasattr(adwithoutruntime::BooleanBinaryExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime::BooleanBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::BooleanUnaryExpression)


def test_adwithoutruntime::booleanunaryexpression_constructor_exists():
    assert callable(adwithoutruntime::BooleanUnaryExpression.__init__)


def test_adwithoutruntime::booleanunaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime::booleanunaryexpression_has_operator():
    assert hasattr(adwithoutruntime::BooleanUnaryExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime::BooleanUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::IntegerComparisonExpression)


def test_adwithoutruntime::integercomparisonexpression_constructor_exists():
    assert callable(adwithoutruntime::IntegerComparisonExpression.__init__)


def test_adwithoutruntime::integercomparisonexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime::integercomparisonexpression_has_operator():
    assert hasattr(adwithoutruntime::IntegerComparisonExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime::IntegerComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime::expression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::Expression)


def test_adwithoutruntime::expression_constructor_exists():
    assert callable(adwithoutruntime::Expression.__init__)


def test_adwithoutruntime::expression_constructor_args():
    sig = inspect.signature(adwithoutruntime::Expression.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::OpaqueAction)


def test_adwithoutruntime::opaqueaction_constructor_exists():
    assert callable(adwithoutruntime::OpaqueAction.__init__)


def test_adwithoutruntime::opaqueaction_constructor_args():
    sig = inspect.signature(adwithoutruntime::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::BooleanExpression)


def test_adwithoutruntime::booleanexpression_constructor_exists():
    assert callable(adwithoutruntime::BooleanExpression.__init__)


def test_adwithoutruntime::booleanexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::integerexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::IntegerExpression)


def test_adwithoutruntime::integerexpression_constructor_exists():
    assert callable(adwithoutruntime::IntegerExpression.__init__)


def test_adwithoutruntime::integerexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::integervalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::IntegerValue)


def test_adwithoutruntime::integervalue_constructor_exists():
    assert callable(adwithoutruntime::IntegerValue.__init__)


def test_adwithoutruntime::integervalue_constructor_args():
    sig = inspect.signature(adwithoutruntime::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adwithoutruntime::integervalue_has_value():
    assert hasattr(adwithoutruntime::IntegerValue, "value")
    descriptor = None
    for klass in adwithoutruntime::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::BooleanValue)


def test_adwithoutruntime::booleanvalue_constructor_exists():
    assert callable(adwithoutruntime::BooleanValue.__init__)


def test_adwithoutruntime::booleanvalue_constructor_args():
    sig = inspect.signature(adwithoutruntime::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adwithoutruntime::booleanvalue_has_value():
    assert hasattr(adwithoutruntime::BooleanValue, "value")
    descriptor = None
    for klass in adwithoutruntime::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::integervariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::IntegerVariable)


def test_adwithoutruntime::integervariable_constructor_exists():
    assert callable(adwithoutruntime::IntegerVariable.__init__)


def test_adwithoutruntime::integervariable_constructor_args():
    sig = inspect.signature(adwithoutruntime::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::value_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::Value)


def test_adwithoutruntime::value_constructor_exists():
    assert callable(adwithoutruntime::Value.__init__)


def test_adwithoutruntime::value_constructor_args():
    sig = inspect.signature(adwithoutruntime::Value.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ActivityFinalNode)


def test_adwithoutruntime::activityfinalnode_constructor_exists():
    assert callable(adwithoutruntime::ActivityFinalNode.__init__)


def test_adwithoutruntime::activityfinalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::joinnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::JoinNode)


def test_adwithoutruntime::joinnode_constructor_exists():
    assert callable(adwithoutruntime::JoinNode.__init__)


def test_adwithoutruntime::joinnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::mergenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::MergeNode)


def test_adwithoutruntime::mergenode_constructor_exists():
    assert callable(adwithoutruntime::MergeNode.__init__)


def test_adwithoutruntime::mergenode_constructor_args():
    sig = inspect.signature(adwithoutruntime::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::finalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::FinalNode)


def test_adwithoutruntime::finalnode_constructor_exists():
    assert callable(adwithoutruntime::FinalNode.__init__)


def test_adwithoutruntime::finalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::decisionnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::DecisionNode)


def test_adwithoutruntime::decisionnode_constructor_exists():
    assert callable(adwithoutruntime::DecisionNode.__init__)


def test_adwithoutruntime::decisionnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::forknode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ForkNode)


def test_adwithoutruntime::forknode_constructor_exists():
    assert callable(adwithoutruntime::ForkNode.__init__)


def test_adwithoutruntime::forknode_constructor_args():
    sig = inspect.signature(adwithoutruntime::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::initialnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::InitialNode)


def test_adwithoutruntime::initialnode_constructor_exists():
    assert callable(adwithoutruntime::InitialNode.__init__)


def test_adwithoutruntime::initialnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::namedelement_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::NamedElement)


def test_adwithoutruntime::namedelement_constructor_exists():
    assert callable(adwithoutruntime::NamedElement.__init__)


def test_adwithoutruntime::namedelement_constructor_args():
    sig = inspect.signature(adwithoutruntime::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adwithoutruntime::namedelement_has_name():
    assert hasattr(adwithoutruntime::NamedElement, "name")
    descriptor = None
    for klass in adwithoutruntime::NamedElement.__mro__:
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



def test_adwithoutruntime::activity_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::Activity)


def test_adwithoutruntime::activity_constructor_exists():
    assert callable(adwithoutruntime::Activity.__init__)


def test_adwithoutruntime::activity_constructor_args():
    sig = inspect.signature(adwithoutruntime::Activity.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::action_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::Action)


def test_adwithoutruntime::action_constructor_exists():
    assert callable(adwithoutruntime::Action.__init__)


def test_adwithoutruntime::action_constructor_args():
    sig = inspect.signature(adwithoutruntime::Action.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::executablenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ExecutableNode)


def test_adwithoutruntime::executablenode_constructor_exists():
    assert callable(adwithoutruntime::ExecutableNode.__init__)


def test_adwithoutruntime::executablenode_constructor_args():
    sig = inspect.signature(adwithoutruntime::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::controlnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ControlNode)


def test_adwithoutruntime::controlnode_constructor_exists():
    assert callable(adwithoutruntime::ControlNode.__init__)


def test_adwithoutruntime::controlnode_constructor_args():
    sig = inspect.signature(adwithoutruntime::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::BooleanVariable)


def test_adwithoutruntime::booleanvariable_constructor_exists():
    assert callable(adwithoutruntime::BooleanVariable.__init__)


def test_adwithoutruntime::booleanvariable_constructor_args():
    sig = inspect.signature(adwithoutruntime::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::controlflow_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ControlFlow)


def test_adwithoutruntime::controlflow_constructor_exists():
    assert callable(adwithoutruntime::ControlFlow.__init__)


def test_adwithoutruntime::controlflow_constructor_args():
    sig = inspect.signature(adwithoutruntime::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::variable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::Variable)


def test_adwithoutruntime::variable_constructor_exists():
    assert callable(adwithoutruntime::Variable.__init__)


def test_adwithoutruntime::variable_constructor_args():
    sig = inspect.signature(adwithoutruntime::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adwithoutruntime::variable_has_name():
    assert hasattr(adwithoutruntime::Variable, "name")
    descriptor = None
    for klass in adwithoutruntime::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime::activityedge_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ActivityEdge)


def test_adwithoutruntime::activityedge_constructor_exists():
    assert callable(adwithoutruntime::ActivityEdge.__init__)


def test_adwithoutruntime::activityedge_constructor_args():
    sig = inspect.signature(adwithoutruntime::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime::activitynode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime::ActivityNode)


def test_adwithoutruntime::activitynode_constructor_exists():
    assert callable(adwithoutruntime::ActivityNode.__init__)


def test_adwithoutruntime::activitynode_constructor_args():
    sig = inspect.signature(adwithoutruntime::ActivityNode.__init__)
    params = list(sig.parameters.keys())

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

def test_integercomparisonoperator_exists():
    # Check that the Enumeration exists
    assert IntegerComparisonOperator is not None

def test_integercomparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegerComparisonOperator]
    expected_literals = [
        "SMALLER",
        "SMALLER_EQUALS",
        "EQUALS",
        "GREATER",
        "GREATER_EQUALS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegerComparisonOperator"

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
adwithoutruntime::IntegerCalculationExpression_strategy = st.builds(
    adwithoutruntime::IntegerCalculationExpression,
    operator=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
adwithoutruntime::BooleanBinaryExpression_strategy = st.builds(
    adwithoutruntime::BooleanBinaryExpression,
    operator=
        safe_text
)
adwithoutruntime::BooleanUnaryExpression_strategy = st.builds(
    adwithoutruntime::BooleanUnaryExpression,
    operator=
        safe_text
)
adwithoutruntime::IntegerComparisonExpression_strategy = st.builds(
    adwithoutruntime::IntegerComparisonExpression,
    operator=
        safe_text
)
adwithoutruntime::Expression_strategy = st.builds(
    adwithoutruntime::Expression,
)
Action_strategy = st.builds(
    Action,
)
adwithoutruntime::OpaqueAction_strategy = st.builds(
    adwithoutruntime::OpaqueAction,
)
Expression_strategy = st.builds(
    Expression,
)
adwithoutruntime::BooleanExpression_strategy = st.builds(
    adwithoutruntime::BooleanExpression,
)
adwithoutruntime::IntegerExpression_strategy = st.builds(
    adwithoutruntime::IntegerExpression,
)
Value_strategy = st.builds(
    Value,
)
adwithoutruntime::IntegerValue_strategy = st.builds(
    adwithoutruntime::IntegerValue,
    value=
        st.integers()
)
adwithoutruntime::BooleanValue_strategy = st.builds(
    adwithoutruntime::BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
adwithoutruntime::IntegerVariable_strategy = st.builds(
    adwithoutruntime::IntegerVariable,
)
adwithoutruntime::Value_strategy = st.builds(
    adwithoutruntime::Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
adwithoutruntime::ActivityFinalNode_strategy = st.builds(
    adwithoutruntime::ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
adwithoutruntime::JoinNode_strategy = st.builds(
    adwithoutruntime::JoinNode,
)
adwithoutruntime::MergeNode_strategy = st.builds(
    adwithoutruntime::MergeNode,
)
adwithoutruntime::FinalNode_strategy = st.builds(
    adwithoutruntime::FinalNode,
)
adwithoutruntime::DecisionNode_strategy = st.builds(
    adwithoutruntime::DecisionNode,
)
adwithoutruntime::ForkNode_strategy = st.builds(
    adwithoutruntime::ForkNode,
)
adwithoutruntime::InitialNode_strategy = st.builds(
    adwithoutruntime::InitialNode,
)
adwithoutruntime::NamedElement_strategy = st.builds(
    adwithoutruntime::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adwithoutruntime::Activity_strategy = st.builds(
    adwithoutruntime::Activity,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
adwithoutruntime::Action_strategy = st.builds(
    adwithoutruntime::Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
adwithoutruntime::ExecutableNode_strategy = st.builds(
    adwithoutruntime::ExecutableNode,
)
adwithoutruntime::ControlNode_strategy = st.builds(
    adwithoutruntime::ControlNode,
)
adwithoutruntime::BooleanVariable_strategy = st.builds(
    adwithoutruntime::BooleanVariable,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
adwithoutruntime::ControlFlow_strategy = st.builds(
    adwithoutruntime::ControlFlow,
)
adwithoutruntime::Variable_strategy = st.builds(
    adwithoutruntime::Variable,
    name=
        safe_text
)
adwithoutruntime::ActivityEdge_strategy = st.builds(
    adwithoutruntime::ActivityEdge,
)
adwithoutruntime::ActivityNode_strategy = st.builds(
    adwithoutruntime::ActivityNode,
)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=adwithoutruntime::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::IntegerCalculationExpression)

@given(instance=adwithoutruntime::IntegerCalculationExpression_strategy)
def test_adwithoutruntime::integercalculationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=adwithoutruntime::IntegerCalculationExpression_strategy)
def test_adwithoutruntime::integercalculationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=adwithoutruntime::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::BooleanBinaryExpression)

@given(instance=adwithoutruntime::BooleanBinaryExpression_strategy)
def test_adwithoutruntime::booleanbinaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=adwithoutruntime::BooleanBinaryExpression_strategy)
def test_adwithoutruntime::booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::BooleanUnaryExpression)

@given(instance=adwithoutruntime::BooleanUnaryExpression_strategy)
def test_adwithoutruntime::booleanunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=adwithoutruntime::BooleanUnaryExpression_strategy)
def test_adwithoutruntime::booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::IntegerComparisonExpression)

@given(instance=adwithoutruntime::IntegerComparisonExpression_strategy)
def test_adwithoutruntime::integercomparisonexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=adwithoutruntime::IntegerComparisonExpression_strategy)
def test_adwithoutruntime::integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime::Expression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::expression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::Expression)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=adwithoutruntime::OpaqueAction_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::opaqueaction_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::OpaqueAction)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=adwithoutruntime::BooleanExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::booleanexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::BooleanExpression)

@given(instance=adwithoutruntime::IntegerExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::integerexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::IntegerExpression)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=adwithoutruntime::IntegerValue_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::integervalue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::IntegerValue)

@given(instance=adwithoutruntime::IntegerValue_strategy)
def test_adwithoutruntime::integervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=adwithoutruntime::IntegerValue_strategy)
def test_adwithoutruntime::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adwithoutruntime::BooleanValue_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::booleanvalue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::BooleanValue)

@given(instance=adwithoutruntime::BooleanValue_strategy)
def test_adwithoutruntime::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=adwithoutruntime::BooleanValue_strategy)
def test_adwithoutruntime::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=adwithoutruntime::IntegerVariable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::integervariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::IntegerVariable)

@given(instance=adwithoutruntime::Value_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::value_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::Value)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=adwithoutruntime::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::activityfinalnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ActivityFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=adwithoutruntime::JoinNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::joinnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::JoinNode)

@given(instance=adwithoutruntime::MergeNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::mergenode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::MergeNode)

@given(instance=adwithoutruntime::FinalNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::finalnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::FinalNode)

@given(instance=adwithoutruntime::DecisionNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::decisionnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::DecisionNode)

@given(instance=adwithoutruntime::ForkNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::forknode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ForkNode)

@given(instance=adwithoutruntime::InitialNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::initialnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::InitialNode)

@given(instance=adwithoutruntime::NamedElement_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::namedelement_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::NamedElement)

@given(instance=adwithoutruntime::NamedElement_strategy)
def test_adwithoutruntime::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adwithoutruntime::NamedElement_strategy)
def test_adwithoutruntime::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adwithoutruntime::Activity_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::activity_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::Activity)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=adwithoutruntime::Action_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::action_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::Action)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=adwithoutruntime::ExecutableNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::executablenode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ExecutableNode)

@given(instance=adwithoutruntime::ControlNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::controlnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ControlNode)

@given(instance=adwithoutruntime::BooleanVariable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::booleanvariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::BooleanVariable)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=adwithoutruntime::ControlFlow_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::controlflow_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ControlFlow)

@given(instance=adwithoutruntime::Variable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::variable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::Variable)

@given(instance=adwithoutruntime::Variable_strategy)
def test_adwithoutruntime::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adwithoutruntime::Variable_strategy)
def test_adwithoutruntime::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adwithoutruntime::ActivityEdge_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::activityedge_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ActivityEdge)

@given(instance=adwithoutruntime::ActivityNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime::activitynode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime::ActivityNode)
