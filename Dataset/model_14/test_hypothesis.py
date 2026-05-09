import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    petrinet::Place,
    petrinet::Transition,
    Arc,
    petrinet::InputArc,
    petrinet::OutputArc,
    Element,
    petrinet::Arc,
    petrinet::Node,
    petrinet::PetriNet,
    petrinet::Element,
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
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "minDelay" in params, "Missing parameter 'minDelay'"
    assert "maxDelay" in params, "Missing parameter 'maxDelay'"

def test_petrinet::transition_has_minDelay():
    assert hasattr(petrinet::Transition, "minDelay")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
        if "minDelay" in klass.__dict__:
            descriptor = klass.__dict__["minDelay"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::transition_has_maxDelay():
    assert hasattr(petrinet::Transition, "maxDelay")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
        if "maxDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxDelay"]
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
    assert not inspect.isabstract(petrinet::InputArc)


def test_petrinet::inputarc_constructor_exists():
    assert callable(petrinet::InputArc.__init__)


def test_petrinet::inputarc_constructor_args():
    sig = inspect.signature(petrinet::InputArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::outputarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::OutputArc)


def test_petrinet::outputarc_constructor_exists():
    assert callable(petrinet::OutputArc.__init__)


def test_petrinet::outputarc_constructor_args():
    sig = inspect.signature(petrinet::OutputArc.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(petrinet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(petrinet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(petrinet::Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::element_has_name():
    assert hasattr(petrinet::Element, "name")
    descriptor = None
    for klass in petrinet::Element.__mro__:
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
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    minDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    maxDelay=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Arc_strategy = st.builds(
    Arc,
)
petrinet::InputArc_strategy = st.builds(
    petrinet::InputArc,
)
petrinet::OutputArc_strategy = st.builds(
    petrinet::OutputArc,
)
Element_strategy = st.builds(
    Element,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
)
petrinet::Element_strategy = st.builds(
    petrinet::Element,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_minDelay_type(instance):
    assert isinstance(instance.minDelay, float)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_minDelay_setter(instance):
    original = instance.minDelay
    instance.minDelay = original
    assert instance.minDelay == original

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_maxDelay_type(instance):
    assert isinstance(instance.maxDelay, float)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_maxDelay_setter(instance):
    original = instance.maxDelay
    instance.maxDelay = original
    assert instance.maxDelay == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::InputArc_strategy)
@settings(max_examples=50)
def test_petrinet::inputarc_instantiation(instance):
    assert isinstance(instance, petrinet::InputArc)

@given(instance=petrinet::OutputArc_strategy)
@settings(max_examples=50)
def test_petrinet::outputarc_instantiation(instance):
    assert isinstance(instance, petrinet::OutputArc)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, petrinet::Element)

@given(instance=petrinet::Element_strategy)
def test_petrinet::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Element_strategy)
def test_petrinet::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
