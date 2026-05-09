import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    extendedPetriNets::OutputArc,
    extendedPetriNets::InputArc,
    extendedPetriNets::Transition,
    GenericPlace,
    extendedPetriNets::Place,
    extendedPetriNets::InputPort,
    extendedPetriNets::OutputPort,
    extendedPetriNets::GenericPlace,
    extendedPetriNets::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extendedpetrinets::outputarc_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::OutputArc)


def test_extendedpetrinets::outputarc_constructor_exists():
    assert callable(extendedPetriNets::OutputArc.__init__)


def test_extendedpetrinets::outputarc_constructor_args():
    sig = inspect.signature(extendedPetriNets::OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_extendedpetrinets::outputarc_has_weight():
    assert hasattr(extendedPetriNets::OutputArc, "weight")
    descriptor = None
    for klass in extendedPetriNets::OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets::inputarc_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::InputArc)


def test_extendedpetrinets::inputarc_constructor_exists():
    assert callable(extendedPetriNets::InputArc.__init__)


def test_extendedpetrinets::inputarc_constructor_args():
    sig = inspect.signature(extendedPetriNets::InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_extendedpetrinets::inputarc_has_weight():
    assert hasattr(extendedPetriNets::InputArc, "weight")
    descriptor = None
    for klass in extendedPetriNets::InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets::transition_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::Transition)


def test_extendedpetrinets::transition_constructor_exists():
    assert callable(extendedPetriNets::Transition.__init__)


def test_extendedpetrinets::transition_constructor_args():
    sig = inspect.signature(extendedPetriNets::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "label" in params, "Missing parameter 'label'"

def test_extendedpetrinets::transition_has_name():
    assert hasattr(extendedPetriNets::Transition, "name")
    descriptor = None
    for klass in extendedPetriNets::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_extendedpetrinets::transition_has_label():
    assert hasattr(extendedPetriNets::Transition, "label")
    descriptor = None
    for klass in extendedPetriNets::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_genericplace_is_not_abstract():
    assert not inspect.isabstract(GenericPlace)


def test_genericplace_constructor_exists():
    assert callable(GenericPlace.__init__)


def test_genericplace_constructor_args():
    sig = inspect.signature(GenericPlace.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets::place_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::Place)


def test_extendedpetrinets::place_constructor_exists():
    assert callable(extendedPetriNets::Place.__init__)


def test_extendedpetrinets::place_constructor_args():
    sig = inspect.signature(extendedPetriNets::Place.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets::inputport_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::InputPort)


def test_extendedpetrinets::inputport_constructor_exists():
    assert callable(extendedPetriNets::InputPort.__init__)


def test_extendedpetrinets::inputport_constructor_args():
    sig = inspect.signature(extendedPetriNets::InputPort.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets::outputport_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::OutputPort)


def test_extendedpetrinets::outputport_constructor_exists():
    assert callable(extendedPetriNets::OutputPort.__init__)


def test_extendedpetrinets::outputport_constructor_args():
    sig = inspect.signature(extendedPetriNets::OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets::genericplace_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::GenericPlace)


def test_extendedpetrinets::genericplace_constructor_exists():
    assert callable(extendedPetriNets::GenericPlace.__init__)


def test_extendedpetrinets::genericplace_constructor_args():
    sig = inspect.signature(extendedPetriNets::GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_extendedpetrinets::genericplace_has_numberOfTokens():
    assert hasattr(extendedPetriNets::GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in extendedPetriNets::GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_extendedpetrinets::genericplace_has_name():
    assert hasattr(extendedPetriNets::GenericPlace, "name")
    descriptor = None
    for klass in extendedPetriNets::GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_extendedpetrinets::genericplace_has_capacity():
    assert hasattr(extendedPetriNets::GenericPlace, "capacity")
    descriptor = None
    for klass in extendedPetriNets::GenericPlace.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets::PetriNet)


def test_extendedpetrinets::petrinet_constructor_exists():
    assert callable(extendedPetriNets::PetriNet.__init__)


def test_extendedpetrinets::petrinet_constructor_args():
    sig = inspect.signature(extendedPetriNets::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extendedpetrinets::petrinet_has_name():
    assert hasattr(extendedPetriNets::PetriNet, "name")
    descriptor = None
    for klass in extendedPetriNets::PetriNet.__mro__:
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
extendedPetriNets::OutputArc_strategy = st.builds(
    extendedPetriNets::OutputArc,
    weight=
        st.integers()
)
extendedPetriNets::InputArc_strategy = st.builds(
    extendedPetriNets::InputArc,
    weight=
        st.integers()
)
extendedPetriNets::Transition_strategy = st.builds(
    extendedPetriNets::Transition,
    name=
        safe_text,
    label=
        safe_text
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
extendedPetriNets::Place_strategy = st.builds(
    extendedPetriNets::Place,
)
extendedPetriNets::InputPort_strategy = st.builds(
    extendedPetriNets::InputPort,
)
extendedPetriNets::OutputPort_strategy = st.builds(
    extendedPetriNets::OutputPort,
)
extendedPetriNets::GenericPlace_strategy = st.builds(
    extendedPetriNets::GenericPlace,
    numberOfTokens=
        st.integers(),
    name=
        safe_text,
    capacity=
        st.integers()
)
extendedPetriNets::PetriNet_strategy = st.builds(
    extendedPetriNets::PetriNet,
    name=
        safe_text
)

@given(instance=extendedPetriNets::OutputArc_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::outputarc_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::OutputArc)

@given(instance=extendedPetriNets::OutputArc_strategy)
def test_extendedpetrinets::outputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=extendedPetriNets::OutputArc_strategy)
def test_extendedpetrinets::outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=extendedPetriNets::InputArc_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::inputarc_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::InputArc)

@given(instance=extendedPetriNets::InputArc_strategy)
def test_extendedpetrinets::inputarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=extendedPetriNets::InputArc_strategy)
def test_extendedpetrinets::inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=extendedPetriNets::Transition_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::transition_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::Transition)

@given(instance=extendedPetriNets::Transition_strategy)
def test_extendedpetrinets::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extendedPetriNets::Transition_strategy)
def test_extendedpetrinets::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extendedPetriNets::Transition_strategy)
def test_extendedpetrinets::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=extendedPetriNets::Transition_strategy)
def test_extendedpetrinets::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=extendedPetriNets::Place_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::place_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::Place)

@given(instance=extendedPetriNets::InputPort_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::inputport_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::InputPort)

@given(instance=extendedPetriNets::OutputPort_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::outputport_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::OutputPort)

@given(instance=extendedPetriNets::GenericPlace_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::genericplace_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::GenericPlace)

@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_numberOfTokens_type(instance):
    assert isinstance(instance.numberOfTokens, int)


@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=extendedPetriNets::GenericPlace_strategy)
def test_extendedpetrinets::genericplace_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=extendedPetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_extendedpetrinets::petrinet_instantiation(instance):
    assert isinstance(instance, extendedPetriNets::PetriNet)

@given(instance=extendedPetriNets::PetriNet_strategy)
def test_extendedpetrinets::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extendedPetriNets::PetriNet_strategy)
def test_extendedpetrinets::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
