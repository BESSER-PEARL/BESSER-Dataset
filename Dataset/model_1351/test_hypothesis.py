import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    FiringElement,
    statemachine::StateAction,
    AbstractState,
    statemachine::InitialState,
    statemachine::FinalState,
    statemachine::State,
    statemachine::FiringElement,
    statemachine::Transition,
    statemachine::AbstractState,
    statemachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_firingelement_is_not_abstract():
    assert not inspect.isabstract(FiringElement)


def test_firingelement_constructor_exists():
    assert callable(FiringElement.__init__)


def test_firingelement_constructor_args():
    sig = inspect.signature(FiringElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::stateaction_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateAction)


def test_statemachine::stateaction_constructor_exists():
    assert callable(statemachine::StateAction.__init__)


def test_statemachine::stateaction_constructor_args():
    sig = inspect.signature(statemachine::StateAction.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(statemachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(statemachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(statemachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(statemachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::firingelement_is_not_abstract():
    assert not inspect.isabstract(statemachine::FiringElement)


def test_statemachine::firingelement_constructor_exists():
    assert callable(statemachine::FiringElement.__init__)


def test_statemachine::firingelement_constructor_args():
    sig = inspect.signature(statemachine::FiringElement.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "action" in params, "Missing parameter 'action'"

def test_statemachine::firingelement_has_trigger():
    assert hasattr(statemachine::FiringElement, "trigger")
    descriptor = None
    for klass in statemachine::FiringElement.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::firingelement_has_action():
    assert hasattr(statemachine::FiringElement, "action")
    descriptor = None
    for klass in statemachine::FiringElement.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(statemachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(statemachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(statemachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine::AbstractState)


def test_statemachine::abstractstate_constructor_exists():
    assert callable(statemachine::AbstractState.__init__)


def test_statemachine::abstractstate_constructor_args():
    sig = inspect.signature(statemachine::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::abstractstate_has_name():
    assert hasattr(statemachine::AbstractState, "name")
    descriptor = None
    for klass in statemachine::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(statemachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(statemachine::StateMachine.__init__)
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
FiringElement_strategy = st.builds(
    FiringElement,
)
statemachine::StateAction_strategy = st.builds(
    statemachine::StateAction,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine::InitialState_strategy = st.builds(
    statemachine::InitialState,
)
statemachine::FinalState_strategy = st.builds(
    statemachine::FinalState,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
)
statemachine::FiringElement_strategy = st.builds(
    statemachine::FiringElement,
    trigger=
        safe_text,
    action=
        safe_text
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::AbstractState_strategy = st.builds(
    statemachine::AbstractState,
    name=
        safe_text
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
)

@given(instance=FiringElement_strategy)
@settings(max_examples=50)
def test_firingelement_instantiation(instance):
    assert isinstance(instance, FiringElement)

@given(instance=statemachine::StateAction_strategy)
@settings(max_examples=50)
def test_statemachine::stateaction_instantiation(instance):
    assert isinstance(instance, statemachine::StateAction)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, statemachine::InitialState)

@given(instance=statemachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, statemachine::FinalState)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::FiringElement_strategy)
@settings(max_examples=50)
def test_statemachine::firingelement_instantiation(instance):
    assert isinstance(instance, statemachine::FiringElement)

@given(instance=statemachine::FiringElement_strategy)
def test_statemachine::firingelement_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=statemachine::FiringElement_strategy)
def test_statemachine::firingelement_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=statemachine::FiringElement_strategy)
def test_statemachine::firingelement_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=statemachine::FiringElement_strategy)
def test_statemachine::firingelement_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine::abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine::AbstractState)

@given(instance=statemachine::AbstractState_strategy)
def test_statemachine::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::AbstractState_strategy)
def test_statemachine::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)
