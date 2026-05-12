import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    resourcePetriNet_GenericPlace,
    resourcePetriNet_PetriNet,
    GenericPlace,
    resourcePetriNet_Place,
    resourcePetriNet_Resource,
    resourcePetriNet_OutputArc,
    resourcePetriNet_InputArc,
    resourcePetriNet_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resourcepetrinet_genericplace_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_GenericPlace)


def test_resourcepetrinet_genericplace_constructor_exists():
    assert callable(resourcePetriNet_GenericPlace.__init__)


def test_resourcepetrinet_genericplace_constructor_args():
    sig = inspect.signature(resourcePetriNet_GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet_genericplace_has_numberOfTokens():
    assert hasattr(resourcePetriNet_GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in resourcePetriNet_GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_resourcepetrinet_genericplace_has_name():
    assert hasattr(resourcePetriNet_GenericPlace, "name")
    descriptor = None
    for klass in resourcePetriNet_GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_PetriNet)


def test_resourcepetrinet_petrinet_constructor_exists():
    assert callable(resourcePetriNet_PetriNet.__init__)


def test_resourcepetrinet_petrinet_constructor_args():
    sig = inspect.signature(resourcePetriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet_petrinet_has_name():
    assert hasattr(resourcePetriNet_PetriNet, "name")
    descriptor = None
    for klass in resourcePetriNet_PetriNet.__mro__:
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



def test_resourcepetrinet_place_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_Place)


def test_resourcepetrinet_place_constructor_exists():
    assert callable(resourcePetriNet_Place.__init__)


def test_resourcepetrinet_place_constructor_args():
    sig = inspect.signature(resourcePetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_resourcepetrinet_place_has_capacity():
    assert hasattr(resourcePetriNet_Place, "capacity")
    descriptor = None
    for klass in resourcePetriNet_Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet_resource_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_Resource)


def test_resourcepetrinet_resource_constructor_exists():
    assert callable(resourcePetriNet_Resource.__init__)


def test_resourcepetrinet_resource_constructor_args():
    sig = inspect.signature(resourcePetriNet_Resource.__init__)
    params = list(sig.parameters.keys())



def test_resourcepetrinet_outputarc_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_OutputArc)


def test_resourcepetrinet_outputarc_constructor_exists():
    assert callable(resourcePetriNet_OutputArc.__init__)


def test_resourcepetrinet_outputarc_constructor_args():
    sig = inspect.signature(resourcePetriNet_OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_resourcepetrinet_outputarc_has_weight():
    assert hasattr(resourcePetriNet_OutputArc, "weight")
    descriptor = None
    for klass in resourcePetriNet_OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet_inputarc_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_InputArc)


def test_resourcepetrinet_inputarc_constructor_exists():
    assert callable(resourcePetriNet_InputArc.__init__)


def test_resourcepetrinet_inputarc_constructor_args():
    sig = inspect.signature(resourcePetriNet_InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_resourcepetrinet_inputarc_has_weight():
    assert hasattr(resourcePetriNet_InputArc, "weight")
    descriptor = None
    for klass in resourcePetriNet_InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_resourcepetrinet_transition_is_not_abstract():
    assert not inspect.isabstract(resourcePetriNet_Transition)


def test_resourcepetrinet_transition_constructor_exists():
    assert callable(resourcePetriNet_Transition.__init__)


def test_resourcepetrinet_transition_constructor_args():
    sig = inspect.signature(resourcePetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resourcepetrinet_transition_has_name():
    assert hasattr(resourcePetriNet_Transition, "name")
    descriptor = None
    for klass in resourcePetriNet_Transition.__mro__:
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
resourcePetriNet_GenericPlace_strategy = st.builds(
    resourcePetriNet_GenericPlace,
    numberOfTokens=
        st.integers(),
    name=
        safe_text
)
resourcePetriNet_PetriNet_strategy = st.builds(
    resourcePetriNet_PetriNet,
    name=
        safe_text
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
resourcePetriNet_Place_strategy = st.builds(
    resourcePetriNet_Place,
    capacity=
        st.integers()
)
resourcePetriNet_Resource_strategy = st.builds(
    resourcePetriNet_Resource,
)
resourcePetriNet_OutputArc_strategy = st.builds(
    resourcePetriNet_OutputArc,
    weight=
        st.integers()
)
resourcePetriNet_InputArc_strategy = st.builds(
    resourcePetriNet_InputArc,
    weight=
        st.integers()
)
resourcePetriNet_Transition_strategy = st.builds(
    resourcePetriNet_Transition,
    name=
        safe_text
)

@given(instance=resourcePetriNet_GenericPlace_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_genericplace_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_GenericPlace)



@given(instance=resourcePetriNet_GenericPlace_strategy)
def test_resourcepetrinet_genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original



@given(instance=resourcePetriNet_GenericPlace_strategy)
def test_resourcepetrinet_genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resourcePetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_petrinet_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_PetriNet)



@given(instance=resourcePetriNet_PetriNet_strategy)
def test_resourcepetrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=resourcePetriNet_Place_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_place_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Place)



@given(instance=resourcePetriNet_Place_strategy)
def test_resourcepetrinet_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=resourcePetriNet_Resource_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_resource_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Resource)

@given(instance=resourcePetriNet_OutputArc_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_outputarc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_OutputArc)



@given(instance=resourcePetriNet_OutputArc_strategy)
def test_resourcepetrinet_outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=resourcePetriNet_InputArc_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_inputarc_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_InputArc)



@given(instance=resourcePetriNet_InputArc_strategy)
def test_resourcepetrinet_inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=resourcePetriNet_Transition_strategy)
@settings(max_examples=50)
def test_resourcepetrinet_transition_instantiation(instance):
    assert isinstance(instance, resourcePetriNet_Transition)



@given(instance=resourcePetriNet_Transition_strategy)
def test_resourcepetrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
