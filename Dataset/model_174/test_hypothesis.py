import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::Net,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::transition_has_name():
    assert hasattr(PetriNet::Transition, "name")
    descriptor = None
    for klass in PetriNet::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::place_has_name():
    assert hasattr(PetriNet::Place, "name")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(PetriNet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(PetriNet::Net.__init__)
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
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
    name=
        safe_text
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    name=
        safe_text
)
PetriNet::Net_strategy = st.builds(
    PetriNet::Net,
)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, PetriNet::Net)
