import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    petriNet_Node,
    petriNet_Arc,
    Node,
    petriNet_Transition,
    petriNet_Place,
    petriNet_Element,
    petriNet_PetriNet,
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



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petriNet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petriNet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petriNet_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "noTokens" in params, "Missing parameter 'noTokens'"

def test_petrinet_place_has_noTokens():
    assert hasattr(petriNet_Place, "noTokens")
    descriptor = None
    for klass in petriNet_Place.__mro__:
        if "noTokens" in klass.__dict__:
            descriptor = klass.__dict__["noTokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(petriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(petriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(petriNet_Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "diagramName" in params, "Missing parameter 'diagramName'"

def test_petrinet_petrinet_has_diagramName():
    assert hasattr(petriNet_PetriNet, "diagramName")
    descriptor = None
    for klass in petriNet_PetriNet.__mro__:
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
petriNet_Node_strategy = st.builds(
    petriNet_Node,
)
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
)
Node_strategy = st.builds(
    Node,
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
)
petriNet_Place_strategy = st.builds(
    petriNet_Place,
    noTokens=
        st.integers()
)
petriNet_Element_strategy = st.builds(
    petriNet_Element,
)
petriNet_PetriNet_strategy = st.builds(
    petriNet_PetriNet,
    diagramName=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petriNet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petriNet_Node)

@given(instance=petriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)



@given(instance=petriNet_Place_strategy)
def test_petrinet_place_noTokens_setter(instance):
    original = instance.noTokens
    instance.noTokens = original
    assert instance.noTokens == original

@given(instance=petriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, petriNet_Element)

@given(instance=petriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNet)



@given(instance=petriNet_PetriNet_strategy)
def test_petrinet_petrinet_diagramName_setter(instance):
    original = instance.diagramName
    instance.diagramName = original
    assert instance.diagramName == original
