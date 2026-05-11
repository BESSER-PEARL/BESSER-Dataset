import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    automata::Action,
    Guard,
    automata::StringGuard,
    automata::NumberGuard,
    automata::BooleanGuard,
    automata::Guard,
    automata::Variable,
    automata::Transition,
    automata::State,
    automata::Automaton,
    DataType,
    StringOperator,
    BooleanOperator,
    NumberOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automata::action_is_not_abstract():
    assert not inspect.isabstract(automata::Action)


def test_automata::action_constructor_exists():
    assert callable(automata::Action.__init__)


def test_automata::action_constructor_args():
    sig = inspect.signature(automata::Action.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata::stringguard_is_not_abstract():
    assert not inspect.isabstract(automata::StringGuard)


def test_automata::stringguard_constructor_exists():
    assert callable(automata::StringGuard.__init__)


def test_automata::stringguard_constructor_args():
    sig = inspect.signature(automata::StringGuard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_automata::stringguard_has_value():
    assert hasattr(automata::StringGuard, "value")
    descriptor = None
    for klass in automata::StringGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_automata::stringguard_has_operator():
    assert hasattr(automata::StringGuard, "operator")
    descriptor = None
    for klass in automata::StringGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_automata::numberguard_is_not_abstract():
    assert not inspect.isabstract(automata::NumberGuard)


def test_automata::numberguard_constructor_exists():
    assert callable(automata::NumberGuard.__init__)


def test_automata::numberguard_constructor_args():
    sig = inspect.signature(automata::NumberGuard.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_automata::numberguard_has_operator():
    assert hasattr(automata::NumberGuard, "operator")
    descriptor = None
    for klass in automata::NumberGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_automata::numberguard_has_value():
    assert hasattr(automata::NumberGuard, "value")
    descriptor = None
    for klass in automata::NumberGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::booleanguard_is_not_abstract():
    assert not inspect.isabstract(automata::BooleanGuard)


def test_automata::booleanguard_constructor_exists():
    assert callable(automata::BooleanGuard.__init__)


def test_automata::booleanguard_constructor_args():
    sig = inspect.signature(automata::BooleanGuard.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_automata::booleanguard_has_operator():
    assert hasattr(automata::BooleanGuard, "operator")
    descriptor = None
    for klass in automata::BooleanGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_automata::booleanguard_has_value():
    assert hasattr(automata::BooleanGuard, "value")
    descriptor = None
    for klass in automata::BooleanGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_automata::guard_is_not_abstract():
    assert not inspect.isabstract(automata::Guard)


def test_automata::guard_constructor_exists():
    assert callable(automata::Guard.__init__)


def test_automata::guard_constructor_args():
    sig = inspect.signature(automata::Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata::variable_is_not_abstract():
    assert not inspect.isabstract(automata::Variable)


def test_automata::variable_constructor_exists():
    assert callable(automata::Variable.__init__)


def test_automata::variable_constructor_args():
    sig = inspect.signature(automata::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_automata::variable_has_type():
    assert hasattr(automata::Variable, "type")
    descriptor = None
    for klass in automata::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_automata::variable_has_name():
    assert hasattr(automata::Variable, "name")
    descriptor = None
    for klass in automata::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::transition_is_not_abstract():
    assert not inspect.isabstract(automata::Transition)


def test_automata::transition_constructor_exists():
    assert callable(automata::Transition.__init__)


def test_automata::transition_constructor_args():
    sig = inspect.signature(automata::Transition.__init__)
    params = list(sig.parameters.keys())



def test_automata::state_is_not_abstract():
    assert not inspect.isabstract(automata::State)


def test_automata::state_constructor_exists():
    assert callable(automata::State.__init__)


def test_automata::state_constructor_args():
    sig = inspect.signature(automata::State.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_automata::state_has_initial():
    assert hasattr(automata::State, "initial")
    descriptor = None
    for klass in automata::State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_automata::state_has_name():
    assert hasattr(automata::State, "name")
    descriptor = None
    for klass in automata::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automata::automaton_is_not_abstract():
    assert not inspect.isabstract(automata::Automaton)


def test_automata::automaton_constructor_exists():
    assert callable(automata::Automaton.__init__)


def test_automata::automaton_constructor_args():
    sig = inspect.signature(automata::Automaton.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Number",
        "String",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_stringoperator_exists():
    # Check that the Enumeration exists
    assert StringOperator is not None

def test_stringoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringOperator]
    expected_literals = [
        "Unequal",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringOperator"

def test_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "Unequal",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"

def test_numberoperator_exists():
    # Check that the Enumeration exists
    assert NumberOperator is not None

def test_numberoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOperator]
    expected_literals = [
        "Equal",
        "Unequal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOperator"


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
automata::Action_strategy = st.builds(
    automata::Action,
)
Guard_strategy = st.builds(
    Guard,
)
automata::StringGuard_strategy = st.builds(
    automata::StringGuard,
    value=
        safe_text,
    operator=
        safe_text
)
automata::NumberGuard_strategy = st.builds(
    automata::NumberGuard,
    operator=
        safe_text,
    value=
        safe_text
)
automata::BooleanGuard_strategy = st.builds(
    automata::BooleanGuard,
    operator=
        safe_text,
    value=
        st.booleans()
)
automata::Guard_strategy = st.builds(
    automata::Guard,
)
automata::Variable_strategy = st.builds(
    automata::Variable,
    type=
        safe_text,
    name=
        safe_text
)
automata::Transition_strategy = st.builds(
    automata::Transition,
)
automata::State_strategy = st.builds(
    automata::State,
    initial=
        st.booleans(),
    name=
        safe_text
)
automata::Automaton_strategy = st.builds(
    automata::Automaton,
)

@given(instance=automata::Action_strategy)
@settings(max_examples=50)
def test_automata::action_instantiation(instance):
    assert isinstance(instance, automata::Action)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=automata::StringGuard_strategy)
@settings(max_examples=50)
def test_automata::stringguard_instantiation(instance):
    assert isinstance(instance, automata::StringGuard)

@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::StringGuard_strategy)
def test_automata::stringguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::NumberGuard_strategy)
@settings(max_examples=50)
def test_automata::numberguard_instantiation(instance):
    assert isinstance(instance, automata::NumberGuard)

@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=automata::NumberGuard_strategy)
def test_automata::numberguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::BooleanGuard_strategy)
@settings(max_examples=50)
def test_automata::booleanguard_instantiation(instance):
    assert isinstance(instance, automata::BooleanGuard)

@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=automata::BooleanGuard_strategy)
def test_automata::booleanguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=automata::Guard_strategy)
@settings(max_examples=50)
def test_automata::guard_instantiation(instance):
    assert isinstance(instance, automata::Guard)

@given(instance=automata::Variable_strategy)
@settings(max_examples=50)
def test_automata::variable_instantiation(instance):
    assert isinstance(instance, automata::Variable)

@given(instance=automata::Variable_strategy)
def test_automata::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=automata::Variable_strategy)
def test_automata::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=automata::Variable_strategy)
def test_automata::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::Variable_strategy)
def test_automata::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Transition_strategy)
@settings(max_examples=50)
def test_automata::transition_instantiation(instance):
    assert isinstance(instance, automata::Transition)

@given(instance=automata::State_strategy)
@settings(max_examples=50)
def test_automata::state_instantiation(instance):
    assert isinstance(instance, automata::State)

@given(instance=automata::State_strategy)
def test_automata::state_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=automata::State_strategy)
def test_automata::state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=automata::State_strategy)
def test_automata::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automata::State_strategy)
def test_automata::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automata::Automaton_strategy)
@settings(max_examples=50)
def test_automata::automaton_instantiation(instance):
    assert isinstance(instance, automata::Automaton)
