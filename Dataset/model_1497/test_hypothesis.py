import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    PetriNet_Transition,
    PetriNet_Place,
    PetriNet_Arc,
    PetriNet_Element,
    PetriNet_PetriNetRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_petrinet_transition_has_maxTime():
    assert hasattr(PetriNet_Transition, "maxTime")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_transition_has_minTime():
    assert hasattr(PetriNet_Transition, "minTime")
    descriptor = None
    for klass in PetriNet_Transition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "Tokens" in params, "Missing parameter 'Tokens'"

def test_petrinet_place_has_Tokens():
    assert hasattr(PetriNet_Place, "Tokens")
    descriptor = None
    for klass in PetriNet_Place.__mro__:
        if "Tokens" in klass.__dict__:
            descriptor = klass.__dict__["Tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(PetriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(PetriNet_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_element_has_name():
    assert hasattr(PetriNet_Element, "name")
    descriptor = None
    for klass in PetriNet_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinetroot_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNetRoot)


def test_petrinet_petrinetroot_constructor_exists():
    assert callable(PetriNet_PetriNetRoot.__init__)


def test_petrinet_petrinetroot_constructor_args():
    sig = inspect.signature(PetriNet_PetriNetRoot.__init__)
    params = list(sig.parameters.keys())


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
Element_strategy = st.builds(
    Element,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
    Tokens=
        st.integers()
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
)
PetriNet_Element_strategy = st.builds(
    PetriNet_Element,
    name=
        safe_text
)
PetriNet_PetriNetRoot_strategy = st.builds(
    PetriNet_PetriNetRoot,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original



@given(instance=PetriNet_Transition_strategy)
def test_petrinet_transition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)



@given(instance=PetriNet_Place_strategy)
def test_petrinet_place_Tokens_setter(instance):
    original = instance.Tokens
    instance.Tokens = original
    assert instance.Tokens == original

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)

@given(instance=PetriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, PetriNet_Element)



@given(instance=PetriNet_Element_strategy)
def test_petrinet_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_PetriNetRoot_strategy)
@settings(max_examples=50)
def test_petrinet_petrinetroot_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNetRoot)
