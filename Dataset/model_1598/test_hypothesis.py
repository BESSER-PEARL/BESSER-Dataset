import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    Petrinet::Place,
    Petrinet::Transition,
    Arc,
    Petrinet::InputArc,
    Petrinet::OutputArc,
    Element,
    Petrinet::Arc,
    Petrinet::Node,
    Petrinet::Petrinet,
    Petrinet::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(Petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(Petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(Petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(Petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"
    assert "minDelay" in params, "Missing parameter 'minDelay'"

def test_petrinet::transition_has_maxDelay():
    assert hasattr(Petrinet::Transition, "maxDelay")
    descriptor = None
    for klass in Petrinet::Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::transition_has_minDelay():
    assert hasattr(Petrinet::Transition, "minDelay")
    descriptor = None
    for klass in Petrinet::Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::inputarc_is_not_abstract():
    assert not inspect.isabstract(Petrinet::InputArc)


def test_petrinet::inputarc_constructor_exists():
    assert callable(Petrinet::InputArc.__init__)


def test_petrinet::inputarc_constructor_args():
    sig = inspect.signature(Petrinet::InputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::outputarc_is_not_abstract():
    assert not inspect.isabstract(Petrinet::OutputArc)


def test_petrinet::outputarc_constructor_exists():
    assert callable(Petrinet::OutputArc.__init__)


def test_petrinet::outputarc_constructor_args():
    sig = inspect.signature(Petrinet::OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(Petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(Petrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(Petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(Petrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Petrinet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(Petrinet::Petrinet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(Petrinet::Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(Petrinet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(Petrinet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(Petrinet::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::element_has_name():
    assert hasattr(Petrinet::Element, "name")
    descriptor = None
    for klass in Petrinet::Element.__mro__:
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
Node_strategy = st.builds(
    Node,
)
Petrinet::Place_strategy = st.builds(
    Petrinet::Place,
)
Petrinet::Transition_strategy = st.builds(
    Petrinet::Transition,
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
Petrinet::InputArc_strategy = st.builds(
    Petrinet::InputArc,
)
Petrinet::OutputArc_strategy = st.builds(
    Petrinet::OutputArc,
)
Element_strategy = st.builds(
    Element,
)
Petrinet::Arc_strategy = st.builds(
    Petrinet::Arc,
)
Petrinet::Node_strategy = st.builds(
    Petrinet::Node,
)
Petrinet::Petrinet_strategy = st.builds(
    Petrinet::Petrinet,
)
Petrinet::Element_strategy = st.builds(
    Petrinet::Element,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, Petrinet::Place)

@given(instance=Petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, Petrinet::Transition)

@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_maxDelay_type(instance):
    assert isinstance(instance.maxDelay, float)


@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_minDelay_type(instance):
    assert isinstance(instance.minDelay, float)


@given(instance=Petrinet::Transition_strategy)
def test_petrinet::transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=Petrinet::InputArc_strategy)
@settings(max_examples=50)
def test_petrinet::inputarc_instantiation(instance):
    assert isinstance(instance, Petrinet::InputArc)

@given(instance=Petrinet::OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet::outputarc_instantiation(instance):
    assert isinstance(instance, Petrinet::OutputArc)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, Petrinet::Arc)

@given(instance=Petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, Petrinet::Node)

@given(instance=Petrinet::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet::Petrinet)

@given(instance=Petrinet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, Petrinet::Element)

@given(instance=Petrinet::Element_strategy)
def test_petrinet::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Petrinet::Element_strategy)
def test_petrinet::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
