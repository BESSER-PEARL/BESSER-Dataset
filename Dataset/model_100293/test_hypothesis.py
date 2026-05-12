import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petriNet_InputArc,
    petriNet_Transition,
    petriNet_GenericPlace,
    petriNet_PetriNet,
    petriNet_OutputArc,
    GenericPlace,
    petriNet_Resource,
    petriNet_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_inputarc_is_not_abstract():
    assert not inspect.isabstract(petriNet_InputArc)


def test_petrinet_inputarc_constructor_exists():
    assert callable(petriNet_InputArc.__init__)


def test_petrinet_inputarc_constructor_args():
    sig = inspect.signature(petriNet_InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_inputarc_has_weight():
    assert hasattr(petriNet_InputArc, "weight")
    descriptor = None
    for klass in petriNet_InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_transition_has_name():
    assert hasattr(petriNet_Transition, "name")
    descriptor = None
    for klass in petriNet_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_genericplace_is_not_abstract():
    assert not inspect.isabstract(petriNet_GenericPlace)


def test_petrinet_genericplace_constructor_exists():
    assert callable(petriNet_GenericPlace.__init__)


def test_petrinet_genericplace_constructor_args():
    sig = inspect.signature(petriNet_GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"

def test_petrinet_genericplace_has_name():
    assert hasattr(petriNet_GenericPlace, "name")
    descriptor = None
    for klass in petriNet_GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_genericplace_has_numberOfTokens():
    assert hasattr(petriNet_GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in petriNet_GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petriNet_PetriNet, "name")
    descriptor = None
    for klass in petriNet_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_outputarc_is_not_abstract():
    assert not inspect.isabstract(petriNet_OutputArc)


def test_petrinet_outputarc_constructor_exists():
    assert callable(petriNet_OutputArc.__init__)


def test_petrinet_outputarc_constructor_args():
    sig = inspect.signature(petriNet_OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_outputarc_has_weight():
    assert hasattr(petriNet_OutputArc, "weight")
    descriptor = None
    for klass in petriNet_OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_genericplace_is_not_abstract():
    assert not inspect.isabstract(GenericPlace)


def test_genericplace_constructor_exists():
    assert callable(GenericPlace.__init__)


def test_genericplace_constructor_args():
    sig = inspect.signature(GenericPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_resource_is_not_abstract():
    assert not inspect.isabstract(petriNet_Resource)


def test_petrinet_resource_constructor_exists():
    assert callable(petriNet_Resource.__init__)


def test_petrinet_resource_constructor_args():
    sig = inspect.signature(petriNet_Resource.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinet_place_has_capacity():
    assert hasattr(petriNet_Place, "capacity")
    descriptor = None
    for klass in petriNet_Place.__mro__:
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
petriNet_InputArc_strategy = st.builds(
    petriNet_InputArc,
    weight=
        st.integers()
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
    name=
        safe_text
)
petriNet_GenericPlace_strategy = st.builds(
    petriNet_GenericPlace,
    name=
        safe_text,
    numberOfTokens=
        st.integers()
)
petriNet_PetriNet_strategy = st.builds(
    petriNet_PetriNet,
    name=
        safe_text
)
petriNet_OutputArc_strategy = st.builds(
    petriNet_OutputArc,
    weight=
        st.integers()
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
petriNet_Resource_strategy = st.builds(
    petriNet_Resource,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    capacity=
        st.integers()
)

@given(instance=petriNet_InputArc_strategy)
@settings(max_examples=50)
def test_petrinet_inputarc_instantiation(instance):
    assert isinstance(instance, petriNet_InputArc)



@given(instance=petriNet_InputArc_strategy)
def test_petrinet_inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)



@given(instance=petriNet_Transition_strategy)
def test_petrinet_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet_GenericPlace_strategy)
@settings(max_examples=50)
def test_petrinet_genericplace_instantiation(instance):
    assert isinstance(instance, petriNet_GenericPlace)



@given(instance=petriNet_GenericPlace_strategy)
def test_petrinet_genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petriNet_GenericPlace_strategy)
def test_petrinet_genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=petriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNet)



@given(instance=petriNet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet_OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet_outputarc_instantiation(instance):
    assert isinstance(instance, petriNet_OutputArc)



@given(instance=petriNet_OutputArc_strategy)
def test_petrinet_outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=petriNet_Resource_strategy)
@settings(max_examples=50)
def test_petrinet_resource_instantiation(instance):
    assert isinstance(instance, petriNet_Resource)

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)



@given(instance=petriNet_Place_strategy)
def test_petrinet_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
