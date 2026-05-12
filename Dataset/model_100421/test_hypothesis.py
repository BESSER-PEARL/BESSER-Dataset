import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statechart02_Transition,
    statechart02_Variable,
    statechart02_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart02_transition_is_not_abstract():
    assert not inspect.isabstract(statechart02_Transition)


def test_statechart02_transition_constructor_exists():
    assert callable(statechart02_Transition.__init__)


def test_statechart02_transition_constructor_args():
    sig = inspect.signature(statechart02_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart02_transition_has_name():
    assert hasattr(statechart02_Transition, "name")
    descriptor = None
    for klass in statechart02_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_transition_has_expression():
    assert hasattr(statechart02_Transition, "expression")
    descriptor = None
    for klass in statechart02_Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart02_variable_is_not_abstract():
    assert not inspect.isabstract(statechart02_Variable)


def test_statechart02_variable_constructor_exists():
    assert callable(statechart02_Variable.__init__)


def test_statechart02_variable_constructor_args():
    sig = inspect.signature(statechart02_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_statechart02_variable_has_type():
    assert hasattr(statechart02_Variable, "type")
    descriptor = None
    for klass in statechart02_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_variable_has_name():
    assert hasattr(statechart02_Variable, "name")
    descriptor = None
    for klass in statechart02_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_variable_has_value():
    assert hasattr(statechart02_Variable, "value")
    descriptor = None
    for klass in statechart02_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statechart02_state_is_not_abstract():
    assert not inspect.isabstract(statechart02_State)


def test_statechart02_state_constructor_exists():
    assert callable(statechart02_State.__init__)


def test_statechart02_state_constructor_args():
    sig = inspect.signature(statechart02_State.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"
    assert "activity" in params, "Missing parameter 'activity'"

def test_statechart02_state_has_type():
    assert hasattr(statechart02_State, "type")
    descriptor = None
    for klass in statechart02_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_state_has_label():
    assert hasattr(statechart02_State, "label")
    descriptor = None
    for klass in statechart02_State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_state_has_name():
    assert hasattr(statechart02_State, "name")
    descriptor = None
    for klass in statechart02_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart02_state_has_activity():
    assert hasattr(statechart02_State, "activity")
    descriptor = None
    for klass in statechart02_State.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)


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
statechart02_Transition_strategy = st.builds(
    statechart02_Transition,
    name=
        safe_text,
    expression=
        safe_text
)
statechart02_Variable_strategy = st.builds(
    statechart02_Variable,
    type=
        safe_text,
    name=
        safe_text,
    value=
        safe_text
)
statechart02_State_strategy = st.builds(
    statechart02_State,
    type=
        safe_text,
    label=
        safe_text,
    name=
        safe_text,
    activity=
        safe_text
)

@given(instance=statechart02_Transition_strategy)
@settings(max_examples=50)
def test_statechart02_transition_instantiation(instance):
    assert isinstance(instance, statechart02_Transition)



@given(instance=statechart02_Transition_strategy)
def test_statechart02_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statechart02_Transition_strategy)
def test_statechart02_transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart02_Variable_strategy)
@settings(max_examples=50)
def test_statechart02_variable_instantiation(instance):
    assert isinstance(instance, statechart02_Variable)



@given(instance=statechart02_Variable_strategy)
def test_statechart02_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statechart02_Variable_strategy)
def test_statechart02_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statechart02_Variable_strategy)
def test_statechart02_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statechart02_State_strategy)
@settings(max_examples=50)
def test_statechart02_state_instantiation(instance):
    assert isinstance(instance, statechart02_State)



@given(instance=statechart02_State_strategy)
def test_statechart02_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statechart02_State_strategy)
def test_statechart02_state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=statechart02_State_strategy)
def test_statechart02_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=statechart02_State_strategy)
def test_statechart02_state_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original
