import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet101_Token,
    Node,
    petrinet101_Transition,
    petrinet101_Place,
    petrinet101_Arc,
    petrinet101_Node,
    petrinet101_Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet101_token_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Token)


def test_petrinet101_token_constructor_exists():
    assert callable(petrinet101_Token.__init__)


def test_petrinet101_token_constructor_args():
    sig = inspect.signature(petrinet101_Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Transition)


def test_petrinet101_transition_constructor_exists():
    assert callable(petrinet101_Transition.__init__)


def test_petrinet101_transition_constructor_args():
    sig = inspect.signature(petrinet101_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101_place_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Place)


def test_petrinet101_place_constructor_exists():
    assert callable(petrinet101_Place.__init__)


def test_petrinet101_place_constructor_args():
    sig = inspect.signature(petrinet101_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Arc)


def test_petrinet101_arc_constructor_exists():
    assert callable(petrinet101_Arc.__init__)


def test_petrinet101_arc_constructor_args():
    sig = inspect.signature(petrinet101_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101_node_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Node)


def test_petrinet101_node_constructor_exists():
    assert callable(petrinet101_Node.__init__)


def test_petrinet101_node_constructor_args():
    sig = inspect.signature(petrinet101_Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet101_Petrinet)


def test_petrinet101_petrinet_constructor_exists():
    assert callable(petrinet101_Petrinet.__init__)


def test_petrinet101_petrinet_constructor_args():
    sig = inspect.signature(petrinet101_Petrinet.__init__)
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
petrinet101_Token_strategy = st.builds(
    petrinet101_Token,
)
Node_strategy = st.builds(
    Node,
)
petrinet101_Transition_strategy = st.builds(
    petrinet101_Transition,
)
petrinet101_Place_strategy = st.builds(
    petrinet101_Place,
)
petrinet101_Arc_strategy = st.builds(
    petrinet101_Arc,
)
petrinet101_Node_strategy = st.builds(
    petrinet101_Node,
)
petrinet101_Petrinet_strategy = st.builds(
    petrinet101_Petrinet,
)

@given(instance=petrinet101_Token_strategy)
@settings(max_examples=50)
def test_petrinet101_token_instantiation(instance):
    assert isinstance(instance, petrinet101_Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet101_Transition_strategy)
@settings(max_examples=50)
def test_petrinet101_transition_instantiation(instance):
    assert isinstance(instance, petrinet101_Transition)

@given(instance=petrinet101_Place_strategy)
@settings(max_examples=50)
def test_petrinet101_place_instantiation(instance):
    assert isinstance(instance, petrinet101_Place)

@given(instance=petrinet101_Arc_strategy)
@settings(max_examples=50)
def test_petrinet101_arc_instantiation(instance):
    assert isinstance(instance, petrinet101_Arc)

@given(instance=petrinet101_Node_strategy)
@settings(max_examples=50)
def test_petrinet101_node_instantiation(instance):
    assert isinstance(instance, petrinet101_Node)

@given(instance=petrinet101_Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet101_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet101_Petrinet)
