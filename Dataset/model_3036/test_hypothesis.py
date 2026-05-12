import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basicfsm_Action,
    basicfsm_Guard,
    basicfsm_Trans,
    basicfsm_State,
    basicfsm_Machine,
    State,
    basicfsm_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicfsm_action_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Action)


def test_basicfsm_action_constructor_exists():
    assert callable(basicfsm_Action.__init__)


def test_basicfsm_action_constructor_args():
    sig = inspect.signature(basicfsm_Action.__init__)
    params = list(sig.parameters.keys())



def test_basicfsm_guard_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Guard)


def test_basicfsm_guard_constructor_exists():
    assert callable(basicfsm_Guard.__init__)


def test_basicfsm_guard_constructor_args():
    sig = inspect.signature(basicfsm_Guard.__init__)
    params = list(sig.parameters.keys())



def test_basicfsm_trans_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Trans)


def test_basicfsm_trans_constructor_exists():
    assert callable(basicfsm_Trans.__init__)


def test_basicfsm_trans_constructor_args():
    sig = inspect.signature(basicfsm_Trans.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_basicfsm_trans_has_event():
    assert hasattr(basicfsm_Trans, "event")
    descriptor = None
    for klass in basicfsm_Trans.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_basicfsm_state_is_not_abstract():
    assert not inspect.isabstract(basicfsm_State)


def test_basicfsm_state_constructor_exists():
    assert callable(basicfsm_State.__init__)


def test_basicfsm_state_constructor_args():
    sig = inspect.signature(basicfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsm_state_has_name():
    assert hasattr(basicfsm_State, "name")
    descriptor = None
    for klass in basicfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basicfsm_machine_is_not_abstract():
    assert not inspect.isabstract(basicfsm_Machine)


def test_basicfsm_machine_constructor_exists():
    assert callable(basicfsm_Machine.__init__)


def test_basicfsm_machine_constructor_args():
    sig = inspect.signature(basicfsm_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_basicfsm_machine_has_name():
    assert hasattr(basicfsm_Machine, "name")
    descriptor = None
    for klass in basicfsm_Machine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_basicfsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(basicfsm_InitialState)


def test_basicfsm_initialstate_constructor_exists():
    assert callable(basicfsm_InitialState.__init__)


def test_basicfsm_initialstate_constructor_args():
    sig = inspect.signature(basicfsm_InitialState.__init__)
    params = list(sig.parameters.keys())


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
basicfsm_Action_strategy = st.builds(
    basicfsm_Action,
)
basicfsm_Guard_strategy = st.builds(
    basicfsm_Guard,
)
basicfsm_Trans_strategy = st.builds(
    basicfsm_Trans,
    event=
        safe_text
)
basicfsm_State_strategy = st.builds(
    basicfsm_State,
    name=
        safe_text
)
basicfsm_Machine_strategy = st.builds(
    basicfsm_Machine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
basicfsm_InitialState_strategy = st.builds(
    basicfsm_InitialState,
)

@given(instance=basicfsm_Action_strategy)
@settings(max_examples=50)
def test_basicfsm_action_instantiation(instance):
    assert isinstance(instance, basicfsm_Action)

@given(instance=basicfsm_Guard_strategy)
@settings(max_examples=50)
def test_basicfsm_guard_instantiation(instance):
    assert isinstance(instance, basicfsm_Guard)

@given(instance=basicfsm_Trans_strategy)
@settings(max_examples=50)
def test_basicfsm_trans_instantiation(instance):
    assert isinstance(instance, basicfsm_Trans)



@given(instance=basicfsm_Trans_strategy)
def test_basicfsm_trans_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=basicfsm_State_strategy)
@settings(max_examples=50)
def test_basicfsm_state_instantiation(instance):
    assert isinstance(instance, basicfsm_State)



@given(instance=basicfsm_State_strategy)
def test_basicfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basicfsm_Machine_strategy)
@settings(max_examples=50)
def test_basicfsm_machine_instantiation(instance):
    assert isinstance(instance, basicfsm_Machine)



@given(instance=basicfsm_Machine_strategy)
def test_basicfsm_machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=basicfsm_InitialState_strategy)
@settings(max_examples=50)
def test_basicfsm_initialstate_instantiation(instance):
    assert isinstance(instance, basicfsm_InitialState)
