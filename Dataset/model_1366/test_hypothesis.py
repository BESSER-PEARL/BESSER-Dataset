import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HSM::AbstractState,
    HSM::Transition,
    HSM::StateMachine,
    AbstractState,
    HSM::RegularState,
    HSM::InitialState,
    HSM::CompositeState,
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
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::abstractstate_has_name():
    assert hasattr(HSM::AbstractState, "name")
    descriptor = None
    for klass in HSM::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm::transition_is_not_abstract():
    assert not inspect.isabstract(HSM::Transition)


def test_hsm::transition_constructor_exists():
    assert callable(HSM::Transition.__init__)


def test_hsm::transition_constructor_args():
    sig = inspect.signature(HSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hsm::transition_has_label():
    assert hasattr(HSM::Transition, "label")
    descriptor = None
    for klass in HSM::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM::StateMachine)


def test_hsm::statemachine_constructor_exists():
    assert callable(HSM::StateMachine.__init__)


def test_hsm::statemachine_constructor_args():
    sig = inspect.signature(HSM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::statemachine_has_name():
    assert hasattr(HSM::StateMachine, "name")
    descriptor = None
    for klass in HSM::StateMachine.__mro__:
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



def test_hsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(HSM::RegularState)


def test_hsm::regularstate_constructor_exists():
    assert callable(HSM::RegularState.__init__)


def test_hsm::regularstate_constructor_args():
    sig = inspect.signature(HSM::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(HSM::InitialState)


def test_hsm::initialstate_constructor_exists():
    assert callable(HSM::InitialState.__init__)


def test_hsm::initialstate_constructor_args():
    sig = inspect.signature(HSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM::CompositeState)


def test_hsm::compositestate_constructor_exists():
    assert callable(HSM::CompositeState.__init__)


def test_hsm::compositestate_constructor_args():
    sig = inspect.signature(HSM::CompositeState.__init__)
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
HSM::AbstractState_strategy = st.builds(
    HSM::AbstractState,
    name=
        safe_text
)
HSM::Transition_strategy = st.builds(
    HSM::Transition,
    label=
        safe_text
)
HSM::StateMachine_strategy = st.builds(
    HSM::StateMachine,
    name=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
HSM::RegularState_strategy = st.builds(
    HSM::RegularState,
)
HSM::InitialState_strategy = st.builds(
    HSM::InitialState,
)
HSM::CompositeState_strategy = st.builds(
    HSM::CompositeState,
)

@given(instance=HSM::AbstractState_strategy)
@settings(max_examples=50)
def test_hsm::abstractstate_instantiation(instance):
    assert isinstance(instance, HSM::AbstractState)

@given(instance=HSM::AbstractState_strategy)
def test_hsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::AbstractState_strategy)
def test_hsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM::Transition_strategy)
@settings(max_examples=50)
def test_hsm::transition_instantiation(instance):
    assert isinstance(instance, HSM::Transition)

@given(instance=HSM::Transition_strategy)
def test_hsm::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=HSM::Transition_strategy)
def test_hsm::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=HSM::StateMachine_strategy)
@settings(max_examples=50)
def test_hsm::statemachine_instantiation(instance):
    assert isinstance(instance, HSM::StateMachine)

@given(instance=HSM::StateMachine_strategy)
def test_hsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::StateMachine_strategy)
def test_hsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=HSM::RegularState_strategy)
@settings(max_examples=50)
def test_hsm::regularstate_instantiation(instance):
    assert isinstance(instance, HSM::RegularState)

@given(instance=HSM::InitialState_strategy)
@settings(max_examples=50)
def test_hsm::initialstate_instantiation(instance):
    assert isinstance(instance, HSM::InitialState)

@given(instance=HSM::CompositeState_strategy)
@settings(max_examples=50)
def test_hsm::compositestate_instantiation(instance):
    assert isinstance(instance, HSM::CompositeState)
