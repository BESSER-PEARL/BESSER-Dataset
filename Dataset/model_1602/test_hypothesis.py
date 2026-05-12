import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet2_Transition,
    petrinet2_Place,
    petrinet2_Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet2_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Transition)


def test_petrinet2_transition_constructor_exists():
    assert callable(petrinet2_Transition.__init__)


def test_petrinet2_transition_constructor_args():
    sig = inspect.signature(petrinet2_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2_transition_has_name():
    assert hasattr(petrinet2_Transition, "name")
    descriptor = None
    for klass in petrinet2_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2_place_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Place)


def test_petrinet2_place_constructor_exists():
    assert callable(petrinet2_Place.__init__)


def test_petrinet2_place_constructor_args():
    sig = inspect.signature(petrinet2_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2_place_has_name():
    assert hasattr(petrinet2_Place, "name")
    descriptor = None
    for klass in petrinet2_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2_net_is_not_abstract():
    assert not inspect.isabstract(petrinet2_Net)


def test_petrinet2_net_constructor_exists():
    assert callable(petrinet2_Net.__init__)


def test_petrinet2_net_constructor_args():
    sig = inspect.signature(petrinet2_Net.__init__)
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
petrinet2_Transition_strategy = st.builds(
    petrinet2_Transition,
    name=
        safe_text
)
petrinet2_Place_strategy = st.builds(
    petrinet2_Place,
    name=
        safe_text
)
petrinet2_Net_strategy = st.builds(
    petrinet2_Net,
)

@given(instance=petrinet2_Transition_strategy)
@settings(max_examples=50)
def test_petrinet2_transition_instantiation(instance):
    assert isinstance(instance, petrinet2_Transition)



@given(instance=petrinet2_Transition_strategy)
def test_petrinet2_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2_Place_strategy)
@settings(max_examples=50)
def test_petrinet2_place_instantiation(instance):
    assert isinstance(instance, petrinet2_Place)



@given(instance=petrinet2_Place_strategy)
def test_petrinet2_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2_Net_strategy)
@settings(max_examples=50)
def test_petrinet2_net_instantiation(instance):
    assert isinstance(instance, petrinet2_Net)
