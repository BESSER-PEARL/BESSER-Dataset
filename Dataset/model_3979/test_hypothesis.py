import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ctmc_Transition,
    ctmc_Label,
    ctmc_State,
    ctmc_CTMC,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ctmc_transition_is_not_abstract():
    assert not inspect.isabstract(ctmc_Transition)


def test_ctmc_transition_constructor_exists():
    assert callable(ctmc_Transition.__init__)


def test_ctmc_transition_constructor_args():
    sig = inspect.signature(ctmc_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "name" in params, "Missing parameter 'name'"
    assert "probability" in params, "Missing parameter 'probability'"

def test_ctmc_transition_has_duration():
    assert hasattr(ctmc_Transition, "duration")
    descriptor = None
    for klass in ctmc_Transition.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_ctmc_transition_has_name():
    assert hasattr(ctmc_Transition, "name")
    descriptor = None
    for klass in ctmc_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ctmc_transition_has_probability():
    assert hasattr(ctmc_Transition, "probability")
    descriptor = None
    for klass in ctmc_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_ctmc_label_is_not_abstract():
    assert not inspect.isabstract(ctmc_Label)


def test_ctmc_label_constructor_exists():
    assert callable(ctmc_Label.__init__)


def test_ctmc_label_constructor_args():
    sig = inspect.signature(ctmc_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ctmc_label_has_text():
    assert hasattr(ctmc_Label, "text")
    descriptor = None
    for klass in ctmc_Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
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
ctmc_Transition_strategy = st.builds(
    ctmc_Transition,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ctmc_Label_strategy = st.builds(
    ctmc_Label,
    text=
        safe_text
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

@given(instance=ctmc_Transition_strategy)
@settings(max_examples=50)
def test_ctmc_transition_instantiation(instance):
    assert isinstance(instance, ctmc_Transition)



@given(instance=ctmc_Transition_strategy)
def test_ctmc_transition_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=ctmc_Transition_strategy)
def test_ctmc_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ctmc_Transition_strategy)
def test_ctmc_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=ctmc_Label_strategy)
@settings(max_examples=50)
def test_ctmc_label_instantiation(instance):
    assert isinstance(instance, ctmc_Label)



@given(instance=ctmc_Label_strategy)
def test_ctmc_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

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
