import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::TransSet,
    stateMachine::FieldState,
    stateMachine::Trans,
    stateMachine::Role,
    stateMachine::DocumentField,
    stateMachine::State,
    stateMachine::Event,
    stateMachine::StateMachine,
    EFieldState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::transset_is_not_abstract():
    assert not inspect.isabstract(stateMachine::TransSet)


def test_statemachine::transset_constructor_exists():
    assert callable(stateMachine::TransSet.__init__)


def test_statemachine::transset_constructor_args():
    sig = inspect.signature(stateMachine::TransSet.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::fieldstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::FieldState)


def test_statemachine::fieldstate_constructor_exists():
    assert callable(stateMachine::FieldState.__init__)


def test_statemachine::fieldstate_constructor_args():
    sig = inspect.signature(stateMachine::FieldState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_statemachine::fieldstate_has_state():
    assert hasattr(stateMachine::FieldState, "state")
    descriptor = None
    for klass in stateMachine::FieldState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::trans_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Trans)


def test_statemachine::trans_constructor_exists():
    assert callable(stateMachine::Trans.__init__)


def test_statemachine::trans_constructor_args():
    sig = inspect.signature(stateMachine::Trans.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::role_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Role)


def test_statemachine::role_constructor_exists():
    assert callable(stateMachine::Role.__init__)


def test_statemachine::role_constructor_args():
    sig = inspect.signature(stateMachine::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::role_has_name():
    assert hasattr(stateMachine::Role, "name")
    descriptor = None
    for klass in stateMachine::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::documentfield_is_not_abstract():
    assert not inspect.isabstract(stateMachine::DocumentField)


def test_statemachine::documentfield_constructor_exists():
    assert callable(stateMachine::DocumentField.__init__)


def test_statemachine::documentfield_constructor_args():
    sig = inspect.signature(stateMachine::DocumentField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::documentfield_has_name():
    assert hasattr(stateMachine::DocumentField, "name")
    descriptor = None
    for klass in stateMachine::DocumentField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::state_has_name():
    assert hasattr(stateMachine::State, "name")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::event_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Event)


def test_statemachine::event_constructor_exists():
    assert callable(stateMachine::Event.__init__)


def test_statemachine::event_constructor_args():
    sig = inspect.signature(stateMachine::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::event_has_name():
    assert hasattr(stateMachine::Event, "name")
    descriptor = None
    for klass in stateMachine::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::statemachine_has_package():
    assert hasattr(stateMachine::StateMachine, "package")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::statemachine_has_name():
    assert hasattr(stateMachine::StateMachine, "name")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_efieldstate_exists():
    # Check that the Enumeration exists
    assert EFieldState is not None

def test_efieldstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EFieldState]
    expected_literals = [
        "READONLY",
        "HIDDEN",
        "EDITABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EFieldState"


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
stateMachine::TransSet_strategy = st.builds(
    stateMachine::TransSet,
)
stateMachine::FieldState_strategy = st.builds(
    stateMachine::FieldState,
    state=
        safe_text
)
stateMachine::Trans_strategy = st.builds(
    stateMachine::Trans,
)
stateMachine::Role_strategy = st.builds(
    stateMachine::Role,
    name=
        safe_text
)
stateMachine::DocumentField_strategy = st.builds(
    stateMachine::DocumentField,
    name=
        safe_text
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    name=
        safe_text
)
stateMachine::Event_strategy = st.builds(
    stateMachine::Event,
    name=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    package=
        safe_text,
    name=
        safe_text
)

@given(instance=stateMachine::TransSet_strategy)
@settings(max_examples=50)
def test_statemachine::transset_instantiation(instance):
    assert isinstance(instance, stateMachine::TransSet)

@given(instance=stateMachine::FieldState_strategy)
@settings(max_examples=50)
def test_statemachine::fieldstate_instantiation(instance):
    assert isinstance(instance, stateMachine::FieldState)

@given(instance=stateMachine::FieldState_strategy)
def test_statemachine::fieldstate_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=stateMachine::FieldState_strategy)
def test_statemachine::fieldstate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=stateMachine::Trans_strategy)
@settings(max_examples=50)
def test_statemachine::trans_instantiation(instance):
    assert isinstance(instance, stateMachine::Trans)

@given(instance=stateMachine::Role_strategy)
@settings(max_examples=50)
def test_statemachine::role_instantiation(instance):
    assert isinstance(instance, stateMachine::Role)

@given(instance=stateMachine::Role_strategy)
def test_statemachine::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Role_strategy)
def test_statemachine::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::DocumentField_strategy)
@settings(max_examples=50)
def test_statemachine::documentfield_instantiation(instance):
    assert isinstance(instance, stateMachine::DocumentField)

@given(instance=stateMachine::DocumentField_strategy)
def test_statemachine::documentfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::DocumentField_strategy)
def test_statemachine::documentfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::Event_strategy)
@settings(max_examples=50)
def test_statemachine::event_instantiation(instance):
    assert isinstance(instance, stateMachine::Event)

@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::Event_strategy)
def test_statemachine::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
