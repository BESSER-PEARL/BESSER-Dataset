import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet_Node,
    Node,
    petrinet_Place,
    petrinet_Transition,
    petrinet_Arc,
    petrinet_Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_node_is_not_abstract():
    assert not inspect.isabstract(petrinet_Node)


def test_petrinet_node_constructor_exists():
    assert callable(petrinet_Node.__init__)


def test_petrinet_node_constructor_args():
    sig = inspect.signature(petrinet_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_node_has_name():
    assert hasattr(petrinet_Node, "name")
    descriptor = None
    for klass in petrinet_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
    assert "tokenNb" in params, "Missing parameter 'tokenNb'"

def test_petrinet_place_has_tokenNb():
    assert hasattr(petrinet_Place, "tokenNb")
    descriptor = None
    for klass in petrinet_Place.__mro__:
        if "tokenNb" in klass.__dict__:
            descriptor = klass.__dict__["tokenNb"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petrinet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petrinet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petrinet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petrinet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_Petrinet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petrinet_Petrinet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petrinet_Petrinet.__init__)
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
petrinet_Node_strategy = st.builds(
    petrinet_Node,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
petrinet_Place_strategy = st.builds(
    petrinet_Place,
    tokenNb=
        st.integers()
)
petrinet_Transition_strategy = st.builds(
    petrinet_Transition,
)
petrinet_Arc_strategy = st.builds(
    petrinet_Arc,
)
petrinet_Petrinet_strategy = st.builds(
    petrinet_Petrinet,
)

@given(instance=petrinet_Node_strategy)
@settings(max_examples=50)
def test_petrinet_node_instantiation(instance):
    assert isinstance(instance, petrinet_Node)



@given(instance=petrinet_Node_strategy)
def test_petrinet_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petrinet_Place)



@given(instance=petrinet_Place_strategy)
def test_petrinet_place_tokenNb_setter(instance):
    original = instance.tokenNb
    instance.tokenNb = original
    assert instance.tokenNb == original

@given(instance=petrinet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petrinet_Transition)

@given(instance=petrinet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petrinet_Arc)

@given(instance=petrinet_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_Petrinet)
