import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet2::Element,
    petrinet2::Petrinet,
    Node,
    petrinet2::Transition,
    petrinet2::Place,
    Element,
    petrinet2::Arc,
    petrinet2::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet2::element_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Element)


def test_petrinet2::element_constructor_exists():
    assert callable(petrinet2::Element.__init__)


def test_petrinet2::element_constructor_args():
    sig = inspect.signature(petrinet2::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet2::element_has_name():
    assert hasattr(petrinet2::Element, "name")
    descriptor = None
    for klass in petrinet2::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Petrinet)


def test_petrinet2::petrinet_constructor_exists():
    assert callable(petrinet2::Petrinet.__init__)


def test_petrinet2::petrinet_constructor_args():
    sig = inspect.signature(petrinet2::Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Transition)


def test_petrinet2::transition_constructor_exists():
    assert callable(petrinet2::Transition.__init__)


def test_petrinet2::transition_constructor_args():
    sig = inspect.signature(petrinet2::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"
    assert "minDelay" in params, "Missing parameter 'minDelay'"

def test_petrinet2::transition_has_maxDelay():
    assert hasattr(petrinet2::Transition, "maxDelay")
    descriptor = None
    for klass in petrinet2::Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet2::transition_has_minDelay():
    assert hasattr(petrinet2::Transition, "minDelay")
    descriptor = None
    for klass in petrinet2::Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)



def test_petrinet2::place_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Place)


def test_petrinet2::place_constructor_exists():
    assert callable(petrinet2::Place.__init__)


def test_petrinet2::place_constructor_args():
    sig = inspect.signature(petrinet2::Place.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Arc)


def test_petrinet2::arc_constructor_exists():
    assert callable(petrinet2::Arc.__init__)


def test_petrinet2::arc_constructor_args():
    sig = inspect.signature(petrinet2::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet2::node_is_not_abstract():
    assert not inspect.isabstract(petrinet2::Node)


def test_petrinet2::node_constructor_exists():
    assert callable(petrinet2::Node.__init__)


def test_petrinet2::node_constructor_args():
    sig = inspect.signature(petrinet2::Node.__init__)
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
petrinet2::Element_strategy = st.builds(
    petrinet2::Element,
    name=
        safe_text
)
petrinet2::Petrinet_strategy = st.builds(
    petrinet2::Petrinet,
)
Node_strategy = st.builds(
    Node,
)
petrinet2::Transition_strategy = st.builds(
    petrinet2::Transition,
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
petrinet2::Place_strategy = st.builds(
    petrinet2::Place,
)
Element_strategy = st.builds(
    Element,
)
petrinet2::Arc_strategy = st.builds(
    petrinet2::Arc,
)
petrinet2::Node_strategy = st.builds(
    petrinet2::Node,
)

@given(instance=petrinet2::Element_strategy)
@settings(max_examples=50)
def test_petrinet2::element_instantiation(instance):
    assert isinstance(instance, petrinet2::Element)

@given(instance=petrinet2::Element_strategy)
def test_petrinet2::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet2::Element_strategy)
def test_petrinet2::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet2::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet2::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet2::Petrinet)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet2::Transition_strategy)
@settings(max_examples=50)
def test_petrinet2::transition_instantiation(instance):
    assert isinstance(instance, petrinet2::Transition)

@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_maxDelay_type(instance):
    assert isinstance(instance.maxDelay, float)


@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_minDelay_type(instance):
    assert isinstance(instance.minDelay, float)


@given(instance=petrinet2::Transition_strategy)
def test_petrinet2::transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=petrinet2::Place_strategy)
@settings(max_examples=50)
def test_petrinet2::place_instantiation(instance):
    assert isinstance(instance, petrinet2::Place)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet2::Arc_strategy)
@settings(max_examples=50)
def test_petrinet2::arc_instantiation(instance):
    assert isinstance(instance, petrinet2::Arc)

@given(instance=petrinet2::Node_strategy)
@settings(max_examples=50)
def test_petrinet2::node_instantiation(instance):
    assert isinstance(instance, petrinet2::Node)
