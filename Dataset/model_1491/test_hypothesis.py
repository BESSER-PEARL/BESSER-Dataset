import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extendedPetriNets_GenericPlace,
    GenericPlace,
    extendedPetriNets_OutputPort,
    extendedPetriNets_InputPort,
    extendedPetriNets_Place,
    extendedPetriNets_OutputArc,
    extendedPetriNets_InputArc,
    extendedPetriNets_Transition,
    extendedPetriNets_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extendedpetrinets_genericplace_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_GenericPlace)


def test_extendedpetrinets_genericplace_constructor_exists():
    assert callable(extendedPetriNets_GenericPlace.__init__)


def test_extendedpetrinets_genericplace_constructor_args():
    sig = inspect.signature(extendedPetriNets_GenericPlace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "numberOfTokens" in params, "Missing parameter 'numberOfTokens'"

def test_extendedpetrinets_genericplace_has_name():
    assert hasattr(extendedPetriNets_GenericPlace, "name")
    descriptor = None
    for klass in extendedPetriNets_GenericPlace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_extendedpetrinets_genericplace_has_capacity():
    assert hasattr(extendedPetriNets_GenericPlace, "capacity")
    descriptor = None
    for klass in extendedPetriNets_GenericPlace.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_extendedpetrinets_genericplace_has_numberOfTokens():
    assert hasattr(extendedPetriNets_GenericPlace, "numberOfTokens")
    descriptor = None
    for klass in extendedPetriNets_GenericPlace.__mro__:
        if "numberOfTokens" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTokens"]
            break
    assert isinstance(descriptor, property)



def test_genericplace_is_not_abstract():
    assert not inspect.isabstract(GenericPlace)


def test_genericplace_constructor_exists():
    assert callable(GenericPlace.__init__)


def test_genericplace_constructor_args():
    sig = inspect.signature(GenericPlace.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets_outputport_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_OutputPort)


def test_extendedpetrinets_outputport_constructor_exists():
    assert callable(extendedPetriNets_OutputPort.__init__)


def test_extendedpetrinets_outputport_constructor_args():
    sig = inspect.signature(extendedPetriNets_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets_inputport_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_InputPort)


def test_extendedpetrinets_inputport_constructor_exists():
    assert callable(extendedPetriNets_InputPort.__init__)


def test_extendedpetrinets_inputport_constructor_args():
    sig = inspect.signature(extendedPetriNets_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets_place_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_Place)


def test_extendedpetrinets_place_constructor_exists():
    assert callable(extendedPetriNets_Place.__init__)


def test_extendedpetrinets_place_constructor_args():
    sig = inspect.signature(extendedPetriNets_Place.__init__)
    params = list(sig.parameters.keys())



def test_extendedpetrinets_outputarc_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_OutputArc)


def test_extendedpetrinets_outputarc_constructor_exists():
    assert callable(extendedPetriNets_OutputArc.__init__)


def test_extendedpetrinets_outputarc_constructor_args():
    sig = inspect.signature(extendedPetriNets_OutputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_extendedpetrinets_outputarc_has_weight():
    assert hasattr(extendedPetriNets_OutputArc, "weight")
    descriptor = None
    for klass in extendedPetriNets_OutputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets_inputarc_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_InputArc)


def test_extendedpetrinets_inputarc_constructor_exists():
    assert callable(extendedPetriNets_InputArc.__init__)


def test_extendedpetrinets_inputarc_constructor_args():
    sig = inspect.signature(extendedPetriNets_InputArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_extendedpetrinets_inputarc_has_weight():
    assert hasattr(extendedPetriNets_InputArc, "weight")
    descriptor = None
    for klass in extendedPetriNets_InputArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets_transition_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_Transition)


def test_extendedpetrinets_transition_constructor_exists():
    assert callable(extendedPetriNets_Transition.__init__)


def test_extendedpetrinets_transition_constructor_args():
    sig = inspect.signature(extendedPetriNets_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extendedpetrinets_transition_has_name():
    assert hasattr(extendedPetriNets_Transition, "name")
    descriptor = None
    for klass in extendedPetriNets_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extendedpetrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(extendedPetriNets_PetriNet)


def test_extendedpetrinets_petrinet_constructor_exists():
    assert callable(extendedPetriNets_PetriNet.__init__)


def test_extendedpetrinets_petrinet_constructor_args():
    sig = inspect.signature(extendedPetriNets_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extendedpetrinets_petrinet_has_name():
    assert hasattr(extendedPetriNets_PetriNet, "name")
    descriptor = None
    for klass in extendedPetriNets_PetriNet.__mro__:
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
extendedPetriNets_GenericPlace_strategy = st.builds(
    extendedPetriNets_GenericPlace,
    name=
        safe_text,
    capacity=
        st.integers(),
    numberOfTokens=
        st.integers()
)
GenericPlace_strategy = st.builds(
    GenericPlace,
)
extendedPetriNets_OutputPort_strategy = st.builds(
    extendedPetriNets_OutputPort,
)
extendedPetriNets_InputPort_strategy = st.builds(
    extendedPetriNets_InputPort,
)
extendedPetriNets_Place_strategy = st.builds(
    extendedPetriNets_Place,
)
extendedPetriNets_OutputArc_strategy = st.builds(
    extendedPetriNets_OutputArc,
    weight=
        st.integers()
)
extendedPetriNets_InputArc_strategy = st.builds(
    extendedPetriNets_InputArc,
    weight=
        st.integers()
)
extendedPetriNets_Transition_strategy = st.builds(
    extendedPetriNets_Transition,
    name=
        safe_text
)
extendedPetriNets_PetriNet_strategy = st.builds(
    extendedPetriNets_PetriNet,
    name=
        safe_text
)

@given(instance=extendedPetriNets_GenericPlace_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_genericplace_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_GenericPlace)



@given(instance=extendedPetriNets_GenericPlace_strategy)
def test_extendedpetrinets_genericplace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=extendedPetriNets_GenericPlace_strategy)
def test_extendedpetrinets_genericplace_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=extendedPetriNets_GenericPlace_strategy)
def test_extendedpetrinets_genericplace_numberOfTokens_setter(instance):
    original = instance.numberOfTokens
    instance.numberOfTokens = original
    assert instance.numberOfTokens == original

@given(instance=GenericPlace_strategy)
@settings(max_examples=50)
def test_genericplace_instantiation(instance):
    assert isinstance(instance, GenericPlace)

@given(instance=extendedPetriNets_OutputPort_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_outputport_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_OutputPort)

@given(instance=extendedPetriNets_InputPort_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_inputport_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_InputPort)

@given(instance=extendedPetriNets_Place_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_place_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_Place)

@given(instance=extendedPetriNets_OutputArc_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_outputarc_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_OutputArc)



@given(instance=extendedPetriNets_OutputArc_strategy)
def test_extendedpetrinets_outputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=extendedPetriNets_InputArc_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_inputarc_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_InputArc)



@given(instance=extendedPetriNets_InputArc_strategy)
def test_extendedpetrinets_inputarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=extendedPetriNets_Transition_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_transition_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_Transition)



@given(instance=extendedPetriNets_Transition_strategy)
def test_extendedpetrinets_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extendedPetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_extendedpetrinets_petrinet_instantiation(instance):
    assert isinstance(instance, extendedPetriNets_PetriNet)



@given(instance=extendedPetriNets_PetriNet_strategy)
def test_extendedpetrinets_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
