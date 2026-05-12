import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinetv3_Token,
    petrinetv3_Transition,
    petrinetv3_Place,
    petrinetv3_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv3_token_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_Token)


def test_petrinetv3_token_constructor_exists():
    assert callable(petrinetv3_Token.__init__)


def test_petrinetv3_token_constructor_args():
    sig = inspect.signature(petrinetv3_Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3_transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_Transition)


def test_petrinetv3_transition_constructor_exists():
    assert callable(petrinetv3_Transition.__init__)


def test_petrinetv3_transition_constructor_args():
    sig = inspect.signature(petrinetv3_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "tmin" in params, "Missing parameter 'tmin'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tmax" in params, "Missing parameter 'tmax'"
    assert "clock" in params, "Missing parameter 'clock'"

def test_petrinetv3_transition_has_tmin():
    assert hasattr(petrinetv3_Transition, "tmin")
    descriptor = None
    for klass in petrinetv3_Transition.__mro__:
        if "tmin" in klass.__dict__:
            descriptor = klass.__dict__["tmin"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3_transition_has_name():
    assert hasattr(petrinetv3_Transition, "name")
    descriptor = None
    for klass in petrinetv3_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3_transition_has_tmax():
    assert hasattr(petrinetv3_Transition, "tmax")
    descriptor = None
    for klass in petrinetv3_Transition.__mro__:
        if "tmax" in klass.__dict__:
            descriptor = klass.__dict__["tmax"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3_transition_has_clock():
    assert hasattr(petrinetv3_Transition, "clock")
    descriptor = None
    for klass in petrinetv3_Transition.__mro__:
        if "clock" in klass.__dict__:
            descriptor = klass.__dict__["clock"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3_place_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_Place)


def test_petrinetv3_place_constructor_exists():
    assert callable(petrinetv3_Place.__init__)


def test_petrinetv3_place_constructor_args():
    sig = inspect.signature(petrinetv3_Place.__init__)
    params = list(sig.parameters.keys())
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetv3_place_has_initialTokens():
    assert hasattr(petrinetv3_Place, "initialTokens")
    descriptor = None
    for klass in petrinetv3_Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3_place_has_name():
    assert hasattr(petrinetv3_Place, "name")
    descriptor = None
    for klass in petrinetv3_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3_net_is_not_abstract():
    assert not inspect.isabstract(petrinetv3_Net)


def test_petrinetv3_net_constructor_exists():
    assert callable(petrinetv3_Net.__init__)


def test_petrinetv3_net_constructor_args():
    sig = inspect.signature(petrinetv3_Net.__init__)
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
petrinetv3_Token_strategy = st.builds(
    petrinetv3_Token,
)
petrinetv3_Transition_strategy = st.builds(
    petrinetv3_Transition,
    tmin=
        st.integers(),
    name=
        safe_text,
    tmax=
        st.integers(),
    clock=
        st.integers()
)
petrinetv3_Place_strategy = st.builds(
    petrinetv3_Place,
    initialTokens=
        st.integers(),
    name=
        safe_text
)
petrinetv3_Net_strategy = st.builds(
    petrinetv3_Net,
)

@given(instance=petrinetv3_Token_strategy)
@settings(max_examples=50)
def test_petrinetv3_token_instantiation(instance):
    assert isinstance(instance, petrinetv3_Token)

@given(instance=petrinetv3_Transition_strategy)
@settings(max_examples=50)
def test_petrinetv3_transition_instantiation(instance):
    assert isinstance(instance, petrinetv3_Transition)



@given(instance=petrinetv3_Transition_strategy)
def test_petrinetv3_transition_tmin_setter(instance):
    original = instance.tmin
    instance.tmin = original
    assert instance.tmin == original



@given(instance=petrinetv3_Transition_strategy)
def test_petrinetv3_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinetv3_Transition_strategy)
def test_petrinetv3_transition_tmax_setter(instance):
    original = instance.tmax
    instance.tmax = original
    assert instance.tmax == original



@given(instance=petrinetv3_Transition_strategy)
def test_petrinetv3_transition_clock_setter(instance):
    original = instance.clock
    instance.clock = original
    assert instance.clock == original

@given(instance=petrinetv3_Place_strategy)
@settings(max_examples=50)
def test_petrinetv3_place_instantiation(instance):
    assert isinstance(instance, petrinetv3_Place)



@given(instance=petrinetv3_Place_strategy)
def test_petrinetv3_place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original



@given(instance=petrinetv3_Place_strategy)
def test_petrinetv3_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv3_Net_strategy)
@settings(max_examples=50)
def test_petrinetv3_net_instantiation(instance):
    assert isinstance(instance, petrinetv3_Net)
