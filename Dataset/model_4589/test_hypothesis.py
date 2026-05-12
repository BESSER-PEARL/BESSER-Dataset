import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IntegerExpression,
    adwithoutruntime_IntegerCalculationExpression,
    BooleanExpression,
    adwithoutruntime_BooleanBinaryExpression,
    adwithoutruntime_BooleanUnaryExpression,
    adwithoutruntime_IntegerComparisonExpression,
    adwithoutruntime_Expression,
    Action,
    adwithoutruntime_OpaqueAction,
    Expression,
    adwithoutruntime_BooleanExpression,
    adwithoutruntime_IntegerExpression,
    Value,
    adwithoutruntime_IntegerValue,
    adwithoutruntime_BooleanValue,
    Variable,
    adwithoutruntime_IntegerVariable,
    adwithoutruntime_Value,
    FinalNode,
    adwithoutruntime_ActivityFinalNode,
    ControlNode,
    adwithoutruntime_JoinNode,
    adwithoutruntime_DecisionNode,
    adwithoutruntime_ForkNode,
    adwithoutruntime_FinalNode,
    adwithoutruntime_MergeNode,
    adwithoutruntime_InitialNode,
    adwithoutruntime_NamedElement,
    NamedElement,
    adwithoutruntime_Activity,
    ExecutableNode,
    adwithoutruntime_Action,
    ActivityNode,
    adwithoutruntime_ExecutableNode,
    adwithoutruntime_ControlNode,
    adwithoutruntime_BooleanVariable,
    ActivityEdge,
    adwithoutruntime_ControlFlow,
    adwithoutruntime_Variable,
    adwithoutruntime_ActivityEdge,
    adwithoutruntime_ActivityNode,
    BooleanBinaryOperator,
    IntegerCalculationOperator,
    BooleanUnaryOperator,
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



def test_adwithoutruntime_integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerCalculationExpression)


def test_adwithoutruntime_integercalculationexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerCalculationExpression.__init__)


def test_adwithoutruntime_integercalculationexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime_integercalculationexpression_has_operator():
    assert hasattr(adwithoutruntime_IntegerCalculationExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime_IntegerCalculationExpression.__mro__:
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



def test_adwithoutruntime_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanBinaryExpression)


def test_adwithoutruntime_booleanbinaryexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanBinaryExpression.__init__)


def test_adwithoutruntime_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime_booleanbinaryexpression_has_operator():
    assert hasattr(adwithoutruntime_BooleanBinaryExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime_BooleanBinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime_booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanUnaryExpression)


def test_adwithoutruntime_booleanunaryexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanUnaryExpression.__init__)


def test_adwithoutruntime_booleanunaryexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime_booleanunaryexpression_has_operator():
    assert hasattr(adwithoutruntime_BooleanUnaryExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime_BooleanUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime_integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerComparisonExpression)


def test_adwithoutruntime_integercomparisonexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerComparisonExpression.__init__)


def test_adwithoutruntime_integercomparisonexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_adwithoutruntime_integercomparisonexpression_has_operator():
    assert hasattr(adwithoutruntime_IntegerComparisonExpression, "operator")
    descriptor = None
    for klass in adwithoutruntime_IntegerComparisonExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime_expression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Expression)


def test_adwithoutruntime_expression_constructor_exists():
    assert callable(adwithoutruntime_Expression.__init__)


def test_adwithoutruntime_expression_constructor_args():
    sig = inspect.signature(adwithoutruntime_Expression.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_OpaqueAction)


def test_adwithoutruntime_opaqueaction_constructor_exists():
    assert callable(adwithoutruntime_OpaqueAction.__init__)


def test_adwithoutruntime_opaqueaction_constructor_args():
    sig = inspect.signature(adwithoutruntime_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanExpression)


def test_adwithoutruntime_booleanexpression_constructor_exists():
    assert callable(adwithoutruntime_BooleanExpression.__init__)


def test_adwithoutruntime_booleanexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_integerexpression_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerExpression)


def test_adwithoutruntime_integerexpression_constructor_exists():
    assert callable(adwithoutruntime_IntegerExpression.__init__)


def test_adwithoutruntime_integerexpression_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_integervalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerValue)


def test_adwithoutruntime_integervalue_constructor_exists():
    assert callable(adwithoutruntime_IntegerValue.__init__)


def test_adwithoutruntime_integervalue_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adwithoutruntime_integervalue_has_value():
    assert hasattr(adwithoutruntime_IntegerValue, "value")
    descriptor = None
    for klass in adwithoutruntime_IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanValue)


def test_adwithoutruntime_booleanvalue_constructor_exists():
    assert callable(adwithoutruntime_BooleanValue.__init__)


def test_adwithoutruntime_booleanvalue_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adwithoutruntime_booleanvalue_has_value():
    assert hasattr(adwithoutruntime_BooleanValue, "value")
    descriptor = None
    for klass in adwithoutruntime_BooleanValue.__mro__:
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



def test_adwithoutruntime_integervariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_IntegerVariable)


def test_adwithoutruntime_integervariable_constructor_exists():
    assert callable(adwithoutruntime_IntegerVariable.__init__)


def test_adwithoutruntime_integervariable_constructor_args():
    sig = inspect.signature(adwithoutruntime_IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_value_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Value)


def test_adwithoutruntime_value_constructor_exists():
    assert callable(adwithoutruntime_Value.__init__)


def test_adwithoutruntime_value_constructor_args():
    sig = inspect.signature(adwithoutruntime_Value.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityFinalNode)


def test_adwithoutruntime_activityfinalnode_constructor_exists():
    assert callable(adwithoutruntime_ActivityFinalNode.__init__)


def test_adwithoutruntime_activityfinalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_joinnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_JoinNode)


def test_adwithoutruntime_joinnode_constructor_exists():
    assert callable(adwithoutruntime_JoinNode.__init__)


def test_adwithoutruntime_joinnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_decisionnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_DecisionNode)


def test_adwithoutruntime_decisionnode_constructor_exists():
    assert callable(adwithoutruntime_DecisionNode.__init__)


def test_adwithoutruntime_decisionnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_forknode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ForkNode)


def test_adwithoutruntime_forknode_constructor_exists():
    assert callable(adwithoutruntime_ForkNode.__init__)


def test_adwithoutruntime_forknode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_finalnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_FinalNode)


def test_adwithoutruntime_finalnode_constructor_exists():
    assert callable(adwithoutruntime_FinalNode.__init__)


def test_adwithoutruntime_finalnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_mergenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_MergeNode)


def test_adwithoutruntime_mergenode_constructor_exists():
    assert callable(adwithoutruntime_MergeNode.__init__)


def test_adwithoutruntime_mergenode_constructor_args():
    sig = inspect.signature(adwithoutruntime_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_initialnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_InitialNode)


def test_adwithoutruntime_initialnode_constructor_exists():
    assert callable(adwithoutruntime_InitialNode.__init__)


def test_adwithoutruntime_initialnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_namedelement_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_NamedElement)


def test_adwithoutruntime_namedelement_constructor_exists():
    assert callable(adwithoutruntime_NamedElement.__init__)


def test_adwithoutruntime_namedelement_constructor_args():
    sig = inspect.signature(adwithoutruntime_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adwithoutruntime_namedelement_has_name():
    assert hasattr(adwithoutruntime_NamedElement, "name")
    descriptor = None
    for klass in adwithoutruntime_NamedElement.__mro__:
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



def test_adwithoutruntime_activity_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Activity)


def test_adwithoutruntime_activity_constructor_exists():
    assert callable(adwithoutruntime_Activity.__init__)


def test_adwithoutruntime_activity_constructor_args():
    sig = inspect.signature(adwithoutruntime_Activity.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_action_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Action)


def test_adwithoutruntime_action_constructor_exists():
    assert callable(adwithoutruntime_Action.__init__)


def test_adwithoutruntime_action_constructor_args():
    sig = inspect.signature(adwithoutruntime_Action.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_executablenode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ExecutableNode)


def test_adwithoutruntime_executablenode_constructor_exists():
    assert callable(adwithoutruntime_ExecutableNode.__init__)


def test_adwithoutruntime_executablenode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_controlnode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ControlNode)


def test_adwithoutruntime_controlnode_constructor_exists():
    assert callable(adwithoutruntime_ControlNode.__init__)


def test_adwithoutruntime_controlnode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_BooleanVariable)


def test_adwithoutruntime_booleanvariable_constructor_exists():
    assert callable(adwithoutruntime_BooleanVariable.__init__)


def test_adwithoutruntime_booleanvariable_constructor_args():
    sig = inspect.signature(adwithoutruntime_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_controlflow_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ControlFlow)


def test_adwithoutruntime_controlflow_constructor_exists():
    assert callable(adwithoutruntime_ControlFlow.__init__)


def test_adwithoutruntime_controlflow_constructor_args():
    sig = inspect.signature(adwithoutruntime_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_variable_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_Variable)


def test_adwithoutruntime_variable_constructor_exists():
    assert callable(adwithoutruntime_Variable.__init__)


def test_adwithoutruntime_variable_constructor_args():
    sig = inspect.signature(adwithoutruntime_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adwithoutruntime_variable_has_name():
    assert hasattr(adwithoutruntime_Variable, "name")
    descriptor = None
    for klass in adwithoutruntime_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adwithoutruntime_activityedge_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityEdge)


def test_adwithoutruntime_activityedge_constructor_exists():
    assert callable(adwithoutruntime_ActivityEdge.__init__)


def test_adwithoutruntime_activityedge_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_adwithoutruntime_activitynode_is_not_abstract():
    assert not inspect.isabstract(adwithoutruntime_ActivityNode)


def test_adwithoutruntime_activitynode_constructor_exists():
    assert callable(adwithoutruntime_ActivityNode.__init__)


def test_adwithoutruntime_activitynode_constructor_args():
    sig = inspect.signature(adwithoutruntime_ActivityNode.__init__)
    params = list(sig.parameters.keys())

def test_booleanbinaryoperator_exists():
    # Check that the Enumeration exists
    assert BooleanBinaryOperator is not None

def test_booleanbinaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanBinaryOperator]
    expected_literals = [
        "OR",
        "AND",
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
        "EQUALS",
        "SMALLER",
        "SMALLER_EQUALS",
        "GREATER",
        "GREATER_EQUALS",
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
adwithoutruntime_IntegerCalculationExpression_strategy = st.builds(
    adwithoutruntime_IntegerCalculationExpression,
    operator=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
adwithoutruntime_BooleanBinaryExpression_strategy = st.builds(
    adwithoutruntime_BooleanBinaryExpression,
    operator=
        safe_text
)
adwithoutruntime_BooleanUnaryExpression_strategy = st.builds(
    adwithoutruntime_BooleanUnaryExpression,
    operator=
        safe_text
)
adwithoutruntime_IntegerComparisonExpression_strategy = st.builds(
    adwithoutruntime_IntegerComparisonExpression,
    operator=
        safe_text
)
adwithoutruntime_Expression_strategy = st.builds(
    adwithoutruntime_Expression,
)
Action_strategy = st.builds(
    Action,
)
adwithoutruntime_OpaqueAction_strategy = st.builds(
    adwithoutruntime_OpaqueAction,
)
Expression_strategy = st.builds(
    Expression,
)
adwithoutruntime_BooleanExpression_strategy = st.builds(
    adwithoutruntime_BooleanExpression,
)
adwithoutruntime_IntegerExpression_strategy = st.builds(
    adwithoutruntime_IntegerExpression,
)
Value_strategy = st.builds(
    Value,
)
adwithoutruntime_IntegerValue_strategy = st.builds(
    adwithoutruntime_IntegerValue,
    value=
        st.integers()
)
adwithoutruntime_BooleanValue_strategy = st.builds(
    adwithoutruntime_BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
adwithoutruntime_IntegerVariable_strategy = st.builds(
    adwithoutruntime_IntegerVariable,
)
adwithoutruntime_Value_strategy = st.builds(
    adwithoutruntime_Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
adwithoutruntime_ActivityFinalNode_strategy = st.builds(
    adwithoutruntime_ActivityFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
adwithoutruntime_JoinNode_strategy = st.builds(
    adwithoutruntime_JoinNode,
)
adwithoutruntime_DecisionNode_strategy = st.builds(
    adwithoutruntime_DecisionNode,
)
adwithoutruntime_ForkNode_strategy = st.builds(
    adwithoutruntime_ForkNode,
)
adwithoutruntime_FinalNode_strategy = st.builds(
    adwithoutruntime_FinalNode,
)
adwithoutruntime_MergeNode_strategy = st.builds(
    adwithoutruntime_MergeNode,
)
adwithoutruntime_InitialNode_strategy = st.builds(
    adwithoutruntime_InitialNode,
)
adwithoutruntime_NamedElement_strategy = st.builds(
    adwithoutruntime_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
adwithoutruntime_Activity_strategy = st.builds(
    adwithoutruntime_Activity,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
adwithoutruntime_Action_strategy = st.builds(
    adwithoutruntime_Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
adwithoutruntime_ExecutableNode_strategy = st.builds(
    adwithoutruntime_ExecutableNode,
)
adwithoutruntime_ControlNode_strategy = st.builds(
    adwithoutruntime_ControlNode,
)
adwithoutruntime_BooleanVariable_strategy = st.builds(
    adwithoutruntime_BooleanVariable,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
adwithoutruntime_ControlFlow_strategy = st.builds(
    adwithoutruntime_ControlFlow,
)
adwithoutruntime_Variable_strategy = st.builds(
    adwithoutruntime_Variable,
    name=
        safe_text
)
adwithoutruntime_ActivityEdge_strategy = st.builds(
    adwithoutruntime_ActivityEdge,
)
adwithoutruntime_ActivityNode_strategy = st.builds(
    adwithoutruntime_ActivityNode,
)

@given(instance=IntegerExpression_strategy)
@settings(max_examples=50)
def test_integerexpression_instantiation(instance):
    assert isinstance(instance, IntegerExpression)

@given(instance=adwithoutruntime_IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_integercalculationexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerCalculationExpression)



@given(instance=adwithoutruntime_IntegerCalculationExpression_strategy)
def test_adwithoutruntime_integercalculationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=adwithoutruntime_BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanBinaryExpression)



@given(instance=adwithoutruntime_BooleanBinaryExpression_strategy)
def test_adwithoutruntime_booleanbinaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime_BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanUnaryExpression)



@given(instance=adwithoutruntime_BooleanUnaryExpression_strategy)
def test_adwithoutruntime_booleanunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime_IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerComparisonExpression)



@given(instance=adwithoutruntime_IntegerComparisonExpression_strategy)
def test_adwithoutruntime_integercomparisonexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=adwithoutruntime_Expression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_expression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Expression)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=adwithoutruntime_OpaqueAction_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_opaqueaction_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_OpaqueAction)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=adwithoutruntime_BooleanExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_booleanexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanExpression)

@given(instance=adwithoutruntime_IntegerExpression_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_integerexpression_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerExpression)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=adwithoutruntime_IntegerValue_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_integervalue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerValue)



@given(instance=adwithoutruntime_IntegerValue_strategy)
def test_adwithoutruntime_integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adwithoutruntime_BooleanValue_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_booleanvalue_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanValue)



@given(instance=adwithoutruntime_BooleanValue_strategy)
def test_adwithoutruntime_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=adwithoutruntime_IntegerVariable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_integervariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_IntegerVariable)

@given(instance=adwithoutruntime_Value_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_value_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Value)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=adwithoutruntime_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_activityfinalnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=adwithoutruntime_JoinNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_joinnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_JoinNode)

@given(instance=adwithoutruntime_DecisionNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_decisionnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_DecisionNode)

@given(instance=adwithoutruntime_ForkNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_forknode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ForkNode)

@given(instance=adwithoutruntime_FinalNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_finalnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_FinalNode)

@given(instance=adwithoutruntime_MergeNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_mergenode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_MergeNode)

@given(instance=adwithoutruntime_InitialNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_initialnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_InitialNode)

@given(instance=adwithoutruntime_NamedElement_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_namedelement_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_NamedElement)



@given(instance=adwithoutruntime_NamedElement_strategy)
def test_adwithoutruntime_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=adwithoutruntime_Activity_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_activity_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Activity)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=adwithoutruntime_Action_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_action_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Action)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=adwithoutruntime_ExecutableNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_executablenode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ExecutableNode)

@given(instance=adwithoutruntime_ControlNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_controlnode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ControlNode)

@given(instance=adwithoutruntime_BooleanVariable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_booleanvariable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_BooleanVariable)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=adwithoutruntime_ControlFlow_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_controlflow_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ControlFlow)

@given(instance=adwithoutruntime_Variable_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_variable_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_Variable)



@given(instance=adwithoutruntime_Variable_strategy)
def test_adwithoutruntime_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adwithoutruntime_ActivityEdge_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_activityedge_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityEdge)

@given(instance=adwithoutruntime_ActivityNode_strategy)
@settings(max_examples=50)
def test_adwithoutruntime_activitynode_instantiation(instance):
    assert isinstance(instance, adwithoutruntime_ActivityNode)
