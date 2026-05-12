import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetv2_Transition,
    petrinetv2_Token,
    petrinetv2_Place,
    petrinetv2_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv2_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv2_Transition)


def test_petrinetv2_transition_constructor_exists():
    assert callable(petrinetv2_Transition.__init__)


def test_petrinetv2_transition_constructor_args():
    sig = inspect.signature(petrinetv2_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetv2_transition_has_name():
    assert hasattr(petrinetv2_Transition, "name")
    descriptor = None
    for klass in petrinetv2_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv2_token_is_not_abstract():
    assert not inspect.isabstract(petrinetv2_Token)


def test_petrinetv2_token_constructor_exists():
    assert callable(petrinetv2_Token.__init__)


def test_petrinetv2_token_constructor_args():
    sig = inspect.signature(petrinetv2_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv2_place_is_not_abstract():
    assert not inspect.isabstract(petrinetv2_Place)


def test_petrinetv2_place_constructor_exists():
    assert callable(petrinetv2_Place.__init__)


def test_petrinetv2_place_constructor_args():
    sig = inspect.signature(petrinetv2_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_petrinetv2_place_has_name():
    assert hasattr(petrinetv2_Place, "name")
    descriptor = None
    for klass in petrinetv2_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv2_place_has_initialTokens():
    assert hasattr(petrinetv2_Place, "initialTokens")
    descriptor = None
    for klass in petrinetv2_Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv2_net_is_not_abstract():
    assert not inspect.isabstract(petrinetv2_Net)


def test_petrinetv2_net_constructor_exists():
    assert callable(petrinetv2_Net.__init__)


def test_petrinetv2_net_constructor_args():
    sig = inspect.signature(petrinetv2_Net.__init__)
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
petrinetv2_Transition_strategy = st.builds(
    petrinetv2_Transition,
    name=
        safe_text
)
petrinetv2_Token_strategy = st.builds(
    petrinetv2_Token,
)
petrinetv2_Place_strategy = st.builds(
    petrinetv2_Place,
    name=
        safe_text,
    initialTokens=
        st.integers()
)
petrinetv2_Net_strategy = st.builds(
    petrinetv2_Net,
)

@given(instance=petrinetv2_Transition_strategy)
@settings(max_examples=50)
def test_petrinetv2_transition_instantiation(instance):
    assert isinstance(instance, petrinetv2_Transition)



@given(instance=petrinetv2_Transition_strategy)
def test_petrinetv2_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv2_Token_strategy)
@settings(max_examples=50)
def test_petrinetv2_token_instantiation(instance):
    assert isinstance(instance, petrinetv2_Token)

@given(instance=petrinetv2_Place_strategy)
@settings(max_examples=50)
def test_petrinetv2_place_instantiation(instance):
    assert isinstance(instance, petrinetv2_Place)



@given(instance=petrinetv2_Place_strategy)
def test_petrinetv2_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinetv2_Place_strategy)
def test_petrinetv2_place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinetv2_Net_strategy)
@settings(max_examples=50)
def test_petrinetv2_net_instantiation(instance):
    assert isinstance(instance, petrinetv2_Net)
