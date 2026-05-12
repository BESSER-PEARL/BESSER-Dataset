import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNets_Token,
    Node,
    PetriNets_Place,
    PetriNets_Transition,
    Object,
    PetriNets_Arc,
    PetriNets_Node,
    PetriNets_Object,
    PetriNets_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets_token_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Token)


def test_petrinets_token_constructor_exists():
    assert callable(PetriNets_Token.__init__)


def test_petrinets_token_constructor_args():
    sig = inspect.signature(PetriNets_Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_place_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Place)


def test_petrinets_place_constructor_exists():
    assert callable(PetriNets_Place.__init__)


def test_petrinets_place_constructor_args():
    sig = inspect.signature(PetriNets_Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinets_place_has_capacity():
    assert hasattr(PetriNets_Place, "capacity")
    descriptor = None
    for klass in PetriNets_Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Transition)


def test_petrinets_transition_constructor_exists():
    assert callable(PetriNets_Transition.__init__)


def test_petrinets_transition_constructor_args():
    sig = inspect.signature(PetriNets_Transition.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Arc)


def test_petrinets_arc_constructor_exists():
    assert callable(PetriNets_Arc.__init__)


def test_petrinets_arc_constructor_args():
    sig = inspect.signature(PetriNets_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_node_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Node)


def test_petrinets_node_constructor_exists():
    assert callable(PetriNets_Node.__init__)


def test_petrinets_node_constructor_args():
    sig = inspect.signature(PetriNets_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets_node_has_name():
    assert hasattr(PetriNets_Node, "name")
    descriptor = None
    for klass in PetriNets_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets_object_is_not_abstract():
    assert not inspect.isabstract(PetriNets_Object)


def test_petrinets_object_constructor_exists():
    assert callable(PetriNets_Object.__init__)


def test_petrinets_object_constructor_args():
    sig = inspect.signature(PetriNets_Object.__init__)
    params = list(sig.parameters.keys())



def test_petrinets_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets_PetriNet)


def test_petrinets_petrinet_constructor_exists():
    assert callable(PetriNets_PetriNet.__init__)


def test_petrinets_petrinet_constructor_args():
    sig = inspect.signature(PetriNets_PetriNet.__init__)
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
PetriNets_Token_strategy = st.builds(
    PetriNets_Token,
)
Node_strategy = st.builds(
    Node,
)
PetriNets_Place_strategy = st.builds(
    PetriNets_Place,
    capacity=
        st.integers()
)
PetriNets_Transition_strategy = st.builds(
    PetriNets_Transition,
)
Object_strategy = st.builds(
    Object,
)
PetriNets_Arc_strategy = st.builds(
    PetriNets_Arc,
)
PetriNets_Node_strategy = st.builds(
    PetriNets_Node,
    name=
        safe_text
)
PetriNets_Object_strategy = st.builds(
    PetriNets_Object,
)
PetriNets_PetriNet_strategy = st.builds(
    PetriNets_PetriNet,
)

@given(instance=PetriNets_Token_strategy)
@settings(max_examples=50)
def test_petrinets_token_instantiation(instance):
    assert isinstance(instance, PetriNets_Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNets_Place_strategy)
@settings(max_examples=50)
def test_petrinets_place_instantiation(instance):
    assert isinstance(instance, PetriNets_Place)



@given(instance=PetriNets_Place_strategy)
def test_petrinets_place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=PetriNets_Transition_strategy)
@settings(max_examples=50)
def test_petrinets_transition_instantiation(instance):
    assert isinstance(instance, PetriNets_Transition)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=PetriNets_Arc_strategy)
@settings(max_examples=50)
def test_petrinets_arc_instantiation(instance):
    assert isinstance(instance, PetriNets_Arc)

@given(instance=PetriNets_Node_strategy)
@settings(max_examples=50)
def test_petrinets_node_instantiation(instance):
    assert isinstance(instance, PetriNets_Node)



@given(instance=PetriNets_Node_strategy)
def test_petrinets_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets_Object_strategy)
@settings(max_examples=50)
def test_petrinets_object_instantiation(instance):
    assert isinstance(instance, PetriNets_Object)

@given(instance=PetriNets_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets_PetriNet)
