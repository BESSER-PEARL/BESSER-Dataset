import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNets::OutputArc,
    PetriNets::InputArc,
    PetriNets::Transition,
    PetriNets::PetriNet,
    PetriNets::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets::outputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::OutputArc)


def test_petrinets::outputarc_constructor_exists():
    assert callable(PetriNets::OutputArc.__init__)


def test_petrinets::outputarc_constructor_args():
    sig = inspect.signature(PetriNets::OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets::outputarc_has_weight():
    assert hasattr(PetriNets::OutputArc, "weight")
    descriptor = None
    for klass in PetriNets::OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::inputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::InputArc)


def test_petrinets::inputarc_constructor_exists():
    assert callable(PetriNets::InputArc.__init__)


def test_petrinets::inputarc_constructor_args():
    sig = inspect.signature(PetriNets::InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets::inputarc_has_weight():
    assert hasattr(PetriNets::InputArc, "weight")
    descriptor = None
    for klass in PetriNets::InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(PetriNets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(PetriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::transition_has_name():
    assert hasattr(PetriNets::Transition, "name")
    descriptor = None
    for klass in PetriNets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets::PetriNet)


def test_petrinets::petrinet_constructor_exists():
    assert callable(PetriNets::PetriNet.__init__)


def test_petrinets::petrinet_constructor_args():
    sig = inspect.signature(PetriNets::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::petrinet_has_name():
    assert hasattr(PetriNets::PetriNet, "name")
    descriptor = None
    for klass in PetriNets::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(PetriNets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(PetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinets::place_has_numberOfTokens():
    assert hasattr(PetriNets::Place, "numberOfTokens")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_petrinets::place_has_name():
    assert hasattr(PetriNets::Place, "name")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinets::place_has_capacity():
    assert hasattr(PetriNets::Place, "capacity")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
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
PetriNets::OutputArc_strategy = st.builds(
    PetriNets::OutputArc,
    weight=
        st.integers()
)
PetriNets::InputArc_strategy = st.builds(
    PetriNets::InputArc,
    weight=
        st.integers()
)
PetriNets::Transition_strategy = st.builds(
    PetriNets::Transition,
    name=
        safe_text
)
PetriNets::PetriNet_strategy = st.builds(
    PetriNets::PetriNet,
    name=
        safe_text
)
PetriNets::Place_strategy = st.builds(
    PetriNets::Place,
    numberOfTokens=
        st.integers(),
    name=
        safe_text,
    capacity=
        st.integers()
)

@given(instance=PetriNets::OutputArc_strategy)
@settings(max_examples=50)
def test_petrinets::outputarc_instantiation(instance):
    assert isinstance(instance, PetriNets::OutputArc)

@given(instance=PetriNets::OutputArc_strategy)
def test_petrinets::outputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNets::OutputArc_strategy)
def test_petrinets::outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets::InputArc_strategy)
@settings(max_examples=50)
def test_petrinets::inputarc_instantiation(instance):
    assert isinstance(instance, PetriNets::InputArc)

@given(instance=PetriNets::InputArc_strategy)
def test_petrinets::inputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNets::InputArc_strategy)
def test_petrinets::inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, PetriNets::Transition)

@given(instance=PetriNets::Transition_strategy)
def test_petrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNets::Transition_strategy)
def test_petrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets::PetriNet)

@given(instance=PetriNets::PetriNet_strategy)
def test_petrinets::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNets::PetriNet_strategy)
def test_petrinets::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, PetriNets::Place)

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_numberOfTokens_type(instance):
    assert isinstance(instance.numberOfTokens, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
