import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    automata_Action,
    Guard,
    automata_StringGuard,
    automata_NumberGuard,
    automata_BooleanGuard,
    automata_Guard,
    automata_Variable,
    automata_Transition,
    automata_State,
    automata_Automaton,
    NumberOperator,
    BooleanOperator,
    StringOperator,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_automata_action_is_not_abstract():
    assert not inspect.isabstract(automata_Action)


def test_automata_action_constructor_exists():
    assert callable(automata_Action.__init__)


def test_automata_action_constructor_args():
    sig = inspect.signature(automata_Action.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata_stringguard_is_not_abstract():
    assert not inspect.isabstract(automata_StringGuard)


def test_automata_stringguard_constructor_exists():
    assert callable(automata_StringGuard.__init__)


def test_automata_stringguard_constructor_args():
    sig = inspect.signature(automata_StringGuard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_automata_stringguard_has_value():
    assert hasattr(automata_StringGuard, "value")
    descriptor = None
    for klass in automata_StringGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_automata_stringguard_has_operator():
    assert hasattr(automata_StringGuard, "operator")
    descriptor = None
    for klass in automata_StringGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_automata_numberguard_is_not_abstract():
    assert not inspect.isabstract(automata_NumberGuard)


def test_automata_numberguard_constructor_exists():
    assert callable(automata_NumberGuard.__init__)


def test_automata_numberguard_constructor_args():
    sig = inspect.signature(automata_NumberGuard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_automata_numberguard_has_value():
    assert hasattr(automata_NumberGuard, "value")
    descriptor = None
    for klass in automata_NumberGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_automata_numberguard_has_operator():
    assert hasattr(automata_NumberGuard, "operator")
    descriptor = None
    for klass in automata_NumberGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_automata_booleanguard_is_not_abstract():
    assert not inspect.isabstract(automata_BooleanGuard)


def test_automata_booleanguard_constructor_exists():
    assert callable(automata_BooleanGuard.__init__)


def test_automata_booleanguard_constructor_args():
    sig = inspect.signature(automata_BooleanGuard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_automata_booleanguard_has_value():
    assert hasattr(automata_BooleanGuard, "value")
    descriptor = None
    for klass in automata_BooleanGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_automata_booleanguard_has_operator():
    assert hasattr(automata_BooleanGuard, "operator")
    descriptor = None
    for klass in automata_BooleanGuard.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_automata_guard_is_not_abstract():
    assert not inspect.isabstract(automata_Guard)


def test_automata_guard_constructor_exists():
    assert callable(automata_Guard.__init__)


def test_automata_guard_constructor_args():
    sig = inspect.signature(automata_Guard.__init__)
    params = list(sig.parameters.keys())



def test_automata_variable_is_not_abstract():
    assert not inspect.isabstract(automata_Variable)


def test_automata_variable_constructor_exists():
    assert callable(automata_Variable.__init__)


def test_automata_variable_constructor_args():
    sig = inspect.signature(automata_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_automata_variable_has_name():
    assert hasattr(automata_Variable, "name")
    descriptor = None
    for klass in automata_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_automata_variable_has_type():
    assert hasattr(automata_Variable, "type")
    descriptor = None
    for klass in automata_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_automata_transition_is_not_abstract():
    assert not inspect.isabstract(automata_Transition)


def test_automata_transition_constructor_exists():
    assert callable(automata_Transition.__init__)


def test_automata_transition_constructor_args():
    sig = inspect.signature(automata_Transition.__init__)
    params = list(sig.parameters.keys())



def test_automata_state_is_not_abstract():
    assert not inspect.isabstract(automata_State)


def test_automata_state_constructor_exists():
    assert callable(automata_State.__init__)


def test_automata_state_constructor_args():
    sig = inspect.signature(automata_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initial" in params, "Missing parameter 'initial'"

def test_automata_state_has_name():
    assert hasattr(automata_State, "name")
    descriptor = None
    for klass in automata_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_automata_state_has_initial():
    assert hasattr(automata_State, "initial")
    descriptor = None
    for klass in automata_State.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)



def test_automata_automaton_is_not_abstract():
    assert not inspect.isabstract(automata_Automaton)


def test_automata_automaton_constructor_exists():
    assert callable(automata_Automaton.__init__)


def test_automata_automaton_constructor_args():
    sig = inspect.signature(automata_Automaton.__init__)
    params = list(sig.parameters.keys())

def test_numberoperator_exists():
    # Check that the Enumeration exists
    assert NumberOperator is not None

def test_numberoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumberOperator]
    expected_literals = [
        "Unequal",
        "Equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumberOperator"

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

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "String",
        "Boolean",
        "Number",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
automata_Action_strategy = st.builds(
    automata_Action,
)
Guard_strategy = st.builds(
    Guard,
)
automata_StringGuard_strategy = st.builds(
    automata_StringGuard,
    value=
        safe_text,
    operator=
        safe_text
)
automata_NumberGuard_strategy = st.builds(
    automata_NumberGuard,
    value=
        safe_text,
    operator=
        safe_text
)
automata_BooleanGuard_strategy = st.builds(
    automata_BooleanGuard,
    value=
        st.booleans(),
    operator=
        safe_text
)
automata_Guard_strategy = st.builds(
    automata_Guard,
)
automata_Variable_strategy = st.builds(
    automata_Variable,
    name=
        safe_text,
    type=
        safe_text
)
automata_Transition_strategy = st.builds(
    automata_Transition,
)
automata_State_strategy = st.builds(
    automata_State,
    name=
        safe_text,
    initial=
        st.booleans()
)
automata_Automaton_strategy = st.builds(
    automata_Automaton,
)

@given(instance=automata_Action_strategy)
@settings(max_examples=50)
def test_automata_action_instantiation(instance):
    assert isinstance(instance, automata_Action)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=automata_StringGuard_strategy)
@settings(max_examples=50)
def test_automata_stringguard_instantiation(instance):
    assert isinstance(instance, automata_StringGuard)



@given(instance=automata_StringGuard_strategy)
def test_automata_stringguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=automata_StringGuard_strategy)
def test_automata_stringguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata_NumberGuard_strategy)
@settings(max_examples=50)
def test_automata_numberguard_instantiation(instance):
    assert isinstance(instance, automata_NumberGuard)



@given(instance=automata_NumberGuard_strategy)
def test_automata_numberguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=automata_NumberGuard_strategy)
def test_automata_numberguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata_BooleanGuard_strategy)
@settings(max_examples=50)
def test_automata_booleanguard_instantiation(instance):
    assert isinstance(instance, automata_BooleanGuard)



@given(instance=automata_BooleanGuard_strategy)
def test_automata_booleanguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=automata_BooleanGuard_strategy)
def test_automata_booleanguard_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=automata_Guard_strategy)
@settings(max_examples=50)
def test_automata_guard_instantiation(instance):
    assert isinstance(instance, automata_Guard)

@given(instance=automata_Variable_strategy)
@settings(max_examples=50)
def test_automata_variable_instantiation(instance):
    assert isinstance(instance, automata_Variable)



@given(instance=automata_Variable_strategy)
def test_automata_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=automata_Variable_strategy)
def test_automata_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=automata_Transition_strategy)
@settings(max_examples=50)
def test_automata_transition_instantiation(instance):
    assert isinstance(instance, automata_Transition)

@given(instance=automata_State_strategy)
@settings(max_examples=50)
def test_automata_state_instantiation(instance):
    assert isinstance(instance, automata_State)



@given(instance=automata_State_strategy)
def test_automata_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=automata_State_strategy)
def test_automata_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=automata_Automaton_strategy)
@settings(max_examples=50)
def test_automata_automaton_instantiation(instance):
    assert isinstance(instance, automata_Automaton)
