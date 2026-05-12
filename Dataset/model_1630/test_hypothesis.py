import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petri_Place,
    petri_RedPetri,
    petri_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petri_place_is_not_abstract():
    assert not inspect.isabstract(petri_Place)


def test_petri_place_constructor_exists():
    assert callable(petri_Place.__init__)


def test_petri_place_constructor_args():
    sig = inspect.signature(petri_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petri_place_has_name():
    assert hasattr(petri_Place, "name")
    descriptor = None
    for klass in petri_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petri_place_has_tokens():
    assert hasattr(petri_Place, "tokens")
    descriptor = None
    for klass in petri_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petri_redpetri_is_not_abstract():
    assert not inspect.isabstract(petri_RedPetri)


def test_petri_redpetri_constructor_exists():
    assert callable(petri_RedPetri.__init__)


def test_petri_redpetri_constructor_args():
    sig = inspect.signature(petri_RedPetri.__init__)
    params = list(sig.parameters.keys())



def test_petri_transition_is_not_abstract():
    assert not inspect.isabstract(petri_Transition)


def test_petri_transition_constructor_exists():
    assert callable(petri_Transition.__init__)


def test_petri_transition_constructor_args():
    sig = inspect.signature(petri_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_transition_has_name():
    assert hasattr(petri_Transition, "name")
    descriptor = None
    for klass in petri_Transition.__mro__:
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
petri_Place_strategy = st.builds(
    petri_Place,
    name=
        safe_text,
    tokens=
        st.integers()
)
petri_RedPetri_strategy = st.builds(
    petri_RedPetri,
)
petri_Transition_strategy = st.builds(
    petri_Transition,
    name=
        safe_text
)

@given(instance=petri_Place_strategy)
@settings(max_examples=50)
def test_petri_place_instantiation(instance):
    assert isinstance(instance, petri_Place)



@given(instance=petri_Place_strategy)
def test_petri_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petri_Place_strategy)
def test_petri_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petri_RedPetri_strategy)
@settings(max_examples=50)
def test_petri_redpetri_instantiation(instance):
    assert isinstance(instance, petri_RedPetri)

@given(instance=petri_Transition_strategy)
@settings(max_examples=50)
def test_petri_transition_instantiation(instance):
    assert isinstance(instance, petri_Transition)



@given(instance=petri_Transition_strategy)
def test_petri_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
