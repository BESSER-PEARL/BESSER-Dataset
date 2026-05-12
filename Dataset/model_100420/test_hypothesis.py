import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statechart01::Transition,
    statechart01::Variable,
    statechart01::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart01::transition_is_not_abstract():
    assert not inspect.isabstract(statechart01::Transition)


def test_statechart01::transition_constructor_exists():
    assert callable(statechart01::Transition.__init__)


def test_statechart01::transition_constructor_args():
    sig = inspect.signature(statechart01::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart01::transition_has_name():
    assert hasattr(statechart01::Transition, "name")
    descriptor = None
    for klass in statechart01::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::transition_has_expression():
    assert hasattr(statechart01::Transition, "expression")
    descriptor = None
    for klass in statechart01::Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart01::variable_is_not_abstract():
    assert not inspect.isabstract(statechart01::Variable)


def test_statechart01::variable_constructor_exists():
    assert callable(statechart01::Variable.__init__)


def test_statechart01::variable_constructor_args():
    sig = inspect.signature(statechart01::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart01::variable_has_name():
    assert hasattr(statechart01::Variable, "name")
    descriptor = None
    for klass in statechart01::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::variable_has_value():
    assert hasattr(statechart01::Variable, "value")
    descriptor = None
    for klass in statechart01::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::variable_has_type():
    assert hasattr(statechart01::Variable, "type")
    descriptor = None
    for klass in statechart01::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statechart01::state_is_not_abstract():
    assert not inspect.isabstract(statechart01::State)


def test_statechart01::state_constructor_exists():
    assert callable(statechart01::State.__init__)


def test_statechart01::state_constructor_args():
    sig = inspect.signature(statechart01::State.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_statechart01::state_has_activity():
    assert hasattr(statechart01::State, "activity")
    descriptor = None
    for klass in statechart01::State.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::state_has_type():
    assert hasattr(statechart01::State, "type")
    descriptor = None
    for klass in statechart01::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::state_has_label():
    assert hasattr(statechart01::State, "label")
    descriptor = None
    for klass in statechart01::State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart01::state_has_name():
    assert hasattr(statechart01::State, "name")
    descriptor = None
    for klass in statechart01::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
statechart01::Transition_strategy = st.builds(
    statechart01::Transition,
    name=
        safe_text,
    expression=
        safe_text
)
statechart01::Variable_strategy = st.builds(
    statechart01::Variable,
    name=
        safe_text,
    value=
        safe_text,
    type=
        safe_text
)
statechart01::State_strategy = st.builds(
    statechart01::State,
    activity=
        safe_text,
    type=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)

@given(instance=statechart01::Transition_strategy)
@settings(max_examples=50)
def test_statechart01::transition_instantiation(instance):
    assert isinstance(instance, statechart01::Transition)

@given(instance=statechart01::Transition_strategy)
def test_statechart01::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart01::Transition_strategy)
def test_statechart01::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart01::Transition_strategy)
def test_statechart01::transition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=statechart01::Transition_strategy)
def test_statechart01::transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart01::Variable_strategy)
@settings(max_examples=50)
def test_statechart01::variable_instantiation(instance):
    assert isinstance(instance, statechart01::Variable)

@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart01::Variable_strategy)
def test_statechart01::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart01::State_strategy)
@settings(max_examples=50)
def test_statechart01::state_instantiation(instance):
    assert isinstance(instance, statechart01::State)

@given(instance=statechart01::State_strategy)
def test_statechart01::state_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=statechart01::State_strategy)
def test_statechart01::state_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=statechart01::State_strategy)
def test_statechart01::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart01::State_strategy)
def test_statechart01::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart01::State_strategy)
def test_statechart01::state_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statechart01::State_strategy)
def test_statechart01::state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statechart01::State_strategy)
def test_statechart01::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart01::State_strategy)
def test_statechart01::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
