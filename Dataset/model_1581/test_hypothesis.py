import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Noeud,
    petrinet::Transition,
    petrinet::Arc,
    petrinet::Noeud,
    petrinet::PetriNet,
    petrinet::Place,
    ArcKindType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_noeud_is_not_abstract():
    assert not inspect.isabstract(Noeud)


def test_noeud_constructor_exists():
    assert callable(Noeud.__init__)


def test_noeud_constructor_args():
    sig = inspect.signature(Noeud.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_petrinet::transition_has_minTime():
    assert hasattr(petrinet::Transition, "minTime")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::transition_has_maxTime():
    assert hasattr(petrinet::Transition, "maxTime")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "arcType" in params, "Missing parameter 'arcType'"
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_name():
    assert hasattr(petrinet::Arc, "name")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_arcType():
    assert hasattr(petrinet::Arc, "arcType")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "arcType" in klass.__dict__:
            descriptor = klass.__dict__["arcType"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::arc_has_weight():
    assert hasattr(petrinet::Arc, "weight")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::noeud_is_not_abstract():
    assert not inspect.isabstract(petrinet::Noeud)


def test_petrinet::noeud_constructor_exists():
    assert callable(petrinet::Noeud.__init__)


def test_petrinet::noeud_constructor_args():
    sig = inspect.signature(petrinet::Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::noeud_has_name():
    assert hasattr(petrinet::Noeud, "name")
    descriptor = None
    for klass in petrinet::Noeud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petrinet::PetriNet, "name")
    descriptor = None
    for klass in petrinet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet::place_has_marking():
    assert hasattr(petrinet::Place, "marking")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)

def test_arckindtype_exists():
    # Check that the Enumeration exists
    assert ArcKindType is not None

def test_arckindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcKindType]
    expected_literals = [
        "read_arc",
        "normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcKindType"


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
Noeud_strategy = st.builds(
    Noeud,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    name=
        safe_text,
    arcType=
        safe_text,
    weight=
        st.integers()
)
petrinet::Noeud_strategy = st.builds(
    petrinet::Noeud,
    name=
        safe_text
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
    name=
        safe_text
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    marking=
        st.integers()
)

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_arcType_type(instance):
    assert isinstance(instance.arcType, str)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_arcType_setter(instance):
    original = instance.arcType
    instance.arcType = original
    assert instance.arcType == original

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petrinet::Noeud_strategy)
@settings(max_examples=50)
def test_petrinet::noeud_instantiation(instance):
    assert isinstance(instance, petrinet::Noeud)

@given(instance=petrinet::Noeud_strategy)
def test_petrinet::noeud_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Noeud_strategy)
def test_petrinet::noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_marking_type(instance):
    assert isinstance(instance.marking, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original
