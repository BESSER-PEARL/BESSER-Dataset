import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    standardPetriNets_InputArc,
    standardPetriNets_PetriNet,
    standardPetriNets_OutputArc,
    standardPetriNets_Transition,
    standardPetriNets_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_standardpetrinets_inputarc_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets_InputArc)


def test_standardpetrinets_inputarc_constructor_exists():
    assert callable(standardPetriNets_InputArc.__init__)


def test_standardpetrinets_inputarc_constructor_args():
    sig = inspect.signature(standardPetriNets_InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_standardpetrinets_inputarc_has_weight():
    assert hasattr(standardPetriNets_InputArc, "weight")
    descriptor = None
    for klass in standardPetriNets_InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets_PetriNet)


def test_standardpetrinets_petrinet_constructor_exists():
    assert callable(standardPetriNets_PetriNet.__init__)


def test_standardpetrinets_petrinet_constructor_args():
    sig = inspect.signature(standardPetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_standardpetrinets_petrinet_has_name():
    assert hasattr(standardPetriNets_PetriNet, "name")
    descriptor = None
    for klass in standardPetriNets_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets_outputarc_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets_OutputArc)


def test_standardpetrinets_outputarc_constructor_exists():
    assert callable(standardPetriNets_OutputArc.__init__)


def test_standardpetrinets_outputarc_constructor_args():
    sig = inspect.signature(standardPetriNets_OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_standardpetrinets_outputarc_has_weight():
    assert hasattr(standardPetriNets_OutputArc, "weight")
    descriptor = None
    for klass in standardPetriNets_OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets_transition_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets_Transition)


def test_standardpetrinets_transition_constructor_exists():
    assert callable(standardPetriNets_Transition.__init__)


def test_standardpetrinets_transition_constructor_args():
    sig = inspect.signature(standardPetriNets_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_standardpetrinets_transition_has_name():
    assert hasattr(standardPetriNets_Transition, "name")
    descriptor = None
    for klass in standardPetriNets_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_standardpetrinets_place_is_not_abstract():
    assert not inspect.isabstract(standardPetriNets_Place)


def test_standardpetrinets_place_constructor_exists():
    assert callable(standardPetriNets_Place.__init__)


def test_standardpetrinets_place_constructor_args():
    sig = inspect.signature(standardPetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "numOfTokens" in params, "Missing parameter 'numOfTokens'"
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_standardpetrinets_place_has_numOfTokens():
    assert hasattr(standardPetriNets_Place, "numOfTokens")
    descriptor = None
    for klass in standardPetriNets_Place.__mro__:
        if "numOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numOfTokens"]
            break
    assert isinstance(descriptor, property)

def test_standardpetrinets_place_has_name():
    assert hasattr(standardPetriNets_Place, "name")
    descriptor = None
    for klass in standardPetriNets_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_standardpetrinets_place_has_capacity():
    assert hasattr(standardPetriNets_Place, "capacity")
    descriptor = None
    for klass in standardPetriNets_Place.__mro__:
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
standardPetriNets_InputArc_strategy = st.builds(
    standardPetriNets_InputArc,
    weight=
        st.integers()
)
standardPetriNets_PetriNet_strategy = st.builds(
    standardPetriNets_PetriNet,
    name=
        safe_text
)
standardPetriNets_OutputArc_strategy = st.builds(
    standardPetriNets_OutputArc,
    weight=
        st.integers()
)
standardPetriNets_Transition_strategy = st.builds(
    standardPetriNets_Transition,
    name=
        safe_text
)
standardPetriNets_Place_strategy = st.builds(
    standardPetriNets_Place,
    numOfTokens=
        st.integers(),
    name=
        safe_text,
    capacity=
        st.integers()
)

@given(instance=standardPetriNets_InputArc_strategy)
@settings(max_examples=50)
def test_standardpetrinets_inputarc_instantiation(instance):
    assert isinstance(instance, standardPetriNets_InputArc)



@given(instance=standardPetriNets_InputArc_strategy)
def test_standardpetrinets_inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=standardPetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_standardpetrinets_petrinet_instantiation(instance):
    assert isinstance(instance, standardPetriNets_PetriNet)



@given(instance=standardPetriNets_PetriNet_strategy)
def test_standardpetrinets_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=standardPetriNets_OutputArc_strategy)
@settings(max_examples=50)
def test_standardpetrinets_outputarc_instantiation(instance):
    assert isinstance(instance, standardPetriNets_OutputArc)



@given(instance=standardPetriNets_OutputArc_strategy)
def test_standardpetrinets_outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=standardPetriNets_Transition_strategy)
@settings(max_examples=50)
def test_standardpetrinets_transition_instantiation(instance):
    assert isinstance(instance, standardPetriNets_Transition)



@given(instance=standardPetriNets_Transition_strategy)
def test_standardpetrinets_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=standardPetriNets_Place_strategy)
@settings(max_examples=50)
def test_standardpetrinets_place_instantiation(instance):
    assert isinstance(instance, standardPetriNets_Place)



@given(instance=standardPetriNets_Place_strategy)
def test_standardpetrinets_place_numOfTokens_setter(instance):
    original = instance.numOfTokens
    instance.numOfTokens = original
    assert instance.numOfTokens == original



@given(instance=standardPetriNets_Place_strategy)
def test_standardpetrinets_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=standardPetriNets_Place_strategy)
def test_standardpetrinets_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
