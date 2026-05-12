import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    lts_Transition,
    lts_LTS,
    lts_State,
    lts_FinalState,
    lts_IntermediateState,
    lts_InitialState,
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



def test_lts_transition_is_not_abstract():
    assert not inspect.isabstract(lts_Transition)


def test_lts_transition_constructor_exists():
    assert callable(lts_Transition.__init__)


def test_lts_transition_constructor_args():
    sig = inspect.signature(lts_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_lts_transition_has_label():
    assert hasattr(lts_Transition, "label")
    descriptor = None
    for klass in lts_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_lts_lts_is_not_abstract():
    assert not inspect.isabstract(lts_LTS)


def test_lts_lts_constructor_exists():
    assert callable(lts_LTS.__init__)


def test_lts_lts_constructor_args():
    sig = inspect.signature(lts_LTS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lts_lts_has_name():
    assert hasattr(lts_LTS, "name")
    descriptor = None
    for klass in lts_LTS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lts_state_is_not_abstract():
    assert not inspect.isabstract(lts_State)


def test_lts_state_constructor_exists():
    assert callable(lts_State.__init__)


def test_lts_state_constructor_args():
    sig = inspect.signature(lts_State.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"

def test_lts_state_has_Id():
    assert hasattr(lts_State, "Id")
    descriptor = None
    for klass in lts_State.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)



def test_lts_finalstate_is_not_abstract():
    assert not inspect.isabstract(lts_FinalState)


def test_lts_finalstate_constructor_exists():
    assert callable(lts_FinalState.__init__)


def test_lts_finalstate_constructor_args():
    sig = inspect.signature(lts_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_lts_intermediatestate_is_not_abstract():
    assert not inspect.isabstract(lts_IntermediateState)


def test_lts_intermediatestate_constructor_exists():
    assert callable(lts_IntermediateState.__init__)


def test_lts_intermediatestate_constructor_args():
    sig = inspect.signature(lts_IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_lts_initialstate_is_not_abstract():
    assert not inspect.isabstract(lts_InitialState)


def test_lts_initialstate_constructor_exists():
    assert callable(lts_InitialState.__init__)


def test_lts_initialstate_constructor_args():
    sig = inspect.signature(lts_InitialState.__init__)
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
lts_Transition_strategy = st.builds(
    lts_Transition,
    label=
        safe_text
)
lts_LTS_strategy = st.builds(
    lts_LTS,
    name=
        safe_text
)
lts_State_strategy = st.builds(
    lts_State,
    Id=
        safe_text
)
lts_FinalState_strategy = st.builds(
    lts_FinalState,
)
lts_IntermediateState_strategy = st.builds(
    lts_IntermediateState,
)
lts_InitialState_strategy = st.builds(
    lts_InitialState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=lts_Transition_strategy)
@settings(max_examples=50)
def test_lts_transition_instantiation(instance):
    assert isinstance(instance, lts_Transition)



@given(instance=lts_Transition_strategy)
def test_lts_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=lts_LTS_strategy)
@settings(max_examples=50)
def test_lts_lts_instantiation(instance):
    assert isinstance(instance, lts_LTS)



@given(instance=lts_LTS_strategy)
def test_lts_lts_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=lts_State_strategy)
@settings(max_examples=50)
def test_lts_state_instantiation(instance):
    assert isinstance(instance, lts_State)



@given(instance=lts_State_strategy)
def test_lts_state_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original

@given(instance=lts_FinalState_strategy)
@settings(max_examples=50)
def test_lts_finalstate_instantiation(instance):
    assert isinstance(instance, lts_FinalState)

@given(instance=lts_IntermediateState_strategy)
@settings(max_examples=50)
def test_lts_intermediatestate_instantiation(instance):
    assert isinstance(instance, lts_IntermediateState)

@given(instance=lts_InitialState_strategy)
@settings(max_examples=50)
def test_lts_initialstate_instantiation(instance):
    assert isinstance(instance, lts_InitialState)
