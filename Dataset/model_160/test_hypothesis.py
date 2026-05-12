import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Petrinet_Transition,
    Petrinet_Place,
    Petrinet_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(Petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(Petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_name():
    assert hasattr(Petrinet_Transition, "name")
    descriptor = None
    for klass in Petrinet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(Petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(Petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(Petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinet_place_has_name():
    assert hasattr(Petrinet_Place, "name")
    descriptor = None
    for klass in Petrinet_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_place_has_tokens():
    assert hasattr(Petrinet_Place, "tokens")
    descriptor = None
    for klass in Petrinet_Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(Petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(Petrinet_PetriNet.__init__)
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
Petrinet_Transition_strategy = st.builds(
    Petrinet_Transition,
    name=
        safe_text
)
Petrinet_Place_strategy = st.builds(
    Petrinet_Place,
    name=
        safe_text,
    tokens=
        st.integers()
)
Petrinet_PetriNet_strategy = st.builds(
    Petrinet_PetriNet,
)

@given(instance=Petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, Petrinet_Transition)



@given(instance=Petrinet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, Petrinet_Place)



@given(instance=Petrinet_Place_strategy)
def test_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Petrinet_Place_strategy)
def test_petrinet_place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=Petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet_PetriNet)
