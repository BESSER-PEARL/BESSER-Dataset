import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::Arc,
    PetriNet::Element,
    PetriNet::PetriNetRoot,
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



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxTime" in params, "Missing parameter 'maxTime'"
    assert "minTime" in params, "Missing parameter 'minTime'"

def test_petrinet::transition_has_maxTime():
    assert hasattr(PetriNet::Transition, "maxTime")
    descriptor = None
    for klass in PetriNet::Transition.__mro__:
        if "maxTime" in klass.__dict__:
            descriptor = klass.__dict__["maxTime"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::transition_has_minTime():
    assert hasattr(PetriNet::Transition, "minTime")
    descriptor = None
    for klass in PetriNet::Transition.__mro__:
        if "minTime" in klass.__dict__:
            descriptor = klass.__dict__["minTime"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "Tokens" in params, "Missing parameter 'Tokens'"

def test_petrinet::place_has_Tokens():
    assert hasattr(PetriNet::Place, "Tokens")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "Tokens" in klass.__dict__:
            descriptor = klass.__dict__["Tokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(PetriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(PetriNet::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::element_has_name():
    assert hasattr(PetriNet::Element, "name")
    descriptor = None
    for klass in PetriNet::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinetroot_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNetRoot)


def test_petrinet::petrinetroot_constructor_exists():
    assert callable(PetriNet::PetriNetRoot.__init__)


def test_petrinet::petrinetroot_constructor_args():
    sig = inspect.signature(PetriNet::PetriNetRoot.__init__)
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
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
    maxTime=
        st.integers(),
    minTime=
        st.integers()
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    Tokens=
        st.integers()
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
)
PetriNet::Element_strategy = st.builds(
    PetriNet::Element,
    name=
        safe_text
)
PetriNet::PetriNetRoot_strategy = st.builds(
    PetriNet::PetriNetRoot,
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_maxTime_type(instance):
    assert isinstance(instance.maxTime, int)


@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_maxTime_setter(instance):
    original = instance.maxTime
    instance.maxTime = original
    assert instance.maxTime == original

@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_minTime_type(instance):
    assert isinstance(instance.minTime, int)


@given(instance=PetriNet::Transition_strategy)
def test_petrinet::transition_minTime_setter(instance):
    original = instance.minTime
    instance.minTime = original
    assert instance.minTime == original

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_Tokens_type(instance):
    assert isinstance(instance.Tokens, int)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_Tokens_setter(instance):
    original = instance.Tokens
    instance.Tokens = original
    assert instance.Tokens == original

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, PetriNet::Element)

@given(instance=PetriNet::Element_strategy)
def test_petrinet::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Element_strategy)
def test_petrinet::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::PetriNetRoot_strategy)
@settings(max_examples=50)
def test_petrinet::petrinetroot_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNetRoot)
