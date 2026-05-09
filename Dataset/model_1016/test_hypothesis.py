import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractState,
    fsm::InitialState,
    fsm::CompositeState,
    fsm::AbstractState,
    fsm::Transition,
    fsm::StateMachine,
    fsm::Root,
    fsm::RegularState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm::InitialState)


def test_fsm::initialstate_constructor_exists():
    assert callable(fsm::InitialState.__init__)


def test_fsm::initialstate_constructor_args():
    sig = inspect.signature(fsm::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(fsm::CompositeState)


def test_fsm::compositestate_constructor_exists():
    assert callable(fsm::CompositeState.__init__)


def test_fsm::compositestate_constructor_args():
    sig = inspect.signature(fsm::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsm::AbstractState)


def test_fsm::abstractstate_constructor_exists():
    assert callable(fsm::AbstractState.__init__)


def test_fsm::abstractstate_constructor_args():
    sig = inspect.signature(fsm::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::abstractstate_has_name():
    assert hasattr(fsm::AbstractState, "name")
    descriptor = None
    for klass in fsm::AbstractState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_fsm::transition_has_label():
    assert hasattr(fsm::Transition, "label")
    descriptor = None
    for klass in fsm::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::statemachine_has_name():
    assert hasattr(fsm::StateMachine, "name")
    descriptor = None
    for klass in fsm::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::root_is_not_abstract():
    assert not inspect.isabstract(fsm::Root)


def test_fsm::root_constructor_exists():
    assert callable(fsm::Root.__init__)


def test_fsm::root_constructor_args():
    sig = inspect.signature(fsm::Root.__init__)
    params = list(sig.parameters.keys())



def test_fsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(fsm::RegularState)


def test_fsm::regularstate_constructor_exists():
    assert callable(fsm::RegularState.__init__)


def test_fsm::regularstate_constructor_args():
    sig = inspect.signature(fsm::RegularState.__init__)
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
AbstractState_strategy = st.builds(
    AbstractState,
)
fsm::InitialState_strategy = st.builds(
    fsm::InitialState,
)
fsm::CompositeState_strategy = st.builds(
    fsm::CompositeState,
)
fsm::AbstractState_strategy = st.builds(
    fsm::AbstractState,
    name=
        safe_text
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
    label=
        safe_text
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
    name=
        safe_text
)
fsm::Root_strategy = st.builds(
    fsm::Root,
)
fsm::RegularState_strategy = st.builds(
    fsm::RegularState,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=fsm::InitialState_strategy)
@settings(max_examples=50)
def test_fsm::initialstate_instantiation(instance):
    assert isinstance(instance, fsm::InitialState)

@given(instance=fsm::CompositeState_strategy)
@settings(max_examples=50)
def test_fsm::compositestate_instantiation(instance):
    assert isinstance(instance, fsm::CompositeState)

@given(instance=fsm::AbstractState_strategy)
@settings(max_examples=50)
def test_fsm::abstractstate_instantiation(instance):
    assert isinstance(instance, fsm::AbstractState)

@given(instance=fsm::AbstractState_strategy)
def test_fsm::abstractstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::AbstractState_strategy)
def test_fsm::abstractstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::Transition_strategy)
def test_fsm::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=fsm::Transition_strategy)
def test_fsm::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)

@given(instance=fsm::StateMachine_strategy)
def test_fsm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::StateMachine_strategy)
def test_fsm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Root_strategy)
@settings(max_examples=50)
def test_fsm::root_instantiation(instance):
    assert isinstance(instance, fsm::Root)

@given(instance=fsm::RegularState_strategy)
@settings(max_examples=50)
def test_fsm::regularstate_instantiation(instance):
    assert isinstance(instance, fsm::RegularState)
