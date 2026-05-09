import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    petrinet::Node,
    petrinet::Arc,
    petrinet::Place,
    petrinet::PNGraph,
    petrinet::Transition,
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



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"

def test_petrinet::arc_has_w():
    assert hasattr(petrinet::Arc, "w")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "markings" in params, "Missing parameter 'markings'"
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet::place_has_markings():
    assert hasattr(petrinet::Place, "markings")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "markings" in klass.__dict__:
            descriptor = klass.__dict__["markings"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_id():
    assert hasattr(petrinet::Place, "id")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::pngraph_is_not_abstract():
    assert not inspect.isabstract(petrinet::PNGraph)


def test_petrinet::pngraph_constructor_exists():
    assert callable(petrinet::PNGraph.__init__)


def test_petrinet::pngraph_constructor_args():
    sig = inspect.signature(petrinet::PNGraph.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet::transition_has_id():
    assert hasattr(petrinet::Transition, "id")
    descriptor = None
    for klass in petrinet::Transition.__mro__:
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
petrinet::Node_strategy = st.builds(
    petrinet::Node,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    w=
        safe_text
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    markings=
        safe_text,
    id=
        safe_text
)
petrinet::PNGraph_strategy = st.builds(
    petrinet::PNGraph,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_w_type(instance):
    assert isinstance(instance.w, str)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_markings_type(instance):
    assert isinstance(instance.markings, str)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_markings_setter(instance):
    original = instance.markings
    instance.markings = original
    assert instance.markings == original

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=petrinet::PNGraph_strategy)
@settings(max_examples=50)
def test_petrinet::pngraph_instantiation(instance):
    assert isinstance(instance, petrinet::PNGraph)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=petrinet::Transition_strategy)
def test_petrinet::transition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
