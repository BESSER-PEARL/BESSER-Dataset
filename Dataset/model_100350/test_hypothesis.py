import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IDBase,
    ctmc::State,
    ctmc::Transition,
    ctmc::Label,
    ctmc::CTMC,
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



def test_ctmc::state_is_not_abstract():
    assert not inspect.isabstract(ctmc::State)


def test_ctmc::state_constructor_exists():
    assert callable(ctmc::State.__init__)


def test_ctmc::state_constructor_args():
    sig = inspect.signature(ctmc::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "exitRate" in params, "Missing parameter 'exitRate'"

def test_ctmc::state_has_name():
    assert hasattr(ctmc::State, "name")
    descriptor = None
    for klass in ctmc::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ctmc::state_has_exitRate():
    assert hasattr(ctmc::State, "exitRate")
    descriptor = None
    for klass in ctmc::State.__mro__:
        if "exitRate" in klass.__dict__:
            descriptor = klass.__dict__["exitRate"]
            break
    assert isinstance(descriptor, property)



def test_ctmc::transition_is_not_abstract():
    assert not inspect.isabstract(ctmc::Transition)


def test_ctmc::transition_constructor_exists():
    assert callable(ctmc::Transition.__init__)


def test_ctmc::transition_constructor_args():
    sig = inspect.signature(ctmc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "rate" in params, "Missing parameter 'rate'"
    assert "prob" in params, "Missing parameter 'prob'"

def test_ctmc::transition_has_rate():
    assert hasattr(ctmc::Transition, "rate")
    descriptor = None
    for klass in ctmc::Transition.__mro__:
        if "rate" in klass.__dict__:
            descriptor = klass.__dict__["rate"]
            break
    assert isinstance(descriptor, property)

def test_ctmc::transition_has_prob():
    assert hasattr(ctmc::Transition, "prob")
    descriptor = None
    for klass in ctmc::Transition.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)



def test_ctmc::label_is_not_abstract():
    assert not inspect.isabstract(ctmc::Label)


def test_ctmc::label_constructor_exists():
    assert callable(ctmc::Label.__init__)


def test_ctmc::label_constructor_args():
    sig = inspect.signature(ctmc::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ctmc::label_has_name():
    assert hasattr(ctmc::Label, "name")
    descriptor = None
    for klass in ctmc::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ctmc::ctmc_is_not_abstract():
    assert not inspect.isabstract(ctmc::CTMC)


def test_ctmc::ctmc_constructor_exists():
    assert callable(ctmc::CTMC.__init__)


def test_ctmc::ctmc_constructor_args():
    sig = inspect.signature(ctmc::CTMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ctmc::ctmc_has_name():
    assert hasattr(ctmc::CTMC, "name")
    descriptor = None
    for klass in ctmc::CTMC.__mro__:
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
ctmc::State_strategy = st.builds(
    ctmc::State,
    name=
        safe_text,
    exitRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc::Transition_strategy = st.builds(
    ctmc::Transition,
    rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    prob=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc::Label_strategy = st.builds(
    ctmc::Label,
    name=
        safe_text
)
ctmc::CTMC_strategy = st.builds(
    ctmc::CTMC,
    name=
        safe_text
)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=ctmc::State_strategy)
@settings(max_examples=50)
def test_ctmc::state_instantiation(instance):
    assert isinstance(instance, ctmc::State)

@given(instance=ctmc::State_strategy)
def test_ctmc::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ctmc::State_strategy)
def test_ctmc::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ctmc::State_strategy)
def test_ctmc::state_exitRate_type(instance):
    assert isinstance(instance.exitRate, float)


@given(instance=ctmc::State_strategy)
def test_ctmc::state_exitRate_setter(instance):
    original = instance.exitRate
    instance.exitRate = original
    assert instance.exitRate == original

@given(instance=ctmc::Transition_strategy)
@settings(max_examples=50)
def test_ctmc::transition_instantiation(instance):
    assert isinstance(instance, ctmc::Transition)

@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_rate_type(instance):
    assert isinstance(instance.rate, float)


@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_rate_setter(instance):
    original = instance.rate
    instance.rate = original
    assert instance.rate == original

@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_prob_type(instance):
    assert isinstance(instance.prob, float)


@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original

@given(instance=ctmc::Label_strategy)
@settings(max_examples=50)
def test_ctmc::label_instantiation(instance):
    assert isinstance(instance, ctmc::Label)

@given(instance=ctmc::Label_strategy)
def test_ctmc::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ctmc::Label_strategy)
def test_ctmc::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ctmc::CTMC_strategy)
@settings(max_examples=50)
def test_ctmc::ctmc_instantiation(instance):
    assert isinstance(instance, ctmc::CTMC)

@given(instance=ctmc::CTMC_strategy)
def test_ctmc::ctmc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ctmc::CTMC_strategy)
def test_ctmc::ctmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
