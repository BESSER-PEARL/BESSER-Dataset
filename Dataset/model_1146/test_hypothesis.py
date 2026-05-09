import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hsm::Root,
    AbstractState,
    hsm::RegularState,
    hsm::InitialState,
    hsm::CompositeState,
    hsm::AbstractState,
    hsm::Transition,
    hsm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hsm::root_is_not_abstract():
    assert not inspect.isabstract(hsm::Root)


def test_hsm::root_constructor_exists():
    assert callable(hsm::Root.__init__)


def test_hsm::root_constructor_args():
    sig = inspect.signature(hsm::Root.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(hsm::RegularState)


def test_hsm::regularstate_constructor_exists():
    assert callable(hsm::RegularState.__init__)


def test_hsm::regularstate_constructor_args():
    sig = inspect.signature(hsm::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(hsm::InitialState)


def test_hsm::initialstate_constructor_exists():
    assert callable(hsm::InitialState.__init__)


def test_hsm::initialstate_constructor_args():
    sig = inspect.signature(hsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(hsm::CompositeState)


def test_hsm::compositestate_constructor_exists():
    assert callable(hsm::CompositeState.__init__)


def test_hsm::compositestate_constructor_args():
    sig = inspect.signature(hsm::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(hsm::AbstractState)


def test_hsm::abstractstate_constructor_exists():
    assert callable(hsm::AbstractState.__init__)


def test_hsm::abstractstate_constructor_args():
    sig = inspect.signature(hsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::abstractstate_has_name():
    assert hasattr(hsm::AbstractState, "name")
    descriptor = None
    for klass in hsm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm::transition_is_not_abstract():
    assert not inspect.isabstract(hsm::Transition)


def test_hsm::transition_constructor_exists():
    assert callable(hsm::Transition.__init__)


def test_hsm::transition_constructor_args():
    sig = inspect.signature(hsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hsm::transition_has_label():
    assert hasattr(hsm::Transition, "label")
    descriptor = None
    for klass in hsm::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(hsm::StateMachine)


def test_hsm::statemachine_constructor_exists():
    assert callable(hsm::StateMachine.__init__)


def test_hsm::statemachine_constructor_args():
    sig = inspect.signature(hsm::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::statemachine_has_name():
    assert hasattr(hsm::StateMachine, "name")
    descriptor = None
    for klass in hsm::StateMachine.__mro__:
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
hsm::Root_strategy = st.builds(
    hsm::Root,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
hsm::RegularState_strategy = st.builds(
    hsm::RegularState,
)
hsm::InitialState_strategy = st.builds(
    hsm::InitialState,
)
hsm::CompositeState_strategy = st.builds(
    hsm::CompositeState,
)
hsm::AbstractState_strategy = st.builds(
    hsm::AbstractState,
    name=
        safe_text
)
hsm::Transition_strategy = st.builds(
    hsm::Transition,
    label=
        safe_text
)
hsm::StateMachine_strategy = st.builds(
    hsm::StateMachine,
    name=
        safe_text
)

@given(instance=hsm::Root_strategy)
@settings(max_examples=50)
def test_hsm::root_instantiation(instance):
    assert isinstance(instance, hsm::Root)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=hsm::RegularState_strategy)
@settings(max_examples=50)
def test_hsm::regularstate_instantiation(instance):
    assert isinstance(instance, hsm::RegularState)

@given(instance=hsm::InitialState_strategy)
@settings(max_examples=50)
def test_hsm::initialstate_instantiation(instance):
    assert isinstance(instance, hsm::InitialState)

@given(instance=hsm::CompositeState_strategy)
@settings(max_examples=50)
def test_hsm::compositestate_instantiation(instance):
    assert isinstance(instance, hsm::CompositeState)

@given(instance=hsm::AbstractState_strategy)
@settings(max_examples=50)
def test_hsm::abstractstate_instantiation(instance):
    assert isinstance(instance, hsm::AbstractState)

@given(instance=hsm::AbstractState_strategy)
def test_hsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hsm::AbstractState_strategy)
def test_hsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hsm::Transition_strategy)
@settings(max_examples=50)
def test_hsm::transition_instantiation(instance):
    assert isinstance(instance, hsm::Transition)

@given(instance=hsm::Transition_strategy)
def test_hsm::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=hsm::Transition_strategy)
def test_hsm::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=hsm::StateMachine_strategy)
@settings(max_examples=50)
def test_hsm::statemachine_instantiation(instance):
    assert isinstance(instance, hsm::StateMachine)

@given(instance=hsm::StateMachine_strategy)
def test_hsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hsm::StateMachine_strategy)
def test_hsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
