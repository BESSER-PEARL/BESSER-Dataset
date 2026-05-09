import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    resourcePetriNet::Transition,
    resourcePetriNet::GenericPlace,
    resourcePetriNet::PetriNet,
    GenericPlace,
    resourcePetriNet::Place,
    resourcePetriNet::Resource,
    resourcePetriNet::OutputArc,
    resourcePetriNet::InputArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resourcepetrinet::transition_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::Transition)


def test_resourcepetrinet::transition_constructor_exists():
    assert callable(resourcePetriNet::Transition.__init__)


def test_resourcepetrinet::transition_constructor_args():
    sig = inspect.signature(resourcePetriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet::transition_has_name():
    assert hasattr(resourcePetriNet::Transition, "name")
    descriptor = None
    for klass in resourcePetriNet::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet::genericplace_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::GenericPlace)


def test_resourcepetrinet::genericplace_constructor_exists():
    assert callable(resourcePetriNet::GenericPlace.__init__)


def test_resourcepetrinet::genericplace_constructor_args():
    sig = inspect.signature(resourcePetriNet::GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet::genericplace_has_numberOfTokens():
    assert hasattr(resourcePetriNet::GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in resourcePetriNet::GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_resourcepetrinet::genericplace_has_name():
    assert hasattr(resourcePetriNet::GenericPlace, "name")
    descriptor = None
    for klass in resourcePetriNet::GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::PetriNet)


def test_resourcepetrinet::petrinet_constructor_exists():
    assert callable(resourcePetriNet::PetriNet.__init__)


def test_resourcepetrinet::petrinet_constructor_args():
    sig = inspect.signature(resourcePetriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet::petrinet_has_name():
    assert hasattr(resourcePetriNet::PetriNet, "name")
    descriptor = None
    for klass in resourcePetriNet::PetriNet.__mro__:
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



def test_resourcepetrinet::place_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::Place)


def test_resourcepetrinet::place_constructor_exists():
    assert callable(resourcePetriNet::Place.__init__)


def test_resourcepetrinet::place_constructor_args():
    sig = inspect.signature(resourcePetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_resourcepetrinet::place_has_capacity():
    assert hasattr(resourcePetriNet::Place, "capacity")
    descriptor = None
    for klass in resourcePetriNet::Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet::resource_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::Resource)


def test_resourcepetrinet::resource_constructor_exists():
    assert callable(resourcePetriNet::Resource.__init__)


def test_resourcepetrinet::resource_constructor_args():
    sig = inspect.signature(resourcePetriNet::Resource.__init__)
    params = list(sig.parameters.keys())



def test_resourcepetrinet::outputarc_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::OutputArc)


def test_resourcepetrinet::outputarc_constructor_exists():
    assert callable(resourcePetriNet::OutputArc.__init__)


def test_resourcepetrinet::outputarc_constructor_args():
    sig = inspect.signature(resourcePetriNet::OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_resourcepetrinet::outputarc_has_weight():
    assert hasattr(resourcePetriNet::OutputArc, "weight")
    descriptor = None
    for klass in resourcePetriNet::OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet::inputarc_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet::InputArc)


def test_resourcepetrinet::inputarc_constructor_exists():
    assert callable(resourcePetriNet::InputArc.__init__)


def test_resourcepetrinet::inputarc_constructor_args():
    sig = inspect.signature(resourcePetriNet::InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_resourcepetrinet::inputarc_has_weight():
    assert hasattr(resourcePetriNet::InputArc, "weight")
    descriptor = None
    for klass in resourcePetriNet::InputArc.__mro__:
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
resourcePetriNet::Transition_strategy = st.builds(
    resourcePetriNet::Transition,
    name=
        safe_text
)
resourcePetriNet::GenericPlace_strategy = st.builds(
    resourcePetriNet::GenericPlace,
    numberOfTokens=
        st.integers(),
    name=
        safe_text
)
resourcePetriNet::PetriNet_strategy = st.builds(
    resourcePetriNet::PetriNet,
    name=
        safe_text
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
resourcePetriNet::Place_strategy = st.builds(
    resourcePetriNet::Place,
    capacity=
        st.integers()
)
resourcePetriNet::Resource_strategy = st.builds(
    resourcePetriNet::Resource,
)
resourcePetriNet::OutputArc_strategy = st.builds(
    resourcePetriNet::OutputArc,
    weight=
        st.integers()
)
resourcePetriNet::InputArc_strategy = st.builds(
    resourcePetriNet::InputArc,
    weight=
        st.integers()
)

@given(instance=resourcePetriNet::Transition_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::transition_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::Transition)

@given(instance=resourcePetriNet::Transition_strategy)
def test_resourcepetrinet::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=resourcePetriNet::Transition_strategy)
def test_resourcepetrinet::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resourcePetriNet::GenericPlace_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::genericplace_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::GenericPlace)

@given(instance=resourcePetriNet::GenericPlace_strategy)
def test_resourcepetrinet::genericplace_numberOfTokens_type(instance):
    assert isinstance(instance.numberOfTokens, int)


@given(instance=resourcePetriNet::GenericPlace_strategy)
def test_resourcepetrinet::genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=resourcePetriNet::GenericPlace_strategy)
def test_resourcepetrinet::genericplace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=resourcePetriNet::GenericPlace_strategy)
def test_resourcepetrinet::genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resourcePetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::petrinet_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::PetriNet)

@given(instance=resourcePetriNet::PetriNet_strategy)
def test_resourcepetrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=resourcePetriNet::PetriNet_strategy)
def test_resourcepetrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=resourcePetriNet::Place_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::place_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::Place)

@given(instance=resourcePetriNet::Place_strategy)
def test_resourcepetrinet::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=resourcePetriNet::Place_strategy)
def test_resourcepetrinet::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=resourcePetriNet::Resource_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::resource_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::Resource)

@given(instance=resourcePetriNet::OutputArc_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::outputarc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::OutputArc)

@given(instance=resourcePetriNet::OutputArc_strategy)
def test_resourcepetrinet::outputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=resourcePetriNet::OutputArc_strategy)
def test_resourcepetrinet::outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=resourcePetriNet::InputArc_strategy)
@settings(max_examples=50)
def test_resourcepetrinet::inputarc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet::InputArc)

@given(instance=resourcePetriNet::InputArc_strategy)
def test_resourcepetrinet::inputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=resourcePetriNet::InputArc_strategy)
def test_resourcepetrinet::inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
