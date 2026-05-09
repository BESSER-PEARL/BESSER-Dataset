import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetv1::Transition,
    petrinetv1::Place,
    petrinetv1::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv1::transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv1::Transition)


def test_petrinetv1::transition_constructor_exists():
    assert callable(petrinetv1::Transition.__init__)


def test_petrinetv1::transition_constructor_args():
    sig = inspect.signature(petrinetv1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetv1::transition_has_name():
    assert hasattr(petrinetv1::Transition, "name")
    descriptor = None
    for klass in petrinetv1::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv1::place_is_not_abstract():
    assert not inspect.isabstract(petrinetv1::Place)


def test_petrinetv1::place_constructor_exists():
    assert callable(petrinetv1::Place.__init__)


def test_petrinetv1::place_constructor_args():
    sig = inspect.signature(petrinetv1::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinetv1::place_has_name():
    assert hasattr(petrinetv1::Place, "name")
    descriptor = None
    for klass in petrinetv1::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv1::place_has_initialTokens():
    assert hasattr(petrinetv1::Place, "initialTokens")
    descriptor = None
    for klass in petrinetv1::Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv1::place_has_tokens():
    assert hasattr(petrinetv1::Place, "tokens")
    descriptor = None
    for klass in petrinetv1::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv1::net_is_not_abstract():
    assert not inspect.isabstract(petrinetv1::Net)


def test_petrinetv1::net_constructor_exists():
    assert callable(petrinetv1::Net.__init__)


def test_petrinetv1::net_constructor_args():
    sig = inspect.signature(petrinetv1::Net.__init__)
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
petrinetv1::Transition_strategy = st.builds(
    petrinetv1::Transition,
    name=
        safe_text
)
petrinetv1::Place_strategy = st.builds(
    petrinetv1::Place,
    name=
        safe_text,
    initialTokens=
        st.integers(),
    tokens=
        st.integers()
)
petrinetv1::Net_strategy = st.builds(
    petrinetv1::Net,
)

@given(instance=petrinetv1::Transition_strategy)
@settings(max_examples=50)
def test_petrinetv1::transition_instantiation(instance):
    assert isinstance(instance, petrinetv1::Transition)

@given(instance=petrinetv1::Transition_strategy)
def test_petrinetv1::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv1::Transition_strategy)
def test_petrinetv1::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv1::Place_strategy)
@settings(max_examples=50)
def test_petrinetv1::place_instantiation(instance):
    assert isinstance(instance, petrinetv1::Place)

@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petrinetv1::Place_strategy)
def test_petrinetv1::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=petrinetv1::Net_strategy)
@settings(max_examples=50)
def test_petrinetv1::net_instantiation(instance):
    assert isinstance(instance, petrinetv1::Net)
