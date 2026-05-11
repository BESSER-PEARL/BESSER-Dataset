import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsa::State,
    fsa::FSA,
    fsa::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsa::state_is_not_abstract():
    assert not inspect.isabstract(fsa::State)


def test_fsa::state_constructor_exists():
    assert callable(fsa::State.__init__)


def test_fsa::state_constructor_args():
    sig = inspect.signature(fsa::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "accepting" in params, "Missing parameter 'accepting'"

def test_fsa::state_has_name():
    assert hasattr(fsa::State, "name")
    descriptor = None
    for klass in fsa::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_fsa::state_has_accepting():
    assert hasattr(fsa::State, "accepting")
    descriptor = None
    for klass in fsa::State.__mro__:
        if "accepting" in klass.__dict__:
            descriptor = klass.__dict__["accepting"]
            break
    assert isinstance(descriptor, property)



def test_fsa::fsa_is_not_abstract():
    assert not inspect.isabstract(fsa::FSA)


def test_fsa::fsa_constructor_exists():
    assert callable(fsa::FSA.__init__)


def test_fsa::fsa_constructor_args():
    sig = inspect.signature(fsa::FSA.__init__)
    params = list(sig.parameters.keys())



def test_fsa::transition_is_not_abstract():
    assert not inspect.isabstract(fsa::Transition)


def test_fsa::transition_constructor_exists():
    assert callable(fsa::Transition.__init__)


def test_fsa::transition_constructor_args():
    sig = inspect.signature(fsa::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"

def test_fsa::transition_has_event():
    assert hasattr(fsa::Transition, "event")
    descriptor = None
    for klass in fsa::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
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
fsa::State_strategy = st.builds(
    fsa::State,
    name=
        safe_text,
    accepting=
        st.booleans()
)
fsa::FSA_strategy = st.builds(
    fsa::FSA,
)
fsa::Transition_strategy = st.builds(
    fsa::Transition,
    event=
        safe_text
)

@given(instance=fsa::State_strategy)
@settings(max_examples=50)
def test_fsa::state_instantiation(instance):
    assert isinstance(instance, fsa::State)

@given(instance=fsa::State_strategy)
def test_fsa::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsa::State_strategy)
def test_fsa::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsa::State_strategy)
def test_fsa::state_accepting_type(instance):
    assert isinstance(instance.accepting, bool)


@given(instance=fsa::State_strategy)
def test_fsa::state_accepting_setter(instance):
    original = instance.accepting
    instance.accepting = original
    assert instance.accepting == original

@given(instance=fsa::FSA_strategy)
@settings(max_examples=50)
def test_fsa::fsa_instantiation(instance):
    assert isinstance(instance, fsa::FSA)

@given(instance=fsa::Transition_strategy)
@settings(max_examples=50)
def test_fsa::transition_instantiation(instance):
    assert isinstance(instance, fsa::Transition)

@given(instance=fsa::Transition_strategy)
def test_fsa::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=fsa::Transition_strategy)
def test_fsa::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original
