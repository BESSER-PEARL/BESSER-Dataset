import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    FSM_EndState,
    FSM_State,
    FSM_StartState,
    FSM_Transition,
    FSM_AbstractState,
    FSM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_endstate_is_not_abstract():
    assert not inspect.isabstract(FSM_EndState)


def test_fsm_endstate_constructor_exists():
    assert callable(FSM_EndState.__init__)


def test_fsm_endstate_constructor_args():
    sig = inspect.signature(FSM_EndState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(FSM_State)


def test_fsm_state_constructor_exists():
    assert callable(FSM_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(FSM_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_startstate_is_not_abstract():
    assert not inspect.isabstract(FSM_StartState)


def test_fsm_startstate_constructor_exists():
    assert callable(FSM_StartState.__init__)


def test_fsm_startstate_constructor_args():
    sig = inspect.signature(FSM_StartState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(FSM_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(FSM_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(FSM_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm_abstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM_AbstractState)


def test_fsm_abstractstate_constructor_exists():
    assert callable(FSM_AbstractState.__init__)


def test_fsm_abstractstate_constructor_args():
    sig = inspect.signature(FSM_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "envs" in params, "Missing parameter 'envs'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_abstractstate_has_envs():
    assert hasattr(FSM_AbstractState, "envs")
    descriptor = None
    for klass in FSM_AbstractState.__mro__:
        if "envs" in klass.__dict__:
            descriptor = klass.__dict__["envs"]
            break
    assert isinstance(descriptor, property)

def test_fsm_abstractstate_has_name():
    assert hasattr(FSM_AbstractState, "name")
    descriptor = None
    for klass in FSM_AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM_StateMachine)


def test_fsm_statemachine_constructor_exists():
    assert callable(FSM_StateMachine.__init__)


def test_fsm_statemachine_constructor_args():
    sig = inspect.signature(FSM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_fsm_statemachine_has_code():
    assert hasattr(FSM_StateMachine, "code")
    descriptor = None
    for klass in FSM_StateMachine.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
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
AbstractState_strategy = st.builds(
    AbstractState,
)
FSM_EndState_strategy = st.builds(
    FSM_EndState,
)
FSM_State_strategy = st.builds(
    FSM_State,
)
FSM_StartState_strategy = st.builds(
    FSM_StartState,
)
FSM_Transition_strategy = st.builds(
    FSM_Transition,
)
FSM_AbstractState_strategy = st.builds(
    FSM_AbstractState,
    envs=
        safe_text,
    name=
        safe_text
)
FSM_StateMachine_strategy = st.builds(
    FSM_StateMachine,
    code=
        safe_text
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=FSM_EndState_strategy)
@settings(max_examples=50)
def test_fsm_endstate_instantiation(instance):
    assert isinstance(instance, FSM_EndState)

@given(instance=FSM_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, FSM_State)

@given(instance=FSM_StartState_strategy)
@settings(max_examples=50)
def test_fsm_startstate_instantiation(instance):
    assert isinstance(instance, FSM_StartState)

@given(instance=FSM_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, FSM_Transition)

@given(instance=FSM_AbstractState_strategy)
@settings(max_examples=50)
def test_fsm_abstractstate_instantiation(instance):
    assert isinstance(instance, FSM_AbstractState)



@given(instance=FSM_AbstractState_strategy)
def test_fsm_abstractstate_envs_setter(instance):
    original = instance.envs
    instance.envs = original
    assert instance.envs == original



@given(instance=FSM_AbstractState_strategy)
def test_fsm_abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM_StateMachine_strategy)
@settings(max_examples=50)
def test_fsm_statemachine_instantiation(instance):
    assert isinstance(instance, FSM_StateMachine)



@given(instance=FSM_StateMachine_strategy)
def test_fsm_statemachine_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original
