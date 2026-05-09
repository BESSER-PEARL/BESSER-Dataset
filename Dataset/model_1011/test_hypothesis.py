import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    fsm::StateFinal,
    fsm::StateOff,
    fsm::StateOn,
    fsm::Transition,
    fsm::State,
    fsm::FSM,
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



def test_fsm::statefinal_is_not_abstract():
    assert not inspect.isabstract(fsm::StateFinal)


def test_fsm::statefinal_constructor_exists():
    assert callable(fsm::StateFinal.__init__)


def test_fsm::statefinal_constructor_args():
    sig = inspect.signature(fsm::StateFinal.__init__)
    params = list(sig.parameters.keys())



def test_fsm::stateoff_is_not_abstract():
    assert not inspect.isabstract(fsm::StateOff)


def test_fsm::stateoff_constructor_exists():
    assert callable(fsm::StateOff.__init__)


def test_fsm::stateoff_constructor_args():
    sig = inspect.signature(fsm::StateOff.__init__)
    params = list(sig.parameters.keys())



def test_fsm::stateon_is_not_abstract():
    assert not inspect.isabstract(fsm::StateOn)


def test_fsm::stateon_constructor_exists():
    assert callable(fsm::StateOn.__init__)


def test_fsm::stateon_constructor_args():
    sig = inspect.signature(fsm::StateOn.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::transition_has_name():
    assert hasattr(fsm::Transition, "name")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::fsm_has_name():
    assert hasattr(fsm::FSM, "name")
    descriptor = None
    for klass in fsm::FSM.__mro__:
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
fsm::StateFinal_strategy = st.builds(
    fsm::StateFinal,
)
fsm::StateOff_strategy = st.builds(
    fsm::StateOff,
)
fsm::StateOn_strategy = st.builds(
    fsm::StateOn,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    name=
        safe_text
)
fsm::State_strategy = st.builds(
    fsm::State,
    name=
        safe_text
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm::StateFinal_strategy)
@settings(max_examples=50)
def test_fsm::statefinal_instantiation(instance):
    assert isinstance(instance, fsm::StateFinal)

@given(instance=fsm::StateOff_strategy)
@settings(max_examples=50)
def test_fsm::stateoff_instantiation(instance):
    assert isinstance(instance, fsm::StateOff)

@given(instance=fsm::StateOn_strategy)
@settings(max_examples=50)
def test_fsm::stateon_instantiation(instance):
    assert isinstance(instance, fsm::StateOn)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::FSM_strategy)
def test_fsm::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
