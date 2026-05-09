import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Petrinet::Transition,
    Petrinet::Place,
    Petrinet::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(Petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(Petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::transition_has_name():
    assert hasattr(Petrinet::Transition, "name")
    descriptor = None
    for klass in Petrinet::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(Petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(Petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::place_has_tokens():
    assert hasattr(Petrinet::Place, "tokens")
    descriptor = None
    for klass in Petrinet::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_name():
    assert hasattr(Petrinet::Place, "name")
    descriptor = None
    for klass in Petrinet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(Petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(Petrinet::PetriNet.__init__)
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
Petrinet::Transition_strategy = st.builds(
    Petrinet::Transition,
    name=
        safe_text
)
Petrinet::Place_strategy = st.builds(
    Petrinet::Place,
    tokens=
        st.integers(),
    name=
        safe_text
)
Petrinet::PetriNet_strategy = st.builds(
    Petrinet::PetriNet,
)

@given(instance=Petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, Petrinet::Transition)

@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, Petrinet::Place)

@given(instance=Petrinet::Place_strategy)
def test_petrinet::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=Petrinet::Place_strategy)
def test_petrinet::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=Petrinet::Place_strategy)
def test_petrinet::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Petrinet::Place_strategy)
def test_petrinet::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet::PetriNet)
