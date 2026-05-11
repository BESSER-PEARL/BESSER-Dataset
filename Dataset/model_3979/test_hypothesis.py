import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ctmc::Transition,
    ctmc::Label,
    ctmc::State,
    ctmc::CTMC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ctmc::transition_is_not_abstract():
    assert not inspect.isabstract(ctmc::Transition)


def test_ctmc::transition_constructor_exists():
    assert callable(ctmc::Transition.__init__)


def test_ctmc::transition_constructor_args():
    sig = inspect.signature(ctmc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "probability" in params, "Missing parameter 'probability'"
    assert "name" in params, "Missing parameter 'name'"

def test_ctmc::transition_has_duration():
    assert hasattr(ctmc::Transition, "duration")
    descriptor = None
    for klass in ctmc::Transition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_ctmc::transition_has_probability():
    assert hasattr(ctmc::Transition, "probability")
    descriptor = None
    for klass in ctmc::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_ctmc::transition_has_name():
    assert hasattr(ctmc::Transition, "name")
    descriptor = None
    for klass in ctmc::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ctmc::label_is_not_abstract():
    assert not inspect.isabstract(ctmc::Label)


def test_ctmc::label_constructor_exists():
    assert callable(ctmc::Label.__init__)


def test_ctmc::label_constructor_args():
    sig = inspect.signature(ctmc::Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ctmc::label_has_text():
    assert hasattr(ctmc::Label, "text")
    descriptor = None
    for klass in ctmc::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



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
ctmc::Transition_strategy = st.builds(
    ctmc::Transition,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text
)
ctmc::Label_strategy = st.builds(
    ctmc::Label,
    text=
        safe_text
)
ctmc::State_strategy = st.builds(
    ctmc::State,
    name=
        safe_text,
    exitRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc::CTMC_strategy = st.builds(
    ctmc::CTMC,
    name=
        safe_text
)

@given(instance=ctmc::Transition_strategy)
@settings(max_examples=50)
def test_ctmc::transition_instantiation(instance):
    assert isinstance(instance, ctmc::Transition)

@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ctmc::Transition_strategy)
def test_ctmc::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ctmc::Label_strategy)
@settings(max_examples=50)
def test_ctmc::label_instantiation(instance):
    assert isinstance(instance, ctmc::Label)

@given(instance=ctmc::Label_strategy)
def test_ctmc::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ctmc::Label_strategy)
def test_ctmc::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

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
