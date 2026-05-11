import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bowling::League,
    bowling::Player,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowling::league_is_not_abstract():
    assert not inspect.isabstract(bowling::League)


def test_bowling::league_constructor_exists():
    assert callable(bowling::League.__init__)


def test_bowling::league_constructor_args():
    sig = inspect.signature(bowling::League.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bowling::league_has_name():
    assert hasattr(bowling::League, "name")
    descriptor = None
    for klass in bowling::League.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bowling::player_is_not_abstract():
    assert not inspect.isabstract(bowling::Player)


def test_bowling::player_constructor_exists():
    assert callable(bowling::Player.__init__)


def test_bowling::player_constructor_args():
    sig = inspect.signature(bowling::Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dateOfBirth" in params, "Missing parameter 'dateOfBirth'"

def test_bowling::player_has_name():
    assert hasattr(bowling::Player, "name")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bowling::player_has_dateOfBirth():
    assert hasattr(bowling::Player, "dateOfBirth")
    descriptor = None
    for klass in bowling::Player.__mro__:
        if "dateOfBirth" in klass.__dict__:
            descriptor = klass.__dict__["dateOfBirth"]
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
bowling::League_strategy = st.builds(
    bowling::League,
    name=
        safe_text
)
bowling::Player_strategy = st.builds(
    bowling::Player,
    name=
        safe_text,
    dateOfBirth=
        st.dates()
)

@given(instance=bowling::League_strategy)
@settings(max_examples=50)
def test_bowling::league_instantiation(instance):
    assert isinstance(instance, bowling::League)

@given(instance=bowling::League_strategy)
def test_bowling::league_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::League_strategy)
def test_bowling::league_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Player_strategy)
@settings(max_examples=50)
def test_bowling::player_instantiation(instance):
    assert isinstance(instance, bowling::Player)

@given(instance=bowling::Player_strategy)
def test_bowling::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=bowling::Player_strategy)
def test_bowling::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_type(instance):
    assert isinstance(instance.dateOfBirth, date)


@given(instance=bowling::Player_strategy)
def test_bowling::player_dateOfBirth_setter(instance):
    original = instance.dateOfBirth
    instance.dateOfBirth = original
    assert instance.dateOfBirth == original
