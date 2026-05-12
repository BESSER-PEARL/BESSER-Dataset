import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    petrinet_Node,
    petrinet_Arc,
    petrinet_Place,
    petrinet_PNGraph,
    petrinet_Transition,
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



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"

def test_petrinet_arc_has_w():
    assert hasattr(petrinet_Arc, "w")
    descriptor = None
    for klass in petrinet_Arc.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petrinet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petrinet_Place.__init__)
    params = list(sig.parameters.keys())
    assert "markings" in params, "Missing parameter 'markings'"
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet_place_has_markings():
    assert hasattr(petrinet_Place, "markings")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "markings" in klass.__dict__:
            descriptor = klass.__dict__["markings"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_place_has_id():
    assert hasattr(petrinet_Place, "id")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_pngraph_is_not_abstract():
    assert not inspect.isabstract(petrinet_PNGraph)


def test_petrinet_pngraph_constructor_exists():
    assert callable(petrinet_PNGraph.__init__)


def test_petrinet_pngraph_constructor_args():
    sig = inspect.signature(petrinet_PNGraph.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet_transition_has_id():
    assert hasattr(petrinet_Transition, "id")
    descriptor = None
    for klass in petrinet_Transition.__mro__:
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
petrinet_Node_strategy = st.builds(
    petrinet_Node,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
    w=
        safe_text
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    markings=
        safe_text,
    id=
        safe_text
)
petrinet_PNGraph_strategy = st.builds(
    petrinet_PNGraph,
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)



@given(instance=petrinet_Arc_strategy)
def test_petrinet_arc_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_markings_setter(instance):
    original = instance.markings
    instance.markings = original
    assert instance.markings == original



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=petrinet_PNGraph_strategy)
@settings(max_examples=50)
def test_petrinet_pngraph_instantiation(instance):
    assert isinstance(instance, petrinet_PNGraph)

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)



@given(instance=petrinet_Transition_strategy)
def test_petrinet_transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
