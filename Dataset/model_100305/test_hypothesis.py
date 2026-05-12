import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    standardPetriNets::InputArc,
    standardPetriNets::PetriNet,
    standardPetriNets::OutputArc,
    standardPetriNets::Transition,
    standardPetriNets::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_standardpetrinets::inputarc_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets::InputArc)


def test_standardpetrinets::inputarc_constructor_exists():
    assert callable(standardPetriNets::InputArc.__init__)


def test_standardpetrinets::inputarc_constructor_args():
    sig = inspect.signature(standardPetriNets::InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_standardpetrinets::inputarc_has_weight():
    assert hasattr(standardPetriNets::InputArc, "weight")
    descriptor = None
    for klass in standardPetriNets::InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets::PetriNet)


def test_standardpetrinets::petrinet_constructor_exists():
    assert callable(standardPetriNets::PetriNet.__init__)


def test_standardpetrinets::petrinet_constructor_args():
    sig = inspect.signature(standardPetriNets::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_standardpetrinets::petrinet_has_name():
    assert hasattr(standardPetriNets::PetriNet, "name")
    descriptor = None
    for klass in standardPetriNets::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets::outputarc_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets::OutputArc)


def test_standardpetrinets::outputarc_constructor_exists():
    assert callable(standardPetriNets::OutputArc.__init__)


def test_standardpetrinets::outputarc_constructor_args():
    sig = inspect.signature(standardPetriNets::OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_standardpetrinets::outputarc_has_weight():
    assert hasattr(standardPetriNets::OutputArc, "weight")
    descriptor = None
    for klass in standardPetriNets::OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets::transition_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets::Transition)


def test_standardpetrinets::transition_constructor_exists():
    assert callable(standardPetriNets::Transition.__init__)


def test_standardpetrinets::transition_constructor_args():
    sig = inspect.signature(standardPetriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_standardpetrinets::transition_has_name():
    assert hasattr(standardPetriNets::Transition, "name")
    descriptor = None
    for klass in standardPetriNets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets::place_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets::Place)


def test_standardpetrinets::place_constructor_exists():
    assert callable(standardPetriNets::Place.__init__)


def test_standardpetrinets::place_constructor_args():
    sig = inspect.signature(standardPetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "numOfTokens" in params, "Missing parameter 'numOfTokens'"
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_standardpetrinets::place_has_numOfTokens():
    assert hasattr(standardPetriNets::Place, "numOfTokens")
    descriptor = None
    for klass in standardPetriNets::Place.__mro__:
        if "numOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_standardpetrinets::place_has_name():
    assert hasattr(standardPetriNets::Place, "name")
    descriptor = None
    for klass in standardPetriNets::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_standardpetrinets::place_has_capacity():
    assert hasattr(standardPetriNets::Place, "capacity")
    descriptor = None
    for klass in standardPetriNets::Place.__mro__:
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
standardPetriNets::InputArc_strategy = st.builds(
    standardPetriNets::InputArc,
    weight=
        st.integers()
)
standardPetriNets::PetriNet_strategy = st.builds(
    standardPetriNets::PetriNet,
    name=
        safe_text
)
standardPetriNets::OutputArc_strategy = st.builds(
    standardPetriNets::OutputArc,
    weight=
        st.integers()
)
standardPetriNets::Transition_strategy = st.builds(
    standardPetriNets::Transition,
    name=
        safe_text
)
standardPetriNets::Place_strategy = st.builds(
    standardPetriNets::Place,
    numOfTokens=
        st.integers(),
    name=
        safe_text,
    capacity=
        st.integers()
)

@given(instance=standardPetriNets::InputArc_strategy)
@settings(max_examples=50)
def test_standardpetrinets::inputarc_instantiation(instance):
    assert isinstance(instance, standardPetriNets::InputArc)

@given(instance=standardPetriNets::InputArc_strategy)
def test_standardpetrinets::inputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=standardPetriNets::InputArc_strategy)
def test_standardpetrinets::inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=standardPetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_standardpetrinets::petrinet_instantiation(instance):
    assert isinstance(instance, standardPetriNets::PetriNet)

@given(instance=standardPetriNets::PetriNet_strategy)
def test_standardpetrinets::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=standardPetriNets::PetriNet_strategy)
def test_standardpetrinets::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=standardPetriNets::OutputArc_strategy)
@settings(max_examples=50)
def test_standardpetrinets::outputarc_instantiation(instance):
    assert isinstance(instance, standardPetriNets::OutputArc)

@given(instance=standardPetriNets::OutputArc_strategy)
def test_standardpetrinets::outputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=standardPetriNets::OutputArc_strategy)
def test_standardpetrinets::outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=standardPetriNets::Transition_strategy)
@settings(max_examples=50)
def test_standardpetrinets::transition_instantiation(instance):
    assert isinstance(instance, standardPetriNets::Transition)

@given(instance=standardPetriNets::Transition_strategy)
def test_standardpetrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=standardPetriNets::Transition_strategy)
def test_standardpetrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=standardPetriNets::Place_strategy)
@settings(max_examples=50)
def test_standardpetrinets::place_instantiation(instance):
    assert isinstance(instance, standardPetriNets::Place)

@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_numOfTokens_type(instance):
    assert isinstance(instance.numOfTokens, int)


@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_numOfTokens_setter(instance):
    original = instance.numOfTokens
    instance.numOfTokens = original
    assert instance.numOfTokens == original

@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=standardPetriNets::Place_strategy)
def test_standardpetrinets::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
