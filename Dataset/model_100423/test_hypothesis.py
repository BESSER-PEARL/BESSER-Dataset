import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statechart101_Thing,
    statechart101_NamedElement,
    Thing,
    NamedElement,
    statechart101_Variable,
    statechart101_Transition,
    statechart101_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statechart101_thing_is_not_abstract():
    assert not inspect.isabstract(statechart101_Thing)


def test_statechart101_thing_constructor_exists():
    assert callable(statechart101_Thing.__init__)


def test_statechart101_thing_constructor_args():
    sig = inspect.signature(statechart101_Thing.__init__)
    params = list(sig.parameters.keys())



def test_statechart101_namedelement_is_not_abstract():
    assert not inspect.isabstract(statechart101_NamedElement)


def test_statechart101_namedelement_constructor_exists():
    assert callable(statechart101_NamedElement.__init__)


def test_statechart101_namedelement_constructor_args():
    sig = inspect.signature(statechart101_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statechart101_namedelement_has_name():
    assert hasattr(statechart101_NamedElement, "name")
    descriptor = None
    for klass in statechart101_NamedElement.__mro__:
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



def test_statechart101_variable_is_not_abstract():
    assert not inspect.isabstract(statechart101_Variable)


def test_statechart101_variable_constructor_exists():
    assert callable(statechart101_Variable.__init__)


def test_statechart101_variable_constructor_args():
    sig = inspect.signature(statechart101_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_statechart101_variable_has_value():
    assert hasattr(statechart101_Variable, "value")
    descriptor = None
    for klass in statechart101_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_statechart101_variable_has_type():
    assert hasattr(statechart101_Variable, "type")
    descriptor = None
    for klass in statechart101_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statechart101_transition_is_not_abstract():
    assert not inspect.isabstract(statechart101_Transition)


def test_statechart101_transition_constructor_exists():
    assert callable(statechart101_Transition.__init__)


def test_statechart101_transition_constructor_args():
    sig = inspect.signature(statechart101_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statechart101_transition_has_expression():
    assert hasattr(statechart101_Transition, "expression")
    descriptor = None
    for klass in statechart101_Transition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statechart101_state_is_not_abstract():
    assert not inspect.isabstract(statechart101_State)


def test_statechart101_state_constructor_exists():
    assert callable(statechart101_State.__init__)


def test_statechart101_state_constructor_args():
    sig = inspect.signature(statechart101_State.__init__)
    params = list(sig.parameters.keys())
    assert "activity" in params, "Missing parameter 'activity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "label" in params, "Missing parameter 'label'"

def test_statechart101_state_has_activity():
    assert hasattr(statechart101_State, "activity")
    descriptor = None
    for klass in statechart101_State.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_statechart101_state_has_type():
    assert hasattr(statechart101_State, "type")
    descriptor = None
    for klass in statechart101_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statechart101_state_has_label():
    assert hasattr(statechart101_State, "label")
    descriptor = None
    for klass in statechart101_State.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
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
statechart101_Thing_strategy = st.builds(
    statechart101_Thing,
)
statechart101_NamedElement_strategy = st.builds(
    statechart101_NamedElement,
    name=
        safe_text
)
Thing_strategy = st.builds(
    Thing,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
statechart101_Variable_strategy = st.builds(
    statechart101_Variable,
    value=
        safe_text,
    type=
        safe_text
)
statechart101_Transition_strategy = st.builds(
    statechart101_Transition,
    expression=
        safe_text
)
statechart101_State_strategy = st.builds(
    statechart101_State,
    activity=
        safe_text,
    type=
        safe_text,
    label=
        safe_text
)

@given(instance=statechart101_Thing_strategy)
@settings(max_examples=50)
def test_statechart101_thing_instantiation(instance):
    assert isinstance(instance, statechart101_Thing)

@given(instance=statechart101_NamedElement_strategy)
@settings(max_examples=50)
def test_statechart101_namedelement_instantiation(instance):
    assert isinstance(instance, statechart101_NamedElement)



@given(instance=statechart101_NamedElement_strategy)
def test_statechart101_namedelement_name_setter(instance):
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

@given(instance=statechart101_Variable_strategy)
@settings(max_examples=50)
def test_statechart101_variable_instantiation(instance):
    assert isinstance(instance, statechart101_Variable)



@given(instance=statechart101_Variable_strategy)
def test_statechart101_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=statechart101_Variable_strategy)
def test_statechart101_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statechart101_Transition_strategy)
@settings(max_examples=50)
def test_statechart101_transition_instantiation(instance):
    assert isinstance(instance, statechart101_Transition)



@given(instance=statechart101_Transition_strategy)
def test_statechart101_transition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=statechart101_State_strategy)
@settings(max_examples=50)
def test_statechart101_state_instantiation(instance):
    assert isinstance(instance, statechart101_State)



@given(instance=statechart101_State_strategy)
def test_statechart101_state_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=statechart101_State_strategy)
def test_statechart101_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statechart101_State_strategy)
def test_statechart101_state_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original
