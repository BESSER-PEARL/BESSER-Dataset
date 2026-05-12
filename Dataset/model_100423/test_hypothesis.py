import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statechart101::Thing,
    statechart101::NamedElement,
    Thing,
    NamedElement,
    statechart101::Variable,
    statechart101::Transition,
    statechart101::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart101::thing_is_not_abstract():
    assert not inspect.isabstract(statechart101::Thing)


def test_statechart101::thing_constructor_exists():
    assert callable(statechart101::Thing.__init__)


def test_statechart101::thing_constructor_args():
    sig = inspect.signature(statechart101::Thing.__init__)
    params = list(sig.parameters.keys())



def test_statechart101::namedelement_is_not_abstract():
    assert not inspect.isabstract(statechart101::NamedElement)


def test_statechart101::namedelement_constructor_exists():
    assert callable(statechart101::NamedElement.__init__)


def test_statechart101::namedelement_constructor_args():
    sig = inspect.signature(statechart101::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart101::namedelement_has_name():
    assert hasattr(statechart101::NamedElement, "name")
    descriptor = None
    for klass in statechart101::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statechart101::variable_is_not_abstract():
    assert not inspect.isabstract(statechart101::Variable)


def test_statechart101::variable_constructor_exists():
    assert callable(statechart101::Variable.__init__)


def test_statechart101::variable_constructor_args():
    sig = inspect.signature(statechart101::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_statechart101::variable_has_type():
    assert hasattr(statechart101::Variable, "type")
    descriptor = None
    for klass in statechart101::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart101::variable_has_value():
    assert hasattr(statechart101::Variable, "value")
    descriptor = None
    for klass in statechart101::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_statechart101::transition_is_not_abstract():
    assert not inspect.isabstract(statechart101::Transition)


def test_statechart101::transition_constructor_exists():
    assert callable(statechart101::Transition.__init__)


def test_statechart101::transition_constructor_args():
    sig = inspect.signature(statechart101::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart101::transition_has_expression():
    assert hasattr(statechart101::Transition, "expression")
    descriptor = None
    for klass in statechart101::Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart101::state_is_not_abstract():
    assert not inspect.isabstract(statechart101::State)


def test_statechart101::state_constructor_exists():
    assert callable(statechart101::State.__init__)


def test_statechart101::state_constructor_args():
    sig = inspect.signature(statechart101::State.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart101::state_has_activity():
    assert hasattr(statechart101::State, "activity")
    descriptor = None
    for klass in statechart101::State.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart101::state_has_label():
    assert hasattr(statechart101::State, "label")
    descriptor = None
    for klass in statechart101::State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_statechart101::state_has_type():
    assert hasattr(statechart101::State, "type")
    descriptor = None
    for klass in statechart101::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
statechart101::Thing_strategy = st.builds(
    statechart101::Thing,
)
statechart101::NamedElement_strategy = st.builds(
    statechart101::NamedElement,
    name=
        safe_text
)
Thing_strategy = st.builds(
    Thing,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statechart101::Variable_strategy = st.builds(
    statechart101::Variable,
    type=
        safe_text,
    value=
        safe_text
)
statechart101::Transition_strategy = st.builds(
    statechart101::Transition,
    expression=
        safe_text
)
statechart101::State_strategy = st.builds(
    statechart101::State,
    activity=
        safe_text,
    label=
        safe_text,
    type=
        safe_text
)

@given(instance=statechart101::Thing_strategy)
@settings(max_examples=50)
def test_statechart101::thing_instantiation(instance):
    assert isinstance(instance, statechart101::Thing)

@given(instance=statechart101::NamedElement_strategy)
@settings(max_examples=50)
def test_statechart101::namedelement_instantiation(instance):
    assert isinstance(instance, statechart101::NamedElement)

@given(instance=statechart101::NamedElement_strategy)
def test_statechart101::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statechart101::NamedElement_strategy)
def test_statechart101::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=statechart101::Variable_strategy)
@settings(max_examples=50)
def test_statechart101::variable_instantiation(instance):
    assert isinstance(instance, statechart101::Variable)

@given(instance=statechart101::Variable_strategy)
def test_statechart101::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart101::Variable_strategy)
def test_statechart101::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart101::Variable_strategy)
def test_statechart101::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=statechart101::Variable_strategy)
def test_statechart101::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=statechart101::Transition_strategy)
@settings(max_examples=50)
def test_statechart101::transition_instantiation(instance):
    assert isinstance(instance, statechart101::Transition)

@given(instance=statechart101::Transition_strategy)
def test_statechart101::transition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=statechart101::Transition_strategy)
def test_statechart101::transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart101::State_strategy)
@settings(max_examples=50)
def test_statechart101::state_instantiation(instance):
    assert isinstance(instance, statechart101::State)

@given(instance=statechart101::State_strategy)
def test_statechart101::state_activity_type(instance):
    assert isinstance(instance.activity, str)


@given(instance=statechart101::State_strategy)
def test_statechart101::state_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original

@given(instance=statechart101::State_strategy)
def test_statechart101::state_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=statechart101::State_strategy)
def test_statechart101::state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=statechart101::State_strategy)
def test_statechart101::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=statechart101::State_strategy)
def test_statechart101::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
