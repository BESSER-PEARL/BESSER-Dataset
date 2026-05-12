import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinets_Transition,
    petrinets_Place,
    petrinets_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(petrinets_Transition)


def test_petrinets_transition_constructor_exists():
    assert callable(petrinets_Transition.__init__)


def test_petrinets_transition_constructor_args():
    sig = inspect.signature(petrinets_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_transition_has_name():
    assert hasattr(petrinets_Transition, "name")
    descriptor = None
    for klass in petrinets_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(petrinets_Place)


def test_petrinets_place_constructor_exists():
    assert callable(petrinets_Place.__init__)


def test_petrinets_place_constructor_args():
    sig = inspect.signature(petrinets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_place_has_name():
    assert hasattr(petrinets_Place, "name")
    descriptor = None
    for klass in petrinets_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_net_is_not_abstract():
    assert not inspect.isabstract(petrinets_Net)


def test_petrinets_net_constructor_exists():
    assert callable(petrinets_Net.__init__)


def test_petrinets_net_constructor_args():
    sig = inspect.signature(petrinets_Net.__init__)
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
petrinets_Transition_strategy = st.builds(
    petrinets_Transition,
    name=
        safe_text
)
petrinets_Place_strategy = st.builds(
    petrinets_Place,
    name=
        safe_text
)
petrinets_Net_strategy = st.builds(
    petrinets_Net,
)

@given(instance=petrinets_Transition_strategy)
@settings(max_examples=50)
def test_petrinets_transition_instantiation(instance):
    assert isinstance(instance, petrinets_Transition)



@given(instance=petrinets_Transition_strategy)
def test_petrinets_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinets_Place_strategy)
@settings(max_examples=50)
def test_petrinets_place_instantiation(instance):
    assert isinstance(instance, petrinets_Place)



@given(instance=petrinets_Place_strategy)
def test_petrinets_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinets_Net_strategy)
@settings(max_examples=50)
def test_petrinets_net_instantiation(instance):
    assert isinstance(instance, petrinets_Net)
