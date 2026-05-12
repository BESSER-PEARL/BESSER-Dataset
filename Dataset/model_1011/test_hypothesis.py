import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    fsm_StateOff,
    fsm_StateFinal,
    fsm_StateOn,
    fsm_Transition,
    fsm_State,
    fsm_FSM,
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



def test_fsm_stateoff_is_not_abstract():
    assert not inspect.isabstract(fsm_StateOff)


def test_fsm_stateoff_constructor_exists():
    assert callable(fsm_StateOff.__init__)


def test_fsm_stateoff_constructor_args():
    sig = inspect.signature(fsm_StateOff.__init__)
    params = list(sig.parameters.keys())



def test_fsm_statefinal_is_not_abstract():
    assert not inspect.isabstract(fsm_StateFinal)


def test_fsm_statefinal_constructor_exists():
    assert callable(fsm_StateFinal.__init__)


def test_fsm_statefinal_constructor_args():
    sig = inspect.signature(fsm_StateFinal.__init__)
    params = list(sig.parameters.keys())



def test_fsm_stateon_is_not_abstract():
    assert not inspect.isabstract(fsm_StateOn)


def test_fsm_stateon_constructor_exists():
    assert callable(fsm_StateOn.__init__)


def test_fsm_stateon_constructor_args():
    sig = inspect.signature(fsm_StateOn.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_transition_has_name():
    assert hasattr(fsm_Transition, "name")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_state_has_name():
    assert hasattr(fsm_State, "name")
    descriptor = None
    for klass in fsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_fsm_has_name():
    assert hasattr(fsm_FSM, "name")
    descriptor = None
    for klass in fsm_FSM.__mro__:
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
State_strategy = st.builds(
    State,
)
fsm_StateOff_strategy = st.builds(
    fsm_StateOff,
)
fsm_StateFinal_strategy = st.builds(
    fsm_StateFinal,
)
fsm_StateOn_strategy = st.builds(
    fsm_StateOn,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    name=
        safe_text
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_StateOff_strategy)
@settings(max_examples=50)
def test_fsm_stateoff_instantiation(instance):
    assert isinstance(instance, fsm_StateOff)

@given(instance=fsm_StateFinal_strategy)
@settings(max_examples=50)
def test_fsm_statefinal_instantiation(instance):
    assert isinstance(instance, fsm_StateFinal)

@given(instance=fsm_StateOn_strategy)
@settings(max_examples=50)
def test_fsm_stateon_instantiation(instance):
    assert isinstance(instance, fsm_StateOn)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fsm_FSM)



@given(instance=fsm_FSM_strategy)
def test_fsm_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
