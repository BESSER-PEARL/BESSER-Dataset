import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachine::Place,
    StateMachine::PNTransition,
    StateMachine::Arc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::place_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Place)


def test_statemachine::place_constructor_exists():
    assert callable(StateMachine::Place.__init__)


def test_statemachine::place_constructor_args():
    sig = inspect.signature(StateMachine::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::place_has_tokens():
    assert hasattr(StateMachine::Place, "tokens")
    descriptor = None
    for klass in StateMachine::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::place_has_name():
    assert hasattr(StateMachine::Place, "name")
    descriptor = None
    for klass in StateMachine::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::pntransition_is_not_abstract():
    assert not inspect.isabstract(StateMachine::PNTransition)


def test_statemachine::pntransition_constructor_exists():
    assert callable(StateMachine::PNTransition.__init__)


def test_statemachine::pntransition_constructor_args():
    sig = inspect.signature(StateMachine::PNTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::arc_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Arc)


def test_statemachine::arc_constructor_exists():
    assert callable(StateMachine::Arc.__init__)


def test_statemachine::arc_constructor_args():
    sig = inspect.signature(StateMachine::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "toPlace" in params, "Missing parameter 'toPlace'"

def test_statemachine::arc_has_weight():
    assert hasattr(StateMachine::Arc, "weight")
    descriptor = None
    for klass in StateMachine::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::arc_has_toPlace():
    assert hasattr(StateMachine::Arc, "toPlace")
    descriptor = None
    for klass in StateMachine::Arc.__mro__:
        if "toPlace" in klass.__dict__:
            descriptor = klass.__dict__["toPlace"]
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
StateMachine::Place_strategy = st.builds(
    StateMachine::Place,
    tokens=
        st.integers(),
    name=
        safe_text
)
StateMachine::PNTransition_strategy = st.builds(
    StateMachine::PNTransition,
)
StateMachine::Arc_strategy = st.builds(
    StateMachine::Arc,
    weight=
        st.integers(),
    toPlace=
        st.booleans()
)

@given(instance=StateMachine::Place_strategy)
@settings(max_examples=50)
def test_statemachine::place_instantiation(instance):
    assert isinstance(instance, StateMachine::Place)

@given(instance=StateMachine::Place_strategy)
def test_statemachine::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=StateMachine::Place_strategy)
def test_statemachine::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=StateMachine::Place_strategy)
def test_statemachine::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::Place_strategy)
def test_statemachine::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine::PNTransition_strategy)
@settings(max_examples=50)
def test_statemachine::pntransition_instantiation(instance):
    assert isinstance(instance, StateMachine::PNTransition)

@given(instance=StateMachine::Arc_strategy)
@settings(max_examples=50)
def test_statemachine::arc_instantiation(instance):
    assert isinstance(instance, StateMachine::Arc)

@given(instance=StateMachine::Arc_strategy)
def test_statemachine::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=StateMachine::Arc_strategy)
def test_statemachine::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=StateMachine::Arc_strategy)
def test_statemachine::arc_toPlace_type(instance):
    assert isinstance(instance.toPlace, bool)


@given(instance=StateMachine::Arc_strategy)
def test_statemachine::arc_toPlace_setter(instance):
    original = instance.toPlace
    instance.toPlace = original
    assert instance.toPlace == original
