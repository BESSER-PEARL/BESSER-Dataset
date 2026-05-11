import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    lts::Transition,
    lts::LTS,
    lts::State,
    lts::FinalState,
    lts::IntermediateState,
    lts::InitialState,
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



def test_lts::transition_is_not_abstract():
    assert not inspect.isabstract(lts::Transition)


def test_lts::transition_constructor_exists():
    assert callable(lts::Transition.__init__)


def test_lts::transition_constructor_args():
    sig = inspect.signature(lts::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_lts::transition_has_label():
    assert hasattr(lts::Transition, "label")
    descriptor = None
    for klass in lts::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_lts::lts_is_not_abstract():
    assert not inspect.isabstract(lts::LTS)


def test_lts::lts_constructor_exists():
    assert callable(lts::LTS.__init__)


def test_lts::lts_constructor_args():
    sig = inspect.signature(lts::LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts::lts_has_name():
    assert hasattr(lts::LTS, "name")
    descriptor = None
    for klass in lts::LTS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts::state_is_not_abstract():
    assert not inspect.isabstract(lts::State)


def test_lts::state_constructor_exists():
    assert callable(lts::State.__init__)


def test_lts::state_constructor_args():
    sig = inspect.signature(lts::State.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"

def test_lts::state_has_Id():
    assert hasattr(lts::State, "Id")
    descriptor = None
    for klass in lts::State.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_lts::finalstate_is_not_abstract():
    assert not inspect.isabstract(lts::FinalState)


def test_lts::finalstate_constructor_exists():
    assert callable(lts::FinalState.__init__)


def test_lts::finalstate_constructor_args():
    sig = inspect.signature(lts::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_lts::intermediatestate_is_not_abstract():
    assert not inspect.isabstract(lts::IntermediateState)


def test_lts::intermediatestate_constructor_exists():
    assert callable(lts::IntermediateState.__init__)


def test_lts::intermediatestate_constructor_args():
    sig = inspect.signature(lts::IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_lts::initialstate_is_not_abstract():
    assert not inspect.isabstract(lts::InitialState)


def test_lts::initialstate_constructor_exists():
    assert callable(lts::InitialState.__init__)


def test_lts::initialstate_constructor_args():
    sig = inspect.signature(lts::InitialState.__init__)
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
State_strategy = st.builds(
    State,
)
lts::Transition_strategy = st.builds(
    lts::Transition,
    label=
        safe_text
)
lts::LTS_strategy = st.builds(
    lts::LTS,
    name=
        safe_text
)
lts::State_strategy = st.builds(
    lts::State,
    Id=
        safe_text
)
lts::FinalState_strategy = st.builds(
    lts::FinalState,
)
lts::IntermediateState_strategy = st.builds(
    lts::IntermediateState,
)
lts::InitialState_strategy = st.builds(
    lts::InitialState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=lts::Transition_strategy)
@settings(max_examples=50)
def test_lts::transition_instantiation(instance):
    assert isinstance(instance, lts::Transition)

@given(instance=lts::Transition_strategy)
def test_lts::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=lts::Transition_strategy)
def test_lts::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=lts::LTS_strategy)
@settings(max_examples=50)
def test_lts::lts_instantiation(instance):
    assert isinstance(instance, lts::LTS)

@given(instance=lts::LTS_strategy)
def test_lts::lts_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lts::LTS_strategy)
def test_lts::lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts::State_strategy)
@settings(max_examples=50)
def test_lts::state_instantiation(instance):
    assert isinstance(instance, lts::State)

@given(instance=lts::State_strategy)
def test_lts::state_Id_type(instance):
    assert isinstance(instance.Id, str)


@given(instance=lts::State_strategy)
def test_lts::state_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=lts::FinalState_strategy)
@settings(max_examples=50)
def test_lts::finalstate_instantiation(instance):
    assert isinstance(instance, lts::FinalState)

@given(instance=lts::IntermediateState_strategy)
@settings(max_examples=50)
def test_lts::intermediatestate_instantiation(instance):
    assert isinstance(instance, lts::IntermediateState)

@given(instance=lts::InitialState_strategy)
@settings(max_examples=50)
def test_lts::initialstate_instantiation(instance):
    assert isinstance(instance, lts::InitialState)
