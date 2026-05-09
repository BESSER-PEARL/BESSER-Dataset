import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    petriNet::Node,
    petriNet::Arc,
    Node,
    petriNet::Transition,
    petriNet::Place,
    petriNet::Element,
    petriNet::PetriNet,
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



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petriNet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petriNet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petriNet::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petriNet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "noTokens" in params, "Missing parameter 'noTokens'"

def test_petrinet::place_has_noTokens():
    assert hasattr(petriNet::Place, "noTokens")
    descriptor = None
    for klass in petriNet::Place.__mro__:
        if "noTokens" in klass.__dict__:
            descriptor = klass.__dict__["noTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(petriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(petriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(petriNet::Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "diagramName" in params, "Missing parameter 'diagramName'"

def test_petrinet::petrinet_has_diagramName():
    assert hasattr(petriNet::PetriNet, "diagramName")
    descriptor = None
    for klass in petriNet::PetriNet.__mro__:
        if "diagramName" in klass.__dict__:
            descriptor = klass.__dict__["diagramName"]
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
Element_strategy = st.builds(
    Element,
)
petriNet::Node_strategy = st.builds(
    petriNet::Node,
)
petriNet::Arc_strategy = st.builds(
    petriNet::Arc,
)
Node_strategy = st.builds(
    Node,
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
    noTokens=
        st.integers()
)
petriNet::Element_strategy = st.builds(
    petriNet::Element,
)
petriNet::PetriNet_strategy = st.builds(
    petriNet::PetriNet,
    diagramName=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petriNet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petriNet::Node)

@given(instance=petriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petriNet::Arc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=petriNet::Place_strategy)
def test_petrinet::place_noTokens_type(instance):
    assert isinstance(instance.noTokens, int)


@given(instance=petriNet::Place_strategy)
def test_petrinet::place_noTokens_setter(instance):
    original = instance.noTokens
    instance.noTokens = original
    assert instance.noTokens == original

@given(instance=petriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, petriNet::Element)

@given(instance=petriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNet)

@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_diagramName_type(instance):
    assert isinstance(instance.diagramName, str)


@given(instance=petriNet::PetriNet_strategy)
def test_petrinet::petrinet_diagramName_setter(instance):
    original = instance.diagramName
    instance.diagramName = original
    assert instance.diagramName == original
