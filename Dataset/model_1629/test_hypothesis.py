import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petri::RedPetri,
    petri::Transition,
    petri::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petri::redpetri_is_not_abstract():
    assert not inspect.isabstract(petri::RedPetri)


def test_petri::redpetri_constructor_exists():
    assert callable(petri::RedPetri.__init__)


def test_petri::redpetri_constructor_args():
    sig = inspect.signature(petri::RedPetri.__init__)
    params = list(sig.parameters.keys())



def test_petri::transition_is_not_abstract():
    assert not inspect.isabstract(petri::Transition)


def test_petri::transition_constructor_exists():
    assert callable(petri::Transition.__init__)


def test_petri::transition_constructor_args():
    sig = inspect.signature(petri::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::transition_has_name():
    assert hasattr(petri::Transition, "name")
    descriptor = None
    for klass in petri::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::place_is_not_abstract():
    assert not inspect.isabstract(petri::Place)


def test_petri::place_constructor_exists():
    assert callable(petri::Place.__init__)


def test_petri::place_constructor_args():
    sig = inspect.signature(petri::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri::place_has_name():
    assert hasattr(petri::Place, "name")
    descriptor = None
    for klass in petri::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petri::place_has_tokens():
    assert hasattr(petri::Place, "tokens")
    descriptor = None
    for klass in petri::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
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
petri::RedPetri_strategy = st.builds(
    petri::RedPetri,
)
petri::Transition_strategy = st.builds(
    petri::Transition,
    name=
        safe_text
)
petri::Place_strategy = st.builds(
    petri::Place,
    name=
        safe_text,
    tokens=
        st.integers()
)

@given(instance=petri::RedPetri_strategy)
@settings(max_examples=50)
def test_petri::redpetri_instantiation(instance):
    assert isinstance(instance, petri::RedPetri)

@given(instance=petri::Transition_strategy)
@settings(max_examples=50)
def test_petri::transition_instantiation(instance):
    assert isinstance(instance, petri::Transition)

@given(instance=petri::Transition_strategy)
def test_petri::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::Transition_strategy)
def test_petri::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::Place_strategy)
@settings(max_examples=50)
def test_petri::place_instantiation(instance):
    assert isinstance(instance, petri::Place)

@given(instance=petri::Place_strategy)
def test_petri::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::Place_strategy)
def test_petri::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::Place_strategy)
def test_petri::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petri::Place_strategy)
def test_petri::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original
