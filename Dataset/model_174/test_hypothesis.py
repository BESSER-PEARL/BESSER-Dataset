import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_Net,
    PetriNet_Transition,
    PetriNet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(PetriNet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(PetriNet_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_name():
    assert hasattr(PetriNet_Transition, "name")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_place_has_name():
    assert hasattr(PetriNet_Place, "name")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
PetriNet_Net_strategy = st.builds(
    PetriNet_Net,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
    name=
        safe_text
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    name=
        safe_text
)

@given(instance=PetriNet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, PetriNet_Net)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
