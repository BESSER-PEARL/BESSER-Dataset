import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    stateMachine_TransSet,
    stateMachine_FieldState,
    stateMachine_Trans,
    stateMachine_Role,
    stateMachine_DocumentField,
    stateMachine_State,
    stateMachine_Event,
    stateMachine_StateMachine,
    EFieldState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_transset_is_not_abstract():
    assert not inspect.isabstract(stateMachine_TransSet)


def test_statemachine_transset_constructor_exists():
    assert callable(stateMachine_TransSet.__init__)


def test_statemachine_transset_constructor_args():
    sig = inspect.signature(stateMachine_TransSet.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_fieldstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_FieldState)


def test_statemachine_fieldstate_constructor_exists():
    assert callable(stateMachine_FieldState.__init__)


def test_statemachine_fieldstate_constructor_args():
    sig = inspect.signature(stateMachine_FieldState.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_statemachine_fieldstate_has_state():
    assert hasattr(stateMachine_FieldState, "state")
    descriptor = None
    for klass in stateMachine_FieldState.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_trans_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Trans)


def test_statemachine_trans_constructor_exists():
    assert callable(stateMachine_Trans.__init__)


def test_statemachine_trans_constructor_args():
    sig = inspect.signature(stateMachine_Trans.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_role_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Role)


def test_statemachine_role_constructor_exists():
    assert callable(stateMachine_Role.__init__)


def test_statemachine_role_constructor_args():
    sig = inspect.signature(stateMachine_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_role_has_name():
    assert hasattr(stateMachine_Role, "name")
    descriptor = None
    for klass in stateMachine_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_documentfield_is_not_abstract():
    assert not inspect.isabstract(stateMachine_DocumentField)


def test_statemachine_documentfield_constructor_exists():
    assert callable(stateMachine_DocumentField.__init__)


def test_statemachine_documentfield_constructor_args():
    sig = inspect.signature(stateMachine_DocumentField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_documentfield_has_name():
    assert hasattr(stateMachine_DocumentField, "name")
    descriptor = None
    for klass in stateMachine_DocumentField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(stateMachine_State, "name")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_event_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Event)


def test_statemachine_event_constructor_exists():
    assert callable(stateMachine_Event.__init__)


def test_statemachine_event_constructor_args():
    sig = inspect.signature(stateMachine_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_event_has_name():
    assert hasattr(stateMachine_Event, "name")
    descriptor = None
    for klass in stateMachine_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_package():
    assert hasattr(stateMachine_StateMachine, "package")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_statemachine_has_name():
    assert hasattr(stateMachine_StateMachine, "name")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
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
stateMachine_TransSet_strategy = st.builds(
    stateMachine_TransSet,
)
stateMachine_FieldState_strategy = st.builds(
    stateMachine_FieldState,
    state=
        safe_text
)
stateMachine_Trans_strategy = st.builds(
    stateMachine_Trans,
)
stateMachine_Role_strategy = st.builds(
    stateMachine_Role,
    name=
        safe_text
)
stateMachine_DocumentField_strategy = st.builds(
    stateMachine_DocumentField,
    name=
        safe_text
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    name=
        safe_text
)
stateMachine_Event_strategy = st.builds(
    stateMachine_Event,
    name=
        safe_text
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    package=
        safe_text,
    name=
        safe_text
)

@given(instance=stateMachine_TransSet_strategy)
@settings(max_examples=50)
def test_statemachine_transset_instantiation(instance):
    assert isinstance(instance, stateMachine_TransSet)

@given(instance=stateMachine_FieldState_strategy)
@settings(max_examples=50)
def test_statemachine_fieldstate_instantiation(instance):
    assert isinstance(instance, stateMachine_FieldState)



@given(instance=stateMachine_FieldState_strategy)
def test_statemachine_fieldstate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=stateMachine_Trans_strategy)
@settings(max_examples=50)
def test_statemachine_trans_instantiation(instance):
    assert isinstance(instance, stateMachine_Trans)

@given(instance=stateMachine_Role_strategy)
@settings(max_examples=50)
def test_statemachine_role_instantiation(instance):
    assert isinstance(instance, stateMachine_Role)



@given(instance=stateMachine_Role_strategy)
def test_statemachine_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_DocumentField_strategy)
@settings(max_examples=50)
def test_statemachine_documentfield_instantiation(instance):
    assert isinstance(instance, stateMachine_DocumentField)



@given(instance=stateMachine_DocumentField_strategy)
def test_statemachine_documentfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_Event_strategy)
@settings(max_examples=50)
def test_statemachine_event_instantiation(instance):
    assert isinstance(instance, stateMachine_Event)



@given(instance=stateMachine_Event_strategy)
def test_statemachine_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
