import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HSM::AbstractState,
    HSM::HSM::RegularState,
    HSM::HSM::InitialState,
    HSM::HSM::CompositeState,
    HSM::HSM::AbstractState,
    HSM::HSM::Transition,
    HSM::HSM::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(HSM::AbstractState)


def test_hsm::abstractstate_constructor_exists():
    assert callable(HSM::AbstractState.__init__)


def test_hsm::abstractstate_constructor_args():
    sig = inspect.signature(HSM::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::hsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::RegularState)


def test_hsm::hsm::regularstate_constructor_exists():
    assert callable(HSM::HSM::RegularState.__init__)


def test_hsm::hsm::regularstate_constructor_args():
    sig = inspect.signature(HSM::HSM::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::hsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::InitialState)


def test_hsm::hsm::initialstate_constructor_exists():
    assert callable(HSM::HSM::InitialState.__init__)


def test_hsm::hsm::initialstate_constructor_args():
    sig = inspect.signature(HSM::HSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::hsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::CompositeState)


def test_hsm::hsm::compositestate_constructor_exists():
    assert callable(HSM::HSM::CompositeState.__init__)


def test_hsm::hsm::compositestate_constructor_args():
    sig = inspect.signature(HSM::HSM::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::hsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::AbstractState)


def test_hsm::hsm::abstractstate_constructor_exists():
    assert callable(HSM::HSM::AbstractState.__init__)


def test_hsm::hsm::abstractstate_constructor_args():
    sig = inspect.signature(HSM::HSM::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::hsm::abstractstate_has_name():
    assert hasattr(HSM::HSM::AbstractState, "name")
    descriptor = None
    for klass in HSM::HSM::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm::hsm::transition_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::Transition)


def test_hsm::hsm::transition_constructor_exists():
    assert callable(HSM::HSM::Transition.__init__)


def test_hsm::hsm::transition_constructor_args():
    sig = inspect.signature(HSM::HSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hsm::hsm::transition_has_label():
    assert hasattr(HSM::HSM::Transition, "label")
    descriptor = None
    for klass in HSM::HSM::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hsm::hsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM::HSM::StateMachine)


def test_hsm::hsm::statemachine_constructor_exists():
    assert callable(HSM::HSM::StateMachine.__init__)


def test_hsm::hsm::statemachine_constructor_args():
    sig = inspect.signature(HSM::HSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::hsm::statemachine_has_name():
    assert hasattr(HSM::HSM::StateMachine, "name")
    descriptor = None
    for klass in HSM::HSM::StateMachine.__mro__:
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
HSM::AbstractState_strategy = st.builds(
    HSM::AbstractState,
)
HSM::HSM::RegularState_strategy = st.builds(
    HSM::HSM::RegularState,
)
HSM::HSM::InitialState_strategy = st.builds(
    HSM::HSM::InitialState,
)
HSM::HSM::CompositeState_strategy = st.builds(
    HSM::HSM::CompositeState,
)
HSM::HSM::AbstractState_strategy = st.builds(
    HSM::HSM::AbstractState,
    name=
        safe_text
)
HSM::HSM::Transition_strategy = st.builds(
    HSM::HSM::Transition,
    label=
        safe_text
)
HSM::HSM::StateMachine_strategy = st.builds(
    HSM::HSM::StateMachine,
    name=
        safe_text
)

@given(instance=HSM::AbstractState_strategy)
@settings(max_examples=50)
def test_hsm::abstractstate_instantiation(instance):
    assert isinstance(instance, HSM::AbstractState)

@given(instance=HSM::HSM::RegularState_strategy)
@settings(max_examples=50)
def test_hsm::hsm::regularstate_instantiation(instance):
    assert isinstance(instance, HSM::HSM::RegularState)

@given(instance=HSM::HSM::InitialState_strategy)
@settings(max_examples=50)
def test_hsm::hsm::initialstate_instantiation(instance):
    assert isinstance(instance, HSM::HSM::InitialState)

@given(instance=HSM::HSM::CompositeState_strategy)
@settings(max_examples=50)
def test_hsm::hsm::compositestate_instantiation(instance):
    assert isinstance(instance, HSM::HSM::CompositeState)

@given(instance=HSM::HSM::AbstractState_strategy)
@settings(max_examples=50)
def test_hsm::hsm::abstractstate_instantiation(instance):
    assert isinstance(instance, HSM::HSM::AbstractState)

@given(instance=HSM::HSM::AbstractState_strategy)
def test_hsm::hsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::HSM::AbstractState_strategy)
def test_hsm::hsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM::HSM::Transition_strategy)
@settings(max_examples=50)
def test_hsm::hsm::transition_instantiation(instance):
    assert isinstance(instance, HSM::HSM::Transition)

@given(instance=HSM::HSM::Transition_strategy)
def test_hsm::hsm::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=HSM::HSM::Transition_strategy)
def test_hsm::hsm::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=HSM::HSM::StateMachine_strategy)
@settings(max_examples=50)
def test_hsm::hsm::statemachine_instantiation(instance):
    assert isinstance(instance, HSM::HSM::StateMachine)

@given(instance=HSM::HSM::StateMachine_strategy)
def test_hsm::hsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::HSM::StateMachine_strategy)
def test_hsm::hsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
