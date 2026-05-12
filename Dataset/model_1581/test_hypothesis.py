import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Noeud,
    petrinet_Transition,
    petrinet_Arc,
    petrinet_Noeud,
    petrinet_PetriNet,
    petrinet_Place,
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



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minTime" in params, "Missing parameter 'minTime'"
    assert "maxTime" in params, "Missing parameter 'maxTime'"

def test_petrinet_transition_has_minTime():
    assert hasattr(petrinet_Transition, "minTime")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_maxTime():
    assert hasattr(petrinet_Transition, "maxTime")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "arcType" in params, "Missing parameter 'arcType'"

def test_petrinet_arc_has_name():
    assert hasattr(petrinet_Arc, "name")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_weight():
    assert hasattr(petrinet_Arc, "weight")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_arcType():
    assert hasattr(petrinet_Arc, "arcType")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "arcType" in klass.__dict__:
            descriptor = klass.__dict__["arcType"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_noeud_is_not_abstract():
    assert not inspect.isabstract(petrinet_Noeud)


def test_petrinet_noeud_constructor_exists():
    assert callable(petrinet_Noeud.__init__)


def test_petrinet_noeud_constructor_args():
    sig = inspect.signature(petrinet_Noeud.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_noeud_has_name():
    assert hasattr(petrinet_Noeud, "name")
    descriptor = None
    for klass in petrinet_Noeud.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_petrinet_has_name():
    assert hasattr(petrinet_PetriNet, "name")
    descriptor = None
    for klass in petrinet_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petrinet_place_has_marking():
    assert hasattr(petrinet_Place, "marking")
    descriptor = None
    for klass in petrinet_Place.__mro__:
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
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    minTime=
        st.integers(),
    maxTime=
        st.integers()
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    name=
        safe_text,
    weight=
        st.integers(),
    arcType=
        safe_text
)
petrinet_Noeud_strategy = st.builds(
    petrinet_Noeud,
    name=
        safe_text
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
    name=
        safe_text
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    marking=
        st.integers()
)

@given(instance=Noeud_strategy)
@settings(max_examples=50)
def test_noeud_instantiation(instance):
    assert isinstance(instance, Noeud)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_arcType_setter(instance):
    original = instance.arcType
    instance.arcType = original
    assert instance.arcType == original

@given(instance=petrinet_Noeud_strategy)
@settings(max_examples=50)
def test_petrinet_noeud_instantiation(instance):
    assert isinstance(instance, petrinet_Noeud)



@given(instance=petrinet_Noeud_strategy)
def test_petrinet_noeud_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)



@given(instance=petrinet_PetriNet_strategy)
def test_petrinet_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original
