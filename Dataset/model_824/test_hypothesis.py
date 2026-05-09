import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simplefsm::Transition,
    simplefsm::State,
    simplefsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplefsm::transition_is_not_abstract():
    assert not inspect.isabstract(simplefsm::Transition)


def test_simplefsm::transition_constructor_exists():
    assert callable(simplefsm::Transition.__init__)


def test_simplefsm::transition_constructor_args():
    sig = inspect.signature(simplefsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_simplefsm::state_is_not_abstract():
    assert not inspect.isabstract(simplefsm::State)


def test_simplefsm::state_constructor_exists():
    assert callable(simplefsm::State.__init__)


def test_simplefsm::state_constructor_args():
    sig = inspect.signature(simplefsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplefsm::state_has_name():
    assert hasattr(simplefsm::State, "name")
    descriptor = None
    for klass in simplefsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplefsm::fsm_is_not_abstract():
    assert not inspect.isabstract(simplefsm::FSM)


def test_simplefsm::fsm_constructor_exists():
    assert callable(simplefsm::FSM.__init__)


def test_simplefsm::fsm_constructor_args():
    sig = inspect.signature(simplefsm::FSM.__init__)
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
simplefsm::Transition_strategy = st.builds(
    simplefsm::Transition,
)
simplefsm::State_strategy = st.builds(
    simplefsm::State,
    name=
        safe_text
)
simplefsm::FSM_strategy = st.builds(
    simplefsm::FSM,
)

@given(instance=simplefsm::Transition_strategy)
@settings(max_examples=50)
def test_simplefsm::transition_instantiation(instance):
    assert isinstance(instance, simplefsm::Transition)

@given(instance=simplefsm::State_strategy)
@settings(max_examples=50)
def test_simplefsm::state_instantiation(instance):
    assert isinstance(instance, simplefsm::State)

@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simplefsm::State_strategy)
def test_simplefsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simplefsm::FSM_strategy)
@settings(max_examples=50)
def test_simplefsm::fsm_instantiation(instance):
    assert isinstance(instance, simplefsm::FSM)
