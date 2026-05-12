import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IDBase,
    ctmc_Label,
    ctmc_Transition,
    ctmc_State,
    ctmc_CTMC,
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



def test_ctmc_label_is_not_abstract():
    assert not inspect.isabstract(ctmc_Label)


def test_ctmc_label_constructor_exists():
    assert callable(ctmc_Label.__init__)


def test_ctmc_label_constructor_args():
    sig = inspect.signature(ctmc_Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ctmc_label_has_name():
    assert hasattr(ctmc_Label, "name")
    descriptor = None
    for klass in ctmc_Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ctmc_transition_is_not_abstract():
    assert not inspect.isabstract(ctmc_Transition)


def test_ctmc_transition_constructor_exists():
    assert callable(ctmc_Transition.__init__)


def test_ctmc_transition_constructor_args():
    sig = inspect.signature(ctmc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "prob" in params, "Missing parameter 'prob'"
    assert "rate" in params, "Missing parameter 'rate'"

def test_ctmc_transition_has_prob():
    assert hasattr(ctmc_Transition, "prob")
    descriptor = None
    for klass in ctmc_Transition.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)

def test_ctmc_transition_has_rate():
    assert hasattr(ctmc_Transition, "rate")
    descriptor = None
    for klass in ctmc_Transition.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)



def test_ctmc_state_is_not_abstract():
    assert not inspect.isabstract(ctmc_State)


def test_ctmc_state_constructor_exists():
    assert callable(ctmc_State.__init__)


def test_ctmc_state_constructor_args():
    sig = inspect.signature(ctmc_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "exitRate" in params, "Missing parameter 'exitRate'"

def test_ctmc_state_has_name():
    assert hasattr(ctmc_State, "name")
    descriptor = None
    for klass in ctmc_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ctmc_state_has_exitRate():
    assert hasattr(ctmc_State, "exitRate")
    descriptor = None
    for klass in ctmc_State.__mro__:
        if "exitRate" in klass.__dict__:
            descriptor = klass.__dict__["exitRate"]
            break
    assert isinstance(descriptor, property)



def test_ctmc_ctmc_is_not_abstract():
    assert not inspect.isabstract(ctmc_CTMC)


def test_ctmc_ctmc_constructor_exists():
    assert callable(ctmc_CTMC.__init__)


def test_ctmc_ctmc_constructor_args():
    sig = inspect.signature(ctmc_CTMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ctmc_ctmc_has_name():
    assert hasattr(ctmc_CTMC, "name")
    descriptor = None
    for klass in ctmc_CTMC.__mro__:
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
ctmc_Label_strategy = st.builds(
    ctmc_Label,
    name=
        safe_text
)
ctmc_Transition_strategy = st.builds(
    ctmc_Transition,
    prob=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc_State_strategy = st.builds(
    ctmc_State,
    name=
        safe_text,
    exitRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc_CTMC_strategy = st.builds(
    ctmc_CTMC,
    name=
        safe_text
)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=ctmc_Label_strategy)
@settings(max_examples=50)
def test_ctmc_label_instantiation(instance):
    assert isinstance(instance, ctmc_Label)



@given(instance=ctmc_Label_strategy)
def test_ctmc_label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ctmc_Transition_strategy)
@settings(max_examples=50)
def test_ctmc_transition_instantiation(instance):
    assert isinstance(instance, ctmc_Transition)



@given(instance=ctmc_Transition_strategy)
def test_ctmc_transition_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original



@given(instance=ctmc_Transition_strategy)
def test_ctmc_transition_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=ctmc_State_strategy)
@settings(max_examples=50)
def test_ctmc_state_instantiation(instance):
    assert isinstance(instance, ctmc_State)



@given(instance=ctmc_State_strategy)
def test_ctmc_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ctmc_State_strategy)
def test_ctmc_state_exitRate_setter(instance):
    original = instance.exitRate
    instance.exitRate = original
    assert instance.exitRate == original

@given(instance=ctmc_CTMC_strategy)
@settings(max_examples=50)
def test_ctmc_ctmc_instantiation(instance):
    assert isinstance(instance, ctmc_CTMC)



@given(instance=ctmc_CTMC_strategy)
def test_ctmc_ctmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
