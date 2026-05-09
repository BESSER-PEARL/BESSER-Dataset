import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    statemachine::Named,
    AbstractState,
    statemachine::State,
    statemachine::Initial,
    Named,
    statemachine::Transition,
    statemachine::AbstractState,
    statemachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::named_is_not_abstract():
    assert not inspect.isabstract(statemachine::Named)


def test_statemachine::named_constructor_exists():
    assert callable(statemachine::Named.__init__)


def test_statemachine::named_constructor_args():
    sig = inspect.signature(statemachine::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::named_has_name():
    assert hasattr(statemachine::Named, "name")
    descriptor = None
    for klass in statemachine::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(statemachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(statemachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(statemachine::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initial_is_not_abstract():
    assert not inspect.isabstract(statemachine::Initial)


def test_statemachine::initial_constructor_exists():
    assert callable(statemachine::Initial.__init__)


def test_statemachine::initial_constructor_args():
    sig = inspect.signature(statemachine::Initial.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



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
statemachine::Named_strategy = st.builds(
    statemachine::Named,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine::State_strategy = st.builds(
    statemachine::State,
)
statemachine::Initial_strategy = st.builds(
    statemachine::Initial,
)
Named_strategy = st.builds(
    Named,
)
statemachine::Transition_strategy = st.builds(
    statemachine::Transition,
)
statemachine::AbstractState_strategy = st.builds(
    statemachine::AbstractState,
)
statemachine::StateMachine_strategy = st.builds(
    statemachine::StateMachine,
)

@given(instance=statemachine::Named_strategy)
@settings(max_examples=50)
def test_statemachine::named_instantiation(instance):
    assert isinstance(instance, statemachine::Named)

@given(instance=statemachine::Named_strategy)
def test_statemachine::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=statemachine::Named_strategy)
def test_statemachine::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, statemachine::State)

@given(instance=statemachine::Initial_strategy)
@settings(max_examples=50)
def test_statemachine::initial_instantiation(instance):
    assert isinstance(instance, statemachine::Initial)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=statemachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, statemachine::Transition)

@given(instance=statemachine::AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine::abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine::AbstractState)

@given(instance=statemachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, statemachine::StateMachine)
