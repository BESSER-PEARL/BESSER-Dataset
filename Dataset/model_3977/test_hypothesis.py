import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IDBase,
    dtmc::Transition,
    dtmc::Label,
    dtmc::DTMC,
    dtmc::State,
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



def test_dtmc::transition_is_not_abstract():
    assert not inspect.isabstract(dtmc::Transition)


def test_dtmc::transition_constructor_exists():
    assert callable(dtmc::Transition.__init__)


def test_dtmc::transition_constructor_args():
    sig = inspect.signature(dtmc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "prob" in params, "Missing parameter 'prob'"

def test_dtmc::transition_has_prob():
    assert hasattr(dtmc::Transition, "prob")
    descriptor = None
    for klass in dtmc::Transition.__mro__:
        if "prob" in klass.__dict__:
            descriptor = klass.__dict__["prob"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::label_is_not_abstract():
    assert not inspect.isabstract(dtmc::Label)


def test_dtmc::label_constructor_exists():
    assert callable(dtmc::Label.__init__)


def test_dtmc::label_constructor_args():
    sig = inspect.signature(dtmc::Label.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc::label_has_name():
    assert hasattr(dtmc::Label, "name")
    descriptor = None
    for klass in dtmc::Label.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::dtmc_is_not_abstract():
    assert not inspect.isabstract(dtmc::DTMC)


def test_dtmc::dtmc_constructor_exists():
    assert callable(dtmc::DTMC.__init__)


def test_dtmc::dtmc_constructor_args():
    sig = inspect.signature(dtmc::DTMC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc::dtmc_has_name():
    assert hasattr(dtmc::DTMC, "name")
    descriptor = None
    for klass in dtmc::DTMC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dtmc::state_is_not_abstract():
    assert not inspect.isabstract(dtmc::State)


def test_dtmc::state_constructor_exists():
    assert callable(dtmc::State.__init__)


def test_dtmc::state_constructor_args():
    sig = inspect.signature(dtmc::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dtmc::state_has_name():
    assert hasattr(dtmc::State, "name")
    descriptor = None
    for klass in dtmc::State.__mro__:
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
dtmc::Transition_strategy = st.builds(
    dtmc::Transition,
    prob=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dtmc::Label_strategy = st.builds(
    dtmc::Label,
    name=
        safe_text
)
dtmc::DTMC_strategy = st.builds(
    dtmc::DTMC,
    name=
        safe_text
)
dtmc::State_strategy = st.builds(
    dtmc::State,
    name=
        safe_text
)

@given(instance=IDBase_strategy)
@settings(max_examples=50)
def test_idbase_instantiation(instance):
    assert isinstance(instance, IDBase)

@given(instance=dtmc::Transition_strategy)
@settings(max_examples=50)
def test_dtmc::transition_instantiation(instance):
    assert isinstance(instance, dtmc::Transition)

@given(instance=dtmc::Transition_strategy)
def test_dtmc::transition_prob_type(instance):
    assert isinstance(instance.prob, float)


@given(instance=dtmc::Transition_strategy)
def test_dtmc::transition_prob_setter(instance):
    original = instance.prob
    instance.prob = original
    assert instance.prob == original

@given(instance=dtmc::Label_strategy)
@settings(max_examples=50)
def test_dtmc::label_instantiation(instance):
    assert isinstance(instance, dtmc::Label)

@given(instance=dtmc::Label_strategy)
def test_dtmc::label_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dtmc::Label_strategy)
def test_dtmc::label_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dtmc::DTMC_strategy)
@settings(max_examples=50)
def test_dtmc::dtmc_instantiation(instance):
    assert isinstance(instance, dtmc::DTMC)

@given(instance=dtmc::DTMC_strategy)
def test_dtmc::dtmc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dtmc::DTMC_strategy)
def test_dtmc::dtmc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dtmc::State_strategy)
@settings(max_examples=50)
def test_dtmc::state_instantiation(instance):
    assert isinstance(instance, dtmc::State)

@given(instance=dtmc::State_strategy)
def test_dtmc::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dtmc::State_strategy)
def test_dtmc::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
