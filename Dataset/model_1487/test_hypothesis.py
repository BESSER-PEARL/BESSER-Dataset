import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petriNet::OutputArc,
    petriNet::InputArc,
    petriNet::Transition,
    petriNet::GenericPlace,
    petriNet::PetriNet,
    GenericPlace,
    petriNet::Resource,
    petriNet::Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::outputarc_is_not_abstract():
    assert not inspect.isabstract(petriNet::OutputArc)


def test_petrinet::outputarc_constructor_exists():
    assert callable(petriNet::OutputArc.__init__)


def test_petrinet::outputarc_constructor_args():
    sig = inspect.signature(petriNet::OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::outputarc_has_weight():
    assert hasattr(petriNet::OutputArc, "weight")
    descriptor = None
    for klass in petriNet::OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::inputarc_is_not_abstract():
    assert not inspect.isabstract(petriNet::InputArc)


def test_petrinet::inputarc_constructor_exists():
    assert callable(petriNet::InputArc.__init__)


def test_petrinet::inputarc_constructor_args():
    sig = inspect.signature(petriNet::InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::inputarc_has_weight():
    assert hasattr(petriNet::InputArc, "weight")
    descriptor = None
    for klass in petriNet::InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::transition_has_name():
    assert hasattr(petriNet::Transition, "name")
    descriptor = None
    for klass in petriNet::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::genericplace_is_not_abstract():
    assert not inspect.isabstract(petriNet::GenericPlace)


def test_petrinet::genericplace_constructor_exists():
    assert callable(petriNet::GenericPlace.__init__)


def test_petrinet::genericplace_constructor_args():
    sig = inspect.signature(petriNet::GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"

def test_petrinet::genericplace_has_name():
    assert hasattr(petriNet::GenericPlace, "name")
    descriptor = None
    for klass in petriNet::GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::genericplace_has_numberOfTokens():
    assert hasattr(petriNet::GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in petriNet::GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petriNet::PetriNet, "name")
    descriptor = None
    for klass in petriNet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_genericplace_is_not_abstract():
    assert not inspect.isabstract(GenericPlace)


def test_genericplace_constructor_exists():
    assert callable(GenericPlace.__init__)


def test_genericplace_constructor_args():
    sig = inspect.signature(GenericPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::resource_is_not_abstract():
    assert not inspect.isabstract(petriNet::Resource)


def test_petrinet::resource_constructor_exists():
    assert callable(petriNet::Resource.__init__)


def test_petrinet::resource_constructor_args():
    sig = inspect.signature(petriNet::Resource.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinet::place_has_capacity():
    assert hasattr(petriNet::Place, "capacity")
    descriptor = None
    for klass in petriNet::Place.__mro__:
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
petriNet::OutputArc_strategy = st.builds(
    petriNet::OutputArc,
    weight=
        st.integers()
)
petriNet::InputArc_strategy = st.builds(
    petriNet::InputArc,
    weight=
        st.integers()
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
    name=
        safe_text
)
petriNet::GenericPlace_strategy = st.builds(
    petriNet::GenericPlace,
    name=
        safe_text,
    numberOfTokens=
        st.integers()
)
petriNet::PetriNet_strategy = st.builds(
    petriNet::PetriNet,
    name=
        safe_text
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
petriNet::Resource_strategy = st.builds(
    petriNet::Resource,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
    capacity=
        st.integers()
)

@given(instance=petriNet::OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet::outputarc_instantiation(instance):
    assert isinstance(instance, petriNet::OutputArc)

@given(instance=petriNet::OutputArc_strategy)
def test_petrinet::outputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petriNet::OutputArc_strategy)
def test_petrinet::outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet::InputArc_strategy)
@settings(max_examples=50)
def test_petrinet::inputarc_instantiation(instance):
    assert isinstance(instance, petriNet::InputArc)

@given(instance=petriNet::InputArc_strategy)
def test_petrinet::inputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petriNet::InputArc_strategy)
def test_petrinet::inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::Transition_strategy)
def test_petrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet::GenericPlace_strategy)
@settings(max_examples=50)
def test_petrinet::genericplace_instantiation(instance):
    assert isinstance(instance, petriNet::GenericPlace)

@given(instance=petriNet::GenericPlace_strategy)
def test_petrinet::genericplace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::GenericPlace_strategy)
def test_petrinet::genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet::GenericPlace_strategy)
def test_petrinet::genericplace_numberOfTokens_type(instance):
    assert isinstance(instance.numberOfTokens, int)


@given(instance=petriNet::GenericPlace_strategy)
def test_petrinet::genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=petriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNet)

@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=petriNet::Resource_strategy)
@settings(max_examples=50)
def test_petrinet::resource_instantiation(instance):
    assert isinstance(instance, petriNet::Resource)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=petriNet::Place_strategy)
def test_petrinet::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=petriNet::Place_strategy)
def test_petrinet::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
