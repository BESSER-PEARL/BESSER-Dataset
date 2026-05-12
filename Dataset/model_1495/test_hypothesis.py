import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petri_net_Place,
    petri_net_Transition,
    petri_net_Arc,
    petri_net_Node,
    petri_net_PetriNet,
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



def test_petri_net_place_is_not_abstract():
    assert not inspect.isabstract(petri_net_Place)


def test_petri_net_place_constructor_exists():
    assert callable(petri_net_Place.__init__)


def test_petri_net_place_constructor_args():
    sig = inspect.signature(petri_net_Place.__init__)
    params = list(sig.parameters.keys())



def test_petri_net_transition_is_not_abstract():
    assert not inspect.isabstract(petri_net_Transition)


def test_petri_net_transition_constructor_exists():
    assert callable(petri_net_Transition.__init__)


def test_petri_net_transition_constructor_args():
    sig = inspect.signature(petri_net_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri_net_arc_is_not_abstract():
    assert not inspect.isabstract(petri_net_Arc)


def test_petri_net_arc_constructor_exists():
    assert callable(petri_net_Arc.__init__)


def test_petri_net_arc_constructor_args():
    sig = inspect.signature(petri_net_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_net_arc_has_name():
    assert hasattr(petri_net_Arc, "name")
    descriptor = None
    for klass in petri_net_Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri_net_node_is_not_abstract():
    assert not inspect.isabstract(petri_net_Node)


def test_petri_net_node_constructor_exists():
    assert callable(petri_net_Node.__init__)


def test_petri_net_node_constructor_args():
    sig = inspect.signature(petri_net_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_net_node_has_name():
    assert hasattr(petri_net_Node, "name")
    descriptor = None
    for klass in petri_net_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri_net_petrinet_is_not_abstract():
    assert not inspect.isabstract(petri_net_PetriNet)


def test_petri_net_petrinet_constructor_exists():
    assert callable(petri_net_PetriNet.__init__)


def test_petri_net_petrinet_constructor_args():
    sig = inspect.signature(petri_net_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri_net_petrinet_has_name():
    assert hasattr(petri_net_PetriNet, "name")
    descriptor = None
    for klass in petri_net_PetriNet.__mro__:
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
petri_net_Place_strategy = st.builds(
    petri_net_Place,
)
petri_net_Transition_strategy = st.builds(
    petri_net_Transition,
)
petri_net_Arc_strategy = st.builds(
    petri_net_Arc,
    name=
        safe_text
)
petri_net_Node_strategy = st.builds(
    petri_net_Node,
    name=
        safe_text
)
petri_net_PetriNet_strategy = st.builds(
    petri_net_PetriNet,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petri_net_Place_strategy)
@settings(max_examples=50)
def test_petri_net_place_instantiation(instance):
    assert isinstance(instance, petri_net_Place)

@given(instance=petri_net_Transition_strategy)
@settings(max_examples=50)
def test_petri_net_transition_instantiation(instance):
    assert isinstance(instance, petri_net_Transition)

@given(instance=petri_net_Arc_strategy)
@settings(max_examples=50)
def test_petri_net_arc_instantiation(instance):
    assert isinstance(instance, petri_net_Arc)



@given(instance=petri_net_Arc_strategy)
def test_petri_net_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri_net_Node_strategy)
@settings(max_examples=50)
def test_petri_net_node_instantiation(instance):
    assert isinstance(instance, petri_net_Node)



@given(instance=petri_net_Node_strategy)
def test_petri_net_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri_net_PetriNet_strategy)
@settings(max_examples=50)
def test_petri_net_petrinet_instantiation(instance):
    assert isinstance(instance, petri_net_PetriNet)



@given(instance=petri_net_PetriNet_strategy)
def test_petri_net_petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
