import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FSM::Transition,
    FSM::AbstractState,
    FSM::StateMachine,
    AbstractState,
    FSM::EndState,
    FSM::State,
    FSM::StartState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(FSM::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(FSM::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(FSM::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(FSM::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(FSM::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(FSM::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "envs" in params, "Missing parameter 'envs'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::abstractstate_has_envs():
    assert hasattr(FSM::AbstractState, "envs")
    descriptor = None
    for klass in FSM::AbstractState.__mro__:
        if "envs" in klass.__dict__:
            descriptor = klass.__dict__["envs"]
            break
    assert isinstance(descriptor, property)

def test_fsm::abstractstate_has_name():
    assert hasattr(FSM::AbstractState, "name")
    descriptor = None
    for klass in FSM::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(FSM::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(FSM::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(FSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"

def test_fsm::statemachine_has_code():
    assert hasattr(FSM::StateMachine, "code")
    descriptor = None
    for klass in FSM::StateMachine.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::endstate_is_not_abstract():
    assert not inspect.isabstract(FSM::EndState)


def test_fsm::endstate_constructor_exists():
    assert callable(FSM::EndState.__init__)


def test_fsm::endstate_constructor_args():
    sig = inspect.signature(FSM::EndState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(FSM::State)


def test_fsm::state_constructor_exists():
    assert callable(FSM::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(FSM::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::startstate_is_not_abstract():
    assert not inspect.isabstract(FSM::StartState)


def test_fsm::startstate_constructor_exists():
    assert callable(FSM::StartState.__init__)


def test_fsm::startstate_constructor_args():
    sig = inspect.signature(FSM::StartState.__init__)
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
FSM::Transition_strategy = st.builds(
    FSM::Transition,
)
FSM::AbstractState_strategy = st.builds(
    FSM::AbstractState,
    envs=
        safe_text,
    name=
        safe_text
)
FSM::StateMachine_strategy = st.builds(
    FSM::StateMachine,
    code=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
FSM::EndState_strategy = st.builds(
    FSM::EndState,
)
FSM::State_strategy = st.builds(
    FSM::State,
)
FSM::StartState_strategy = st.builds(
    FSM::StartState,
)

@given(instance=FSM::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, FSM::Transition)

@given(instance=FSM::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, FSM::AbstractState)

@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_envs_type(instance):
    assert isinstance(instance.envs, str)


@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_envs_setter(instance):
    original = instance.envs
    instance.envs = original
    assert instance.envs == original

@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FSM::AbstractState_strategy)
def test_fsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSM::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, FSM::StateMachine)

@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=FSM::StateMachine_strategy)
def test_fsm::statemachine_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=FSM::EndState_strategy)
@settings(max_examples=50)
def test_fsm::endstate_instantiation(instance):
    assert isinstance(instance, FSM::EndState)

@given(instance=FSM::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, FSM::State)

@given(instance=FSM::StartState_strategy)
@settings(max_examples=50)
def test_fsm::startstate_instantiation(instance):
    assert isinstance(instance, FSM::StartState)
