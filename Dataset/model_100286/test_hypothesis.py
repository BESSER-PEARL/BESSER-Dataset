import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    pETRI_Transition,
    pETRI_Place,
    pETRI_PetriNet,
    PetriNetElement,
    pETRI_Arc,
    pETRI_Node,
    pETRI_PetriNetElement,
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



def test_petri_transition_is_not_abstract():
    assert not inspect.isabstract(pETRI_Transition)


def test_petri_transition_constructor_exists():
    assert callable(pETRI_Transition.__init__)


def test_petri_transition_constructor_args():
    sig = inspect.signature(pETRI_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri_place_is_not_abstract():
    assert not inspect.isabstract(pETRI_Place)


def test_petri_place_constructor_exists():
    assert callable(pETRI_Place.__init__)


def test_petri_place_constructor_args():
    sig = inspect.signature(pETRI_Place.__init__)
    params = list(sig.parameters.keys())
    assert "marking" in params, "Missing parameter 'marking'"

def test_petri_place_has_marking():
    assert hasattr(pETRI_Place, "marking")
    descriptor = None
    for klass in pETRI_Place.__mro__:
        if "marking" in klass.__dict__:
            descriptor = klass.__dict__["marking"]
            break
    assert isinstance(descriptor, property)



def test_petri_petrinet_is_not_abstract():
    assert not inspect.isabstract(pETRI_PetriNet)


def test_petri_petrinet_constructor_exists():
    assert callable(pETRI_PetriNet.__init__)


def test_petri_petrinet_constructor_args():
    sig = inspect.signature(pETRI_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_petrinet_has_name():
    assert hasattr(pETRI_PetriNet, "name")
    descriptor = None
    for klass in pETRI_PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinetelement_is_not_abstract():
    assert not inspect.isabstract(PetriNetElement)


def test_petrinetelement_constructor_exists():
    assert callable(PetriNetElement.__init__)


def test_petrinetelement_constructor_args():
    sig = inspect.signature(PetriNetElement.__init__)
    params = list(sig.parameters.keys())



def test_petri_arc_is_not_abstract():
    assert not inspect.isabstract(pETRI_Arc)


def test_petri_arc_constructor_exists():
    assert callable(pETRI_Arc.__init__)


def test_petri_arc_constructor_args():
    sig = inspect.signature(pETRI_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"

def test_petri_arc_has_readOnly():
    assert hasattr(pETRI_Arc, "readOnly")
    descriptor = None
    for klass in pETRI_Arc.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)

def test_petri_arc_has_multiplicity():
    assert hasattr(pETRI_Arc, "multiplicity")
    descriptor = None
    for klass in pETRI_Arc.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)



def test_petri_node_is_not_abstract():
    assert not inspect.isabstract(pETRI_Node)


def test_petri_node_constructor_exists():
    assert callable(pETRI_Node.__init__)


def test_petri_node_constructor_args():
    sig = inspect.signature(pETRI_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_node_has_name():
    assert hasattr(pETRI_Node, "name")
    descriptor = None
    for klass in pETRI_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri_petrinetelement_is_not_abstract():
    assert not inspect.isabstract(pETRI_PetriNetElement)


def test_petri_petrinetelement_constructor_exists():
    assert callable(pETRI_PetriNetElement.__init__)


def test_petri_petrinetelement_constructor_args():
    sig = inspect.signature(pETRI_PetriNetElement.__init__)
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
Node_strategy = st.builds(
    Node,
)
pETRI_Transition_strategy = st.builds(
    pETRI_Transition,
)
pETRI_Place_strategy = st.builds(
    pETRI_Place,
    marking=
        st.integers()
)
pETRI_PetriNet_strategy = st.builds(
    pETRI_PetriNet,
    name=
        safe_text
)
PetriNetElement_strategy = st.builds(
    PetriNetElement,
)
pETRI_Arc_strategy = st.builds(
    pETRI_Arc,
    readOnly=
        st.booleans(),
    multiplicity=
        st.integers()
)
pETRI_Node_strategy = st.builds(
    pETRI_Node,
    name=
        safe_text
)
pETRI_PetriNetElement_strategy = st.builds(
    pETRI_PetriNetElement,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=pETRI_Transition_strategy)
@settings(max_examples=50)
def test_petri_transition_instantiation(instance):
    assert isinstance(instance, pETRI_Transition)

@given(instance=pETRI_Place_strategy)
@settings(max_examples=50)
def test_petri_place_instantiation(instance):
    assert isinstance(instance, pETRI_Place)



@given(instance=pETRI_Place_strategy)
def test_petri_place_marking_setter(instance):
    original = instance.marking
    instance.marking = original
    assert instance.marking == original

@given(instance=pETRI_PetriNet_strategy)
@settings(max_examples=50)
def test_petri_petrinet_instantiation(instance):
    assert isinstance(instance, pETRI_PetriNet)



@given(instance=pETRI_PetriNet_strategy)
def test_petri_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNetElement_strategy)
@settings(max_examples=50)
def test_petrinetelement_instantiation(instance):
    assert isinstance(instance, PetriNetElement)

@given(instance=pETRI_Arc_strategy)
@settings(max_examples=50)
def test_petri_arc_instantiation(instance):
    assert isinstance(instance, pETRI_Arc)



@given(instance=pETRI_Arc_strategy)
def test_petri_arc_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original



@given(instance=pETRI_Arc_strategy)
def test_petri_arc_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=pETRI_Node_strategy)
@settings(max_examples=50)
def test_petri_node_instantiation(instance):
    assert isinstance(instance, pETRI_Node)



@given(instance=pETRI_Node_strategy)
def test_petri_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pETRI_PetriNetElement_strategy)
@settings(max_examples=50)
def test_petri_petrinetelement_instantiation(instance):
    assert isinstance(instance, pETRI_PetriNetElement)
