import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_FSM,
    fsm_SuperState,
    fsm_Transition,
    State,
    fsm_TransientState,
    fsm_SteadyState,
    fsm_eAction,
    fsm_Action,
    SuperState,
    fsm_State,
    fsm_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm_superstate_is_not_abstract():
    assert not inspect.isabstract(fsm_SuperState)


def test_fsm_superstate_constructor_exists():
    assert callable(fsm_SuperState.__init__)


def test_fsm_superstate_constructor_args():
    sig = inspect.signature(fsm_SuperState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Guard" in params, "Missing parameter 'Guard'"
    assert "Effect" in params, "Missing parameter 'Effect'"

def test_fsm_transition_has_Guard():
    assert hasattr(fsm_Transition, "Guard")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "Guard" in klass.__dict__:
            descriptor = klass.__dict__["Guard"]
            break
    assert isinstance(descriptor, property)

def test_fsm_transition_has_Effect():
    assert hasattr(fsm_Transition, "Effect")
    descriptor = None
    for klass in fsm_Transition.__mro__:
        if "Effect" in klass.__dict__:
            descriptor = klass.__dict__["Effect"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_transientstate_is_not_abstract():
    assert not inspect.isabstract(fsm_TransientState)


def test_fsm_transientstate_constructor_exists():
    assert callable(fsm_TransientState.__init__)


def test_fsm_transientstate_constructor_args():
    sig = inspect.signature(fsm_TransientState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_steadystate_is_not_abstract():
    assert not inspect.isabstract(fsm_SteadyState)


def test_fsm_steadystate_constructor_exists():
    assert callable(fsm_SteadyState.__init__)


def test_fsm_steadystate_constructor_args():
    sig = inspect.signature(fsm_SteadyState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_eaction_is_not_abstract():
    assert not inspect.isabstract(fsm_eAction)


def test_fsm_eaction_constructor_exists():
    assert callable(fsm_eAction.__init__)


def test_fsm_eaction_constructor_args():
    sig = inspect.signature(fsm_eAction.__init__)
    params = list(sig.parameters.keys())
    assert "exitLabel" in params, "Missing parameter 'exitLabel'"

def test_fsm_eaction_has_exitLabel():
    assert hasattr(fsm_eAction, "exitLabel")
    descriptor = None
    for klass in fsm_eAction.__mro__:
        if "exitLabel" in klass.__dict__:
            descriptor = klass.__dict__["exitLabel"]
            break
    assert isinstance(descriptor, property)



def test_fsm_action_is_not_abstract():
    assert not inspect.isabstract(fsm_Action)


def test_fsm_action_constructor_exists():
    assert callable(fsm_Action.__init__)


def test_fsm_action_constructor_args():
    sig = inspect.signature(fsm_Action.__init__)
    params = list(sig.parameters.keys())
    assert "entryLabel" in params, "Missing parameter 'entryLabel'"

def test_fsm_action_has_entryLabel():
    assert hasattr(fsm_Action, "entryLabel")
    descriptor = None
    for klass in fsm_Action.__mro__:
        if "entryLabel" in klass.__dict__:
            descriptor = klass.__dict__["entryLabel"]
            break
    assert isinstance(descriptor, property)



def test_superstate_is_not_abstract():
    assert not inspect.isabstract(SuperState)


def test_superstate_constructor_exists():
    assert callable(SuperState.__init__)


def test_superstate_constructor_args():
    sig = inspect.signature(SuperState.__init__)
    params = list(sig.parameters.keys())



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



def test_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_InitialState)


def test_fsm_initialstate_constructor_exists():
    assert callable(fsm_InitialState.__init__)


def test_fsm_initialstate_constructor_args():
    sig = inspect.signature(fsm_InitialState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_initialstate_has_name():
    assert hasattr(fsm_InitialState, "name")
    descriptor = None
    for klass in fsm_InitialState.__mro__:
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
fsm_FSM_strategy = st.builds(
    fsm_FSM,
)
fsm_SuperState_strategy = st.builds(
    fsm_SuperState,
)
fsm_Transition_strategy = st.builds(
    fsm_Transition,
    Guard=
        safe_text,
    Effect=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm_TransientState_strategy = st.builds(
    fsm_TransientState,
)
fsm_SteadyState_strategy = st.builds(
    fsm_SteadyState,
)
fsm_eAction_strategy = st.builds(
    fsm_eAction,
    exitLabel=
        safe_text
)
fsm_Action_strategy = st.builds(
    fsm_Action,
    entryLabel=
        safe_text
)
SuperState_strategy = st.builds(
    SuperState,
)
fsm_State_strategy = st.builds(
    fsm_State,
    name=
        safe_text
)
fsm_InitialState_strategy = st.builds(
    fsm_InitialState,
    name=
        safe_text
)

@given(instance=fsm_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fsm_FSM)

@given(instance=fsm_SuperState_strategy)
@settings(max_examples=50)
def test_fsm_superstate_instantiation(instance):
    assert isinstance(instance, fsm_SuperState)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_Guard_setter(instance):
    original = instance.Guard
    instance.Guard = original
    assert instance.Guard == original



@given(instance=fsm_Transition_strategy)
def test_fsm_transition_Effect_setter(instance):
    original = instance.Effect
    instance.Effect = original
    assert instance.Effect == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_TransientState_strategy)
@settings(max_examples=50)
def test_fsm_transientstate_instantiation(instance):
    assert isinstance(instance, fsm_TransientState)

@given(instance=fsm_SteadyState_strategy)
@settings(max_examples=50)
def test_fsm_steadystate_instantiation(instance):
    assert isinstance(instance, fsm_SteadyState)

@given(instance=fsm_eAction_strategy)
@settings(max_examples=50)
def test_fsm_eaction_instantiation(instance):
    assert isinstance(instance, fsm_eAction)



@given(instance=fsm_eAction_strategy)
def test_fsm_eaction_exitLabel_setter(instance):
    original = instance.exitLabel
    instance.exitLabel = original
    assert instance.exitLabel == original

@given(instance=fsm_Action_strategy)
@settings(max_examples=50)
def test_fsm_action_instantiation(instance):
    assert isinstance(instance, fsm_Action)



@given(instance=fsm_Action_strategy)
def test_fsm_action_entryLabel_setter(instance):
    original = instance.entryLabel
    instance.entryLabel = original
    assert instance.entryLabel == original

@given(instance=SuperState_strategy)
@settings(max_examples=50)
def test_superstate_instantiation(instance):
    assert isinstance(instance, SuperState)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)



@given(instance=fsm_State_strategy)
def test_fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_InitialState)



@given(instance=fsm_InitialState_strategy)
def test_fsm_initialstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
