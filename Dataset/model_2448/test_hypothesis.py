import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsa_Transition,
    fsa_State,
    fsa_FSA,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsa_transition_is_not_abstract():
    assert not inspect.isabstract(fsa_Transition)


def test_fsa_transition_constructor_exists():
    assert callable(fsa_Transition.__init__)


def test_fsa_transition_constructor_args():
    sig = inspect.signature(fsa_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_fsa_transition_has_event():
    assert hasattr(fsa_Transition, "event")
    descriptor = None
    for klass in fsa_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_fsa_state_is_not_abstract():
    assert not inspect.isabstract(fsa_State)


def test_fsa_state_constructor_exists():
    assert callable(fsa_State.__init__)


def test_fsa_state_constructor_args():
    sig = inspect.signature(fsa_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accepting" in params, "Missing parameter 'accepting'"

def test_fsa_state_has_name():
    assert hasattr(fsa_State, "name")
    descriptor = None
    for klass in fsa_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsa_state_has_accepting():
    assert hasattr(fsa_State, "accepting")
    descriptor = None
    for klass in fsa_State.__mro__:
        if "accepting" in klass.__dict__:
            descriptor = klass.__dict__["accepting"]
            break
    assert isinstance(descriptor, property)



def test_fsa_fsa_is_not_abstract():
    assert not inspect.isabstract(fsa_FSA)


def test_fsa_fsa_constructor_exists():
    assert callable(fsa_FSA.__init__)


def test_fsa_fsa_constructor_args():
    sig = inspect.signature(fsa_FSA.__init__)
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
fsa_Transition_strategy = st.builds(
    fsa_Transition,
    event=
        safe_text
)
fsa_State_strategy = st.builds(
    fsa_State,
    name=
        safe_text,
    accepting=
        st.booleans()
)
fsa_FSA_strategy = st.builds(
    fsa_FSA,
)

@given(instance=fsa_Transition_strategy)
@settings(max_examples=50)
def test_fsa_transition_instantiation(instance):
    assert isinstance(instance, fsa_Transition)



@given(instance=fsa_Transition_strategy)
def test_fsa_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=fsa_State_strategy)
@settings(max_examples=50)
def test_fsa_state_instantiation(instance):
    assert isinstance(instance, fsa_State)



@given(instance=fsa_State_strategy)
def test_fsa_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=fsa_State_strategy)
def test_fsa_state_accepting_setter(instance):
    original = instance.accepting
    instance.accepting = original
    assert instance.accepting == original

@given(instance=fsa_FSA_strategy)
@settings(max_examples=50)
def test_fsa_fsa_instantiation(instance):
    assert isinstance(instance, fsa_FSA)
