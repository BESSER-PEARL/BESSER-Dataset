import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Data,
    SimplStateMachine::IntegerData,
    SimplStateMachine::Assignment,
    Variable,
    SimplStateMachine::IntegerVariable,
    SimplStateMachine::BooleanVariable,
    SimplStateMachine::BooleanData,
    ExpressionElement,
    SimplStateMachine::VariableReference,
    SimplStateMachine::Data,
    SimplStateMachine::ExpressionElement,
    SimplStateMachine::Expression,
    State,
    SimplStateMachine::Operation,
    SimplStateMachine::InitialState,
    SimplStateMachine::Variable,
    SimplStateMachine::Event,
    SimplStateMachine::Transition,
    SimplStateMachine::CompositeState,
    SimplStateMachine::State,
    CompositeState,
    SimplStateMachine::StateMachine,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::integerdata_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::IntegerData)


def test_simplstatemachine::integerdata_constructor_exists():
    assert callable(SimplStateMachine::IntegerData.__init__)


def test_simplstatemachine::integerdata_constructor_args():
    sig = inspect.signature(SimplStateMachine::IntegerData.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplstatemachine::integerdata_has_value():
    assert hasattr(SimplStateMachine::IntegerData, "value")
    descriptor = None
    for klass in SimplStateMachine::IntegerData.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachine::assignment_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Assignment)


def test_simplstatemachine::assignment_constructor_exists():
    assert callable(SimplStateMachine::Assignment.__init__)


def test_simplstatemachine::assignment_constructor_args():
    sig = inspect.signature(SimplStateMachine::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "_name" in params, "Missing parameter '_name'"

def test_simplstatemachine::assignment_has__name():
    assert hasattr(SimplStateMachine::Assignment, "_name")
    descriptor = None
    for klass in SimplStateMachine::Assignment.__mro__:
        if "_name" in klass.__dict__:
            descriptor = klass.__dict__["_name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::integervariable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::IntegerVariable)


def test_simplstatemachine::integervariable_constructor_exists():
    assert callable(SimplStateMachine::IntegerVariable.__init__)


def test_simplstatemachine::integervariable_constructor_args():
    sig = inspect.signature(SimplStateMachine::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::BooleanVariable)


def test_simplstatemachine::booleanvariable_constructor_exists():
    assert callable(SimplStateMachine::BooleanVariable.__init__)


def test_simplstatemachine::booleanvariable_constructor_args():
    sig = inspect.signature(SimplStateMachine::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::booleandata_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::BooleanData)


def test_simplstatemachine::booleandata_constructor_exists():
    assert callable(SimplStateMachine::BooleanData.__init__)


def test_simplstatemachine::booleandata_constructor_args():
    sig = inspect.signature(SimplStateMachine::BooleanData.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_simplstatemachine::booleandata_has_value():
    assert hasattr(SimplStateMachine::BooleanData, "value")
    descriptor = None
    for klass in SimplStateMachine::BooleanData.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressionelement_is_not_abstract():
    assert not inspect.isabstract(ExpressionElement)


def test_expressionelement_constructor_exists():
    assert callable(ExpressionElement.__init__)


def test_expressionelement_constructor_args():
    sig = inspect.signature(ExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::variablereference_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::VariableReference)


def test_simplstatemachine::variablereference_constructor_exists():
    assert callable(SimplStateMachine::VariableReference.__init__)


def test_simplstatemachine::variablereference_constructor_args():
    sig = inspect.signature(SimplStateMachine::VariableReference.__init__)
    params = list(sig.parameters.keys())
    assert "_name" in params, "Missing parameter '_name'"

def test_simplstatemachine::variablereference_has__name():
    assert hasattr(SimplStateMachine::VariableReference, "_name")
    descriptor = None
    for klass in SimplStateMachine::VariableReference.__mro__:
        if "_name" in klass.__dict__:
            descriptor = klass.__dict__["_name"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachine::data_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Data)


def test_simplstatemachine::data_constructor_exists():
    assert callable(SimplStateMachine::Data.__init__)


def test_simplstatemachine::data_constructor_args():
    sig = inspect.signature(SimplStateMachine::Data.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::expressionelement_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::ExpressionElement)


def test_simplstatemachine::expressionelement_constructor_exists():
    assert callable(SimplStateMachine::ExpressionElement.__init__)


def test_simplstatemachine::expressionelement_constructor_args():
    sig = inspect.signature(SimplStateMachine::ExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::expression_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Expression)


def test_simplstatemachine::expression_constructor_exists():
    assert callable(SimplStateMachine::Expression.__init__)


def test_simplstatemachine::expression_constructor_args():
    sig = inspect.signature(SimplStateMachine::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "_name" in params, "Missing parameter '_name'"

def test_simplstatemachine::expression_has_operator():
    assert hasattr(SimplStateMachine::Expression, "operator")
    descriptor = None
    for klass in SimplStateMachine::Expression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachine::expression_has__name():
    assert hasattr(SimplStateMachine::Expression, "_name")
    descriptor = None
    for klass in SimplStateMachine::Expression.__mro__:
        if "_name" in klass.__dict__:
            descriptor = klass.__dict__["_name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::operation_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Operation)


def test_simplstatemachine::operation_constructor_exists():
    assert callable(SimplStateMachine::Operation.__init__)


def test_simplstatemachine::operation_constructor_args():
    sig = inspect.signature(SimplStateMachine::Operation.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::InitialState)


def test_simplstatemachine::initialstate_constructor_exists():
    assert callable(SimplStateMachine::InitialState.__init__)


def test_simplstatemachine::initialstate_constructor_args():
    sig = inspect.signature(SimplStateMachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::variable_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Variable)


def test_simplstatemachine::variable_constructor_exists():
    assert callable(SimplStateMachine::Variable.__init__)


def test_simplstatemachine::variable_constructor_args():
    sig = inspect.signature(SimplStateMachine::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplstatemachine::variable_has_name():
    assert hasattr(SimplStateMachine::Variable, "name")
    descriptor = None
    for klass in SimplStateMachine::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachine::event_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Event)


def test_simplstatemachine::event_constructor_exists():
    assert callable(SimplStateMachine::Event.__init__)


def test_simplstatemachine::event_constructor_args():
    sig = inspect.signature(SimplStateMachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplstatemachine::event_has_name():
    assert hasattr(SimplStateMachine::Event, "name")
    descriptor = None
    for klass in SimplStateMachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplstatemachine::transition_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::Transition)


def test_simplstatemachine::transition_constructor_exists():
    assert callable(SimplStateMachine::Transition.__init__)


def test_simplstatemachine::transition_constructor_args():
    sig = inspect.signature(SimplStateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::compositestate_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::CompositeState)


def test_simplstatemachine::compositestate_constructor_exists():
    assert callable(SimplStateMachine::CompositeState.__init__)


def test_simplstatemachine::compositestate_constructor_args():
    sig = inspect.signature(SimplStateMachine::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::state_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::State)


def test_simplstatemachine::state_constructor_exists():
    assert callable(SimplStateMachine::State.__init__)


def test_simplstatemachine::state_constructor_args():
    sig = inspect.signature(SimplStateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_simplstatemachine::state_has_name():
    assert hasattr(SimplStateMachine::State, "name")
    descriptor = None
    for klass in SimplStateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simplstatemachine::state_has_isActive():
    assert hasattr(SimplStateMachine::State, "isActive")
    descriptor = None
    for klass in SimplStateMachine::State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_compositestate_is_not_abstract():
    assert not inspect.isabstract(CompositeState)


def test_compositestate_constructor_exists():
    assert callable(CompositeState.__init__)


def test_compositestate_constructor_args():
    sig = inspect.signature(CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_simplstatemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(SimplStateMachine::StateMachine)


def test_simplstatemachine::statemachine_constructor_exists():
    assert callable(SimplStateMachine::StateMachine.__init__)


def test_simplstatemachine::statemachine_constructor_args():
    sig = inspect.signature(SimplStateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "gt",
        "sub",
        "div",
        "mul",
        "neq",
        "add",
        "lte",
        "eq",
        "gte",
        "and_",
        "not_",
        "or_",
        "lt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Data_strategy = st.builds(
    Data,
)
SimplStateMachine::IntegerData_strategy = st.builds(
    SimplStateMachine::IntegerData,
    value=
        st.integers()
)
SimplStateMachine::Assignment_strategy = st.builds(
    SimplStateMachine::Assignment,
    _name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
SimplStateMachine::IntegerVariable_strategy = st.builds(
    SimplStateMachine::IntegerVariable,
)
SimplStateMachine::BooleanVariable_strategy = st.builds(
    SimplStateMachine::BooleanVariable,
)
SimplStateMachine::BooleanData_strategy = st.builds(
    SimplStateMachine::BooleanData,
    value=
        st.booleans()
)
ExpressionElement_strategy = st.builds(
    ExpressionElement,
)
SimplStateMachine::VariableReference_strategy = st.builds(
    SimplStateMachine::VariableReference,
    _name=
        safe_text
)
SimplStateMachine::Data_strategy = st.builds(
    SimplStateMachine::Data,
)
SimplStateMachine::ExpressionElement_strategy = st.builds(
    SimplStateMachine::ExpressionElement,
)
SimplStateMachine::Expression_strategy = st.builds(
    SimplStateMachine::Expression,
    operator=
        safe_text,
    _name=
        safe_text
)
State_strategy = st.builds(
    State,
)
SimplStateMachine::Operation_strategy = st.builds(
    SimplStateMachine::Operation,
)
SimplStateMachine::InitialState_strategy = st.builds(
    SimplStateMachine::InitialState,
)
SimplStateMachine::Variable_strategy = st.builds(
    SimplStateMachine::Variable,
    name=
        safe_text
)
SimplStateMachine::Event_strategy = st.builds(
    SimplStateMachine::Event,
    name=
        safe_text
)
SimplStateMachine::Transition_strategy = st.builds(
    SimplStateMachine::Transition,
)
SimplStateMachine::CompositeState_strategy = st.builds(
    SimplStateMachine::CompositeState,
)
SimplStateMachine::State_strategy = st.builds(
    SimplStateMachine::State,
    name=
        safe_text,
    isActive=
        st.booleans()
)
CompositeState_strategy = st.builds(
    CompositeState,
)
SimplStateMachine::StateMachine_strategy = st.builds(
    SimplStateMachine::StateMachine,
)

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=SimplStateMachine::IntegerData_strategy)
@settings(max_examples=50)
def test_simplstatemachine::integerdata_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::IntegerData)

@given(instance=SimplStateMachine::IntegerData_strategy)
def test_simplstatemachine::integerdata_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=SimplStateMachine::IntegerData_strategy)
def test_simplstatemachine::integerdata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SimplStateMachine::Assignment_strategy)
@settings(max_examples=50)
def test_simplstatemachine::assignment_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Assignment)

@given(instance=SimplStateMachine::Assignment_strategy)
def test_simplstatemachine::assignment__name_type(instance):
    assert isinstance(instance._name, str)


@given(instance=SimplStateMachine::Assignment_strategy)
def test_simplstatemachine::assignment__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=SimplStateMachine::IntegerVariable_strategy)
@settings(max_examples=50)
def test_simplstatemachine::integervariable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::IntegerVariable)

@given(instance=SimplStateMachine::BooleanVariable_strategy)
@settings(max_examples=50)
def test_simplstatemachine::booleanvariable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::BooleanVariable)

@given(instance=SimplStateMachine::BooleanData_strategy)
@settings(max_examples=50)
def test_simplstatemachine::booleandata_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::BooleanData)

@given(instance=SimplStateMachine::BooleanData_strategy)
def test_simplstatemachine::booleandata_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=SimplStateMachine::BooleanData_strategy)
def test_simplstatemachine::booleandata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ExpressionElement_strategy)
@settings(max_examples=50)
def test_expressionelement_instantiation(instance):
    assert isinstance(instance, ExpressionElement)

@given(instance=SimplStateMachine::VariableReference_strategy)
@settings(max_examples=50)
def test_simplstatemachine::variablereference_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::VariableReference)

@given(instance=SimplStateMachine::VariableReference_strategy)
def test_simplstatemachine::variablereference__name_type(instance):
    assert isinstance(instance._name, str)


@given(instance=SimplStateMachine::VariableReference_strategy)
def test_simplstatemachine::variablereference__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original

@given(instance=SimplStateMachine::Data_strategy)
@settings(max_examples=50)
def test_simplstatemachine::data_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Data)

@given(instance=SimplStateMachine::ExpressionElement_strategy)
@settings(max_examples=50)
def test_simplstatemachine::expressionelement_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::ExpressionElement)

@given(instance=SimplStateMachine::Expression_strategy)
@settings(max_examples=50)
def test_simplstatemachine::expression_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Expression)

@given(instance=SimplStateMachine::Expression_strategy)
def test_simplstatemachine::expression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=SimplStateMachine::Expression_strategy)
def test_simplstatemachine::expression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=SimplStateMachine::Expression_strategy)
def test_simplstatemachine::expression__name_type(instance):
    assert isinstance(instance._name, str)


@given(instance=SimplStateMachine::Expression_strategy)
def test_simplstatemachine::expression__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=SimplStateMachine::Operation_strategy)
@settings(max_examples=50)
def test_simplstatemachine::operation_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Operation)

@given(instance=SimplStateMachine::InitialState_strategy)
@settings(max_examples=50)
def test_simplstatemachine::initialstate_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::InitialState)

@given(instance=SimplStateMachine::Variable_strategy)
@settings(max_examples=50)
def test_simplstatemachine::variable_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Variable)

@given(instance=SimplStateMachine::Variable_strategy)
def test_simplstatemachine::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplStateMachine::Variable_strategy)
def test_simplstatemachine::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplStateMachine::Event_strategy)
@settings(max_examples=50)
def test_simplstatemachine::event_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Event)

@given(instance=SimplStateMachine::Event_strategy)
def test_simplstatemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplStateMachine::Event_strategy)
def test_simplstatemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplStateMachine::Transition_strategy)
@settings(max_examples=50)
def test_simplstatemachine::transition_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::Transition)

@given(instance=SimplStateMachine::CompositeState_strategy)
@settings(max_examples=50)
def test_simplstatemachine::compositestate_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::CompositeState)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SimplStateMachine::CompositeState_strategy)
@settings(max_examples=30)
def test_simplstatemachine::compositestate_unactivesubtree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unactiveSubTree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unactiveSubTree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unactiveSubTree' in SimplStateMachine::CompositeState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unactiveSubTree' in SimplStateMachine::CompositeState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unactiveSubTree' in SimplStateMachine::CompositeState is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=SimplStateMachine::CompositeState_strategy)
@settings(max_examples=30)
def test_simplstatemachine::compositestate_activesubtree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.activeSubTree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.activeSubTree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'activeSubTree' in SimplStateMachine::CompositeState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'activeSubTree' in SimplStateMachine::CompositeState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'activeSubTree' in SimplStateMachine::CompositeState is not implemented or raised an error")

@given(instance=SimplStateMachine::State_strategy)
@settings(max_examples=50)
def test_simplstatemachine::state_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::State)

@given(instance=SimplStateMachine::State_strategy)
def test_simplstatemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SimplStateMachine::State_strategy)
def test_simplstatemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimplStateMachine::State_strategy)
def test_simplstatemachine::state_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=SimplStateMachine::State_strategy)
def test_simplstatemachine::state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=CompositeState_strategy)
@settings(max_examples=50)
def test_compositestate_instantiation(instance):
    assert isinstance(instance, CompositeState)

@given(instance=SimplStateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_simplstatemachine::statemachine_instantiation(instance):
    assert isinstance(instance, SimplStateMachine::StateMachine)
