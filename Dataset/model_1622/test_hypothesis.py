import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetv1_Transition,
    petrinetv1_Place,
    petrinetv1_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv1_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv1_Transition)


def test_petrinetv1_transition_constructor_exists():
    assert callable(petrinetv1_Transition.__init__)


def test_petrinetv1_transition_constructor_args():
    sig = inspect.signature(petrinetv1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetv1_transition_has_name():
    assert hasattr(petrinetv1_Transition, "name")
    descriptor = None
    for klass in petrinetv1_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv1_place_is_not_abstract():
    assert not inspect.isabstract(petrinetv1_Place)


def test_petrinetv1_place_constructor_exists():
    assert callable(petrinetv1_Place.__init__)


def test_petrinetv1_place_constructor_args():
    sig = inspect.signature(petrinetv1_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_petrinetv1_place_has_tokens():
    assert hasattr(petrinetv1_Place, "tokens")
    descriptor = None
    for klass in petrinetv1_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv1_place_has_name():
    assert hasattr(petrinetv1_Place, "name")
    descriptor = None
    for klass in petrinetv1_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv1_place_has_initialTokens():
    assert hasattr(petrinetv1_Place, "initialTokens")
    descriptor = None
    for klass in petrinetv1_Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv1_net_is_not_abstract():
    assert not inspect.isabstract(petrinetv1_Net)


def test_petrinetv1_net_constructor_exists():
    assert callable(petrinetv1_Net.__init__)


def test_petrinetv1_net_constructor_args():
    sig = inspect.signature(petrinetv1_Net.__init__)
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
petrinetv1_Transition_strategy = st.builds(
    petrinetv1_Transition,
    name=
        safe_text
)
petrinetv1_Place_strategy = st.builds(
    petrinetv1_Place,
    tokens=
        st.integers(),
    name=
        safe_text,
    initialTokens=
        st.integers()
)
petrinetv1_Net_strategy = st.builds(
    petrinetv1_Net,
)

@given(instance=petrinetv1_Transition_strategy)
@settings(max_examples=50)
def test_petrinetv1_transition_instantiation(instance):
    assert isinstance(instance, petrinetv1_Transition)



@given(instance=petrinetv1_Transition_strategy)
def test_petrinetv1_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv1_Place_strategy)
@settings(max_examples=50)
def test_petrinetv1_place_instantiation(instance):
    assert isinstance(instance, petrinetv1_Place)



@given(instance=petrinetv1_Place_strategy)
def test_petrinetv1_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original



@given(instance=petrinetv1_Place_strategy)
def test_petrinetv1_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinetv1_Place_strategy)
def test_petrinetv1_place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinetv1_Net_strategy)
@settings(max_examples=50)
def test_petrinetv1_net_instantiation(instance):
    assert isinstance(instance, petrinetv1_Net)
