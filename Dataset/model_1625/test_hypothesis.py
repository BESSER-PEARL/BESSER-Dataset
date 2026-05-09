import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetv2::Transition,
    petrinetv2::Token,
    petrinetv2::Place,
    petrinetv2::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv2::transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv2::Transition)


def test_petrinetv2::transition_constructor_exists():
    assert callable(petrinetv2::Transition.__init__)


def test_petrinetv2::transition_constructor_args():
    sig = inspect.signature(petrinetv2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetv2::transition_has_name():
    assert hasattr(petrinetv2::Transition, "name")
    descriptor = None
    for klass in petrinetv2::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv2::token_is_not_abstract():
    assert not inspect.isabstract(petrinetv2::Token)


def test_petrinetv2::token_constructor_exists():
    assert callable(petrinetv2::Token.__init__)


def test_petrinetv2::token_constructor_args():
    sig = inspect.signature(petrinetv2::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv2::place_is_not_abstract():
    assert not inspect.isabstract(petrinetv2::Place)


def test_petrinetv2::place_constructor_exists():
    assert callable(petrinetv2::Place.__init__)


def test_petrinetv2::place_constructor_args():
    sig = inspect.signature(petrinetv2::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_petrinetv2::place_has_name():
    assert hasattr(petrinetv2::Place, "name")
    descriptor = None
    for klass in petrinetv2::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv2::place_has_initialTokens():
    assert hasattr(petrinetv2::Place, "initialTokens")
    descriptor = None
    for klass in petrinetv2::Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv2::net_is_not_abstract():
    assert not inspect.isabstract(petrinetv2::Net)


def test_petrinetv2::net_constructor_exists():
    assert callable(petrinetv2::Net.__init__)


def test_petrinetv2::net_constructor_args():
    sig = inspect.signature(petrinetv2::Net.__init__)
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
petrinetv2::Transition_strategy = st.builds(
    petrinetv2::Transition,
    name=
        safe_text
)
petrinetv2::Token_strategy = st.builds(
    petrinetv2::Token,
)
petrinetv2::Place_strategy = st.builds(
    petrinetv2::Place,
    name=
        safe_text,
    initialTokens=
        st.integers()
)
petrinetv2::Net_strategy = st.builds(
    petrinetv2::Net,
)

@given(instance=petrinetv2::Transition_strategy)
@settings(max_examples=50)
def test_petrinetv2::transition_instantiation(instance):
    assert isinstance(instance, petrinetv2::Transition)

@given(instance=petrinetv2::Transition_strategy)
def test_petrinetv2::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv2::Transition_strategy)
def test_petrinetv2::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv2::Token_strategy)
@settings(max_examples=50)
def test_petrinetv2::token_instantiation(instance):
    assert isinstance(instance, petrinetv2::Token)

@given(instance=petrinetv2::Place_strategy)
@settings(max_examples=50)
def test_petrinetv2::place_instantiation(instance):
    assert isinstance(instance, petrinetv2::Place)

@given(instance=petrinetv2::Place_strategy)
def test_petrinetv2::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv2::Place_strategy)
def test_petrinetv2::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv2::Place_strategy)
def test_petrinetv2::place_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=petrinetv2::Place_strategy)
def test_petrinetv2::place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinetv2::Net_strategy)
@settings(max_examples=50)
def test_petrinetv2::net_instantiation(instance):
    assert isinstance(instance, petrinetv2::Net)
