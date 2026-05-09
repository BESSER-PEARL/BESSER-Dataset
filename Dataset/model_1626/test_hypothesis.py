import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinetv3::Token,
    petrinetv3::Transition,
    petrinetv3::Place,
    petrinetv3::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetv3::token_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::Token)


def test_petrinetv3::token_constructor_exists():
    assert callable(petrinetv3::Token.__init__)


def test_petrinetv3::token_constructor_args():
    sig = inspect.signature(petrinetv3::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinetv3::transition_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::Transition)


def test_petrinetv3::transition_constructor_exists():
    assert callable(petrinetv3::Transition.__init__)


def test_petrinetv3::transition_constructor_args():
    sig = inspect.signature(petrinetv3::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "clock" in params, "Missing parameter 'clock'"
    assert "tmax" in params, "Missing parameter 'tmax'"
    assert "name" in params, "Missing parameter 'name'"
    assert "tmin" in params, "Missing parameter 'tmin'"

def test_petrinetv3::transition_has_clock():
    assert hasattr(petrinetv3::Transition, "clock")
    descriptor = None
    for klass in petrinetv3::Transition.__mro__:
        if "clock" in klass.__dict__:
            descriptor = klass.__dict__["clock"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3::transition_has_tmax():
    assert hasattr(petrinetv3::Transition, "tmax")
    descriptor = None
    for klass in petrinetv3::Transition.__mro__:
        if "tmax" in klass.__dict__:
            descriptor = klass.__dict__["tmax"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3::transition_has_name():
    assert hasattr(petrinetv3::Transition, "name")
    descriptor = None
    for klass in petrinetv3::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3::transition_has_tmin():
    assert hasattr(petrinetv3::Transition, "tmin")
    descriptor = None
    for klass in petrinetv3::Transition.__mro__:
        if "tmin" in klass.__dict__:
            descriptor = klass.__dict__["tmin"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3::place_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::Place)


def test_petrinetv3::place_constructor_exists():
    assert callable(petrinetv3::Place.__init__)


def test_petrinetv3::place_constructor_args():
    sig = inspect.signature(petrinetv3::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialTokens" in params, "Missing parameter 'initialTokens'"

def test_petrinetv3::place_has_name():
    assert hasattr(petrinetv3::Place, "name")
    descriptor = None
    for klass in petrinetv3::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetv3::place_has_initialTokens():
    assert hasattr(petrinetv3::Place, "initialTokens")
    descriptor = None
    for klass in petrinetv3::Place.__mro__:
        if "initialTokens" in klass.__dict__:
            descriptor = klass.__dict__["initialTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinetv3::net_is_not_abstract():
    assert not inspect.isabstract(petrinetv3::Net)


def test_petrinetv3::net_constructor_exists():
    assert callable(petrinetv3::Net.__init__)


def test_petrinetv3::net_constructor_args():
    sig = inspect.signature(petrinetv3::Net.__init__)
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
petrinetv3::Token_strategy = st.builds(
    petrinetv3::Token,
)
petrinetv3::Transition_strategy = st.builds(
    petrinetv3::Transition,
    clock=
        st.integers(),
    tmax=
        st.integers(),
    name=
        safe_text,
    tmin=
        st.integers()
)
petrinetv3::Place_strategy = st.builds(
    petrinetv3::Place,
    name=
        safe_text,
    initialTokens=
        st.integers()
)
petrinetv3::Net_strategy = st.builds(
    petrinetv3::Net,
)

@given(instance=petrinetv3::Token_strategy)
@settings(max_examples=50)
def test_petrinetv3::token_instantiation(instance):
    assert isinstance(instance, petrinetv3::Token)

@given(instance=petrinetv3::Transition_strategy)
@settings(max_examples=50)
def test_petrinetv3::transition_instantiation(instance):
    assert isinstance(instance, petrinetv3::Transition)

@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_clock_type(instance):
    assert isinstance(instance.clock, int)


@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_clock_setter(instance):
    original = instance.clock
    instance.clock = original
    assert instance.clock == original

@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_tmax_type(instance):
    assert isinstance(instance.tmax, int)


@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_tmax_setter(instance):
    original = instance.tmax
    instance.tmax = original
    assert instance.tmax == original

@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_tmin_type(instance):
    assert isinstance(instance.tmin, int)


@given(instance=petrinetv3::Transition_strategy)
def test_petrinetv3::transition_tmin_setter(instance):
    original = instance.tmin
    instance.tmin = original
    assert instance.tmin == original

@given(instance=petrinetv3::Place_strategy)
@settings(max_examples=50)
def test_petrinetv3::place_instantiation(instance):
    assert isinstance(instance, petrinetv3::Place)

@given(instance=petrinetv3::Place_strategy)
def test_petrinetv3::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinetv3::Place_strategy)
def test_petrinetv3::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinetv3::Place_strategy)
def test_petrinetv3::place_initialTokens_type(instance):
    assert isinstance(instance.initialTokens, int)


@given(instance=petrinetv3::Place_strategy)
def test_petrinetv3::place_initialTokens_setter(instance):
    original = instance.initialTokens
    instance.initialTokens = original
    assert instance.initialTokens == original

@given(instance=petrinetv3::Net_strategy)
@settings(max_examples=50)
def test_petrinetv3::net_instantiation(instance):
    assert isinstance(instance, petrinetv3::Net)
