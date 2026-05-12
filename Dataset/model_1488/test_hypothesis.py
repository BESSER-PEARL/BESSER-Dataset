import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNets_OutputArc,
    PetriNets_InputArc,
    PetriNets_Transition,
    PetriNets_PetriNet,
    PetriNets_Place,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets_outputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_OutputArc)


def test_petrinets_outputarc_constructor_exists():
    assert callable(PetriNets_OutputArc.__init__)


def test_petrinets_outputarc_constructor_args():
    sig = inspect.signature(PetriNets_OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets_outputarc_has_weight():
    assert hasattr(PetriNets_OutputArc, "weight")
    descriptor = None
    for klass in PetriNets_OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_inputarc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_InputArc)


def test_petrinets_inputarc_constructor_exists():
    assert callable(PetriNets_InputArc.__init__)


def test_petrinets_inputarc_constructor_args():
    sig = inspect.signature(PetriNets_InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinets_inputarc_has_weight():
    assert hasattr(PetriNets_InputArc, "weight")
    descriptor = None
    for klass in PetriNets_InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Transition)


def test_petrinets_transition_constructor_exists():
    assert callable(PetriNets_Transition.__init__)


def test_petrinets_transition_constructor_args():
    sig = inspect.signature(PetriNets_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_transition_has_name():
    assert hasattr(PetriNets_Transition, "name")
    descriptor = None
    for klass in PetriNets_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PetriNet)


def test_petrinets_petrinet_constructor_exists():
    assert callable(PetriNets_PetriNet.__init__)


def test_petrinets_petrinet_constructor_args():
    sig = inspect.signature(PetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_petrinet_has_name():
    assert hasattr(PetriNets_PetriNet, "name")
    descriptor = None
    for klass in PetriNets_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Place)


def test_petrinets_place_constructor_exists():
    assert callable(PetriNets_Place.__init__)


def test_petrinets_place_constructor_args():
    sig = inspect.signature(PetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"

def test_petrinets_place_has_name():
    assert hasattr(PetriNets_Place, "name")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinets_place_has_capacity():
    assert hasattr(PetriNets_Place, "capacity")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_petrinets_place_has_numberOfTokens():
    assert hasattr(PetriNets_Place, "numberOfTokens")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
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
PetriNets_OutputArc_strategy = st.builds(
    PetriNets_OutputArc,
    weight=
        st.integers()
)
PetriNets_InputArc_strategy = st.builds(
    PetriNets_InputArc,
    weight=
        st.integers()
)
PetriNets_Transition_strategy = st.builds(
    PetriNets_Transition,
    name=
        safe_text
)
PetriNets_PetriNet_strategy = st.builds(
    PetriNets_PetriNet,
    name=
        safe_text
)
PetriNets_Place_strategy = st.builds(
    PetriNets_Place,
    name=
        safe_text,
    capacity=
        st.integers(),
    numberOfTokens=
        st.integers()
)

@given(instance=PetriNets_OutputArc_strategy)
@settings(max_examples=50)
def test_petrinets_outputarc_instantiation(instance):
    assert isinstance(instance, PetriNets_OutputArc)



@given(instance=PetriNets_OutputArc_strategy)
def test_petrinets_outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets_InputArc_strategy)
@settings(max_examples=50)
def test_petrinets_inputarc_instantiation(instance):
    assert isinstance(instance, PetriNets_InputArc)



@given(instance=PetriNets_InputArc_strategy)
def test_petrinets_inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNets_Transition_strategy)
@settings(max_examples=50)
def test_petrinets_transition_instantiation(instance):
    assert isinstance(instance, PetriNets_Transition)



@given(instance=PetriNets_Transition_strategy)
def test_petrinets_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets_PetriNet)



@given(instance=PetriNets_PetriNet_strategy)
def test_petrinets_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=50)
def test_petrinets_place_instantiation(instance):
    assert isinstance(instance, PetriNets_Place)



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original
