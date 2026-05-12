import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    State,
    fsm::TransientState,
    fsm::SteadyState,
    fsm::SuperState,
    fsm::FSM,
    fsm::eAction,
    fsm::Action,
    SuperState,
    fsm::State,
    fsm::InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "Guard" in params, "Missing parameter 'Guard'"
    assert "Effect" in params, "Missing parameter 'Effect'"

def test_fsm::transition_has_Guard():
    assert hasattr(fsm::Transition, "Guard")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "Guard" in klass.__dict__:
            descriptor = klass.__dict__["Guard"]
            break
    assert isinstance(descriptor, property)

def test_fsm::transition_has_Effect():
    assert hasattr(fsm::Transition, "Effect")
    descriptor = None
    for klass in fsm::Transition.__mro__:
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



def test_fsm::transientstate_is_not_abstract():
    assert not inspect.isabstract(fsm::TransientState)


def test_fsm::transientstate_constructor_exists():
    assert callable(fsm::TransientState.__init__)


def test_fsm::transientstate_constructor_args():
    sig = inspect.signature(fsm::TransientState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::steadystate_is_not_abstract():
    assert not inspect.isabstract(fsm::SteadyState)


def test_fsm::steadystate_constructor_exists():
    assert callable(fsm::SteadyState.__init__)


def test_fsm::steadystate_constructor_args():
    sig = inspect.signature(fsm::SteadyState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::superstate_is_not_abstract():
    assert not inspect.isabstract(fsm::SuperState)


def test_fsm::superstate_constructor_exists():
    assert callable(fsm::SuperState.__init__)


def test_fsm::superstate_constructor_args():
    sig = inspect.signature(fsm::SuperState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm::eaction_is_not_abstract():
    assert not inspect.isabstract(fsm::eAction)


def test_fsm::eaction_constructor_exists():
    assert callable(fsm::eAction.__init__)


def test_fsm::eaction_constructor_args():
    sig = inspect.signature(fsm::eAction.__init__)
    params = list(sig.parameters.keys())
    assert "exitLabel" in params, "Missing parameter 'exitLabel'"

def test_fsm::eaction_has_exitLabel():
    assert hasattr(fsm::eAction, "exitLabel")
    descriptor = None
    for klass in fsm::eAction.__mro__:
        if "exitLabel" in klass.__dict__:
            descriptor = klass.__dict__["exitLabel"]
            break
    assert isinstance(descriptor, property)



def test_fsm::action_is_not_abstract():
    assert not inspect.isabstract(fsm::Action)


def test_fsm::action_constructor_exists():
    assert callable(fsm::Action.__init__)


def test_fsm::action_constructor_args():
    sig = inspect.signature(fsm::Action.__init__)
    params = list(sig.parameters.keys())
    assert "entryLabel" in params, "Missing parameter 'entryLabel'"

def test_fsm::action_has_entryLabel():
    assert hasattr(fsm::Action, "entryLabel")
    descriptor = None
    for klass in fsm::Action.__mro__:
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



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::state_has_name():
    assert hasattr(fsm::State, "name")
    descriptor = None
    for klass in fsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    Guard=
        safe_text,
    Effect=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm::TransientState_strategy = st.builds(
    fsm::TransientState,
)
fsm::SteadyState_strategy = st.builds(
    fsm::SteadyState,
)
fsm::SuperState_strategy = st.builds(
    fsm::SuperState,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)
fsm::eAction_strategy = st.builds(
    fsm::eAction,
    exitLabel=
        safe_text
)
fsm::Action_strategy = st.builds(
    fsm::Action,
    entryLabel=
        safe_text
)
SuperState_strategy = st.builds(
    SuperState,
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_Guard_type(instance):
    assert isinstance(instance.Guard, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_Guard_setter(instance):
    original = instance.Guard
    instance.Guard = original
    assert instance.Guard == original

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_Effect_type(instance):
    assert isinstance(instance.Effect, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_Effect_setter(instance):
    original = instance.Effect
    instance.Effect = original
    assert instance.Effect == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::TransientState_strategy)
@settings(max_examples=50)
def test_fsm::transientstate_instantiation(instance):
    assert isinstance(instance, fsm::TransientState)

@given(instance=fsm::SteadyState_strategy)
@settings(max_examples=50)
def test_fsm::steadystate_instantiation(instance):
    assert isinstance(instance, fsm::SteadyState)

@given(instance=fsm::SuperState_strategy)
@settings(max_examples=50)
def test_fsm::superstate_instantiation(instance):
    assert isinstance(instance, fsm::SuperState)

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::eAction_strategy)
@settings(max_examples=50)
def test_fsm::eaction_instantiation(instance):
    assert isinstance(instance, fsm::eAction)

@given(instance=fsm::eAction_strategy)
def test_fsm::eaction_exitLabel_type(instance):
    assert isinstance(instance.exitLabel, str)


@given(instance=fsm::eAction_strategy)
def test_fsm::eaction_exitLabel_setter(instance):
    original = instance.exitLabel
    instance.exitLabel = original
    assert instance.exitLabel == original

@given(instance=fsm::Action_strategy)
@settings(max_examples=50)
def test_fsm::action_instantiation(instance):
    assert isinstance(instance, fsm::Action)

@given(instance=fsm::Action_strategy)
def test_fsm::action_entryLabel_type(instance):
    assert isinstance(instance.entryLabel, str)


@given(instance=fsm::Action_strategy)
def test_fsm::action_entryLabel_setter(instance):
    original = instance.entryLabel
    instance.entryLabel = original
    assert instance.entryLabel == original

@given(instance=SuperState_strategy)
@settings(max_examples=50)
def test_superstate_instantiation(instance):
    assert isinstance(instance, SuperState)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::State_strategy)
def test_fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::State_strategy)
def test_fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)
