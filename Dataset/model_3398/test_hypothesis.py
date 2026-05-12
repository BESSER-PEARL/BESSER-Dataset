import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StateMachine_Place,
    StateMachine_PNTransition,
    StateMachine_Arc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine_place_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Place)


def test_statemachine_place_constructor_exists():
    assert callable(StateMachine_Place.__init__)


def test_statemachine_place_constructor_args():
    sig = inspect.signature(StateMachine_Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_place_has_tokens():
    assert hasattr(StateMachine_Place, "tokens")
    descriptor = None
    for klass in StateMachine_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_place_has_name():
    assert hasattr(StateMachine_Place, "name")
    descriptor = None
    for klass in StateMachine_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_pntransition_is_not_abstract():
    assert not inspect.isabstract(StateMachine_PNTransition)


def test_statemachine_pntransition_constructor_exists():
    assert callable(StateMachine_PNTransition.__init__)


def test_statemachine_pntransition_constructor_args():
    sig = inspect.signature(StateMachine_PNTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_arc_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Arc)


def test_statemachine_arc_constructor_exists():
    assert callable(StateMachine_Arc.__init__)


def test_statemachine_arc_constructor_args():
    sig = inspect.signature(StateMachine_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "toPlace" in params, "Missing parameter 'toPlace'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_statemachine_arc_has_toPlace():
    assert hasattr(StateMachine_Arc, "toPlace")
    descriptor = None
    for klass in StateMachine_Arc.__mro__:
        if "toPlace" in klass.__dict__:
            descriptor = klass.__dict__["toPlace"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_arc_has_weight():
    assert hasattr(StateMachine_Arc, "weight")
    descriptor = None
    for klass in StateMachine_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
StateMachine_Place_strategy = st.builds(
    StateMachine_Place,
    tokens=
        st.integers(),
    name=
        safe_text
)
StateMachine_PNTransition_strategy = st.builds(
    StateMachine_PNTransition,
)
StateMachine_Arc_strategy = st.builds(
    StateMachine_Arc,
    toPlace=
        st.booleans(),
    weight=
        st.integers()
)

@given(instance=StateMachine_Place_strategy)
@settings(max_examples=50)
def test_statemachine_place_instantiation(instance):
    assert isinstance(instance, StateMachine_Place)



@given(instance=StateMachine_Place_strategy)
def test_statemachine_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original



@given(instance=StateMachine_Place_strategy)
def test_statemachine_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=StateMachine_PNTransition_strategy)
@settings(max_examples=50)
def test_statemachine_pntransition_instantiation(instance):
    assert isinstance(instance, StateMachine_PNTransition)

@given(instance=StateMachine_Arc_strategy)
@settings(max_examples=50)
def test_statemachine_arc_instantiation(instance):
    assert isinstance(instance, StateMachine_Arc)



@given(instance=StateMachine_Arc_strategy)
def test_statemachine_arc_toPlace_setter(instance):
    original = instance.toPlace
    instance.toPlace = original
    assert instance.toPlace == original



@given(instance=StateMachine_Arc_strategy)
def test_statemachine_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
