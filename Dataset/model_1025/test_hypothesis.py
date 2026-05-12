import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    nicoLang_State,
    nicoLang_Transition,
    State,
    nicoLang_FinalState,
    nicoLang_InitState,
    nicoLang_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nicolang_state_is_not_abstract():
    assert not inspect.isabstract(nicoLang_State)


def test_nicolang_state_constructor_exists():
    assert callable(nicoLang_State.__init__)


def test_nicolang_state_constructor_args():
    sig = inspect.signature(nicoLang_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nicolang_state_has_name():
    assert hasattr(nicoLang_State, "name")
    descriptor = None
    for klass in nicoLang_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nicolang_transition_is_not_abstract():
    assert not inspect.isabstract(nicoLang_Transition)


def test_nicolang_transition_constructor_exists():
    assert callable(nicoLang_Transition.__init__)


def test_nicolang_transition_constructor_args():
    sig = inspect.signature(nicoLang_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_nicolang_transition_has_trigger():
    assert hasattr(nicoLang_Transition, "trigger")
    descriptor = None
    for klass in nicoLang_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_nicolang_transition_has_name():
    assert hasattr(nicoLang_Transition, "name")
    descriptor = None
    for klass in nicoLang_Transition.__mro__:
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



def test_nicolang_finalstate_is_not_abstract():
    assert not inspect.isabstract(nicoLang_FinalState)


def test_nicolang_finalstate_constructor_exists():
    assert callable(nicoLang_FinalState.__init__)


def test_nicolang_finalstate_constructor_args():
    sig = inspect.signature(nicoLang_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_nicolang_initstate_is_not_abstract():
    assert not inspect.isabstract(nicoLang_InitState)


def test_nicolang_initstate_constructor_exists():
    assert callable(nicoLang_InitState.__init__)


def test_nicolang_initstate_constructor_args():
    sig = inspect.signature(nicoLang_InitState.__init__)
    params = list(sig.parameters.keys())



def test_nicolang_fsm_is_not_abstract():
    assert not inspect.isabstract(nicoLang_FSM)


def test_nicolang_fsm_constructor_exists():
    assert callable(nicoLang_FSM.__init__)


def test_nicolang_fsm_constructor_args():
    sig = inspect.signature(nicoLang_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nicolang_fsm_has_name():
    assert hasattr(nicoLang_FSM, "name")
    descriptor = None
    for klass in nicoLang_FSM.__mro__:
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
nicoLang_State_strategy = st.builds(
    nicoLang_State,
    name=
        safe_text
)
nicoLang_Transition_strategy = st.builds(
    nicoLang_Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
nicoLang_FinalState_strategy = st.builds(
    nicoLang_FinalState,
)
nicoLang_InitState_strategy = st.builds(
    nicoLang_InitState,
)
nicoLang_FSM_strategy = st.builds(
    nicoLang_FSM,
    name=
        safe_text
)

@given(instance=nicoLang_State_strategy)
@settings(max_examples=50)
def test_nicolang_state_instantiation(instance):
    assert isinstance(instance, nicoLang_State)



@given(instance=nicoLang_State_strategy)
def test_nicolang_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nicoLang_Transition_strategy)
@settings(max_examples=50)
def test_nicolang_transition_instantiation(instance):
    assert isinstance(instance, nicoLang_Transition)



@given(instance=nicoLang_Transition_strategy)
def test_nicolang_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=nicoLang_Transition_strategy)
def test_nicolang_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=nicoLang_FinalState_strategy)
@settings(max_examples=50)
def test_nicolang_finalstate_instantiation(instance):
    assert isinstance(instance, nicoLang_FinalState)

@given(instance=nicoLang_InitState_strategy)
@settings(max_examples=50)
def test_nicolang_initstate_instantiation(instance):
    assert isinstance(instance, nicoLang_InitState)

@given(instance=nicoLang_FSM_strategy)
@settings(max_examples=50)
def test_nicolang_fsm_instantiation(instance):
    assert isinstance(instance, nicoLang_FSM)



@given(instance=nicoLang_FSM_strategy)
def test_nicolang_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
