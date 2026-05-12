import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    statemachine_Transition,
    statemachine_StateMachine,
    State,
    statemachine_Simple,
    statemachine_Final,
    statemachine_Initial,
    statemachine_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"

def test_statemachine_transition_has_Id():
    assert hasattr(statemachine_Transition, "Id")
    descriptor = None
    for klass in statemachine_Transition.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_statemachine_has_name():
    assert hasattr(statemachine_StateMachine, "name")
    descriptor = None
    for klass in statemachine_StateMachine.__mro__:
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



def test_statemachine_simple_is_not_abstract():
    assert not inspect.isabstract(statemachine_Simple)


def test_statemachine_simple_constructor_exists():
    assert callable(statemachine_Simple.__init__)


def test_statemachine_simple_constructor_args():
    sig = inspect.signature(statemachine_Simple.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_final_is_not_abstract():
    assert not inspect.isabstract(statemachine_Final)


def test_statemachine_final_constructor_exists():
    assert callable(statemachine_Final.__init__)


def test_statemachine_final_constructor_args():
    sig = inspect.signature(statemachine_Final.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initial_is_not_abstract():
    assert not inspect.isabstract(statemachine_Initial)


def test_statemachine_initial_constructor_exists():
    assert callable(statemachine_Initial.__init__)


def test_statemachine_initial_constructor_args():
    sig = inspect.signature(statemachine_Initial.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_state_has_name():
    assert hasattr(statemachine_State, "name")
    descriptor = None
    for klass in statemachine_State.__mro__:
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
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
    Id=
        st.integers()
)
statemachine_StateMachine_strategy = st.builds(
    statemachine_StateMachine,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
statemachine_Simple_strategy = st.builds(
    statemachine_Simple,
)
statemachine_Final_strategy = st.builds(
    statemachine_Final,
)
statemachine_Initial_strategy = st.builds(
    statemachine_Initial,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    name=
        safe_text
)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)



@given(instance=statemachine_Transition_strategy)
def test_statemachine_transition_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=statemachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_StateMachine)



@given(instance=statemachine_StateMachine_strategy)
def test_statemachine_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=statemachine_Simple_strategy)
@settings(max_examples=50)
def test_statemachine_simple_instantiation(instance):
    assert isinstance(instance, statemachine_Simple)

@given(instance=statemachine_Final_strategy)
@settings(max_examples=50)
def test_statemachine_final_instantiation(instance):
    assert isinstance(instance, statemachine_Final)

@given(instance=statemachine_Initial_strategy)
@settings(max_examples=50)
def test_statemachine_initial_instantiation(instance):
    assert isinstance(instance, statemachine_Initial)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
