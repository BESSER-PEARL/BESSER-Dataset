import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IDBase,
    dtmc_Label,
    dtmc_Transition,
    dtmc_DTMC,
    dtmc_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idbase_is_not_abstract():
    assert not inspect.isabstract(IDBase)


def test_idbase_constructor_exists():
    assert callable(IDBase.__init__)


def test_idbase_constructor_args():
    sig = inspect.signature(IDBase.__init__)
    params = list(sig.parameters.keys())



def test_dtmc_label_is_not_abstract():
    assert not inspect.isabstract(dtmc_Label)


def test_dtmc_label_constructor_exists():
    assert callable(dtmc_Label.__init__)


def test_dtmc_label_constructor_args():
    sig = inspect.signature(dtmc_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc_label_has_name():
    assert hasattr(dtmc_Label, "name")
    descriptor = None
    for klass in dtmc_Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dtmc_transition_is_not_abstract():
    assert not inspect.isabstract(dtmc_Transition)


def test_dtmc_transition_constructor_exists():
    assert callable(dtmc_Transition.__init__)


def test_dtmc_transition_constructor_args():
    sig = inspect.signature(dtmc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "prob" in params, "Missing parameter 'prob'"

def test_dtmc_transition_has_prob():
    assert hasattr(dtmc_Transition, "prob")
    descriptor = None
    for klass in dtmc_Transition.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)



def test_dtmc_dtmc_is_not_abstract():
    assert not inspect.isabstract(dtmc_DTMC)


def test_dtmc_dtmc_constructor_exists():
    assert callable(dtmc_DTMC.__init__)


def test_dtmc_dtmc_constructor_args():
    sig = inspect.signature(dtmc_DTMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc_dtmc_has_name():
    assert hasattr(dtmc_DTMC, "name")
    descriptor = None
    for klass in dtmc_DTMC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dtmc_state_is_not_abstract():
    assert not inspect.isabstract(dtmc_State)


def test_dtmc_state_constructor_exists():
    assert callable(dtmc_State.__init__)


def test_dtmc_state_constructor_args():
    sig = inspect.signature(dtmc_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc_state_has_name():
    assert hasattr(dtmc_State, "name")
    descriptor = None
    for klass in dtmc_State.__mro__:
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
IDBase_strategy = st.builds(
    IDBase,
)
dtmc_Label_strategy = st.builds(
    dtmc_Label,
    name=
        safe_text
)
dtmc_Transition_strategy = st.builds(
    dtmc_Transition,
    prob=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dtmc_DTMC_strategy = st.builds(
    dtmc_DTMC,
    name=
        safe_text
)
dtmc_State_strategy = st.builds(
    dtmc_State,
    name=
        safe_text
)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=dtmc_Label_strategy)
@settings(max_examples=50)
def test_dtmc_label_instantiation(instance):
    assert isinstance(instance, dtmc_Label)



@given(instance=dtmc_Label_strategy)
def test_dtmc_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dtmc_Transition_strategy)
@settings(max_examples=50)
def test_dtmc_transition_instantiation(instance):
    assert isinstance(instance, dtmc_Transition)



@given(instance=dtmc_Transition_strategy)
def test_dtmc_transition_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original

@given(instance=dtmc_DTMC_strategy)
@settings(max_examples=50)
def test_dtmc_dtmc_instantiation(instance):
    assert isinstance(instance, dtmc_DTMC)



@given(instance=dtmc_DTMC_strategy)
def test_dtmc_dtmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dtmc_State_strategy)
@settings(max_examples=50)
def test_dtmc_state_instantiation(instance):
    assert isinstance(instance, dtmc_State)



@given(instance=dtmc_State_strategy)
def test_dtmc_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
