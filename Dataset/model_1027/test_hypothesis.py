import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    mydsl_IntitialState,
    mydsl_Transition,
    mydsl_State,
    mydsl_FSM,
    mydsl_FinalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_intitialstate_is_not_abstract():
    assert not inspect.isabstract(mydsl_IntitialState)


def test_mydsl_intitialstate_constructor_exists():
    assert callable(mydsl_IntitialState.__init__)


def test_mydsl_intitialstate_constructor_args():
    sig = inspect.signature(mydsl_IntitialState.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_transition_is_not_abstract():
    assert not inspect.isabstract(mydsl_Transition)


def test_mydsl_transition_constructor_exists():
    assert callable(mydsl_Transition.__init__)


def test_mydsl_transition_constructor_args():
    sig = inspect.signature(mydsl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_transition_has_name():
    assert hasattr(mydsl_Transition, "name")
    descriptor = None
    for klass in mydsl_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_state_is_not_abstract():
    assert not inspect.isabstract(mydsl_State)


def test_mydsl_state_constructor_exists():
    assert callable(mydsl_State.__init__)


def test_mydsl_state_constructor_args():
    sig = inspect.signature(mydsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_state_has_name():
    assert hasattr(mydsl_State, "name")
    descriptor = None
    for klass in mydsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_fsm_is_not_abstract():
    assert not inspect.isabstract(mydsl_FSM)


def test_mydsl_fsm_constructor_exists():
    assert callable(mydsl_FSM.__init__)


def test_mydsl_fsm_constructor_args():
    sig = inspect.signature(mydsl_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_fsm_has_name():
    assert hasattr(mydsl_FSM, "name")
    descriptor = None
    for klass in mydsl_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_finalstate_is_not_abstract():
    assert not inspect.isabstract(mydsl_FinalState)


def test_mydsl_finalstate_constructor_exists():
    assert callable(mydsl_FinalState.__init__)


def test_mydsl_finalstate_constructor_args():
    sig = inspect.signature(mydsl_FinalState.__init__)
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
State_strategy = st.builds(
    State,
)
mydsl_IntitialState_strategy = st.builds(
    mydsl_IntitialState,
)
mydsl_Transition_strategy = st.builds(
    mydsl_Transition,
    name=
        safe_text
)
mydsl_State_strategy = st.builds(
    mydsl_State,
    name=
        safe_text
)
mydsl_FSM_strategy = st.builds(
    mydsl_FSM,
    name=
        safe_text
)
mydsl_FinalState_strategy = st.builds(
    mydsl_FinalState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=mydsl_IntitialState_strategy)
@settings(max_examples=50)
def test_mydsl_intitialstate_instantiation(instance):
    assert isinstance(instance, mydsl_IntitialState)

@given(instance=mydsl_Transition_strategy)
@settings(max_examples=50)
def test_mydsl_transition_instantiation(instance):
    assert isinstance(instance, mydsl_Transition)



@given(instance=mydsl_Transition_strategy)
def test_mydsl_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl_State_strategy)
@settings(max_examples=50)
def test_mydsl_state_instantiation(instance):
    assert isinstance(instance, mydsl_State)



@given(instance=mydsl_State_strategy)
def test_mydsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl_FSM_strategy)
@settings(max_examples=50)
def test_mydsl_fsm_instantiation(instance):
    assert isinstance(instance, mydsl_FSM)



@given(instance=mydsl_FSM_strategy)
def test_mydsl_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl_FinalState_strategy)
@settings(max_examples=50)
def test_mydsl_finalstate_instantiation(instance):
    assert isinstance(instance, mydsl_FinalState)
