import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petrinet_Place,
    petrinet_Transition,
    petrinet_PetriNet,
    Identifyable,
    petrinet_Arc,
    petrinet_Node,
    petrinet_Identifyable,
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



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_identifyable_is_not_abstract():
    assert not inspect.isabstract(Identifyable)


def test_identifyable_constructor_exists():
    assert callable(Identifyable.__init__)


def test_identifyable_constructor_args():
    sig = inspect.signature(Identifyable.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_identifyable_is_not_abstract():
    assert not inspect.isabstract(petrinet_Identifyable)


def test_petrinet_identifyable_constructor_exists():
    assert callable(petrinet_Identifyable.__init__)


def test_petrinet_identifyable_constructor_args():
    sig = inspect.signature(petrinet_Identifyable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet_identifyable_has_id():
    assert hasattr(petrinet_Identifyable, "id")
    descriptor = None
    for klass in petrinet_Identifyable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
petrinet_Place_strategy = st.builds(
    petrinet_Place,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_PetriNet_strategy = st.builds(
    petrinet_PetriNet,
)
Identifyable_strategy = st.builds(
    Identifyable,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
)
petrinet_Node_strategy = st.builds(
    petrinet_Node,
)
petrinet_Identifyable_strategy = st.builds(
    petrinet_Identifyable,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_PetriNet)

@given(instance=Identifyable_strategy)
@settings(max_examples=50)
def test_identifyable_instantiation(instance):
    assert isinstance(instance, Identifyable)

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)

@given(instance=petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)

@given(instance=petrinet_Identifyable_strategy)
@settings(max_examples=50)
def test_petrinet_identifyable_instantiation(instance):
    assert isinstance(instance, petrinet_Identifyable)



@given(instance=petrinet_Identifyable_strategy)
def test_petrinet_identifyable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
